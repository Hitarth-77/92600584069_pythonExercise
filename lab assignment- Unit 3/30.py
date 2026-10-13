
import re
from tkinter import Tk, filedialog

root = Tk()
root.withdraw()

file_path = filedialog.askopenfilename(
    title="Select details.txt",
    filetypes=[("Text files", "*.txt")]
)

if file_path:
    with open(file_path, "r") as f:
        text = f.read()

    emails = re.findall(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        text
    )

    phones = re.findall(r"\b\d{10}\b", text)

    print("Email addresses:", emails)
    print("Phone numbers:", phones)
else:
    print("No file selected.")
