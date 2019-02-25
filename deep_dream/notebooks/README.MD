All code is in deepdream.ipynb. The primary modifications to the original algorithm in the notebook are as follows:

Cell labeled 160: Layer 41 is calculated at a low frequency, while Layer 139 is calculated at a high frequency, and blended together.

Cell labeled 149: The building layer is filtered with a Gaussian low-pass filter, so it has only low frequencies. The dog layer is filtered with a Gaussian low-pass filter which is then subtracted out, so it has only high freqencies. After experimenting with the sigma values for the filters, we combine these two images - the result is a hybrid image that includes more visible dog-like features from up close, but building-like features are more visible from farther away.

Cell labeled 156: We decided to implement a “dream sharpening” function. We experimented with different smoothing filters such as Laplacian smoothing, low-pass filtering, and Savitsky-Golay smoothing. All of these methods blur the edges and corners of an object; we realized that subtracting this edges-blurred version of the dream from the original dream creates an image X consisting of only the sharp edges and corners. We then added this image X to the original image, resulting in the edges and corners being much sharper than before. The result of this is that the dream now relies less on the original input image and more on the applied dream layer features.
