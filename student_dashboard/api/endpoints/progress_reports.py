from fastapi import APIRouter, HTTPException
from models.progress_report import ProgressReport

router = APIRouter()

@router.get("/students/{student_id}/progress_report")
async def get_progress_report(student_id: int):
    report = await ProgressReport.get(student_id)
    if report is None:
        raise HTTPException(status_code=404, detail="Progress Report not found")
    return report
