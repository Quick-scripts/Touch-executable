from __future__ import annotations
import subprocess as sp
import sys
import manual_docstr

def main():
    filenames = sys.argv[1:]
    
    if len(filenames) == 0:
        print(manual_docstr.__doc__)
        return
    
    for file in filenames:
        sp.run(["touch", file])
        sp.run(["sudo", "chmod", "+x", file])


if __name__ == "__main__":
    main()



