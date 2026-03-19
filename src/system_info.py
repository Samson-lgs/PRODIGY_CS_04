"""
System Information Module
Captures system metrics and context information
"""

import psutil
import platform
from datetime import datetime
import os


class SystemInfoCapture:
    """Capture and log system information"""
    
    @staticmethod
    def get_system_info():
        """Get complete system information"""
        try:
            info = {
                "timestamp": datetime.now().isoformat(),
                "os": platform.system(),
                "os_version": platform.version(),
                "processor": platform.processor(),
                "machine": platform.machine(),
                "python_version": platform.python_version(),
                "hostname": platform.node(),
                "user": os.environ.get('USERNAME', 'unknown'),
                "cpu_count": psutil.cpu_count(),
                "total_memory": f"{psutil.virtual_memory().total / (1024**3):.2f} GB"
            }
            return info
        except Exception as e:
            print(f"Error getting system info: {e}")
            return None
    
    @staticmethod
    def get_cpu_usage():
        """Get current CPU usage percentage"""
        try:
            return psutil.cpu_percent(interval=1)
        except Exception as e:
            print(f"Error getting CPU usage: {e}")
            return None
    
    @staticmethod
    def get_memory_usage():
        """Get current memory usage statistics"""
        try:
            memory = psutil.virtual_memory()
            return {
                "total": f"{memory.total / (1024**3):.2f} GB",
                "used": f"{memory.used / (1024**3):.2f} GB",
                "available": f"{memory.available / (1024**3):.2f} GB",
                "percent": f"{memory.percent}%"
            }
        except Exception as e:
            print(f"Error getting memory usage: {e}")
            return None
    
    @staticmethod
    def get_disk_usage():
        """Get disk usage for all partitions"""
        try:
            disks = {}
            for partition in psutil.disk_partitions():
                try:
                    usage = psutil.disk_usage(partition.mountpoint)
                    disks[partition.device] = {
                        "total": f"{usage.total / (1024**3):.2f} GB",
                        "used": f"{usage.used / (1024**3):.2f} GB",
                        "free": f"{usage.free / (1024**3):.2f} GB",
                        "percent": f"{usage.percent}%"
                    }
                except PermissionError:
                    pass
            return disks
        except Exception as e:
            print(f"Error getting disk usage: {e}")
            return None
    
    @staticmethod
    def get_processes():
        """Get list of running processes"""
        try:
            processes = []
            for proc in psutil.process_iter(['pid', 'name', 'username']):
                try:
                    processes.append({
                        "pid": proc.info['pid'],
                        "name": proc.info['name'],
                        "username": proc.info['username']
                    })
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    pass
            return processes
        except Exception as e:
            print(f"Error getting processes: {e}")
            return None
    
    @staticmethod
    def get_network_interfaces():
        """Get network interface information"""
        try:
            interfaces = {}
            for interface_name, interface_addrs in psutil.net_if_addrs().items():
                interfaces[interface_name] = [
                    {
                        "family": str(addr.family),
                        "address": addr.address,
                        "netmask": addr.netmask,
                        "broadcast": addr.broadcast
                    }
                    for addr in interface_addrs
                ]
            return interfaces
        except Exception as e:
            print(f"Error getting network interfaces: {e}")
            return None
    
    @staticmethod
    def get_connected_users():
        """Get list of connected users"""
        try:
            users = psutil.users()
            return [
                {
                    "username": user.name,
                    "terminal": user.terminal,
                    "host": user.host,
                    "started": datetime.fromtimestamp(user.started).isoformat()
                }
                for user in users
            ]
        except Exception as e:
            print(f"Error getting connected users: {e}")
            return None


if __name__ == "__main__":
    sic = SystemInfoCapture()
    
    print("=== System Information ===")
    print(sic.get_system_info())
    
    print("\n=== CPU Usage ===")
    print(f"{sic.get_cpu_usage()}%")
    
    print("\n=== Memory Usage ===")
    print(sic.get_memory_usage())
    
    print("\n=== Disk Usage ===")
    print(sic.get_disk_usage())
    
    print("\n=== Network Interfaces ===")
    print(sic.get_network_interfaces())
