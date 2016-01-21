#!/usr/bin/env bash
# This script creates a diff with colored words in HTML. It requires
# http://www.pixelbeat.org/scripts/ansi2html.sh

git show 71bd282ca2 --word-diff --color > archive/proof-diff.diff
cat archive/proof-diff.diff | ansi2html.sh > archive/proof-diff.html
