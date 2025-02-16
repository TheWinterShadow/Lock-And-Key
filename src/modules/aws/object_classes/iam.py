from typing import Dict, List, Union
from datetime import datetime

class IAMObject:
    """
    A base class representing a generic IAM object (e.g., User, Role, etc.).
    This class stores raw data and exposes computed properties like 'path', 'arn', and 'create_date'.
    """

    def __init__(self, raw_data: Dict[str, str]):
        """
        Initializes the IAMObject with the given raw data.

        Args:
            raw_data (Dict[str, str]): A dictionary containing raw data for the IAM object
        """
        self.raw_data = raw_data

    @property
    def path(self) -> str:
        """
        Returns the 'Path' attribute from the raw data.

        Returns:
            str: The path of the IAM object.
        """
        return self.raw_data['Path']

    @property
    def arn(self) -> str:
        """
        Returns the 'Arn' attribute from the raw data.

        Returns:
            str: The ARN (Amazon Resource Name) of the IAM object.
        """
        return self.raw_data['Arn']

    @property
    def create_date(self) -> datetime:
        """
        Parses and returns the 'CreateDate' attribute from the raw data as a datetime object.

        Returns:
            datetime: The creation date of the IAM object as a datetime object.
        """
        return self.raw_data['CreateDate']

    def to_dict(self) -> Dict[str, str]:
        """
        Converts the IAMObject instance into a dictionary representation, 
        including both regular attributes and computed properties, excluding 'raw_data'.

        Returns:
            Dict[str, str]: A dictionary representation of the IAM object with its attributes and properties.
        """
        # Create a dictionary to hold the regular attributes and properties
        data = {key: value for key, value in self.__dict__.items() if key != 'raw_data'}  # Exclude raw_data

        # Include all properties dynamically
        for attr in dir(self):
            prop = getattr(self.__class__, attr, None)  # Get the class attribute
            if isinstance(prop, property):  # Check if it's a property
                data[attr] = getattr(self, attr)  # Add property value to the dict

        return data


class IAMRole(IAMObject):
    """
    A class representing an IAM Role, which inherits from IAMObject.
    It exposes additional attributes and properties specific to IAM roles, such as 'role_name', 'role_id', and 'max_session_duration'.
    """
    
    def __init__(self, raw_data: Dict[str, str]):
        """
        Initializes the IAMRole object with the given raw data.

        Args:
            raw_data (Dict[str, str]): A dictionary containing raw data for the IAM Role object
        """
        super().__init__(raw_data)

    @property
    def role_name(self) -> str:
        """
        Returns the 'RoleName' attribute from the raw data.

        Returns:
            str: The role name of the IAM role.
        """
        return self.raw_data['RoleName']

    @property
    def role_id(self) -> str:
        """
        Returns the 'RoleId' attribute from the raw data.

        Returns:
            str: The role ID of the IAM role.
        """
        return self.raw_data['RoleId']

    @property
    def policy_doc(self) -> Dict[str, Union[str, List[Dict[str, Dict[str, str]]]]]:
        """
        Returns the 'AssumeRolePolicyDocument' from the raw data.

        Returns:
            Dict[str, Union[str, List[Dict[str, Dict[str, str]]]]]: The policy document associated with the IAM role.
        """
        return self.raw_data['AssumeRolePolicyDocument']

    @property
    def max_session_duration(self) -> int:
        """
        Returns the 'MaxSessionDuration' attribute from the raw data.

        Returns:
            int: The maximum session duration for the IAM role, in seconds.
        """
        return self.raw_data['MaxSessionDuration']


class IAMUser(IAMObject):
    """
    A class representing an IAM User, which inherits from IAMObject.
    It exposes additional attributes and properties specific to IAM users, such as 'user_name' and 'user_id'.
    """
    
    def __init__(self, raw_data: Dict[str, str]):
        """
        Initializes the IAMUser object with the given raw data.

        Args:
            raw_data (Dict[str, str]): A dictionary containing raw data for the IAM User object
        """
        super().__init__(raw_data)

    @property
    def user_name(self) -> str:
        """
        Returns the 'UserName' attribute from the raw data.

        Returns:
            str: The user name of the IAM user.
        """
        return self.raw_data['UserName']

    @property
    def user_id(self) -> str:
        """
        Returns the 'UserId' attribute from the raw data.

        Returns:
            str: The user ID of the IAM user.
        """
        return self.raw_data['UserId']

