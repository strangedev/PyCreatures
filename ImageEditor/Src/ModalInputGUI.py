"""
Contains modal dialoges for tkinter.
The class names are self explaining.
Modal dialoges present a number of inputs and call a callback
function which is passed in __init__.
"""

import tkinter

__author__ = "5966916: Noah Hummel, 5987733: Kyle Rinfreschi"


class ModalScaleByFactor(object):

    def __init__(self, parent, callback):
        top = self.top = tkinter.Toplevel(parent)
        self.l = tkinter.Label(top, text="Scaling options:")
        self.l.grid(row=0, column=0, sticky=tkinter.W)

        self.callback = callback

        self.input_label = tkinter.Label(top, text="Scaling factor: ")
        self.input_label.grid(row=1, column=0, sticky=tkinter.W)
        self.input_entry = tkinter.Entry(top)
        self.input_entry.grid(row=1, column=1, sticky=tkinter.W)

        self.submit_button = tkinter.Button(
            top, text='Ok', command=self.cleanup)
        self.submit_button.grid(
            row=2,
            columnspan=2,
            sticky=tkinter.W + tkinter.E + tkinter.N + tkinter.S)

    def cleanup(self):

        try:
            self.callback(float(self.input_entry.get()))
        except Exception as e:
            print(e)

        self.top.destroy()


class ModalScaleToSize(object):

    def __init__(self, parent, callback):
        top = self.top = tkinter.Toplevel(parent)
        self.l = tkinter.Label(top, text="Scaling options:")
        self.l.grid(row=0,
                    column=0,
                    pady=10,
                    sticky=tkinter.W + tkinter.E + tkinter.N + tkinter.S)

        self.callback = callback

        self.input_label_w = tkinter.Label(top, text="Width: ")
        self.input_label_w.grid(row=1, column=0, sticky=tkinter.W)
        self.input_entry_w = tkinter.Entry(top)
        self.input_entry_w.grid(row=1, column=1, sticky=tkinter.W)

        self.input_label_h = tkinter.Label(top, text="Height: ")
        self.input_label_h.grid(row=2, column=0, sticky=tkinter.W)
        self.input_entry_h = tkinter.Entry(top)
        self.input_entry_h.grid(row=2, column=1, sticky=tkinter.W)

        self.submit_button = tkinter.Button(
            top, text='Ok', command=self.cleanup)
        self.submit_button.grid(
            row=3,
            columnspan=2,
            sticky=tkinter.W + tkinter.E + tkinter.N + tkinter.S)

    def cleanup(self):

        try:
            self.callback(int(self.input_entry_w.get()),
                          int(self.input_entry_h.get()))
        except Exception as e:
            print(e)

        self.top.destroy()


class ModalGaussianBlur(object):

    def __init__(self, parent, callback):
        top = self.top = tkinter.Toplevel(parent)
        self.l = tkinter.Label(top, text="Gaussian blur options:")
        self.l.grid(row=0,
                    column=0,
                    pady=10,
                    sticky=tkinter.W + tkinter.E + tkinter.N + tkinter.S)

        self.callback = callback

        self.input_label = tkinter.Label(top, text="Sigma (std. deviation): ")
        self.input_label.grid(row=1, column=0, sticky=tkinter.W)
        self.input_entry = tkinter.Entry(top)
        self.input_entry.grid(row=1, column=1, sticky=tkinter.W)
        self.input_entry.insert(0, "2")

        self.submit_button = tkinter.Button(
            top, text='Ok', command=self.cleanup)
        self.submit_button.grid(
            row=2,
            columnspan=2,
            sticky=tkinter.W + tkinter.E + tkinter.N + tkinter.S)

    def cleanup(self):

        try:
            self.callback(int(self.input_entry.get()))
        except Exception as e:
            print(e)

        self.top.destroy()


class ModalMedianBlur(object):

    def __init__(self, parent, callback):
        top = self.top = tkinter.Toplevel(parent)
        self.l = tkinter.Label(top, text="Median blur options:")
        self.l.grid(row=0,
                    column=0,
                    pady=10,
                    sticky=tkinter.W + tkinter.E + tkinter.N + tkinter.S)

        self.callback = callback

        self.input_label = tkinter.Label(
            top, text="Kernel size (diameter^2): ")
        self.input_label.grid(row=1, column=0, sticky=tkinter.W)
        self.input_entry = tkinter.Entry(top)
        self.input_entry.grid(row=1, column=1, sticky=tkinter.W)
        self.input_entry.insert(0, "9")

        self.submit_button = tkinter.Button(
            top, text='Ok', command=self.cleanup)
        self.submit_button.grid(
            row=2,
            columnspan=2,
            sticky=tkinter.W + tkinter.E + tkinter.N + tkinter.S)

    def cleanup(self):

        try:
            self.callback(int(self.input_entry.get()))
        except Exception as e:
            print(e)

        self.top.destroy()


