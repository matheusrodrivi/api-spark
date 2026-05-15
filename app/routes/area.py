from fastapi import APIRouter
from app.services.loader import load_json_lines

router = APIRouter(
    prefix="/areas",
    tags=["Areas"]
)

areas = load_json_lines("refined/area/data.json")

@router.get("/")
def get_area():
    return areas

@router.get("/top")
def get_top_area():
    return max(areas, key=lambda x: x["count"])

@router.get("/bottom")
def get_bottom_area():
    return min(areas, key=lambda x: x["count"])

@router.get("/average")
def get_average_area():
    average = sum(c["count"] for c in areas) / len(areas)

    formatted = f"{average:,.2f}" \
        .replace(",", "X") \
        .replace(".", ",") \
        .replace("X", ".")

    return {
        "average": formatted
    }