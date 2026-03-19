# Advanced Keylogger Application - PRODIGY_CS_04

**Prodigy InfoTech Internship - Task 04: Simple Keylogger with Advanced Features**

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py
```

## Features

- ✅ Keystroke Logging
- ✅ Advanced Session Logging (JSON/CSV)
- ✅ System Information Capture
- ✅ Screenshot Capture
- ✅ Clipboard Tracking
- ✅ Email Alert System
- ✅ Configuration Management
- ✅ Multi-threaded Architecture

## Documentation

For detailed documentation, features, API reference, and usage examples, see [DOCUMENTATION.md](DOCUMENTATION.md)

## Project Structure

```
├── main.py                 # Main application
├── config/config.json      # Configuration
├── src/                    # Source modules
│   ├── keylogger.py
│   ├── advanced_logger.py
│   ├── system_info.py
│   ├── screenshot.py
│   ├── clipboard_tracker.py
│   ├── email_alert.py
│   └── config_manager.py
├── logs/                   # Log files (empty directory)
└── screenshots/            # Screenshots (empty directory)
```

## Key Modules

| Module | Purpose |
|--------|---------|
| `keylogger.py` | Core keystroke capture |
| `advanced_logger.py` | Timestamped logging with session tracking |
| `system_info.py` | CPU, memory, disk, network monitoring |
| `screenshot.py` | Screen capture functionality |
| `clipboard_tracker.py` | Clipboard monitoring |
| `email_alert.py` | Email notification system |
| `config_manager.py` | Configuration management |

## ⚠️ Ethical & Legal Notice

This application is for educational and authorized security testing ONLY. 

**AUTHOR'S RESPONSIBILITY**: Unauthorized monitoring is illegal. Users are responsible for obtaining proper authorization before deployment.

## Technology Stack

- **Language**: Python 3.7+
- **Key Libraries**:
  - `pynput` - Keyboard monitoring
  - `Pillow` - Screenshot capture
  - `psutil` - System monitoring
  - Standard `smtplib` - Email sending

## Version Control

All features implemented incrementally with Git commits tracking each enhancement.

## More Information

See [DOCUMENTATION.md](DOCUMENTATION.md) for comprehensive API reference, configuration guide, and troubleshooting.