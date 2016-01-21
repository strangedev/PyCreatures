import ImageManipulator
import ModalInputGUI

import tkinter
from PIL import ImageTk
from tkinter.filedialog import askopenfilename, asksaveasfile
import webbrowser

__author__ = "5966916: Noah Hummel, 5987733: Kyle Rinfreschi"

MAX_WIN_WIDTH = 1000  # Hard coded and ugly.
MAX_WIN_HEIGHT = 800
MIN_WIN_WIDTH = 640  # I really didn't have time for this.
MIN_WIN_HEIGHT = 480


class EditorGUI(tkinter.Frame):

    """
    Displays all of the GUI elements.
    """

    def __init__(self, parent):
        """
        Inits frame by adding menu bar.
        """

        tkinter.Frame.__init__(self, parent)

        self.parent = parent
        self.man = ImageManipulator.ImageManipulator()

        #  This sets the window title
        self.parent.title("RickAstleyEdit")

        #  Create child frames
        self.menubar = tkinter.Menu(self)

        self.filemenu = tkinter.Menu(self.menubar, tearoff=1)
        self.filemenu.add_command(label="Open", command=self.open_file)
        self.filemenu.add_command(label="Save", command=self.save_file)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.parent.quit)
        self.menubar.add_cascade(label="File", menu=self.filemenu)

        self.editmenu = tkinter.Menu(self.menubar, tearoff=1)
        self.editmenu.add_command(label="Undo", command=self.perform_undo)
        self.editmenu.add_command(label="Redo", command=self.perform_redo)
        self.editmenu.add_separator()
        self.editmenu.add_command(label="Magic", command=self.perform_magic)
        self.editmenu.add_separator()
        self.editmenu.add_command(
            label="Flip horizontally", command=self.flip_horizontal)
        self.editmenu.add_command(
            label="Flip vertically", command=self.flip_vertical)
        self.editmenu.add_command(
            label="Scale by factor", command=self.scale_by_factor)
        self.editmenu.add_command(
            label="Scale to size", command=self.scale_to_size)
        self.menubar.add_cascade(label="Edit", menu=self.editmenu)

        self.colormenu = tkinter.Menu(self.menubar, tearoff=1)
        self.colormenu.add_command(label="Grayscale", command=self.grayscale)
        self.colormenu.add_separator()
        self.colormenu.add_command(
            label="Invert colors", command=self.invert_colors)
        self.colormenu.add_command(
            label="Contrast strech", command=self.contrast_stretch)
        self.colormenu.add_command(
            label="Threshold", command=self.threshold)
        self.menubar.add_cascade(label="Color", menu=self.colormenu)

        self.filtermenu = tkinter.Menu(self.menubar, tearoff=1)
        self.filtermenu.add_command(
            label="Sobel edge-detection", command=self.sobel)
        self.filtermenu.add_command(
            label="Laplace edge-detection", command=self.laplace)
        self.filtermenu.add_separator()
        self.filtermenu.add_command(
            label="Median blur", command=self.median_blur)
        self.filtermenu.add_command(
            label="Gaussian blur", command=self.gaussian_blur)
        self.menubar.add_cascade(label="Filters", menu=self.filtermenu)

        self.analyticsmenu = tkinter.Menu(self.menubar, tearoff=1)
        self.analyticsmenu.add_command(
            label="Histogram", command=self.histogram)
        self.analyticsmenu.add_command(
            label="Fourier transform", command=self.fft)
        self.menubar.add_cascade(label="Analytics", menu=self.analyticsmenu)

        self.parent.config(menu=self.menubar)

        self.canvas = tkinter.Label(self)
        self.canvas.pack()
        self.pack(fill=tkinter.BOTH, expand=1)

    def open_file(self):
        """
        Displays a file dialog for opening a file.
        Called as UI callback by tkinter.
        """

        fname = askopenfilename(filetypes=[
            ("All files", "*.*")], initialdir="./")
        if fname:
            self.man.load_image_from_file(fname)
            self.draw_image()

    def save_file(self):
        """
        Displays a file dialog for saving a file.
        Called as UI callback by tkinter.
        """

        f = asksaveasfile(mode='w', defaultextension=".png")
        if f:
            self.man.save_image_to_file(f.name)

    def draw_image(self):
        """
        Updates the image widget according to the current
        contents of ImageManipulator.
        """

        photo = ImageTk.PhotoImage(self.man.image_rendered)

        self.canvas.image = photo
        self.canvas.configure(image=photo)

        w, h = self.man.image_rendered.size

        w = w if w < MAX_WIN_WIDTH else MAX_WIN_WIDTH  # keep dimensions
        h = h if h < MAX_WIN_HEIGHT else MAX_WIN_HEIGHT  # within bounds.
        w = w if w > MIN_WIN_WIDTH else MIN_WIN_WIDTH
        h = h if h > MIN_WIN_HEIGHT else MIN_WIN_HEIGHT

        self.parent.geometry(str(w + 50) + "x" + str(h + 50))

    # The following are GUI callback methods
    # Trivial stuff *mumble*
    # Nothing to see here, move along!

    def perform_undo(self):

        self.man.perform_undo()
        self.draw_image()

    def perform_redo(self):

        self.man.perform_redo()
        self.draw_image()

    def invert_colors(self):

        self.man.invert_colors()
        self.draw_image()

    def grayscale(self):

        self.man.grayscale()
        self.draw_image()

    def flip_horizontal(self):

        self.man.flip_horizontal()
        self.draw_image()

    def flip_vertical(self):

        self.man.flip_vertical()
        self.draw_image()

    # Some methods have a separate callback method
    # that is called from a modal dialog.

    def scale_by_factor(self):

        self.w = ModalInputGUI.ModalScaleByFactor(
            self, self.scale_by_factor_callback)
        self.parent.wait_window(self.w.top)

    def scale_by_factor_callback(self, scaling_factor):

        self.man.scale_by_factor(scaling_factor)
        self.draw_image()

    def scale_to_size(self):

        self.w = ModalInputGUI.ModalScaleToSize(
            self, self.scale_to_size_callback)
        self.parent.wait_window(self.w.top)

    def scale_to_size_callback(self, width, height):

        self.man.scale_to_size(width, height)
        self.draw_image()

    def fft(self):

        self.man.fft()
        self.draw_image()

    def sobel(self):

        self.man.sobel()
        self.draw_image()

    def laplace(self):

        self.w = ModalInputGUI.ModalLaplace(
            self, self.laplace_callback)
        self.parent.wait_window(self.w.top)

    def laplace_callback(self, sigma):

        self.man.laplace(sigma=sigma)
        self.draw_image()

    def contrast_stretch(self):

        self.man.contrast_stretch()
        self.draw_image()

    def median_blur(self):

        self.w = ModalInputGUI.ModalMedianBlur(
            self, self.median_blur_callback)
        self.parent.wait_window(self.w.top)

    def median_blur_callback(self, kernel_size):

        self.man.median_blur(size=kernel_size)
        self.draw_image()

    def gaussian_blur(self):

        self.w = ModalInputGUI.ModalGaussianBlur(
            self, self.gaussian_blur_callback)
        self.parent.wait_window(self.w.top)

    def gaussian_blur_callback(self, sigma):

        self.man.gaussian_blur(sigma=sigma)
        self.draw_image()

    def histogram(self):

        self.man.histogram()
        self.draw_image()

    def threshold(self):

        self.w = ModalInputGUI.ModalThresholding(
            self, self.threshold_callback)
        self.parent.wait_window(self.w.top)

    def threshold_callback(self, mode, threshold):

        self.man.threshold(threshold, mode=mode)
        self.draw_image()

    def perform_magic(self):

        webbrowser.open("https://www.youtube.com/watch?v=oHg5SJYRHA0")
        # Never gonna give you up
        # Never gonna let you down
        # Never gonna run around and desert you
        # Never gonna make you cry
        # Never gonna say goodbye
        # Never gonna tell a lie and hurt you
