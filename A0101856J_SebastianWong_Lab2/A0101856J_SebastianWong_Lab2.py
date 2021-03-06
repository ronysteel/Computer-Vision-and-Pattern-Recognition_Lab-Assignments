import numpy as np
import cv2
from matplotlib import pyplot as plt

figureCdf = plt.figure(1)
figureHistogram = plt.figure(2)
# read an image in greyscale
img = cv2.imread("pic5.jpg", cv2.CV_LOAD_IMAGE_GRAYSCALE)
# Computes array values of histogram and occurrences of input data
# that fall within each bin
hist,bins = np.histogram(img.flatten(),256,[0,256])
# Computing cummulative distribution function
cdf = hist.cumsum()
# two rows, 1 column, 1st row diagram
plt.figure(1)
cdfDiagram = figureCdf.add_subplot(2,1,1)
cdfDiagram = plt.plot(cdf, color = 'b', label = 'cdf')
cdfDiagram = plt.xlim([0,256])
cdfDiagram = plt.legend(loc = 'upper left')
plt.figure(2)
histogram = figureHistogram.add_subplot(2,1,1)
# plotting normalized cdf with histogram
histogram = plt.hist(img.flatten(),256,[0,256], color = 'r',label = 'histogram')
histogram = plt.xlim([0,256])
histogram = plt.legend(loc = 'upper left')
# Find minimum histogram value excluding 0
# mask where value in array is 0
cdfMasked = np.ma.masked_equal(cdf,0)
# Applying Histogram Equalization formula
cdfMasked = (cdfMasked - cdfMasked.min())*255/(cdfMasked.max()-cdfMasked.min())
# Fill mask array with 0s
# Fill as uint8 for images with 256 intensity levels
cdf = np.ma.filled(cdfMasked,0).astype('uint8')
imgEqualized = cdf[img]
hist,bins = np.histogram(imgEqualized.flatten(),256,[0,256])
cdfEqualized = hist.cumsum()
plt.figure(1)
cdfEqualizedDiagram = figureCdf.add_subplot(2,1,2)
cdfEqualizedDiagram = plt.plot(cdfEqualized, color = 'b', label = 'cdf after equalization')
cdfEqualizedDiagram = plt.xlim([0,256])
cdfEqualizedDiagram = plt.legend(loc = 'upper left')
plt.figure(2)
histogramEqualized = figureHistogram.add_subplot(2,1,2)
histogramEqualized = plt.hist(imgEqualized.flatten(),256,[0,256], color = 'r', label = 'histogram after equalization')
histogramEqualized = plt.xlim([0,256])
histogramEqualized = plt.legend(loc = 'upper left')
plt.show()
# printing two images side by side
# left is before histogram equalization, right is after
result = np.hstack((img,imgEqualized))
cv2.imwrite("resultforpic5.jpg",result)