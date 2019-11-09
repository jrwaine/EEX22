# Buzzer e LED
ON = 1
OFF = 0

# Servo
MIN = 2
MAX = 20
PASSO = 0.2  # (MAX - MIN)/90

# Parafusadeira
CIMA = 1
MEIO = 0
BAIXO = -1

# Ultrassonico
CLOSE_OBJECT_DISTANCE = 10  # cm
LIM_TIME = 0.5  # seg

# -----------------------------

PATH = "./img/"
filenames = [PATH+"img"+str('%04d' % i) + ".bmp" for i in range(0, 14)]

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

# ------------------------

HOST = '192.168.100.74'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
COMMUNICATION_LIMIT_TIME = 60