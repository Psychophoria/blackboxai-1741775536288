"""
Email templates and routing configuration for Storm911 application.
"""

from typing import Dict, List, Optional
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import SMTP_SETTINGS

# Email routing configuration
EMAIL_ROUTES = {
    "APPROVED": ["LEADS@STORM911.COM"],
    "DENIED": ["MINA@ASSURECALL.COM"],
    "CONFIRMATION": ["MINA@ASSURECALL.COM"],
    "REVIEW_NEEDED": ["MINA@ASSURECALL.COM", "EMAN@ASSURECALL.COM"]
}

# Email templates
TEMPLATES = {
    "APPROVED": {
        "subject": "Storm911 - Approved Inspection Report",
        "body": """
Dear {customer_name},

We are pleased to inform you that your roof inspection has been approved. Here are the details:

Property Address: {address}
Inspection Date: {inspection_date}
Inspector: {inspector_name}

Key Findings:
{findings}

Next Steps:
{next_steps}

If you have any questions, please don't hesitate to contact us.

Best regards,
Storm911 Team
        """
    },
    
    "DENIED": {
        "subject": "Storm911 - Inspection Review Required",
        "body": """
Dear {customer_name},

We have completed the inspection of your property at {address}. Based on our findings:

Inspection Date: {inspection_date}
Inspector: {inspector_name}

Findings:
{findings}

Reason for Denial:
{denial_reason}

If you would like to discuss this further or have any questions, please contact us.

Best regards,
Storm911 Team
        """
    },
    
    "CONFIRMATION": {
        "subject": "Storm911 - Inspection Appointment Confirmation",
        "body": """
Dear {customer_name},

This email confirms your upcoming roof inspection appointment:

Date: {appointment_date}
Time: {appointment_time}
Address: {address}

What to Expect:
- Our inspector will arrive at the scheduled time
- The inspection will take approximately 45-60 minutes
- No preparation is required on your part
- We will provide a detailed report of our findings

If you need to reschedule or have any questions, please contact us.

Best regards,
Storm911 Team
        """
    },
    
    "REVIEW_NEEDED": {
        "subject": "Storm911 - Inspection Review Required",
        "body": """
Dear {customer_name},

Your recent roof inspection requires additional review:

Property Address: {address}
Inspection Date: {inspection_date}
Inspector: {inspector_name}

Areas Requiring Review:
{review_areas}

Additional Notes:
{notes}

Our team will contact you within 24-48 hours with more information.

Best regards,
Storm911 Team
        """
    }
}

class EmailManager:
    """Handles email template processing and sending."""
    
    def __init__(self):
        self.smtp_settings = SMTP_SETTINGS
        
    def _create_message(self, template_name: str, to_emails: List[str], 
                       template_data: Dict) -> MIMEMultipart:
        """
        Create email message from template.
        
        Args:
            template_name: Name of template to use
            to_emails: List of recipient email addresses
            template_data: Dictionary of template variables
            
        Returns:
            MIMEMultipart: Prepared email message
        """
        if template_name not in TEMPLATES:
            raise ValueError(f"Unknown template: {template_name}")
            
        template = TEMPLATES[template_name]
        msg = MIMEMultipart()
        msg["From"] = self.smtp_settings["username"]
        msg["To"] = ", ".join(to_emails)
        msg["Subject"] = template["subject"]
        
        # Format template body with provided data
        body = template["body"].format(**template_data)
        msg.attach(MIMEText(body, "plain"))
        
        return msg
        
    def send_email(self, template_name: str, template_data: Dict,
                  additional_recipients: Optional[List[str]] = None) -> bool:
        """
        Send email using specified template and routing.
        
        Args:
            template_name: Name of template to use
            template_data: Dictionary of template variables
            additional_recipients: Optional list of additional recipients
            
        Returns:
            bool: True if email sent successfully, False otherwise
        """
        try:
            # Get default recipients for this template
            to_emails = EMAIL_ROUTES.get(template_name, [])
            
            # Add any additional recipients
            if additional_recipients:
                to_emails.extend(additional_recipients)
                
            if not to_emails:
                raise ValueError(f"No recipients specified for template: {template_name}")
                
            # Create message
            msg = self._create_message(template_name, to_emails, template_data)
            
            # Send email
            with smtplib.SMTP(self.smtp_settings["server"], 
                            self.smtp_settings["port"]) as server:
                server.starttls()
                server.login(self.smtp_settings["username"],
                           self.smtp_settings["password"])
                server.send_message(msg)
                
            return True
            
        except Exception as e:
            print(f"Error sending email: {str(e)}")
            return False
            
    def preview_email(self, template_name: str, template_data: Dict) -> str:
        """
        Generate preview of email content without sending.
        
        Args:
            template_name: Name of template to use
            template_data: Dictionary of template variables
            
        Returns:
            str: Formatted email content
        """
        if template_name not in TEMPLATES:
            raise ValueError(f"Unknown template: {template_name}")
            
        template = TEMPLATES[template_name]
        return template["body"].format(**template_data)

# Example usage:
"""
email_mgr = EmailManager()

# Template data
data = {
    "customer_name": "John Doe",
    "address": "123 Main St",
    "inspection_date": "2024-01-15",
    "inspector_name": "Mike Smith",
    "findings": "No significant damage found",
    "next_steps": "Schedule follow-up in 6 months"
}

# Send confirmation email
success = email_mgr.send_email("CONFIRMATION", data)

# Preview email content
preview = email_mgr.preview_email("APPROVED", data)
print(preview)
"""
