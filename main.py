import numpy as np
import cv2
import glob
from collections import Counter
import matplotlib.pyplot as plt

path = "C:\\Users\\Hrishkesh Sunny\\project\\Clahe_contraststretching\\data\\grayscale\\"
files = glob.glob(path + "*.png")
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
fgbg = cv2.createBackgroundSubtractorMOG2()
imgcount = 0
meanValue = []
#maxValue = []
for file in files:
    img = cv2.imread(file,-1)
    blur = cv2.GaussianBlur(img, (7,7),-1)
    imgcount += 1
    #fgmask = fgbg.apply(img)
    fgmask = fgbg.apply(blur)
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
    count = np.count_nonzero(fgmask)
    meanValue.append(count)
    #print('img: %d, Pixel Count: %d' %(imgcount,count))
    #cv2.imshow("Original", blur)
    #cv2.imshow("original", img)
    #cv2.imshow('back',fgmask)
    cv2.waitKey()
    cv2.destroyAllWindows()
print(meanValue)
plt.plot(meanValue)
plt.show()
#print(maxValue)

def get_feature(path, blury=False):

    return np.ones()


if __name__ == "__main__":
    f1 = get_feature("")

    # compare all vectors with l2 norm to get distance between each other