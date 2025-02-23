# cv-examples
### Gaussian Filtering
- The Gaussian Smoothing Operator performs a **weighted average** of surrounding pixels
  based on the Gaussian noise and is a realistic model of de-focused lense
  - Sigma defines the amount of blurring.
  ![img.png](gaussian_filtering.png)
- Examples
  - ![gaussian.png](./images/results/otsu_filter_noise.png)

### HPFs and LPFs
- HPF - High-pass Filter: allow high frequency pass
  - In an image, edges are high frequency components. in OpenCV, examples include:
    - Laplacian
    - Sobel
    - Scharr
- LPF - Low-pass Filter: allow low frequency pass
  - LPF will smoothen the pixel if the difference with the surrounding pixels 
    is lower than a certain threshold.
  - Used for:
    - De-noising
    - Blurring(i.e. Gaussian blur)

### Color models
- Color model in computing are called **additive** models, they deal with lights
- Paints follow subtractive color model

### Fourier transform
- All waveforms are just the sum of simple sinusoids of different frequencies
- NumPy has a **fast Fourier transform(FFT)**
- DFT - discrete Fourier transform

### Kernel
- Kernels are square numerical metrics. can be used to blur or sharpen images
  - Determine how each output pixel is calculated from a neighbourhood of input pixels.
  - also called: **Convolution Matrix**
- A kernel is a set of weights that are applied to a region in a source image to generate a single pixel in the destination image.
- hdf = orig_img - blurred_image  (differential HPF)
  - obtaining an HPF by applying an LPF and calculating the difference between the original image
- HPF boosts the intensity of a pixel, given its difference with neighbors 
- LPF will smoothen the pixel if the difference from surrounding pixels is lower than a certain threshold
### Noise
- Noise in images or videos, defined as the undesired variation of intensity and color of pixels.
- Signal-to-noise ration:
  ```
  Signal to Noise Ratio = (Power of Signal)/(Power of Noise)
  ```
- Normally distributed noise is called **Gaussian Noise**
```
  -- add Gaussian Noise to image
  row, col = img.shape
  img = img.astype(np.float32)
  mean = 0
  var = 0.1
  sigma = var**0.5
  gauss = np.random.normal(mean, sigma, (row, col))
  gauss = gauss.reshape(row, col)
  noisy = img + gauss
```