from pydantic import BaseModel, Field


class StudentModel(BaseModel):
    name: str = Field(...)
    surname: str = Field(...)
    age: int = Field(...)
    phone: str | None = Field(...)

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