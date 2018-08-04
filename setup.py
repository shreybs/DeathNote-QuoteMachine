import os

os.environ['TCL_LIBRARY'] = r'C:\Users\shrey.DESKTOP-TMB676J\AppData\Local\Programs\Python\Python36\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\shrey.DESKTOP-TMB676J\AppData\Local\Programs\Python\Python36\tcl\tk8.6'

import sys
from cx_Freeze import setup, Executable

setup(
    name = "Death Note Quotes",
    version = "1",
    description = "A quote generator for the best anime ever made.",
    executables = [Executable("generator.py", base = "Win32GUI")])
