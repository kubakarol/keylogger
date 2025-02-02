# SimpleKeyLogger

## 📌 Description
SimpleKeyLogger is a lightweight keylogger written in Python using the `pynput` library. It captures keystrokes and logs them into a `log.txt` file. The program supports:
- Letters and numbers (logged as-is)
- Spaces (logged as a normal space)
- Special keys (logged as "Enter", "Ctrl", "Backspace", etc.)

---

## 🛠 Requirements
- Python 3.x
- `pynput` library

To install `pynput`, run:
```sh
pip install pynput
```

---

## 🚀 Usage
To start the keylogger, run:
```sh
python main.py
```

Keystrokes will be logged in `log.txt`.

---

## 🔧 Configuration
If you want to modify how keys are logged:
- Regular characters are logged as they are.
- Spaces are logged as a single space.
- Special keys are logged in capitalized format (e.g., "Enter", "Ctrl").
- Left (`_l`) and right (`_r`) variants of keys (e.g., `ctrl_l`, `ctrl_r`) are normalized to "Ctrl".

---

## ⚠️ Disclaimer
This program is intended for educational purposes only. Unauthorized use of keyloggers can be illegal. Ensure you have permission before running this script on any device.

