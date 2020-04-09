import cv2
import numpy
from data_information import dcm_information as di
imgOrig = di.load_dcm("../datasets/OriginalCT/Imagem{}.dcm".format(z))

