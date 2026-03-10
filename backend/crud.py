from datetime import datetime
from database import complaints_collection
from utils import serialize_doc


async def create_complaint(text, location, category, sentiment):

    complaint = {
        "text": text,
        "location": location,
        "category": category,
        "sentiment": sentiment,
        "status": "Pending",
        "timestamp": datetime.utcnow().isoformat()
    }

    result = await complaints_collection.insert_one(complaint)

    complaint["_id"] = result.inserted_id

    return serialize_doc(complaint)
