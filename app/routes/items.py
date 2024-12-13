from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db

router = APIRouter()

@router.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None, db: Session = Depends(get_db)):
    # Example query (replace with your actual query)
    result = db.execute("SELECT * FROM items WHERE id = :id", {"id": item_id}).fetchone()
    return {"item_id": item_id, "q": q, "result": result}