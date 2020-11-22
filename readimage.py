# Import necessary libraries
import numpy as np
from PIL import Image

# Read our image and convert into a Numpy Array
img = Image.open('Food.JPG')
array = np.array(img)

# Print the size of our image
print(array.shape)
print(array)