class ModalThresholding(object):

    def __init__(self, parent, callback):
        top = self.top = tkinter.Toplevel(parent)
        self.l = tkinter.Label(top, text="Thresholding options:")
        self.l.grid(row=0,
                    column=0,
                    pady=10,
                    sticky=tkinter.W + tkinter.E + tkinter.N + tkinter.S)

        self.callback = callback

        self.binary = tkinter.IntVar()
        self.binary_inverted = tkinter.IntVar()
        self.drop_smaller_to_zero = tkinter.IntVar()
        self.raise_smaller_to_max = tkinter.IntVar()
        self.drop_bigger_to_zero = tkinter.IntVar()
        self.raise_bigger_to_max = tkinter.IntVar()
        self.clip_bigger = tkinter.IntVar()
        self.raise_smaller = tkinter.IntVar()

        self.input_label_m = tkinter.Label(
            top, text="Mode: (binary if multiple are chosen)")
        self.input_label_m.grid(row=1, column=0, sticky=tkinter.W)
        self.cb1 = tkinter.Checkbutton(
            top, text="Binary", variable=self.binary)
        self.cb1.grid(row=2, column=0, sticky=tkinter.W)
        self.cb1 = tkinter.Checkbutton(
            top, text="Binary Inverted", variable=self.binary_inverted)
        self.cb1.grid(row=3, column=0, sticky=tkinter.W)
        self.cb1 = tkinter.Checkbutton(
            top, text="Drop smaller to 0", variable=self.drop_smaller_to_zero)
        self.cb1.grid(row=4, column=0, sticky=tkinter.W)
        self.cb1 = tkinter.Checkbutton(
            top, text="Raise smaller to 255",
            variable=self.raise_smaller_to_max)
        self.cb1.grid(row=5, column=0, sticky=tkinter.W)
        self.cb1 = tkinter.Checkbutton(
            top, text="Drop bigger to 0", variable=self.drop_bigger_to_zero)
        self.cb1.grid(row=2, column=1, sticky=tkinter.W)
        self.cb1 = tkinter.Checkbutton(
            top, text="Raise bigger to 255", variable=self.raise_bigger_to_max)
        self.cb1.grid(row=3, column=1, sticky=tkinter.W)
        self.cb1 = tkinter.Checkbutton(
            top, text="Drop bigger to threshold", variable=self.clip_bigger)
        self.cb1.grid(row=4, column=1, sticky=tkinter.W)
        self.cb1 = tkinter.Checkbutton(
            top, text="Raise smaller to threshold",
            variable=self.raise_smaller)
        self.cb1.grid(row=5, column=1, sticky=tkinter.W)

        self.input_label_v = tkinter.Label(
            top, text="Threshold value (0-255): ")
        self.input_label_v.grid(row=6, column=0, sticky=tkinter.W)
        self.input_entry_v = tkinter.Entry(top)
        self.input_entry_v.grid(row=6, column=1, sticky=tkinter.W)

        self.submit_button = tkinter.Button(
            top, text='Ok', command=self.cleanup)
        self.submit_button.grid(
            row=7,
            columnspan=2,
            sticky=tkinter.W + tkinter.E + tkinter.N + tkinter.S)

    def cleanup(self):

        selected = "binary"

        if self.binary_inverted.get() == 1:
            selected = "binary_inverted"
        elif self.drop_smaller_to_zero.get() == 1:
            selected = "drop_smaller_to_zero"
        elif self.raise_smaller_to_max.get() == 1:
            selected = "raise_smaller_to_max"
        elif self.drop_bigger_to_zero.get() == 1:
            selected = "drop_bigger_to_zero"
        elif self.raise_bigger_to_max.get() == 1:
            selected = "raise_bigger_to_max"
        elif self.clip_bigger.get() == 1:
            selected = "clip_bigger"
        elif self.raise_smaller.get() == 1:
            selected = "raise_smaller"

        try:
            self.callback(selected, int(self.input_entry_v.get()))
        except Exception as e:
            print(e)

        self.top.destroy()


class ModalLaplace(object):

    def __init__(self, parent, callback):
        top = self.top = tkinter.Toplevel(parent)
        self.l = tkinter.Label(top, text="Laplacian edge-detection options:")
        self.l.grid(row=0,
                    column=0,
                    pady=10,
                    sticky=tkinter.W + tkinter.E + tkinter.N + tkinter.S)

        self.callback = callback

        self.input_label = tkinter.Label(
            top, text="Sigma (std. deviation) for gaussian derivatives: ")
        self.input_label.grid(row=1, column=0, sticky=tkinter.W)
        self.input_entry = tkinter.Entry(top)
        self.input_entry.grid(row=1, column=1, sticky=tkinter.W)
        self.input_entry.insert(0, "1")

        self.submit_button = tkinter.Button(
            top, text='Ok', command=self.cleanup)
        self.submit_button.grid(
            row=2,
            columnspan=2,
            sticky=tkinter.W + tkinter.E + tkinter.N + tkinter.S)

    def cleanup(self):

        try:
            self.callback(int(self.input_entry.get()))
        except Exception as e:
            print(e)

        self.top.destroy()
