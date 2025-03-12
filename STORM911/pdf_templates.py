"""
PDF template generation and export functionality for Storm911 application.
"""

import os
from typing import Dict, Optional
from datetime import datetime
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
from config import PDF_SETTINGS, ASSETS_DIR

# PDF templates matching email templates
TEMPLATES = {
    "APPROVED": {
        "title": "Storm911 - Approved Inspection Report",
        "sections": [
            {
                "heading": "Property Information",
                "fields": [
                    "Customer Name: {customer_name}",
                    "Property Address: {address}",
                    "Inspection Date: {inspection_date}",
                    "Inspector: {inspector_name}"
                ]
            },
            {
                "heading": "Inspection Findings",
                "fields": [
                    "Key Findings:",
                    "{findings}",
                    "",
                    "Next Steps:",
                    "{next_steps}"
                ]
            },
            {
                "heading": "Contact Information",
                "fields": [
                    "Storm911",
                    "Phone: 1-800-STORM911",
                    "Email: support@storm911.com"
                ]
            }
        ]
    },
    
    "DENIED": {
        "title": "Storm911 - Inspection Denial Report",
        "sections": [
            {
                "heading": "Property Information",
                "fields": [
                    "Customer Name: {customer_name}",
                    "Property Address: {address}",
                    "Inspection Date: {inspection_date}",
                    "Inspector: {inspector_name}"
                ]
            },
            {
                "heading": "Inspection Results",
                "fields": [
                    "Findings:",
                    "{findings}",
                    "",
                    "Reason for Denial:",
                    "{denial_reason}"
                ]
            },
            {
                "heading": "Contact Information",
                "fields": [
                    "For questions or concerns, please contact:",
                    "Storm911",
                    "Phone: 1-800-STORM911",
                    "Email: support@storm911.com"
                ]
            }
        ]
    },
    
    "CONFIRMATION": {
        "title": "Storm911 - Inspection Appointment Confirmation",
        "sections": [
            {
                "heading": "Appointment Details",
                "fields": [
                    "Customer Name: {customer_name}",
                    "Property Address: {address}",
                    "Appointment Date: {appointment_date}",
                    "Appointment Time: {appointment_time}"
                ]
            },
            {
                "heading": "What to Expect",
                "fields": [
                    "• Our inspector will arrive at the scheduled time",
                    "• The inspection will take approximately 45-60 minutes",
                    "• No preparation is required on your part",
                    "• We will provide a detailed report of our findings"
                ]
            },
            {
                "heading": "Contact Information",
                "fields": [
                    "If you need to reschedule, please contact:",
                    "Storm911",
                    "Phone: 1-800-STORM911",
                    "Email: support@storm911.com"
                ]
            }
        ]
    },
    
    "REVIEW_NEEDED": {
        "title": "Storm911 - Inspection Review Report",
        "sections": [
            {
                "heading": "Property Information",
                "fields": [
                    "Customer Name: {customer_name}",
                    "Property Address: {address}",
                    "Inspection Date: {inspection_date}",
                    "Inspector: {inspector_name}"
                ]
            },
            {
                "heading": "Areas Requiring Review",
                "fields": [
                    "{review_areas}",
                    "",
                    "Additional Notes:",
                    "{notes}"
                ]
            },
            {
                "heading": "Next Steps",
                "fields": [
                    "Our team will contact you within 24-48 hours with more information.",
                    "",
                    "For immediate assistance:",
                    "Storm911",
                    "Phone: 1-800-STORM911",
                    "Email: support@storm911.com"
                ]
            }
        ]
    }
}

