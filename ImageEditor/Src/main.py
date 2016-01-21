"""
Main module.
Creates GUI.
"""

import tkinter
import EditorGUI

__author__ = "5966916: Noah Hummel, 5987733: Kyle Rinfreschi"


def main():

    #  Create a root for the GUI
    root = tkinter.Tk()

    geometry_string = "300x300"
    root.geometry(geometry_string)

    #  Editor_GUI is the container for all
    #  GUI elements, append it to root.
    app = EditorGUI.EditorGUI(root)
    root.mainloop()

if __name__ == '__main__':
    main()
