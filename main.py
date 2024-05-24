from typing import Optional, List
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel
from api import users, courses, sections

app = FastAPI(
    title="LMS API",
    description="LMS for managing courses",
    version="0.1.0",
    contact={
        "name": "LMS",
        "email": "admin@lms.com"
    },
    license_info={
        "name": "LMS",
        "url": "http://lms.com"
    }
)


app.include_router(users.router)
app.include_router(sections.router)
app.include_router(courses.router)