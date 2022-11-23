from re import match

from pydantic import BaseModel, Field, validator


class StudentModel(BaseModel):
    name: str = Field(..., min_length=1, description="The name size must be greater than zero")
    surname: str = Field(
        ...,
        min_length=1,
        description="The surname size must be greater than zero"
    )
    age: int = Field(..., gt=0, description="The age must be greater than zero")
    phone: str | None = Field(...)

    @validator("phone")
    def phone_validation(cls, phone: str) -> ValueError | str:
        if not match(r'[\d]{3} [\d]{3} [\d]{3}', phone):
            raise ValueError(f"The phone {phone} is not correct")
        return phone

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        schema_extra = {
            'example': {
                'name': 'John',
                'surname': 'Doe',
                'age': 24,
                'phone': '678 340 253'
            }
        }