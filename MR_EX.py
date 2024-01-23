import os, sys
os.system("git pull")
try:
    __import__("MR_EX").danger_menu()
except Exception as e:
    exit(str(e))
