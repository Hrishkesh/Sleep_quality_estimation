import cv2
import matplotlib.pyplot as plt
import numpy as np
import glob
import os


last_list=[]
rem=0
L=255
rs=0

path = "E:\\sem4\\Sleep_quality_project\\sleep_Dataset\\2018-11-24-22h44m36s\\"
files = glob.glob(path + "*.png")

for file in files:
    img=cv2.imread(file,-1)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    res = clahe.apply(img)

    x,y,z=plt.hist(img.ravel(),256,[0,256],label='x')

    k=np.sum(x)

    for i in range(len(x)):
        test=x[i]/k
        rs=test+rs
        last=(L-1)*rs
        if rem!=0:
            rem=int(last % last)
        if rem >=0.5:
            last=int(last)+1
        else:
            last=int(last)
        last_list.append(last)

    number_of_rows=(int(np.ma.count(img)/img[1].size))
    number_of_cols=img[1].size
    #print("last list is =".format(last_list))

    for i in range(number_of_cols):
        for j in range(number_of_rows):
            num=img[j][i]
            if num != last_list[num]:
                img[j][i]=last_list[num]

    plt.hist(img.ravel(),256,[0,256])

    #path_out = path+"preprocessing_ouput\\"
    file = os.path.basename(file)
    file = file.split('.png')[0]
    cv2.imwrite("E:\\sem4\\Sleep_quality_project\\sleep_Dataset\\2018-11-24-22h44m36s\\preprocessing_output\\histclahe{}.png".format(file),res)
    print("E:\\sem4\\Sleep_quality_project\\sleep_Dataset\\2018-11-24-22h44m36s\\preprocessing_output\\histclahe{}.png".format(file))
    #cv2.imshow('histclahe.png',,,res)
    cv2.waitKey(0)
    cv2.destroyAllWindows()