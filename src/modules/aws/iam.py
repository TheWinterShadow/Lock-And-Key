# Created by TheWintersShadow.

from dataclasses import dataclass, field
from typing import List
from mypy_boto3_iam import IAMClient

from src.modules.aws.base import AWS
from src.modules.aws.object_classes.iam import IAMRole, IAMUser


@dataclass
class IAM(AWS):
    """IAM service class with role and user management."""
    
    iam_client: IAMClient = field(init=False)
    
    def __post_init__(self):
        super().__post_init__()
        self.iam_client = self.create_client(service_name='iam')

    def list_roles(self) -> List[IAMRole]:
        roles = self.iam_client.list_roles()
        return [IAMRole(**x) for x in roles['Roles']]

    def list_users(self) -> List[IAMUser]:
        users = self.iam_client.list_users()
        return [IAMUser(**x) for x in users['Users']]
