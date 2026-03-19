"""
Advanced Logging Module
Provides time-stamped logging with session tracking and JSON export
"""

from datetime import datetime
import json
import os
from pathlib import Path


class AdvancedLogger:
    """Advanced logging with timestamps and session management"""
    
    def __init__(self, log_dir="logs"):
        """
        Initialize advanced logger
        
        Args:
            log_dir (str): Directory for storing logs
        """
        self.log_dir = log_dir
        self.session_id = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.session_file = os.path.join(log_dir, f"session_{self.session_id}.json")
        self.text_log = os.path.join(log_dir, f"keylog_{self.session_id}.txt")
        
        # Create log directory
        Path(log_dir).mkdir(parents=True, exist_ok=True)
        
        # Initialize session data
        self.session_data = {
            "start_time": datetime.now().isoformat(),
            "session_id": self.session_id,
            "events": []
        }
    
    def log_event(self, event_type, data, timestamp=None):
        """
        Log an event with timestamp
        
        Args:
            event_type (str): Type of event (keystroke, screenshot, clipboard, etc.)
            data (str): Event data
            timestamp (datetime): Optional timestamp, defaults to now
        """
        if timestamp is None:
            timestamp = datetime.now()
        
        event = {
            "timestamp": timestamp.isoformat(),
            "type": event_type,
            "data": data
        }
        
        self.session_data["events"].append(event)
        
        # Write to text log for real-time viewing
        try:
            with open(self.text_log, 'a', encoding='utf-8') as f:
                if event_type == "keystroke":
                    f.write(data)
                else:
                    f.write(f"\n[{timestamp.strftime('%Y-%m-%d %H:%M:%S')}] [{event_type}]: {data}\n")
                f.flush()
        except Exception as e:
            print(f"Error writing to text log: {e}")
    
    def save_session(self):
        """Save session data to JSON file"""
        try:
            self.session_data["end_time"] = datetime.now().isoformat()
            with open(self.session_file, 'w', encoding='utf-8') as f:
                json.dump(self.session_data, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving session: {e}")
            return False
    
    def get_session_stats(self):
        """Get statistics for the current session"""
        keystroke_events = [e for e in self.session_data["events"] if e["type"] == "keystroke"]
        
        stats = {
            "session_id": self.session_id,
            "start_time": self.session_data["start_time"],
            "total_events": len(self.session_data["events"]),
            "keystrokes": len(keystroke_events),
            "keystroke_data": ''.join([e["data"] for e in keystroke_events])
        }
        return stats
    
    def export_to_csv(self, csv_file=None):
        """Export session data to CSV format"""
        import csv
        
        if csv_file is None:
            csv_file = os.path.join(self.log_dir, f"session_{self.session_id}.csv")
        
        try:
            with open(csv_file, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=["timestamp", "type", "data"])
                writer.writeheader()
                writer.writerows(self.session_data["events"])
            return csv_file
        except Exception as e:
            print(f"Error exporting to CSV: {e}")
            return None


if __name__ == "__main__":
    logger = AdvancedLogger()
    logger.log_event("keystroke", "H")
    logger.log_event("keystroke", "e")
    logger.log_event("keystroke", "l")
    logger.log_event("keystroke", "l")
    logger.log_event("keystroke", "o")
    logger.save_session()
    print(logger.get_session_stats())
