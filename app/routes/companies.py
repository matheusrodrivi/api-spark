from fastapi import APIRouter
from app.services.loader import load_json_lines

router = APIRouter(
    prefix="/companies",
    tags=["Companies"]
)

companies = load_json_lines("refined/top-companies/data.json")

@router.get("/")
def get_companies():
    return companies

@router.get("/top")
def get_top_companies():
    return max(companies, key=lambda x: x["count"])

@router.get("/bottom")
def get_bottom_company():
    return min(companies, key=lambda x: x["count"])

@router.get("/average")
def get_average():
    average = sum(c["count"] for c in companies) / len(companies)

    formatted = f"{average:,.2f}" \
        .replace(",", "X") \
        .replace(".", ",") \
        .replace("X", ".")

    return {
        "average": formatted
    }