from .populate_service import students_bulkwrite
from .student_service import (
    create_student,
    delete_student,
    read_student,
    update_student,
)

__all__ = ["students_bulkwrite", "create_student", "delete_student", "read_student", "update_student"]
