from fastapi import APIRouter, Depends
from src.auth.base_config import current_user

from .tasks import send_email_dashboard

router = APIRouter(prefix="/report")


@router.get("/dashboard")
def get_dashboard_report(user=Depends(current_user)):
    send_email_dashboard.delay(user.username, user.email)
    return {
        "status": 200,
        "data": "Письмо отправлено",
        "details": None
    }
