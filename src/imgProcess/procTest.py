import cv2 as cv
import numpy as np
import time
from blob import Blob
from sklearn.cluster import KMeans
from pandas import DataFrame
from pprint import PrettyPrinter
# import piCamera

pp = PrettyPrinter(indent=4)

PATH = "./img/"
filenames = [PATH+"img"+str('%04d' % i) + ".bmp" for i in range(0, 15)]

# camera setup
CAMERA_SET = False
CAM_RESOLUTION = (640, 480)
num_imgs = 0

# area to crop image in x
CROP_X = [0.1, 0.7]
# interval to consider blobs (ymax > 0.05 and ymin < 0.95)
VALID_BLOB_RANGE_Y = [0.05, 0.95]

# treshold for black pixel
TRESHOLD = 50
# minimal difference to box blur
AVG_DIFF = 30
# box filter size
BOX_SIZE = 131

# size of morphological operation
MORPH_OPEN_SIZE = 13
MORPH_DILATE_SIZE = 7

# color values
WHITE = 255
BLACK = 0
ROTULATED = 254 # value of rotulated pixel

MIN_WIDTH = 30
MIN_HEIGHT = 7

# percentage of white pixels in x line to consider it as containing the desired blobs
LINE_WHITE_PERCENTAGE = 0.4

'''
def take_picture():
    with picamera.PiCamera() as camera:
        if(not CAMERA_SET):
            camera.resolution(CAM_RESOLUTION)
            time.sleep(2)
        filename = PATH+"img%04d.bmp" % num_imgs
        camera.capture(filename, format='bmp')
        num_imgs += 1
    return filename, img
'''

def treat_image(img):
    imgTreated = img[:, int(img.shape[1]*CROP_X[0]):int(img.shape[1]*CROP_X[1]), :]
    return imgTreated


def binarize(img):
    # see if there's betther way
    imgAvg = cv.blur(imgGray, (BOX_SIZE, BOX_SIZE))
    imgBin = np.where(np.logical_and(imgGray <= imgAvg - AVG_DIFF, imgGray < TRESHOLD), WHITE, BLACK)
    return imgBin


def morpholigical_operations(imgBin):
    kernel = cv.getStructuringElement(cv.MORPH_RECT,(MORPH_OPEN_SIZE,MORPH_OPEN_SIZE))
    imgBin = cv.morphologyEx(imgBin.astype('uint8'), cv.MORPH_OPEN, kernel)
    kernel = cv.getStructuringElement(cv.MORPH_RECT,(MORPH_DILATE_SIZE, MORPH_DILATE_SIZE))
    imgBin = cv.morphologyEx(imgBin, cv.MORPH_DILATE, kernel)
    imgErode = cv.morphologyEx(imgBin, cv.MORPH_ERODE, kernel)
    imgBin = np.bitwise_xor(imgBin, imgErode)
    
    return imgBin


def rotula(img, blob, y0, x0):
    img[y0, x0] = ROTULATED
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
                        if(img[y, x] == WHITE):
                            img[y, x] = ROTULATED
                            blob.addPixel(y, x)
                            pixels.append((y, x)) 


def get_blobs(img):
    blobs = []

    # only looks for blobs in x=0.1, x=0.2 ... x=0.9
    for x in [int(i*img.shape[1]) for i in np.arange(0, 1, 0.1)]:
        for y in range(0, img.shape[0]):
            if(img[y, x] == WHITE):
                blobs.append(Blob())
                rotula(img, blobs[-1], y, x)
    return blobs


def get_desired_blobs(blobs, imgBin):
    desiredBlobs = []
    for i in range(0, len(blobs)):
        # validade width and height of blob
        if((blobs[i].xmax - blobs[i].xmin) < MIN_WIDTH):
            continue
        if((blobs[i].ymax - blobs[i].ymin) < MIN_HEIGHT):
            continue
        # validate blob y range
        if((blobs[i].ymax/imgBin.shape[0] > VALID_BLOB_RANGE_Y[1] or\
            blobs[i].ymin/imgBin.shape[0] < VALID_BLOB_RANGE_Y[0])):
            continue
        blobs[i].valid = True
        
    for i in range(0, len(blobs)):
        if(blobs[i].valid == False):
            continue
        
        # check if blob line in x has "a lot" of white. If so
        # the blobs in the range are considered to be the desired ones
        desired_y = -1
        for y in range(blobs[i].ymin, blobs[i].ymax+1):
            total_x = 0
            for blob in blobs:
                if(blob.ymin <= y and blob.ymax >= y and blob.valid == True):
                    total_x += blob.xmax-blob.xmin
            if(total_x >= imgBin.shape[0]*LINE_WHITE_PERCENTAGE):
                desired_y = y
                break
            '''
            if(np.sum(imgBin[y, :])/WHITE >= img.shape[0]*LINE_WHITE_PERCENTAGE):
                desired_y = y
                break
            '''
        if(desired_y == -1):
            continue

        # get all blobs in the height of the y desired
        for j in range(0, len(blobs)):
            if(blobs[j].ymax >= desired_y and blobs[j].ymin <= desired_y):
                if(blobs[j].valid == True):
                    desiredBlobs.append(blobs[j])

        # if it found less than 3 blobs
        if(len(desiredBlobs) < 3):
            desiredBlobs = []
        else:
            break

    return desiredBlobs


def get_blobs_directions(blobs):
    for blob in blobs:
        data = {'x': blob.pixelsX, 'y': blob.pixelsY}

        df = DataFrame(data,columns=['x','y'])
    
        kmeans = KMeans(n_clusters=2).fit(df)
        blob.centroids = kmeans.cluster_centers_
    

for number in range(0, 15):
    times = {}
    ini_time = time.time()

    t0 = time.time()
    #filename, img = take_picture()
    img = cv.imread(filenames[number], cv.IMREAD_COLOR)
    times['Read image'] = time.time()-t0
    
    t0 = time.time()
    imgTreated = treat_image(img)
    times['Treat image'] = time.time()-t0
    
    imgGray = cv.cvtColor(imgTreated, cv.COLOR_BGR2GRAY) # convert to gray scale
    cv.normalize(imgGray, imgGray, 0, 255, cv.NORM_MINMAX)
    
    t0 = time.time()
    imgBin = binarize(imgGray)
    times['Binarize'] = time.time()-t0

    t0 = time.time()
    imgBin = morpholigical_operations(imgBin)
    times['Morph operations'] = time.time() - t0

    t0 = time.time()
    blobs = get_blobs(imgBin)
    times['Blob detection'] = time.time() - t0

    t0 = time.time()
    desiredBlobs = get_desired_blobs(blobs, imgBin)
    times['Blobs validation'] = time.time() - t0
    
    t0 = time.time()
    get_blobs_directions(desiredBlobs)
    times['Blobs processing'] = time.time() - t0

    print(len(desiredBlobs), len(blobs))
    print([i.ymin for i in desiredBlobs])

    t0 = time.time()
    imgSave = cv.cvtColor(imgBin, cv.COLOR_GRAY2RGB)
    for blob in desiredBlobs:
        cv.line(imgSave, tuple(blob.centroids[0].astype('int')), tuple(blob.centroids[1].astype('int')), (255, 0, 0), 3)
    times['Drawing line'] = time.time() - t0
    
    t0 = time.time()

    cv.imwrite(filenames[number][:-4]+"treated.bmp", imgSave)
    #cv.imwrite(filename[:-4]+"treated.bmp", imgSave)
    times['Saving'] = time.time() - t0

    times['Total'] = time.time()- ini_time
    print(filenames[number])
    pp.pprint(times)
    print()
    