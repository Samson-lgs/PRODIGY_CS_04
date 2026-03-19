"""
Clipboard Tracking Module
Monitors and logs clipboard changes
"""

import threading
import time
from datetime import datetime
from pathlib import Path


class ClipboardTracker:
    """Monitor and log clipboard changes"""
    
    def __init__(self, log_file="logs/clipboard.txt"):
        """
        Initialize clipboard tracker
        
        Args:
            log_file (str): File to log clipboard changes to
        """
        self.log_file = log_file
        self.is_running = False
        self.monitor_thread = None
        self.last_clipboard = ""
        
        Path(log_file).parent.mkdir(parents=True, exist_ok=True)
    
    def _get_clipboard(self):
        """Get current clipboard content"""
        try:
            import tkinter as tk
            root = tk.Tk()
            root.withdraw()
            root.update()
            clipboard = root.clipboard_get()
            root.destroy()
            return clipboard
        except Exception as e:
            print(f"Error reading clipboard: {e}")
            return ""
    
    def _log_clipboard_change(self, clipboard_content):
        """
        Log a clipboard change
        
        Args:
            clipboard_content (str): The clipboard content to log
        """
        try:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(self.log_file, 'a', encoding='utf-8') as f:
                f.write(f"\n[{timestamp}] CLIPBOARD CHANGE:\n")
                f.write(f"{clipboard_content}\n")
                f.write("-" * 50 + "\n")
                f.flush()
        except Exception as e:
            print(f"Error logging clipboard: {e}")
    
    def _monitor_clipboard(self):
        """Continuously monitor clipboard"""
        while self.is_running:
            try:
                current_clipboard = self._get_clipboard()
                
                if current_clipboard != self.last_clipboard and current_clipboard.strip():
                    self._log_clipboard_change(current_clipboard)
                    self.last_clipboard = current_clipboard
                    print(f"[*] Clipboard change detected: {current_clipboard[:50]}...")
                
                time.sleep(1)  # Check every second
                
            except Exception as e:
                print(f"Error in clipboard monitoring: {e}")
                time.sleep(1)
    
    def start(self):
        """Start clipboard monitoring"""
        if not self.is_running:
            self.is_running = True
            self.last_clipboard = self._get_clipboard()
            
            self.monitor_thread = threading.Thread(target=self._monitor_clipboard, daemon=True)
            self.monitor_thread.start()
            
            print(f"[*] Clipboard tracker started. Logging to {self.log_file}")
    
    def stop(self):
        """Stop clipboard monitoring"""
        self.is_running = False
        if self.monitor_thread:
            self.monitor_thread.join(timeout=2)
        print("[*] Clipboard tracker stopped")
    
    def get_clipboard_history(self, limit=10):
        """
        Get clipboard history
        
        Args:
            limit (int): Number of recent entries to retrieve
            
        Returns:
            list: List of clipboard entries
        """
        try:
            with open(self.log_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            entries = content.split("-" * 50)
            return [entry.strip() for entry in entries if entry.strip()][-limit:]
        except Exception as e:
            print(f"Error reading clipboard history: {e}")
            return []
    
    def export_clipboard_log(self, export_format="txt"):
        """
        Export clipboard log in various formats
        
        Args:
            export_format (str): Format to export (txt, json, csv)
            
        Returns:
            str: Path to exported file or None if failed
        """
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            base_path = Path(self.log_file).parent / f"clipboard_export_{timestamp}"
            
            if export_format == "json":
                import json
                history = self.get_clipboard_history(limit=None)
                export_path = f"{base_path}.json"
                with open(export_path, 'w', encoding='utf-8') as f:
                    json.dump(history, f, indent=2)
            
            elif export_format == "csv":
                import csv
                history = self.get_clipboard_history(limit=None)
                export_path = f"{base_path}.csv"
                with open(export_path, 'w', newline='', encoding='utf-8') as f:
                    writer = csv.writer(f)
                    writer.writerow(['Timestamp', 'Content'])
                    for entry in history:
                        writer.writerow([datetime.now().isoformat(), entry[:100]])
            
            else:  # txt format
                export_path = f"{base_path}.txt"
                with open(export_path, 'w', encoding='utf-8') as f:
                    f.write(self._read_log_file())
            
            print(f"[*] Clipboard log exported to {export_path}")
            return export_path
            
        except Exception as e:
            print(f"Error exporting clipboard log: {e}")
            return None
    
    def _read_log_file(self):
        """Read the entire log file"""
        try:
            with open(self.log_file, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            print(f"Error reading log file: {e}")
            return ""
    
    def clear_history(self):
        """Clear clipboard history"""
        try:
            with open(self.log_file, 'w', encoding='utf-8') as f:
                f.write("")
            print("[*] Clipboard history cleared")
            return True
        except Exception as e:
            print(f"Error clearing history: {e}")
            return False


if __name__ == "__main__":
    tracker = ClipboardTracker()
    tracker.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        tracker.stop()
        print("\n[*] Clipboard tracker terminated")
