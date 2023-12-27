from enum import Enum
from pydantic import BaseModel
from typing import List

class NotificationType(str, Enum):
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"

class Notification(BaseModel):
    type: NotificationType
    message: str

class NotificationManager:
    notifications: List[Notification] = []

    @classmethod
    def add_notification(cls, type: NotificationType, message: str):
        notification = Notification(type=type, message=message)
        cls.notifications.append(notification)

    @classmethod
    def get_notifications(cls) -> List[Notification]:
        return cls.notifications

    @classmethod
    def clear_notifications(cls):
        cls.notifications = []

notification_manager = NotificationManager()
