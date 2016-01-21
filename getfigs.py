#!/usr/bin/env python
"""This script copies figures from the RVAT Reynolds number dependence
experiment directory.
"""

import os
import sys
import shutil

figdir = os.path.join("RVAT-Re-dep", "Figures")

figlist = ["cp_curves.pdf",
           "cd_curves.pdf",
           "perf_re_dep.pdf",
           "K_trans_bar_graph.pdf",
           "mom_bar_graph.pdf",
           "wake_spectra.pdf",
           "wake_trans_totals.pdf",
           "mean_u_k_profiles.pdf"]

for fig in figlist:
    shutil.copy2(os.path.join(figdir, fig), os.path.join("figures", fig))


figdir = os.path.join(os.path.expanduser("~"), "Google Drive", "Research",
                      "Foils", "Data", "NACAXX20_QBlade", "figures")

figlist = ["all_foils_re_dep.pdf",
           "cft_re_dep_foils.pdf",
           "foil_kinematics_ct.pdf"]

for fig in figlist:
    shutil.copy2(os.path.join(figdir, fig), os.path.join("figures", fig))
