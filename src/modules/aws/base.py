# Created by TheWhiteWolf
# This is the base class for all AWS modules
import json
from abc import ABC
from dataclasses import dataclass, field
from boto3 import Session, client, resource
from typing import Dict
from pydantic import BaseModel, validator


@dataclass
class AWS(ABC, BaseModel):
    """Base AWS class with session management."""
    
    creds: Dict[str, str] = field(init=False)
    session: Session = field(init=False)
    
    class Config:
        arbitrary_types_allowed = True
    
    def __post_init__(self):
        self.creds = self._get_creds()
        self.session = self._create_session()

    @property
    def account_id(self) -> str:
        return self.session.client("sts").get_caller_identity()["Account"]

    def _get_creds(self) -> Dict[str, str]:
        with open('key.json', 'r') as f:
            creds = json.load(f)
        return creds

    def _create_session(self) -> Session:
        return Session(self.creds['id'], self.creds['key'])

    def create_client(self, service_name: str) -> client:
        return self.session.client(service_name)

    def create_resource(self, resource_name: str) -> resource:
        return self.session.resource(resource_name)
