from fastapi import FastAPI
from api import users, courses, sections
from db.db_setup import engine
from db.models import user, course


user.Base.metadata.create_all(bind=engine)
course.Base.metadata.create_all(bind=engine)

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