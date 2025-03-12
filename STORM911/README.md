# Storm911 Application

A comprehensive call center solution for managing leads, scheduling appointments, and handling customer interactions.

## Features

- Secure login with API authentication
- Interactive call script system
- Sophisticated objection handling
- Appointment scheduling via Calendly
- PDF report generation
- Email notification system
- Data validation and input sanitization

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/storm911.git
cd storm911
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the application:
```bash
python run.py
```

2. Login with your ReadyMode API credentials

3. Use the interface to:
   - Search for leads
   - Follow call scripts
   - Handle objections
   - Schedule appointments
   - Generate reports
   - Send emails

## Directory Structure

- `assets/` - Application images and resources
- `exports/` - Generated PDF reports
- `logs/` - Application log files
- `temp/` - Temporary files

## Configuration

Edit `config.py` to modify:
- API endpoints
- Email settings
- PDF templates
- UI customization
- Logging configuration

## Support

For support, please contact:
- Email: support@assurecall.com
- Phone: 1-800-SUPPORT

## License

Copyright © 2024 AssureCall. All rights reserved.
