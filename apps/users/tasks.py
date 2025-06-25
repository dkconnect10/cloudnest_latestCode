from celery import shared_task
from .models import User

@shared_task
def userActivation_Task(user_id):
    user=User.objects.filter(pk = user_id).first()
    if user:
        user.is_active=True
        user.save()
        return "User Activate Successfully after 90 days."
    return "User not found"

