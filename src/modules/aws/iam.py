# Created by TheWintersShadow.

from base import AWS
from object_classes.iam import IAMRole, IAMUser
from typing import List
import json

class IAM(AWS):
    def __init__(self):
        super().__init__()
        self.iam_client = self.create_client(service_name='iam')

    def list_roles(self) -> List[IAMRole]:
        roles = self.iam_client.list_roles()
        return [IAMRole(x) for x in roles['Roles']]

    def list_users(self) -> List[IAMUser]:
        users = self.iam_client.list_users()
        return [IAMUser(x) for x in users['Users']]
