# Created by TheWhiteWolf
# This is the base class for all AWS modules
import json
from abc import ABC
from typing import Any, Dict

from boto3 import Session  # type: ignore
from pydantic import BaseModel, ConfigDict, PrivateAttr  # type: ignore


class AWS(ABC, BaseModel):
    """Base AWS class with session management."""

    model_config = ConfigDict(arbitrary_types_allowed=True)

    _creds: Dict[str, str] = PrivateAttr()
    _session: Session = PrivateAttr()

    def __init__(self, **data):
        super().__init__(**data)
        self._creds = self._get_creds()
        self._session = self._create_session()

    @property
    def creds(self) -> Dict[str, str]:
        return self._creds

    @property
    def session(self) -> Session:
        return self._session

    @property
    def account_id(self) -> str:
        return self._session.client("sts").get_caller_identity()["Account"]

    def _get_creds(self) -> Dict[str, str]:
        with open("key.json", "r") as f:
            creds = json.load(f)
        return creds

    def _create_session(self) -> Session:
        return Session(
            aws_access_key_id=self._creds["id"],
            aws_secret_access_key=self._creds["key"],
        )

    def create_client(self, service_name: str) -> Any:
        return self._session.client(service_name)

    def create_resource(self, resource_name: str) -> Any:
        return self._session.resource(resource_name)
