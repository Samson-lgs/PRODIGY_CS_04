# Setup Guide

Complete guide to set up and run the Advanced Keylogger Application.

## System Requirements

- **OS**: Windows, macOS, or Linux
- **Python**: 3.7 or higher
- **Memory**: 256 MB minimum
- **Disk Space**: 100 MB minimum
- **Privileges**: Regular user (Admin for some features recommended)

## Step 1: Install Python

### Windows
1. Download Python from [python.org](https://www.python.org/downloads/)
2. Run installer with "Add Python to PATH" checked
3. Verify installation:
   ```bash
   python --version
   ```

### macOS
```bash
# Using Homebrew
brew install python3

# Or download from python.org
```

### Linux
```bash
# Ubuntu/Debian
sudo apt-get install python3 python3-pip

# Fedora
sudo dnf install python3 python3-pip
```

## Step 2: Download/Clone Project

```bash
# If you have git
git clone <repository-url>
cd PRODIGY_CS_04

# Or extract from ZIP file
unzip PRODIGY_CS_04.zip
cd PRODIGY_CS_04
```

## Step 3: Install Dependencies

```bash
# Navigate to project directory
cd PRODIGY_CS_04

# Install Python packages
pip install -r requirements.txt

# On Linux, you might need tkinter for clipboard support
# Ubuntu/Debian:
sudo apt-get install python3-tk

# Fedora:
sudo dnf install python3-tkinter
```

## Step 4: Verify Installation

### Quick Test
```bash
# Run demo to verify everything works
python demo.py

# Choose option 9 (Run All Demos)
```

### Test Individual Modules
```bash
# Test system info
python -c "from src.system_info import SystemInfoCapture; print(SystemInfoCapture.get_system_info())"

# Test keylogger (will require ESC to stop)
python src/keylogger.py

# Test screenshot
python src/screenshot.py
```

## Step 5: Configure Application

Edit `config/config.json` to enable/disable features:

```json
{
  "keylogger": {
    "enabled": true,
    "log_file": "logs/keylog.txt"
  },
  "email_alerts": {
    "enabled": false
  }
}
```

## Step 6: Run Application

### Main Application
```bash
python main.py
```

### Demo Mode (No actual logging)
```bash
python demo.py
```

### Run Tests
```bash
python demo.py --auto
```

## Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'pynput'"

**Solution**: Install dependencies
```bash
pip install -r requirements.txt
```

### Issue: Permission Denied (Linux/macOS)

**Solution**: Run with appropriate permissions
```bash
sudo python main.py
# OR check file permissions
chmod +x main.py
```

### Issue: "No module named 'tkinter'" (Linux)

**Solution**: Install tkinter
```bash
# Ubuntu/Debian
sudo apt-get install python3-tk

# Fedora
sudo dnf install python3-tkinter

# macOS
brew install python-tk3
```

### Issue: Keylogger not capturing keys

**Solutions**:
- Ensure terminal/application has focus
- Check if using virtual machine (may not capture)
- Try running with administrator privileges
- Some keyboard layouts may not be fully supported

### Issue: Screenshot captures blank image

**Solution**: The application needs focus or try testing with:
```python
from src.screenshot import ScreenshotCapture
sc = ScreenshotCapture()
sc.capture_full_screen()  # Should save screenshot
```

## First Run Checklist

- [ ] Python installed (`python --version`)
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] Demo runs without errors (`python demo.py`)
- [ ] Configuration file exists (`config/config.json`)
- [ ] Logs directory created (`logs/`)
- [ ] Screenshots directory created (`screenshots/`)

## Features to Test

### 1. Basic Keystroke Logging
```bash
python src/keylogger.py
# Type some text, press ESC to stop
# Check logs/keylog.txt
```

### 2. Advanced Logging
```python
from src.advanced_logger import AdvancedLogger
logger = AdvancedLogger()
logger.log_event("keystroke", "test")
logger.save_session()
```

### 3. System Information
```bash
python -c "from src.system_info import SystemInfoCapture; import json; print(json.dumps(SystemInfoCapture.get_system_info(), indent=2))"
```

### 4. Screenshots
```bash
python -c "from src.screenshot import ScreenshotCapture; sc = ScreenshotCapture(); sc.capture_full_screen()"
```

### 5. Clipboard Tracking
```bash
# In one terminal
python -c "from src.clipboard_tracker import ClipboardTracker; t = ClipboardTracker(); t.start()"

# In another, copy something to clipboard
# You should see it logged
```

## Environment Variables (Optional)

Create a `.env` file for sensitive data:

```env
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
RECIPIENT_EMAIL=recipient@example.com
```

Then in code:
```python
from dotenv import load_dotenv
load_dotenv()
email = os.getenv('EMAIL_ADDRESS')
```

## Next Steps

1. Read [DOCUMENTATION.md](DOCUMENTATION.md) for detailed API reference
2. Check the [README.md](README.md) for quick reference
3. Review `config/config.json` for customization options
4. Run `python demo.py` to explore features
5. Check Git commit history: `git log --oneline`

## Support

### For Issues:
1. Check error messages in terminal
2. Run `python demo.py --auto` for diagnostics
3. Review logs in `logs/` directory
4. Check file permissions and disk space

### Common Paths:
- Configuration: `config/config.json`
- Logs: `logs/` (after first run)
- Screenshots: `screenshots/` (after first screenshot)

## Uninstall

To completely remove the application:

```bash
# Remove directories
rm -rf PRODIGY_CS_04

# Or on Windows
rmdir /s PRODIGY_CS_04

# Optional: Remove Python packages if not using elsewhere
pip uninstall pynput Pillow psutil python-dotenv
```

## Advanced Setup

### Running at Startup (Windows)

Create a batch file `start_keylogger.bat`:
```batch
@echo off
cd C:\path\to\PRODIGY_CS_04
python main.py
```

Then add to Task Scheduler.

### Running as Service (Linux)

Create `/etc/systemd/system/keylogger.service`:
```ini
[Unit]
Description=Advanced Keylogger
After=network.target

[Service]
Type=simple
User=username
WorkingDirectory=/path/to/PRODIGY_CS_04
ExecStart=/usr/bin/python3 /path/to/PRODIGY_CS_04/main.py
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

Then enable:
```bash
sudo systemctl daemon-reload
sudo systemctl enable keylogger
sudo systemctl start keylogger
```

## Performance Optimization

### For Slower Systems:
```json
{
  "system_info": {
    "capture_interval": 600
  },
  "screenshots": {
    "enabled": false
  }
}
```

### For Maximum Logging:
Keep default settings and ensure sufficient disk space.

---

**Ready to start?** Run `python main.py` or `python demo.py`!
