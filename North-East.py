import cv2
import numpy as np
from PIL import Image

img = cv2.imread("girl.png")
height, width, depth = np.shape(img)

# Detects East Direction edge
N = [[-1,0,1],
     [-2,0,2],
     [-1,0,1]]

# Detects North-West Direction edge     
NW = [[0,1,2],
     [-1,0,1],
     [-2,-1,0]]

# Detects West Direction edge     
W = [[1,2,1],
     [0,0,0],
     [-1,-2,-1]]

# Detects West-South Direction edge     
WS = [[2,1,0],
     [1,0,-1],
     [0,-1,-2]]

# Detects South Direction edge     
S = [[1,0,-1],
     [2,0,-2],
     [1,0,-1]]

# Detects South-East Direction edge     
SE = [[0,-1,-2],
     [1,0,-1],
     [2,1,0]]

# Detects East Direction edge     
E = [[-1,-2,-1],
     [0,0,0],
     [1,2,1]]

# Detects North-East Direction edge     
NE = [[-2,-1,0],
     [-1,0,1],
     [0,1,2]]                                         
       
H = int(len(N))

for i in range(0, height-H):
    for j in range(0, width-H):
        summ = 0
        for k in range(0, H):
            for l in range(0, H):
                summ = summ + NE[k][l]*img[i+k][j+l]  
        if(summ[0]>255):
           summ = [255,255,255]
        elif(summ[0]<0):
           summ = [0,0,0]          
        img[i][j] = summ  
            

cv2.imshow('image',img)
cv2.waitKey(0)               
