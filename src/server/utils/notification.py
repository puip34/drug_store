class NotificationManager:
    def __init__(self):
        self.notifications = []

    def add_notification(self, notification_type, message):
        self.notifications.append({"type": notification_type, "message": message})

    def get_notifications(self):
        return self.notifications

    def clear_notifications(self):
        self.notifications = []
