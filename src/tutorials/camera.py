import io
import time
import picamera

SAVE = True

with picamera.PiCamera() as camera:
    # Set the camera's resolution to VGA @40fps and give it a couple
    # of seconds to measure exposure etc.
    camera.resolution = (1980, 1485)
    #camera.crop = (0.25, 0.25, 0.5, 0.5)
    time.sleep(2)
    # Set up 40 in-memory streams
    if(not SAVE):
        outputs = [io.BytesIO() for i in range(40)]
        start = time.time()
        camera.capture_sequence(outputs, 'bmp', use_video_port=True)
        finish = time.time()
    else:
        outputs = []
        start = time.time()
        for i in range(0, 10):
            camera.capture("img%04d.bmp" % int(len(outputs)), format='bmp')
            outputs.append(1)
        finish = time.time()

    # How fast were we?
    print('Captured 10 images at %.2ffps' % (10 / (finish - start)))
