from fastapi import FastAPI, HTTPException
import schemas
import crud
import ai_engine

from database import complaints_collection, admins_collection
from utils import serialize_doc
from auth import hash_password, verify_password, create_token

app = FastAPI(title="Smart Public Service CRM API")


# ---------------- SUBMIT COMPLAINT ---------------- #

@app.post("/submit-complaint")
async def submit_complaint(complaint: schemas.ComplaintCreate):

    text = complaint.text
    location = complaint.location

    category = ai_engine.detect_category(text)

    sentiment = ai_engine.detect_sentiment(text)

    new_complaint = await crud.create_complaint(
        text,
        location,
        category,
        sentiment
    )

    return new_complaint


# ---------------- GET ALL COMPLAINTS ---------------- #

@app.get("/complaints")
async def get_complaints():

    complaints = []

    async for doc in complaints_collection.find():

        complaints.append(serialize_doc(doc))

    return complaints


# ---------------- ADMIN SIGNUP ---------------- #

@app.post("/admin/signup")
async def admin_signup(admin: schemas.AdminSignup):

    existing = await admins_collection.find_one(
        {"username": admin.username}
    )

    if existing:
        raise HTTPException(status_code=400, detail="Admin already exists")

    hashed_password = hash_password(admin.password)

    await admins_collection.insert_one({
        "username": admin.username,
        "password": hashed_password
    })

    return {"message": "Admin created successfully"}


# ---------------- ADMIN LOGIN ---------------- #

@app.post("/admin/login")
async def admin_login(admin: schemas.AdminLogin):

    user = await admins_collection.find_one(
        {"username": admin.username}
    )

    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    if not verify_password(admin.password, user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_token(admin.username)

    return {"access_token": token}


# ---------------- AI SUMMARY ---------------- #

@app.post("/summarize")
async def summarize(req: schemas.SummaryRequest):

    summary = ai_engine.summarize_text(req.text)

    return {"summary": summary}
