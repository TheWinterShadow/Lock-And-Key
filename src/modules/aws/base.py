# Created by TheWhiteWolf
# This is the base class for all AWS modules
import json
import boto3
from typing import Dict

class AWS:
    def __init__(self):
        self.creds = self._get_creds()
        self.session = self._create_session()

    @property
    def account_id(self) -> str:
        return self.session.client("sts").get_caller_identity()["Account"]

    def _get_creds(self) -> Dict[str, str]:
        with open('key.json', 'r') as f:
            creds = json.load(f)
        return creds

    def _create_session(self) -> boto3.Session:
        return boto3.Session(self.creds['id'], self.creds['key'])
    
    def create_client(self, service_name: str) -> boto3.client:
        return  self.session.client(service_name)
    
    def create_resource(self, resource_name: str) -> boto3.resource:
        return self.session.resource(resource_name)

    
