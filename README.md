# touchexec

## Description

Creates a file for each of the given filenames and enables its executable permission. If a filename already exists, it will not be overwritten and will be given executable permissions.

## Installation

First, build `main.py` with

```bash
source build.sh
```

Then, move the binary `touchexec` to PATH (`$HOME/.local/bin`)
```bash
mv ./touchexec $HOME/.local/bin/touchexec
```
