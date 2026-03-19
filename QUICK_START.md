# Quick Start Guide

## 🚀 Get Started in 3 Minutes

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the Application
```bash
python main.py
```

### 3. Press ESC to Stop
The keylogger will run until you press ESC.

---

## 📁 File Locations

| File | Purpose |
|------|---------|
| `main.py` | **Start here** - Main application |
| `demo.py` | Test features without logging |
| `config/config.json` | Configure features (on/off) |
| `logs/keylog.txt` | Keystroke log file |
| `logs/clipboard.txt` | Clipboard log file |
| `screenshots/` | Saved screenshots |

---

## 🎛️ Config Quick Reference

Edit `config/config.json`:

```json
{
  "keylogger": {
    "enabled": true           // Enable keystroke capture
  },
  "screenshots": {
    "enabled": true           // Enable screenshot capture
  },
  "clipboard": {
    "enabled": true           // Enable clipboard tracking
  },
  "email_alerts": {
    "enabled": false          // Disable email sending
  }
}
```

---

## 🧪 Testing

### Run All Tests
```bash
python demo.py --auto
```

### Interactive Demo
```bash
python demo.py
# Choose option 9 for all demos
```

### Test Individual Modules
```bash
# Test keylogger
python src/keylogger.py

# Test system info
python src/system_info.py

# Test clipboard
python -c "from src.clipboard_tracker import ClipboardTracker; t = ClipboardTracker(); t.start()"
```

---

## 📊 View Logs

### Keystroke Log
```bash
type logs/keylog.txt          # Windows
cat logs/keylog.txt           # Linux/macOS
```

### Session Data (JSON)
```bash
type logs/session_*.json      # Windows
cat logs/session_*.json       # Linux/macOS
```

### Clipboard Log
```bash
type logs/clipboard.txt       # Windows
cat logs/clipboard.txt        # Linux/macOS
```

---

## 🔧 Module Quick Reference

### Keylogger Only
```python
from src.keylogger import Keylogger
logger = Keylogger()
logger.start()
```

### Advanced Logger
```python
from src.advanced_logger import AdvancedLogger
logger = AdvancedLogger()
logger.log_event("keystroke", "A")
logger.save_session()
```

### System Info
```python
from src.system_info import SystemInfoCapture
info = SystemInfoCapture.get_system_info()
cpu = SystemInfoCapture.get_cpu_usage()
```

### Screenshots
```python
from src.screenshot import ScreenshotCapture
sc = ScreenshotCapture()
sc.capture_full_screen()
```

### Clipboard Tracking
```python
from src.clipboard_tracker import ClipboardTracker
tracker = ClipboardTracker()
tracker.start()
```

### Email Alerts
```python
from src.email_alert import EmailAlertSystem
email = EmailAlertSystem("sender@gmail.com", "password")
email.send_alert("recipient@gmail.com", "Subject", "Message")
```

---

## 🐛 Troubleshooting

| Problem | Solution |
|---------|----------|
| Module not found | `pip install -r requirements.txt` |
| Permission denied | Run as admin or check file permissions |
| Keylogger not working | Ensure application has focus |
| No screenshots | Check screenshot directory, ensure display is active |
| Clipboard not tracking | Install tkinter (Linux: `sudo apt install python3-tk`) |

---

## 📚 Documentation

| File | Content |
|------|---------|
| `README.md` | Quick overview |
| `SETUP.md` | Installation guide |
| `DOCUMENTATION.md` | Complete API reference |
| `PROJECT_SUMMARY.md` | Project completion details |

---

## ✨ Key Features

✅ **Keystroke Logging** - Capture all keys pressed  
✅ **Timestamps** - Know when each event occurred  
✅ **System Monitoring** - CPU, memory, disk, network  
✅ **Screenshots** - Visual record of screen activity  
✅ **Clipboard Tracking** - Monitor copied content  
✅ **Email Alerts** - Receive reports via email  
✅ **Export Options** - JSON, CSV, TXT formats  
✅ **Configuration** - Easy on/off toggle for features  

---

## 🔒 Important Reminders

⚠️ **LEGAL**: This tool is for educational purposes and authorized testing only.  
⚠️ **ETHICAL**: Only use with explicit permission from system owner.  
⚠️ **PRIVACY**: Respect user privacy and data protection laws.  
⚠️ **SECURITY**: Keep logs and configurations secure.

---

## 📞 Need Help?

1. Check [SETUP.md](SETUP.md) for installation issues
2. Run `python demo.py --auto` for diagnostics
3. Review [DOCUMENTATION.md](DOCUMENTATION.md) for API details
4. Check logs for error messages
5. Verify all dependencies: `pip list | grep -E "pynput|Pillow|psutil"`

---

## 🎯 Common Workflows

### Basic Logging Only
1. Open `config/config.json`
2. Disable all except `keylogger`
3. Run `python main.py`
4. Check `logs/keylog.txt`

### Full Monitoring
1. Keep all features enabled in config
2. Run `python main.py`
3. Check all log files:
   - `logs/keylog.txt`
   - `logs/clipboard.txt`
   - `logs/session_*.json`
   - `screenshots/*.png`

### Testing Only
1. Run `python demo.py --auto`
2. No files will be saved
3. Perfect for verifying installation

---

## ✅ Verification Checklist

- [ ] Python 3.7+ installed
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] `config/config.json` exists
- [ ] `demo.py --auto` runs without errors
- [ ] `main.py` starts successfully
- [ ] Press ESC stops execution properly
- [ ] `logs/` directory created after first run
- [ ] `screenshots/` directory created

---

**Ready?** Run: `python main.py`

For detailed help, see [DOCUMENTATION.md](DOCUMENTATION.md)
