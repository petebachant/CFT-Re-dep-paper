#!/usr/bin/env python
"""
This script zips up all the necessary source files to compile the paper.
"""

from zipfile import ZipFile
from subprocess import check_output
import os

# Describe version via git
version = check_output(["git", "describe"]).strip().decode()

figures = ["figures/" + f for f in os.listdir("figures")
           if f not in ["SolidWorks", "McMasters-Henderson-1980"]]

files = ["paper.tex", "library.bib", "mdpi.bst", "mdpi.cls"]

with ZipFile("archive/paper-{}.zip".format(version), "w") as f:
    for fig in figures:
        f.write(fig)
    for file in files:
        f.write(file)
