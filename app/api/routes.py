from fastapi import APIRouter

from app.services.parser_service import parse_text

router = APIRouter()


@router.post("/parse")
def parse(data: dict):
    text = data.get("text")
    return parse_text(text)
