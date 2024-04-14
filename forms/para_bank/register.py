from pydantic import BaseModel, SecretStr, Field
from common.providers import DictWithAttributes
from framework.utils import DataGenerator
import random


class RegisterValidationError(Exception):
    """Custom exception for registration validation errors"""
    pass


class RegistrationForm(BaseModel):
    first_name: str = Field(examples=["test_user"],
                            description="first name")
    last_name: str = Field(examples=["test_user"],
                           description="last name")
    address: str = Field(examples=["473 Big Rock Cove Street Metairie, LA 70001"],
                         description="address")
    city: str = Field(examples=["San Diego"],
                      description="City name")
    state: str = Field(examples=["CA"],
                       description="State name")
    zip_code: int = Field(examples=[92103],
                          description="Zip code")
    phone_number: int = Field(examples=[6193317553],
                              description="Phone number")
    ssn: int = Field(examples=[502948172],
                     description="Social security number")
    user_name: str = Field(examples=["test_user"],
                           description="User name")
    password: SecretStr = Field(examples=["Password123"],
                                description="Password of the user")
    confirm_password: SecretStr = Field(examples=["Password123"],
                                        description="Confirmation for password input must be the same")


class RegistrationFactory(DictWithAttributes):
    """Factory class for creating a new user"""
    first_name: str = DataGenerator.first_name()
    last_name: str = DataGenerator.last_name()
    # address: str =
    # city: str =
    # state: str =
    # zip_code: str =
    # phone_number: str =
    # ssn: str = DataGenerator.ssn()
    # user_name: str =
    # password: str =


if __name__ == '__main__':
    f = RegistrationFactory()
    print(f)
