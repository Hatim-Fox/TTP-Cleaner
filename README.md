# 🧹 Windows Temp Cleaner

A simple and safe Windows cleaner written in **Python**, compiled into a standalone **.exe** file.  
It automatically moves temporary system files to the Recycle Bin instead of deleting them permanently.

---

## 🚀 Features
- Cleans common Windows temporary folders:
  - `C:\Windows\Temp`
  - `C:\Users\<YourUsername>\AppData\Local\Temp`
  - `C:\Windows\Prefetch`
- Safe deletion using [Send2Trash](https://pypi.org/project/Send2Trash/)
- Colorful console output using [Colorama](https://pypi.org/project/colorama/)
- Requires **Administrator privileges** for full access

---

## ⚙️ How to Use

1. [Download the latest release](https://github.com/Hatim-Fox/TTP-Cleaner/releases)
2. Run **`CleanTempFiles.exe`** as **Administrator**
3. Wait until the console finishes showing all files transferred to the Recycle Bin

---

## 🪄 Example Output
```text
✅ Transferred C:\Users\User\AppData\Local\Temp\abc.tmp to the recycle bin.
⚠️ Permission denied for C:\Windows\Prefetch\xyz.dat
