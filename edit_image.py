import numpy as np
import cv2
from matplotlib import pyplot as plt
img = cv2.imread("/home/adriell/Documentos/Sem título.png")
imgclone=img.copy()
imgclone[imgclone < 120] = 0
cv2.imshow('testadno', imgclone)
# img=img+170
# img[img<=70]=0
# rows,cols=img.shape[:2]
#
# for row in range(rows):
#     for col in range(cols):
#         valor=img[row,col]
#         if img[row,col]>190:
#             img[row,col]=255
#
#         # if img[row,col]>190:
#         #     img[row,col]=valor-100
# cv2.imshow('teste',img)
# cv2.imwrite('testando.png',img)
# cv2.waitKey(0)


    # define criteria, number of clusters(K) and apply kmeans()
    # img=np.array((img),dtype=float,axis=None)
    # image=np.zeros((img.shape[:2]),np.uint8)
    # image=img
    # image=np.float32(image)
    # image=np.array
    # image=np(image)
    # img=np.float32(img)
    # img=img.ravel()
    # Z = img.reshape((-1, 3))
K=5
Z = img.reshape((-1, 3))
Z=np.float32(Z)

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)


ret, label, center = cv2.kmeans(Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    # Now convert back into uint8, and make original image
center = np.uint8(center)
res = center[label.flatten()]
res2 = res.reshape((img.shape))

cv2.imshow('res2', res2)
cv2.waitKey(0)
cv2.imwrite('usar.png',res2)
cv2.destroyAllWindows()