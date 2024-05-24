from typing import Optional, List
import fastapi
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel

router = fastapi.APIRouter()


@router.get("/sections/:id")
async def read_sec():
    return {"section": []}


@router.post("/sections/:id/content-blocks")
async def read_sec_content_blocks():
    return {"courses": []}


@router.get("/content-blocks/:id")
async def read_content_blocks():
    return {"courses": []}
