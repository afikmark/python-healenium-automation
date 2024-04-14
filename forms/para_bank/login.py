from pydantic import BaseModel, SecretStr, Field


class LoginValidationError(Exception):
    """Custom exception for login validation errors"""
    pass


class LoginForm(BaseModel):
    user_name: str = Field(examples=["test_user"],
                           description="User name")
    password: SecretStr = Field(examples=["Password123"],
                                description="Password of the user")
