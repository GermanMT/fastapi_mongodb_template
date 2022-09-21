from pydantic import BaseModel, Field, validator

from re import match


class StudentModel(BaseModel):
    name: str = Field(min_length = 1, description = "The name size must be greater than zero")
    surname: str = Field(min_length = 1, description = "The surname size must be greater than zero")
    age: int = Field(gt = 0, description = "The age must be greater than zero")
    phone: str | None = Field(...)

    @validator("phone")
    def phone_must_be_positive(cls, phone):
        if match(r'[\+\d]?(\d{2,3}[-\.\s]??\d{2,3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})', phone):
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
                'phone': '678340253'
            }
        }