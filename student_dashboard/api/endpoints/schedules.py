from fastapi import APIRouter
from models.schedule import Schedule, HTTPException

router = APIRouter()

@router.get("/students/{student_id}/schedule")
async def get_schedule(student_id: int):
    schedule = await Schedule.get(student_id)
    if schedule is None:
        raise HTTPException(status_code=404, detail="Schedule not found")
    return schedule
