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
    address_street: str = Field(examples=["473 Big Rock Cove Street Metairie, LA 70001"],
                         description="address")
    city: str = Field(examples=["San Diego"],
                      description="City name")
    state: str = Field(examples=["CA"],
                       description="State name")
    zip_code: str = Field(examples=["92103"],
                          description="Zip code")
    phone_number: str = Field(examples=["6193317553"],
                              description="Phone number")
    ssn: str = Field(examples=["502948172"],
                     description="Social security number")
    user_name: str = Field(examples=["test_user"],
                           description="User name")
    password: SecretStr = Field(examples=["Password123"],
                                description="Password of the user")
    confirm_password: SecretStr = Field(examples=["Password123"],
                                        description="Confirmation for password input must be the same")


class RegistrationFactory(DictWithAttributes):
    """Factory class for creating a new user"""
    first_name: str = f'{DataGenerator.first_name()}{random.randint(0,1000)}'
    last_name: str = DataGenerator.last_name()
    address: dict = DataGenerator.address()
    address_street: str = address['street']
    city: str = address['city']
    state: str = address['state']
    zip_code: str = address['zip_code']
    phone_number: str = DataGenerator.phone_number()
    ssn: str = DataGenerator.ssn()
    user_name: str = first_name
    password: str = "test_password"
    confirm_password: str = "test_password"


if __name__ == '__main__':
    f = RegistrationFactory()
    print(f)
