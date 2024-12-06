from fastapi import APIRouter, HTTPException
from models.student import Student

router = APIRouter()

@router.get("/students/{student_id}")
async def get_student(student_id: int):
    student = await Student.get(student_id)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student
