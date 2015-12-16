#!/usr/bin/env bash
# This script creates a diff version comparing the recent with whatever revision
# is supplied as the first argument. This can be any valid Git identifier, e.g.,
# a commit hash, tag, etc.

rev=$1
git show $rev:paper.tex > Archive/paper-$rev.tex
latexdiff --exclude-textcmd="section,subsection,subsubsection" --math-markup=off Archive/paper-$rev.tex Archive/paper-unix.tex > paper-$rev-diff.tex
latexmk paper-$rev-diff.tex -pdf -f
mv paper-$rev-diff.pdf Archive
rm paper-$rev*
