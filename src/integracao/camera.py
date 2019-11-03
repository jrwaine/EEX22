import ports
from led import Led
import time
import cv2 as cv
import numpy as np
from blob import Blob
from sklearn.cluster import KMeans
from pandas import DataFrame
from pprint import PrettyPrinter
import globals
import picamera
from math import atan, pi

pp = PrettyPrinter(indent=4)

class Camera:
    def __init__(self):
        print("Criando camera...")
        self.led = Led()
        self.n_images = 0
        with picamera.PiCamera() as camera:
            camera.resolution = globals.CAM_RESOLUTION
            time.sleep(2)

    def verificar(self):
        self.led.acender()
        print("\nProcessando a imagem...")

        angle = self.process()
        # processar imagem
        print("Imagem processada!\n")
        self.led.apagar()
        print('procesor e achou',angle, 'graus')
        return angle  # angle

    def take_picture(self):
        with picamera.PiCamera() as camera:
            filename = globals.PATH+"img%04d.bmp" % self.n_images
            camera.capture(filename, format='bmp')
            self.n_images += 1
            img = cv.imread(filename, cv.IMREAD_COLOR)
        return filename, img

    def process(self):
        times = {}
        ini_time = time.time()

        t0 = time.time()
        filename, img = self.take_picture()
        #img = cv.imread(filenames[number], cv.IMREAD_COLOR)
        times['Read image'] = time.time()-t0
        
        t0 = time.time()
        imgTreated = self.treat_image(img)
        times['Treat image'] = time.time()-t0
        
        imgGray = cv.cvtColor(imgTreated, cv.COLOR_BGR2GRAY) # convert to gray scale
        cv.normalize(imgGray, imgGray, 0, 255, cv.NORM_MINMAX)
        
        t0 = time.time()
        imgBin = self.binarize(imgGray)
        times['Binarize'] = time.time()-t0

        t0 = time.time()
        imgBin = self.morpholigical_operations(imgBin)
        times['Morph operations'] = time.time() - t0

        t0 = time.time()
        blobs = self.get_blobs(imgBin)
        times['Blob detection'] = time.time() - t0

        t0 = time.time()
        desiredBlobs = self.get_desired_blobs(blobs, imgBin)
        times['Blobs validation'] = time.time() - t0
        
        t0 = time.time()
        self.get_blobs_directions(desiredBlobs)
        times['Blobs processing'] = time.time() - t0

        t0 = time.time()
        imgSave = cv.cvtColor(imgBin, cv.COLOR_GRAY2RGB)

        desiredBlobs.sort()
        for blob in desiredBlobs:
            y1 = blob.centroids[0][1]
            y2 = blob.centroids[1][1]
            x1 = blob.centroids[0][0]
            x2 = blob.centroids[1][0]
            coef_ang = (y2-y1) / (x2-x1+10e-10)
            theta = atan(coef_ang)
            blob.theta = theta/pi*180
        
        theta_diff = None
        
        if(len(desiredBlobs) == 3):
            theta_diff = (desiredBlobs[0].theta + desiredBlobs[2].theta) - desiredBlobs[1].theta
            if(theta_diff < 0):
                theta_diff += 180
        
        t0 = time.time()
        for blob in desiredBlobs:
            cv.line(imgSave, tuple(blob.centroids[0].astype('int')), tuple(blob.centroids[1].astype('int')), (255, 0, 0), 3)
        times['Drawing line'] = time.time() - t0
        
        t0 = time.time()
        #cv.imwrite(filenames[number][:-4]+"treated.bmp", imgSave)
        cv.imwrite(filename[:-4]+"treated.bmp", imgSave)
        times['Saving'] = time.time() - t0

        times['Total'] = time.time()- ini_time
        pp.pprint(times)
        print()

        return theta_diff

    def treat_image(self, img):
        imgTreated = img[:, int(img.shape[1]*globals.CROP_X[0]):int(img.shape[1]*globals.CROP_X[1]), :]
        return imgTreated


    def binarize(self, imgGray):
        # see if there's betther way
        imgAvg = cv.blur(imgGray, (globals.BOX_SIZE, globals.BOX_SIZE))
        imgBin = np.where(np.logical_and(imgGray <= imgAvg - globals.AVG_DIFF, imgGray < globals.TRESHOLD), globals.WHITE, globals.BLACK)
        return imgBin


    def morpholigical_operations(self, imgBin):
        kernel = cv.getStructuringElement(cv.MORPH_RECT,(globals.MORPH_OPEN_SIZE,globals.MORPH_OPEN_SIZE))
        imgBin = cv.morphologyEx(imgBin.astype('uint8'), cv.MORPH_OPEN, kernel)
        kernel = cv.getStructuringElement(cv.MORPH_RECT,(globals.MORPH_DILATE_SIZE, globals.MORPH_DILATE_SIZE))
        imgBin = cv.morphologyEx(imgBin, cv.MORPH_DILATE, kernel)
        return imgBin


    def rotula(self, img, blob, y0, x0):
        img[y0, x0] = globals.ROTULATED
        blob.addPixel(y0, x0)
        pixels = list()
        pixels.append((y0, x0))
        while(len(pixels) > 0):
            y0, x0 = pixels[0]        
            del pixels[0]    
            # 8 neighbourhood
            for y in range(y0-1, y0+2):
                if(y < len(img) and y >= 0):
                    for x in range(x0-1, x0+2):
                        if (x >= 0 and x < len(img[y])):
                            if(img[y, x] == globals.WHITE):
                                img[y, x] = globals.ROTULATED
                                blob.addPixel(y, x)
                                pixels.append((y, x)) 


    def get_blobs(self, img):
        blobs = []

        # only looks for blobs in x=0.25 or x=0.5 or x=0.75
        for x in [img.shape[1]//4, img.shape[1]//2, (img.shape[1]*3)//4]:
            for y in range(0, img.shape[0]):
                if(img[y, x] == globals.WHITE):
                    blobs.append(Blob())
                    self.rotula(img, blobs[-1], y, x)
        return blobs


    def get_desired_blobs(self, blobs, imgBin):
        desiredBlobs = []
        for i in range(0, len(blobs)):
            # validade width and height of blob
            if((blobs[i].xmax - blobs[i].xmin) < globals.MIN_WIDTH):
                continue
            if((blobs[i].ymax - blobs[i].ymin) < globals.MIN_HEIGHT):
                continue
            # validate blob y range
            if((blobs[i].ymax/imgBin.shape[0] > globals.VALID_BLOB_RANGE_Y[1] or\
                blobs[i].ymin/imgBin.shape[0] < globals.VALID_BLOB_RANGE_Y[0])):
                continue
            
            # check if blob line in x has "a lot" of white. If so
            # the blobs in the range are considered to be the desired ones
            desired_y = -1
            for y in range(blobs[i].ymin, blobs[i].ymax+1):
                if(np.sum(imgBin[y, :])/globals.WHITE >= imgBin.shape[0]*globals.LINE_WHITE_PERCENTAGE):
                    desired_y = y
                    break
            if(desired_y == -1):
                continue
            
            # get all blobs in the height of the y desired
            for j in range(0, len(blobs)):
                if(blobs[j].ymax >= desired_y and blobs[j].ymin <= desired_y):
                    desiredBlobs.append(blobs[j])
            
            # if it found less than 3 blobs
            if(len(desiredBlobs) < 3):
                desiredBlobs = []
            else:
                break
        return desiredBlobs


    def get_blobs_directions(self, blobs):
        for blob in blobs:
            data = {'x': blob.pixelsX, 'y': blob.pixelsY}

            df = DataFrame(data,columns=['x','y'])
        
            kmeans = KMeans(n_clusters=2).fit(df)
            blob.centroids = kmeans.cluster_centers_
        