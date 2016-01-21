import ImageHistory
import ImageUtils

import numpy
from scipy import ndimage
from scipy import misc
import PIL
from matplotlib import pyplot

__author__ = "5966916: Noah Hummel, 5987733: Kyle Rinfreschi"


class ImageManipulator(object):
    """
    Keeps the image data as ndarray and as PIL.Image.
    Also keeps track of editing steps.
    Provides high-level access to various image processing methods.
    """

    def __init__(self):

        self._image_history = ImageHistory.ImageHistory()
        self._image_rendered = None

        self._image_data_updated = False  # When this is set,
        # self.image_rendered will re-convert the image by calling
        # self._render_image.

    def load_image_from_file(self, path):
        """
        Loads an image from path.
        """

        try:

            img_data = ndimage.imread(path)
            self._image_history.advance_state(img_data, "File load")

            self._image_data_updated = True

        except Exception as e:
            print(e)

    def save_image_to_file(self, path):
        """
        Saves an image at path.
        """

        try:

            self.image_rendered.save(path)

        except Exception as e:
            print(e)

    def _render_image(self):
        """
        Converts the internal ndarray representation to PIL.Image for
        displaying with tkinter.
        This is called automatically by the image_rendered getter method.
        """

        self._image_rendered = PIL.Image.fromarray(
            numpy.uint8(self.image_array))

        self._image_data_updated = False

    def _update_image_data(self, data, label):
        """
        Setter method for self.image_array.
        Ties in with ImageHistory to track editing steps and flags the
        image data as dirty.
        """

        self._image_history.advance_state(data, label)
        self._image_data_updated = True

    def perform_undo(self):
        """
        Undoes the previous action by getting the previous state from
        ImageHistory. Flags image data as dirty.
        """

        if self._image_history.undo_available:

            self._image_history.restore_past_state()
            self._image_data_updated = True

    def perform_redo(self):
        """
        Reverts the previous undo by getting the original state from
        ImageHistory. Flags image data as dirty.
        """

        if self._image_history.redo_available:

            self._image_history.restore_future_state()
            self._image_data_updated = True

    @property
    def image_rendered(self):
        """
        Getter method for self.image_rendered.
        Converts self.image_array to PIL.Image when _image_data_updated
        is set. This is so that Conversion can happen lazily.
        """
        if self._image_data_updated:
            self._render_image()
        return self._image_rendered

    @property
    def image_array(self):
        """
        Getter method for self.image_array.
        This is as close as we can get to using pointers lol.
        """
        return self._image_history.current

    def scale_by_factor(self, factor, interpolation="bilinear"):
        """
        Scales image by a given factor.
        Uses bilinear interpolation by default.
        """

        scaled = misc.imresize(self.image_array, factor, interpolation)
        self._update_image_data(scaled, "Image scaling")

    def scale_to_size(self, x, y, interpolation="bilinear"):
        """
        Scales image desired dimensions (x, y).
        Uses bilinear interpolation by default.
        """

        scaled = misc.imresize(self.image_array, (x, y), interpolation)
        self._update_image_data(scaled, "Image scaling")

    def invert_colors(self):
        """
        Inverts the colors of the image.
        """

        inverted = numpy.invert(numpy.uint8(self.image_array))
        self._update_image_data(inverted, "Invert colors")

    def grayscale(self):
        """
        Converts RGB values of the image to luminosity values, thus giving
        the image a 'grayscale' effect.
        """

        grey = ImageUtils.rgb2grey_fixed(self.image_array)
        self._update_image_data(grey, "Grayscale")

    def flip_horizontal(self):
        """
        Reverses the image along it's vertical axis.
        I know, confusing right? I didn't invent this naming convention.
        """

        flipped = numpy.fliplr(self.image_array)
        self._update_image_data(flipped, "Flip horizontally")

    def flip_vertical(self):
        """
        Reverses the image along it's horizontal axis.
        """

        flipped = numpy.flipud(self.image_array)
        self._update_image_data(flipped, "Flip vertically")

    def fft(self):
        """
        Converts the color to l-values, then calculates the 2 dimensional
        Fourier transform.
        Displays the values shifted to the center of the image, on a
        logarithmic scale.
        """

        gray = ImageUtils.rgb2grey_fixed(self.image_array)

        transformed = numpy.fft.fft2(gray)
        fshift = numpy.fft.fftshift(transformed)
        fshift = 20 * numpy.log(numpy.abs(fshift))
        fshift += fshift.min()
        fshift *= (255 / fshift.max())

        pyplot.figure(1)
        pyplot.subplot(121)
        pyplot.imshow(gray, cmap="gray")
        pyplot.title("Input image")

        pyplot.subplot(122)
        pyplot.imshow(fshift, cmap="Set1")
        pyplot.title("Fourier transformation")
        pyplot.show()

    def sobel(self):
        """
        Performs the sobel operator in x and y direction and combines the
        output. The output is normalized by using contrast_stretch.
        """

        gray = ImageUtils.rgb2grey_fixed(self.image_array) / 255

        sobel_x = ndimage.sobel(gray, 0)
        sobel_y = ndimage.sobel(gray, 1)
        sobel_xy = numpy.hypot(sobel_x, sobel_y)
        sobel_xy = ImageUtils.normalize_intensity_p298(sobel_xy)
        # sobel_xy *= (255 / sobel_xy.max())
        sobel_xy = ImageUtils.rgb2grey_fixed(sobel_xy)

        self._update_image_data(sobel_xy, "Sobel edge-detection")

    def laplace(self, sigma=1):
        """
        Performs the laplacian filter based on gaussian derivatives.
        This allows for controlling the level of detail in the output image.
        """

        gray = ImageUtils.rgb2grey_fixed(self.image_array)
        laplace = ndimage.gaussian_laplace(gray, sigma)
        self._update_image_data(laplace, "Laplace edge-detection")

    def median_blur(self, size=5):
        """
        Performs a median filter on the image with a convolution kernel of
        a given size.
        """

        if len(self.image_array.shape) == 2:
            blurred = ndimage.median_filter(self.image_array, size=size)
        else:

            r = self.image_array[:, :, 0]
            g = self.image_array[:, :, 1]
            b = self.image_array[:, :, 2]

            r = ndimage.median_filter(r, size=size)
            g = ndimage.median_filter(g, size=size)
            b = ndimage.median_filter(b, size=size)

            blurred = numpy.empty(self.image_array.shape)
            blurred[:, :, 0] = r
            blurred[:, :, 1] = g
            blurred[:, :, 2] = b
            blurred = numpy.uint8(blurred)

        self._update_image_data(blurred, "Median blur")

    def gaussian_blur(self, sigma=2):
        """
        Performs a gaussian filter in the image with a given standard deviation
        of sigma. By default, sigma is set to 2.
        """

        # Why do I even have to check these things? @_@
        # Talk about well designed libraries...
        # Apparently, gaussian blur is too stupid to handle
        # ndarrays, it'll just put out a greyscale image no matter what.

        if len(self.image_array.shape) == 2:
            blurred = ndimage.gaussian_filter(
                self.image_array, sigma=sigma)
        else:

            r = self.image_array[:, :, 0]
            g = self.image_array[:, :, 1]
            b = self.image_array[:, :, 2]

            r = ndimage.gaussian_filter(r, sigma=sigma)
            g = ndimage.gaussian_filter(g, sigma=sigma)
            b = ndimage.gaussian_filter(b, sigma=sigma)

            blurred = numpy.empty(self.image_array.shape)
            blurred[:, :, 0] = r
            blurred[:, :, 1] = g
            blurred[:, :, 2] = b
            blurred = numpy.uint8(blurred)

        self._update_image_data(blurred, "Gaussian blur")

    def threshold(self, threshold, mode="binary"):

        gray = ImageUtils.rgb2grey_fixed(self.image_array)

        print(mode)

        if mode == "binary":

            for i in range(len(gray)):
                gray[i] = [(0 if x < threshold else 255) for x in gray[i]]

        elif mode == "binary_inverted":

            for i in range(len(gray)):
                gray[i] = [(255 if x < threshold else 0) for x in gray[i]]

        elif mode == "drop_smaller_to_zero":

            for i in range(len(gray)):
                gray[i] = [(0 if x < threshold else x) for x in gray[i]]

        elif mode == "raise_smaller_to_max":

            for i in range(len(gray)):
                gray[i] = [(255 if x < threshold else x) for x in gray[i]]

        elif mode == "drop_bigger_to_zero":

            for i in range(len(gray)):
                gray[i] = [(0 if x > threshold else x) for x in gray[i]]

        elif mode == "raise_bigger_to_max":

            for i in range(len(gray)):
                gray[i] = [(255 if x > threshold else x) for x in gray[i]]

        elif mode == "clip_bigger":

            for i in range(len(gray)):
                gray[i] = [(threshold if x > threshold else x)
                           for x in gray[i]]

        elif mode == "raise_smaller":

            for i in range(len(gray)):
                gray[i] = [(threshold if x < threshold else x)
                           for x in gray[i]]

        self._update_image_data(gray, "Threshold")

    def contrast_stretch(self):
        """
        Rescales the intensity values of the image based on the 2 and 98
        percentiles.
        """

        normalized = ImageUtils.normalize_intensity_p298(self.image_array)
        self._update_image_data(normalized, "Contrast stretch")

    def histogram(self):
        """
        Calculates the histogram of the image.
        """

        if len(self.image_array.shape) == 2:

            pyplot.hist(self.image_array.flatten(), bins=255,
                        color='black', label='Luminosity')
            pyplot.title("Histogram for L-Channel")
            pyplot.xlabel("Intensity")
            pyplot.ylabel("Count")
            pyplot.legend()
            pyplot.show()

        else:

            r = self.image_array[:, :, 0].flatten()
            g = self.image_array[:, :, 1].flatten()
            b = self.image_array[:, :, 2].flatten()

            pyplot.hist(r, bins=255,  color='r', label='R')
            pyplot.hist(g, bins=255,  color='g', label='G')
            pyplot.hist(b, bins=255,  color='b', label='B')
            pyplot.title("Histogram for RGB-Channels")
            pyplot.xlabel("Intensity")
            pyplot.ylabel("Count")
            pyplot.legend()
            pyplot.show()
