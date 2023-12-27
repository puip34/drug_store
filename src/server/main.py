from fastapi import FastAPI
from drug_store.src.server.routers import applications
from drug_store.src.server.utils.notification import NotificationManager

app = FastAPI()

# Include additional routers
app.include_router(applications.router)

# Initialize Notification Manager
notification_manager = NotificationManager()

# Include Notification Manager in dependency for routers
app.dependency_overrides[applications.get_notification_manager] = lambda: notification_manager

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
