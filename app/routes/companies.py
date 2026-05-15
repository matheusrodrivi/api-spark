from fastapi import APIRouter
from app.services.loader import load_json_lines

router = APIRouter(prefix="/companies")

companies = load_json_lines("refined/top-companies/data.json")

@router.get("/")
def get_companies():
    return companies

@router.get("/top")
def get_top_companies():
    return max(companies, key=lambda x: x["count"])