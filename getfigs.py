#!/usr/bin/env python
"""
This script copies figures from the RVAT Reynolds number dependence
experiment directory.
"""

import os
import sys
import shutil

figdir = os.path.join(os.path.expanduser("~"), "Research",
                      "Experiments", "RVAT Re dep", "Figures")

figlist = ["cp_vs_tsr.pdf",
           "mean_u.pdf",
           "mean_upvp.pdf"]

for fig in figlist:
    shutil.copy2(os.path.join(figdir, fig), os.path.join("figures", fig))

    
figdir = os.path.join(os.path.expanduser("~"), "Google Drive", "Research",
                      "Foils", "Data", "NACAXX20_QBlade", "figures")

figlist = ["all_foils_re_dep.pdf",
           "cft_re_dep_foils.pdf",
           "foil_kinematics_ct.pdf"]

for fig in figlist:
    shutil.copy2(os.path.join(figdir, fig), os.path.join("figures", fig))