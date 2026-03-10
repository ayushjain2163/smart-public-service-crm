from pydantic import BaseModel
from typing import Optional


class ComplaintCreate(BaseModel):
    text: str
    location: str


class ComplaintResponse(BaseModel):

    id: Optional[str]
    text: str
    location: str
    category: str
    sentiment: str
    status: str
    timestamp: str


class SummaryRequest(BaseModel):
    text: str


class AdminSignup(BaseModel):
    username: str
    password: str


class AdminLogin(BaseModel):
    username: str
    password: str
