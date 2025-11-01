# 🧹 Windows Temp Cleaner

A simple Python script that safely transfers Windows temporary files and folders to the recycle bin instead of deleting them permanently.

---

## 🚀 Features
- Cleans common temporary folders:
  - `C:\Windows\Temp`
  - `C:\Users\<YourUsername>\AppData\Local\Temp`
  - `C:\Windows\Prefetch`
- Uses `Send2Trash` for safe deletion.
- Colorful output using `colorama`.

---

## ⚙️ Installation

```bash
pip install -r requirements.txt
