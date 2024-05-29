import numpy as np
import matplotlib.pyplot as plt
import sys
import scipy
import time
# Load the image into a 3D matrix
image = plt.imread("tiger.jpg")
print(np.shape(image))
# Convert the image to a 2D matrix (grayscale)
# The axis=2 argument tells numpy.mean() to average values across all three color channels.
# (axis=0 would average across pixel rows and axis=1 would average across pixel columns.)
gray_image = np.mean(image, axis=2)
print(np.shape(gray_image))
library = sys.argv[2]
start = time.time()
# Singular Value Decomposition with numpy
if library == "numpy":
    U, S, Vt = np.linalg.svd(gray_image)
    print(np.shape(S))
if library == "scipy":
    U, S, Vt = np.linalg.svd(gray_image)
print(np.shape(S))
# Set the number of singular values to keep (compression level)
end = time.time()
print("The SVD opreration with", sys.argv[2], "took:", end-start)
r = 0
#print(S)
epsilon = float(sys.argv[1])
for i in range(0,np.shape(S)[0]):
    if (S[i]/S[0] > epsilon):
        r = r+1
    else:
        break
#print(r, "----")

# Reconstruct the compressed image using the selected singular values
compressed_image = np.dot(U[:, :r], np.dot(np.diag(S[:r]), Vt[:r, :]))
print(np.shape(compressed_image))
# Plot the original and compressed images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(gray_image - compressed_image, cmap='gray')
plt.title("Absolute error with original image")

plt.subplot(1, 2, 2)
plt.imshow(compressed_image, cmap='gray')
plt.title("Compressed Image (r = {})".format(r))

plt.show()
