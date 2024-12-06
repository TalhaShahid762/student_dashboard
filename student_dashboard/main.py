from fastapi import FastAPI, HTTPException
from api.endpoints import students, progress_reports, schedules, announcements
from db.database import engine, Base

# Create the database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include the routers for each endpoint
app.include_router(students.router)
app.include_router(progress_reports.router)
app.include_router(schedules.router)
app.include_router(announcements.router)
