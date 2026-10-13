import os
import sys

print("Current directory:", os.getcwd())

if not os.path.exists("MyFolder"):
    os.mkdir("MyFolder")

print("Directory created or already exists.")
print("Files and folders:", os.listdir("."))
print("Python version:", sys.version)
print("Command-line arguments:", sys.argv)