class PDFGenerator:
    """Handles PDF template generation and export."""
    
    def __init__(self):
        """Initialize PDF generator with styles."""
        self.styles = getSampleStyleSheet()
        
        # Add custom styles
        self.styles.add(ParagraphStyle(
            name='CustomTitle',
            parent=self.styles['Title'],
            fontSize=24,
            spaceAfter=30
        ))
        
        self.styles.add(ParagraphStyle(
            name='SectionHeading',
            parent=self.styles['Heading1'],
            fontSize=16,
            spaceAfter=12
        ))
        
        self.styles.add(ParagraphStyle(
            name='BodyText',
            parent=self.styles['Normal'],
            fontSize=12,
            spaceAfter=8
        ))
        
    def _create_header(self, canvas, doc):
        """Add header with logos to each page."""
        # Add Storm911 logo
        storm_logo_path = os.path.join(ASSETS_DIR, "storm911.png")
        if os.path.exists(storm_logo_path):
            canvas.drawImage(storm_logo_path, 
                           doc.pagesize[0]/2 - 100,  # Center horizontally
                           doc.pagesize[1] - 1.2*inch,  # Top of page
                           width=200, height=60)
            
        # Add AssureCall logo
        assure_logo_path = os.path.join(ASSETS_DIR, "assurecall.png")
        if os.path.exists(assure_logo_path):
            canvas.drawImage(assure_logo_path,
                           0.5*inch,  # Left side
                           doc.pagesize[1] - 1.2*inch,  # Top of page
                           width=100, height=40)
            
        # Add date
        canvas.setFont("Helvetica", 10)
        canvas.drawRightString(
            doc.pagesize[0] - 0.5*inch,
            doc.pagesize[1] - 0.5*inch,
            datetime.now().strftime("%Y-%m-%d")
        )
        
    def generate_pdf(self, template_name: str, output_path: str,
                    template_data: Dict) -> bool:
        """
        Generate PDF from template.
        
        Args:
            template_name: Name of template to use
            output_path: Path to save PDF
            template_data: Dictionary of template variables
            
        Returns:
            bool: True if PDF generated successfully, False otherwise
        """
        try:
            if template_name not in TEMPLATES:
                raise ValueError(f"Unknown template: {template_name}")
                
            template = TEMPLATES[template_name]
            
            # Create PDF document
            doc = SimpleDocTemplate(
                output_path,
                pagesize=letter,
                rightMargin=PDF_SETTINGS["margin_right"],
                leftMargin=PDF_SETTINGS["margin_left"],
                topMargin=PDF_SETTINGS["margin_top"],
                bottomMargin=PDF_SETTINGS["margin_bottom"]
            )
            
            # Build content
            story = []
            
            # Add title
            story.append(Paragraph(template["title"], self.styles["CustomTitle"]))
            story.append(Spacer(1, 20))
            
            # Add sections
            for section in template["sections"]:
                # Add section heading
                story.append(Paragraph(section["heading"], 
                                    self.styles["SectionHeading"]))
                story.append(Spacer(1, 12))
                
                # Add fields
                for field in section["fields"]:
                    # Format field with template data
                    formatted_field = field.format(**template_data)
                    story.append(Paragraph(formatted_field, 
                                        self.styles["BodyText"]))
                    
                story.append(Spacer(1, 20))
            
            # Build PDF
            doc.build(story, onFirstPage=self._create_header, 
                     onLaterPages=self._create_header)
            
            return True
            
        except Exception as e:
            print(f"Error generating PDF: {str(e)}")
            return False
            
    def preview_pdf(self, template_name: str, template_data: Dict) -> str:
        """
        Generate preview of PDF content without creating file.
        
        Args:
            template_name: Name of template to use
            template_data: Dictionary of template variables
            
        Returns:
            str: Formatted content preview
        """
        if template_name not in TEMPLATES:
            raise ValueError(f"Unknown template: {template_name}")
            
        template = TEMPLATES[template_name]
        preview = [template["title"], ""]
        
        for section in template["sections"]:
            preview.append(section["heading"])
            preview.append("-" * len(section["heading"]))
            
            for field in section["fields"]:
                preview.append(field.format(**template_data))
                
            preview.append("")
            
        return "\n".join(preview)

# Example usage:
"""
pdf_gen = PDFGenerator()

# Template data
data = {
    "customer_name": "John Doe",
    "address": "123 Main St",
    "inspection_date": "2024-01-15",
    "inspector_name": "Mike Smith",
    "findings": "No significant damage found",
    "next_steps": "Schedule follow-up in 6 months"
}

# Generate PDF
success = pdf_gen.generate_pdf("APPROVED", "inspection_report.pdf", data)

# Preview content
preview = pdf_gen.preview_pdf("APPROVED", data)
print(preview)
"""
