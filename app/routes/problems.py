from fastapi import APIRouter
from app.services.loader import load_json_lines

router = APIRouter(
    prefix="/problems",
    tags=["Problems"]
)

problems = load_json_lines("refined/top-problems/data.json")

@router.get("/")
def get_problems():
    return problems

@router.get("/top")
def get_top_problems():
    return max(problems, key=lambda x: x["count"])

@router.get("/bottom")
def get_bottom_problem():
    return min(problems, key=lambda x: x["count"])

@router.get("/average")
def get_average_problems():
    average = sum(c["count"] for c in problems) / len(problems)

    formatted = f"{average:,.2f}" \
        .replace(",", "X") \
        .replace(".", ",") \
        .replace("X", ".")

    return {
        "average": formatted
    }