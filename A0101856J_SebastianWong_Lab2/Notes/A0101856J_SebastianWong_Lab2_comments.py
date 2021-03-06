import numpy as np
import cv2
from matplotlib import pyplot as plt

# for displaying histograms at the end of program
figure = plt.figure()
# read an image in greyscale
img = cv2.imread("pic1.jpg", cv2.CV_LOAD_IMAGE_GRAYSCALE)
# Computes array values of histogram and occurrences of input data
# that fall within each bin
hist,bins = np.histogram(img.flatten(),256,[0,256])
# Computing cummulative distribution function
cdf = hist.cumsum()
# two rows, 1 column, 1st row diagram
histogram = figure.add_subplot(2,1,1)
# Compute and draw the histogram of img with 256 bins
# range from 0-256
histogram = plt.hist(img.flatten(),256,[0,256], color = 'r',label = 'histogram')
# set the limits of the x axes
histogram = plt.xlim([0,256])
# include the legend in the plot
histogram = plt.legend(loc = 'upper left')
# Find minimum histogram value excluding 0
# mask where value in array is 0
cdfMasked = np.ma.masked_equal(cdf,0)
# Applying Histogram Equalization formula
cdfMasked= (cdfMasked - cdfMasked.min())*255/(cdfMasked.max()-cdfMasked.min())
# Fill mask array with 0s
# Fill as uint8 for images with 256 intensity levels
cdf = np.ma.filled(cdfMasked,0).astype('uint8')
imgEqualized = cdf[img]
# Computes new array values of histogram
hist,bins = np.histogram(imgEqualized.flatten(),256,[0,256])
#cdfEqualized = hist.cumsum()
histogramEqualized = figure.add_subplot(2,1,2)
histogramEqualized = plt.hist(imgEqualized.flatten(),256,[0,256], color = 'r', label = 'histogram after equalization')
histogramEqualized = plt.xlim([0,256])
histogramEqualized = plt.legend(loc = 'upper left')
plt.show()
# printing two images side by side
# left is before histogram equalization, right is after
# histogram equalization
result = np.hstack((img,imgEqualized))
cv2.imwrite("resultforpic1.jpg",result)