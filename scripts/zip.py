#!/usr/bin/env python
"""This script zips up all the necessary source files to compile the paper."""

from zipfile import ZipFile
from subprocess import check_output
import os

# Describe version via git
version = check_output(["git", "describe"]).strip().decode()

figures = ["figures/" + f for f in os.listdir("figures")
           if f not in ["SolidWorks",
                        "McMasters-Henderson-1980",
                        "McMasters-Henderson-1980.PNG",
                        "summary"]]

files = ["paper.tex", "mdpi.bst", "mdpi.cls", "logo-ccby.png", "logo-mdpi.png",
         "energies-logo.png", "graphical-abstract.png"]

with ZipFile("archive/paper-{}.zip".format(version), "w") as f:
    for fig in figures:
        f.write(fig)
    for file in files:
        f.write(file)
