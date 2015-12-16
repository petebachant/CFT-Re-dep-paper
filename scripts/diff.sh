#!/usr/bin/env bash

rev=$1
git show $rev:paper.tex > Archive/paper-$rev.tex
latexdiff Archive/paper-$rev.tex paper.tex > paper-$rev-diff.tex
# latexmk paper-$rev-diff.tex -pdf -f
