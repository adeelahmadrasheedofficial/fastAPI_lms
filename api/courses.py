from typing import Optional, List
import fastapi
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel

router = fastapi.APIRouter()


@router.get("/courses/{id}")
async def read_courses():
    return {"courses": []}


@router.post("/courses/")
async def create_courses_api():
    return {"courses": []}


@router.get("/courses/{id}")
async def get_courses_api():
    return {"courses": []}


@router.patch("/courses/{id}")
async def update_courses_api():
    return {"courses": []}


@router.delete("/courses/{id}")
async def delete_courses_api():
    return {"courses": []}
