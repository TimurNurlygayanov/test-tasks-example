#!/usr/bin/env bash

find . -type d -name __pycache__ -delete
find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
git add -A

