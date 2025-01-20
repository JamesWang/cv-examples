import numpy as np
from numpy import ndarray


def build_sample_image():
    """Builds a sample image with 50x50 regions of different tones of gray"""

    # Define the different tones.
    # The end of interval is not included
    tones: ndarray = np.arange(start=50, stop=300, step=50)

    # Initialize result with the first 50x50 region with 0-intensity level
    result: ndarray = np.zeros((50, 50, 3), dtype="uint8")

    # Build the image concatenating horizontally the regions:
    for tone in np.nditer(tones):  # get iterator of ndarray
        img = np.ones((50, 50, 3), dtype="uint8") * tone
        result = np.concatenate((result, img), axis=1)
    return np.float32(result)


'''
Result looks like:
[[[  0   0   0]
  [  0   0   0]
  [  0   0   0]
  ...
  [250 250 250]
  [250 250 250]
  [250 250 250]]

 [[  0   0   0]
  [  0   0   0]
  [  0   0   0]
  ...
  [250 250 250]
  [250 250 250]
  [250 250 250]]

 [[  0   0   0]
  [  0   0   0]
  [  0   0   0]
  ...
  [250 250 250]
  [250 250 250]
  [250 250 250]]

 ...

 [[  0   0   0]
  [  0   0   0]
  [  0   0   0]
  ...
  [250 250 250]
  [250 250 250]
  [250 250 250]]

 [[  0   0   0]
  [  0   0   0]
  [  0   0   0]
  ...
  [250 250 250]
  [250 250 250]
  [250 250 250]]

 [[  0   0   0]
  [  0   0   0]
  [  0   0   0]
  ...
  [250 250 250]
  [250 250 250]
  [250 250 250]]]
'''