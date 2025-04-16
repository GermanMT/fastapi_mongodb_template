from re import match

from pydantic import BaseModel, Field, field_validator, ConfigDict


class StudentModel(BaseModel):
    name: str = Field(
        ...,
        min_length=1,
        description="The name size must be greater than zero"
    )
    surname: str = Field(
        ...,
        min_length=1,
        description="The surname size must be greater than zero"
    )
    age: int = Field(
        ...,
        gt=0,
        description="The age must be greater than zero"
    )
    phone: str | None = None

    @field_validator("phone")
    def phone_validation(cls, phone: str) -> str:
        if not match(r"[\d]{3} [\d]{3} [\d]{3}", phone):
            raise ValueError(f"The phone {phone} is not correct")
        return phone

    model_config = ConfigDict(from_attributes=True)