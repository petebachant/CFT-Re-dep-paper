#!/usr/bin/env bash

cd RVAT-Re-dep
python plot.py --save --noshow "$@"
cd ..
python getfigs.py
