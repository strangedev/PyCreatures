"""
#rant
Contains dirty workarounds for broken libraries.
Why do I even have to do this @_@
I mean seriously, how hard can it be to implement
your methods to support all kinds of ndimages?
And even if you're too lazy or don't give a f***,
you could at least document your limitations!
I strongly advise against using scipy or skimage for anything.
#endrant
"""

import numpy
from skimage import exposure, color

__author__ = "5966916: Noah Hummel, 5987733: Kyle Rinfreschi"


def rgb2grey_fixed(arr):
    """
    skimage converts uint8 to float by default, which is annoying.
    """

    grey = color.rgb2grey(arr)

    if grey.max() <= 1:
        grey *= 255  # stupid skimage converting to 0-1 *mumble mumble*

    return numpy.uint8(grey)


def grey2rgb_fixed(arr):
    """
    skimage converts uint8 to float by default, which is annoying.
    """

    rgb = color.gray2rgb(arr)

    if rgb.max() <= 1:
        rgb *= 255  # stupid skimage converting to 0-1 *mumble mumble*

    return numpy.uint8(rgb)


def normalize_intensity_p298(arr):
    """
    skimage exposure does contrast stretching, but it's broken for
    L-Value images. This is a dirty workaround.
    """

    if len(arr.shape) == 2:
        arr = grey2rgb_fixed(arr)

    p2, p98 = numpy.percentile(arr, (2, 98))
    normalized = exposure.rescale_intensity(
        arr, in_range=(p2, p98))

    if len(arr.shape) == 2:
        arr = rgb2grey_fixed(arr)

    return normalized
