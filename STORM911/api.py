"""
API client module for Storm911.
Handles interactions with the ReadyMode API service.
"""

import os
import json
import logging
import requests
from typing import Dict, List, Optional, Union
from urllib.parse import urljoin

from config import API_SETTINGS

logger = logging.getLogger(__name__)

class APIError(Exception):
    """Base exception for API errors."""
    pass

class AuthenticationError(APIError):
    """Raised when API authentication fails."""
    pass

class ReadyModeAPI:
    """Client for interacting with the ReadyMode API."""
    
    def __init__(self, username: str, password: str):
        """Initialize API client with credentials."""
        self.username = username
        self.password = password
        self.base_url = "https://roofingappointments.readymode.com/TPI"
        self.session = requests.Session()
        self.session.headers.update({
            "Accept": "application/json",
            "Content-Type": "application/json"
        })

    def _make_request(
        self, 
        method: str, 
        endpoint: str, 
        params: Optional[Dict] = None, 
        data: Optional[Dict] = None,
        timeout: int = 30
    ) -> Dict:
        """Make an HTTP request to the API."""
        url = urljoin(self.base_url, endpoint)
        
        # Add authentication parameters
        if params is None:
            params = {}
        params.update({
            "API_user": self.username,
            "API_pass": self.password
        })
        
        try:
            response = self.session.request(
                method=method,
                url=url,
                params=params,
                json=data,
                timeout=timeout
            )
            
            logger.debug(f"API request: {method} {url}")
            logger.debug(f"Params: {params}")
            logger.debug(f"Data: {data}")
            logger.debug(f"Response status: {response.status_code}")
            
            # Handle common error responses
            if response.status_code == 401:
                raise AuthenticationError("Invalid API credentials")
            
            response.raise_for_status()
            
            return response.json()
            
        except requests.exceptions.RequestException as e:
            logger.error(f"API request failed: {str(e)}")
            raise APIError(f"API request failed: {str(e)}")

    def search_lead(self, phone: str) -> List[Dict]:
        """Search for a lead by phone number."""
        try:
            response = self._make_request(
                method="GET",
                endpoint=f"/search/Lead/{phone}"
            )
            return response
        except Exception as e:
            logger.error(f"Lead search failed: {str(e)}")
            raise

    def create_lead(self, lead_data: Dict) -> Dict:
        """Create a new lead."""
        try:
            response = self._make_request(
                method="POST",
                endpoint="/create/Lead",
                data=lead_data
            )
            return response
        except Exception as e:
            logger.error(f"Lead creation failed: {str(e)}")
            raise

    def update_lead(self, lead_id: str, lead_data: Dict) -> Dict:
        """Update an existing lead."""
        try:
            response = self._make_request(
                method="PUT",
                endpoint=f"/update/Lead/{lead_id}",
                data=lead_data
            )
            return response
        except Exception as e:
            logger.error(f"Lead update failed: {str(e)}")
            raise

    def get_lead_status(self, lead_id: str) -> Dict:
        """Get the current status of a lead."""
        try:
            response = self._make_request(
                method="GET",
                endpoint=f"/status/Lead/{lead_id}"
            )
            return response
        except Exception as e:
            logger.error(f"Lead status check failed: {str(e)}")
            raise

    def create_appointment(self, appointment_data: Dict) -> Dict:
        """Create a new appointment."""
        try:
            response = self._make_request(
                method="POST",
                endpoint="/create/Appointment",
                data=appointment_data
            )
            return response
        except Exception as e:
            logger.error(f"Appointment creation failed: {str(e)}")
            raise

    def update_appointment(self, appointment_id: str, appointment_data: Dict) -> Dict:
        """Update an existing appointment."""
        try:
            response = self._make_request(
                method="PUT",
                endpoint=f"/update/Appointment/{appointment_id}",
                data=appointment_data
            )
            return response
        except Exception as e:
            logger.error(f"Appointment update failed: {str(e)}")
            raise

    def get_appointment_status(self, appointment_id: str) -> Dict:
        """Get the current status of an appointment."""
        try:
            response = self._make_request(
                method="GET",
                endpoint=f"/status/Appointment/{appointment_id}"
            )
            return response
        except Exception as e:
            logger.error(f"Appointment status check failed: {str(e)}")
            raise

    def validate_credentials(self) -> bool:
        """Validate API credentials."""
        try:
            # Make a test request
            self._make_request(
                method="GET",
                endpoint="/test",
                timeout=5
            )
            return True
        except AuthenticationError:
            return False
        except Exception as e:
            logger.error(f"Credential validation failed: {str(e)}")
            return False

# Create a singleton instance
_api_client: Optional[ReadyModeAPI] = None

def get_api_client(username: str = None, password: str = None) -> ReadyModeAPI:
    """Get or create the API client singleton."""
    global _api_client
    
    if _api_client is None and username and password:
        _api_client = ReadyModeAPI(username, password)
    
    if _api_client is None:
        raise RuntimeError("API client not initialized. Provide credentials first.")
    
    return _api_client
