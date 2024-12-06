from fastapi import APIRouter, HTTPException
from models.announcement import Announcement

router = APIRouter()

@router.get("/announcements")
async def get_announcements():
    announcements = await Announcement.all()
    return announcements
