"""
Calendly API integration module for Storm911 application.
Handles all API calls to Calendly service.
"""

import requests
import logging
import json
from typing import Dict, Optional, Union, List
from datetime import datetime
from config import LOGGING_CONFIG

logger = logging.getLogger(__name__)

class CalendlyAPI:
    """
    Handles all interactions with the Calendly API service.
    Implements OAuth2 authentication and API operations.
    """
    def __init__(self):
        self.base_url = "https://api.calendly.com"
        self.auth_url = "https://auth.calendly.com"
        self.access_token = None
        self.refresh_token = None
        self.session = requests.Session()
        
    def set_auth_token(self, access_token: str, refresh_token: Optional[str] = None):
        """Set the OAuth access token and optional refresh token."""
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.session.headers.update({
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json'
        })

    def get_auth_url(self, client_id: str, redirect_uri: str) -> str:
        """
        Get the OAuth authorization URL.
        
        Args:
            client_id: Calendly client ID
            redirect_uri: OAuth redirect URI
            
        Returns:
            str: Authorization URL
        """
        params = {
            'client_id': client_id,
            'response_type': 'code',
            'redirect_uri': redirect_uri
        }
        return f"{self.auth_url}/oauth/authorize?" + '&'.join(f"{k}={v}" for k, v in params.items())

    def get_access_token(self, client_id: str, client_secret: str, code: str, redirect_uri: str) -> Dict:
        """
        Exchange authorization code for access token.
        
        Args:
            client_id: Calendly client ID
            client_secret: Calendly client secret
            code: Authorization code from OAuth flow
            redirect_uri: OAuth redirect URI
            
        Returns:
            Dict: Token response including access_token and refresh_token
        """
        data = {
            'client_id': client_id,
            'client_secret': client_secret,
            'code': code,
            'redirect_uri': redirect_uri,
            'grant_type': 'authorization_code'
        }
        
        response = requests.post(f"{self.auth_url}/oauth/token", data=data)
        response.raise_for_status()
        token_data = response.json()
        
        self.set_auth_token(token_data['access_token'], token_data.get('refresh_token'))
        return token_data

    def refresh_access_token(self, client_id: str, client_secret: str, refresh_token: str) -> Dict:
        """
        Refresh an expired access token.
        
        Args:
            client_id: Calendly client ID
            client_secret: Calendly client secret
            refresh_token: Refresh token from previous auth
            
        Returns:
            Dict: New token response
        """
        data = {
            'client_id': client_id,
            'client_secret': client_secret,
            'refresh_token': refresh_token,
            'grant_type': 'refresh_token'
        }
        
        response = requests.post(f"{self.auth_url}/oauth/token", data=data)
        response.raise_for_status()
        token_data = response.json()
        
        self.set_auth_token(token_data['access_token'], token_data.get('refresh_token'))
        return token_data

    def get_user(self) -> Dict:
        """Get current user information."""
        response = self.session.get(f"{self.base_url}/users/me")
        response.raise_for_status()
        return response.json()

    def get_event_types(self) -> List[Dict]:
        """Get list of event types for the current user."""
        response = self.session.get(f"{self.base_url}/event_types")
        response.raise_for_status()
        return response.json()['data']

    def get_scheduled_events(self, params: Optional[Dict] = None) -> List[Dict]:
        """
        Get list of scheduled events.
        
        Args:
            params: Optional query parameters
            
        Returns:
            List[Dict]: List of scheduled events
        """
        response = self.session.get(f"{self.base_url}/scheduled_events", params=params)
        response.raise_for_status()
        return response.json()['data']

    def create_webhook(self, url: str, events: List[str], scope: str) -> Dict:
        """
        Create a webhook subscription.
        
        Args:
            url: Webhook callback URL
            events: List of event types to subscribe to
            scope: Webhook scope ('user' or 'organization')
            
        Returns:
            Dict: Created webhook data
        """
        data = {
            'url': url,
            'events': events,
            'scope': scope
        }
        
        response = self.session.post(f"{self.base_url}/webhook_subscriptions", json=data)
        response.raise_for_status()
        return response.json()['resource']

    def delete_webhook(self, webhook_uuid: str):
        """
        Delete a webhook subscription.
        
        Args:
            webhook_uuid: UUID of webhook to delete
        """
        response = self.session.delete(f"{self.base_url}/webhook_subscriptions/{webhook_uuid}")
        response.raise_for_status()

    def get_organization_memberships(self) -> List[Dict]:
        """Get list of organization memberships for the current user."""
        response = self.session.get(f"{self.base_url}/organization_memberships")
        response.raise_for_status()
        return response.json()['data']

    def get_user_availability_schedules(self) -> List[Dict]:
        """Get list of availability schedules for the current user."""
        response = self.session.get(f"{self.base_url}/user_availability_schedules")
        response.raise_for_status()
        return response.json()['data']

    def get_event_invitee(self, event_uuid: str, invitee_uuid: str) -> Dict:
        """
        Get information about a specific event invitee.
        
        Args:
            event_uuid: UUID of the event
            invitee_uuid: UUID of the invitee
            
        Returns:
            Dict: Invitee information
        """
        response = self.session.get(
            f"{self.base_url}/scheduled_events/{event_uuid}/invitees/{invitee_uuid}"
        )
        response.raise_for_status()
        return response.json()['resource']

    def list_event_types_by_organization(self, organization_uri: str) -> List[Dict]:
        """
        Get list of event types for an organization.
        
        Args:
            organization_uri: URI of the organization
            
        Returns:
            List[Dict]: List of event types
        """
        params = {'organization': organization_uri}
        response = self.session.get(f"{self.base_url}/event_types", params=params)
        response.raise_for_status()
        return response.json()['data']

    def get_user_busy_times(self, user_uri: str, start_time: str, end_time: str) -> List[Dict]:
        """
        Get user's busy times within a date range.
        
        Args:
            user_uri: URI of the user
            start_time: Start time in ISO format
            end_time: End time in ISO format
            
        Returns:
            List[Dict]: List of busy time periods
        """
        params = {
            'user': user_uri,
            'start_time': start_time,
            'end_time': end_time
        }
        response = self.session.get(f"{self.base_url}/user_busy_times", params=params)
        response.raise_for_status()
        return response.json()['data']
