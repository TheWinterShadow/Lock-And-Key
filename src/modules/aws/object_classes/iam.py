from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime
from typing import Dict, List, Union

from pydantic import BaseModel, Field


class IAMObjectBase(ABC, BaseModel):
    """Abstract base class for IAM objects with Pydantic validation."""
    
    path: str = Field(..., alias='Path')
    arn: str = Field(..., alias='Arn')
    create_date: datetime = Field(..., alias='CreateDate')
    
    class Config:
        allow_population_by_field_name = True
        
    @abstractmethod
    def get_identifier(self) -> str:
        """Return the primary identifier for this IAM object."""
        pass


@dataclass
class IAMRole(IAMObjectBase):
    """IAM Role with Pydantic validation and dataclass structure."""
    
    role_name: str = Field(..., alias='RoleName')
    role_id: str = Field(..., alias='RoleId')
    policy_doc: Dict[str, Union[str, List[Dict[str, Dict[str, str]]]]] = Field(..., alias='AssumeRolePolicyDocument')
    max_session_duration: int = Field(..., alias='MaxSessionDuration')
    
    def get_identifier(self) -> str:
        return self.role_name


@dataclass
class IAMUser(IAMObjectBase):
    """IAM User with Pydantic validation and dataclass structure."""
    
    user_name: str = Field(..., alias='UserName')
    user_id: str = Field(..., alias='UserId')
    
    def get_identifier(self) -> str:
        return self.user_name

