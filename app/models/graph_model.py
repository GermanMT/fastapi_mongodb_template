from pydantic import BaseModel, Field

from app.models.requirement_file_model import RequirementFile


class GraphModel(BaseModel):
    owner: str = Field(...)
    name: str = Field(...)
    manager: str = Field(...)
    add_extras: bool = Field(...)
    is_complete: bool = Field(...)
    requirement_files: list[RequirementFile] | None = None

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        schema_extra = {
            'example': {
                'owner': 'urllib3',
                'name': 'urllib3',
                'manager': 'PIP',
                'add_extras': False,
                'is_complete': False
            }
        }