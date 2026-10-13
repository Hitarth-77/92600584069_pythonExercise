import os
import shutil

with open("sample.txt", "w") as f:
    f.write("Hello Python")

shutil.copy("sample.txt", "copy.txt")
print("File copied successfully.")

os.mkdir("MyFolder")
shutil.move("copy.txt", "MyFolder/copy.txt")
print("File moved successfully.")

os.remove("sample.txt")
print("Original file deleted.")

os.remove("MyFolder/copy.txt")
os.rmdir("MyFolder")
print("Copied file and folder deleted.")