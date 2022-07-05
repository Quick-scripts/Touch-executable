#!/bin/bash

# compiling
pyinstaller --onefile src/main.py

# renaming to touchexec and moving to main directory
mv dist/main ./touchexec


