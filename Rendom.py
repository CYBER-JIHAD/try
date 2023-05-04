import os, sys
try:
    __import__("cy").Main()
except Exception as e:
    exit(str(e))

