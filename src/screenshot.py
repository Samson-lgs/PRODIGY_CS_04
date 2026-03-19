"""
Screenshot Module
Captures and saves screenshots with various options
"""

from PIL import ImageGrab
from datetime import datetime
import os
from pathlib import Path


class ScreenshotCapture:
    """Capture and save screenshots"""
    
    def __init__(self, save_dir="screenshots"):
        """
        Initialize screenshot capture
        
        Args:
            save_dir (str): Directory where screenshots will be saved
        """
        self.save_dir = save_dir
        Path(save_dir).mkdir(parents=True, exist_ok=True)
    
    def capture_full_screen(self, filename=None):
        """
        Capture the full screen
        
        Args:
            filename (str): Optional filename for the screenshot
            
        Returns:
            str: Path to saved screenshot or None if failed
        """
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            
            if filename is None:
                filename = f"screenshot_full_{timestamp}.png"
            
            filepath = os.path.join(self.save_dir, filename)
            
            # Capture full screen
            screenshot = ImageGrab.grab()
            screenshot.save(filepath)
            
            print(f"[*] Screenshot saved: {filepath}")
            return filepath
            
        except Exception as e:
            print(f"Error capturing screenshot: {e}")
            return None
    
    def capture_region(self, bbox=None, filename=None):
        """
        Capture a specific region of the screen
        
        Args:
            bbox (tuple): Bounding box (left, top, right, bottom) for region capture
            filename (str): Optional filename for the screenshot
            
        Returns:
            str: Path to saved screenshot or None if failed
        """
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            
            if filename is None:
                filename = f"screenshot_region_{timestamp}.png"
            
            filepath = os.path.join(self.save_dir, filename)
            
            if bbox is None:
                # Default region (e.g., top-left 800x600)
                bbox = (0, 0, 800, 600)
            
            # Capture region
            screenshot = ImageGrab.grab(bbox=bbox)
            screenshot.save(filepath)
            
            print(f"[*] Region screenshot saved: {filepath}")
            return filepath
            
        except Exception as e:
            print(f"Error capturing region screenshot: {e}")
            return None
    
    def capture_active_window(self, filename=None):
        """
        Attempt to capture the active window (Windows only)
        
        Args:
            filename (str): Optional filename for the screenshot
            
        Returns:
            str: Path to saved screenshot or None if failed
        """
        import platform
        
        if platform.system() != "Windows":
            print("Active window capture only supported on Windows")
            return None
        
        try:
            import win32gui
            import win32ui
            import win32con
            
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            
            if filename is None:
                filename = f"screenshot_window_{timestamp}.png"
            
            filepath = os.path.join(self.save_dir, filename)
            
            # Get active window
            hwnd = win32gui.GetForegroundWindow()
            
            # Get window dimensions
            left, top, right, bottom = win32gui.GetWindowRect(hwnd)
            w = right - left
            h = bottom - top
            
            # Capture window
            hwndDC = win32gui.GetWindowDC(hwnd)
            mfcDC = win32ui.CreateDCFromHandle(hwndDC)
            saveDC = mfcDC.CreateCompatibleDC()
            
            saveBitMap = win32ui.CreateBitmap()
            saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
            saveDC.SelectObject(saveBitMap)
            saveDC.BitBlt((0, 0), (w, h), mfcDC, (0, 0), win32con.SRCCOPY)
            
            saveBitMap.SaveBitmapFile(saveDC, filepath)
            
            win32gui.ReleaseDC(hwnd, hwndDC)
            mfcDC.DeleteDC()
            saveDC.DeleteDC()
            win32ui.ReleaseDC(saveDC)
            
            print(f"[*] Active window screenshot saved: {filepath}")
            return filepath
            
        except ImportError:
            print("pywin32 library not found. Install with: pip install pywin32")
            return None
        except Exception as e:
            print(f"Error capturing active window: {e}")
            return None
    
    def capture_periodic(self, interval=300, duration=3600, filename_template=None):
        """
        Capture screenshots at regular intervals
        
        Args:
            interval (int): Interval between captures in seconds (default: 5 minutes)
            duration (int): Total duration of periodic capture in seconds (default: 1 hour)
            filename_template (str): Template for filenames
            
        Returns:
            list: List of saved screenshot paths
        """
        import time
        
        saved_files = []
        elapsed_time = 0
        
        try:
            while elapsed_time < duration:
                filepath = self.capture_full_screen(
                    filename=filename_template if filename_template else None
                )
                if filepath:
                    saved_files.append(filepath)
                
                elapsed_time += interval
                if elapsed_time < duration:
                    print(f"[*] Next screenshot in {interval} seconds")
                    time.sleep(interval)
        
        except KeyboardInterrupt:
            print("[*] Periodic capture stopped by user")
        
        return saved_files
    
    def get_screenshot_info(self):
        """Get information about saved screenshots"""
        try:
            screenshots = []
            for file in os.listdir(self.save_dir):
                if file.endswith(('.png', '.jpg', '.bmp')):
                    filepath = os.path.join(self.save_dir, file)
                    size = os.path.getsize(filepath)
                    mod_time = datetime.fromtimestamp(os.path.getmtime(filepath))
                    screenshots.append({
                        "filename": file,
                        "path": filepath,
                        "size": f"{size / (1024**2):.2f} MB",
                        "modified": mod_time.isoformat()
                    })
            return screenshots
        except Exception as e:
            print(f"Error getting screenshot info: {e}")
            return None


if __name__ == "__main__":
    sc = ScreenshotCapture()
    
    # Capture full screen
    sc.capture_full_screen()
    
    # Get screenshot info
    print(sc.get_screenshot_info())
