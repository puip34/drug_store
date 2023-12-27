# drug_store/src/server/database/models.py

from pydantic import BaseModel
from typing import List

class UserBase(BaseModel):
    username: str
    email: str
    role: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

class DrugBase(BaseModel):
    name: str
    description: str

class DrugCreate(DrugBase):
    pass

class Drug(DrugBase):
    id: int

    class Config:
        orm_mode = True

class ApplicationBase(BaseModel):
    application_number: int
    date_added: str
    drug_id: int
    customer_data: str
    status: str

class ApplicationCreate(ApplicationBase):
    pass

class Application(ApplicationBase):
    id: int

    class Config:
        orm_mode = True

# Add the new tables below

# UserRole model
class UserRoleBase(BaseModel):
    user_id: int
    role_id: int

class UserRoleCreate(UserRoleBase):
    pass

class UserRole(UserRoleBase):
    id: int

    class Config:
        orm_mode = True

# ProjectUserRole model (assuming it's related to projects, adjust as needed)
class ProjectUserRoleBase(BaseModel):
    project_id: int
    user_id: int
    role_id: int

class ProjectUserRoleCreate(ProjectUserRoleBase):
    pass

class ProjectUserRole(ProjectUserRoleBase):
    id: int

    class Config:
        orm_mode = True

# CompletedProject model
class CompletedProjectBase(BaseModel):
    project_id: int
    completion_date: str

class CompletedProjectCreate(CompletedProjectBase):
    pass

class CompletedProject(CompletedProjectBase):
    id: int

    class Config:
        orm_mode = True

# TaskStatus model
class TaskStatusBase(BaseModel):
    status_name: str

class TaskStatusCreate(TaskStatusBase):
    pass

class TaskStatus(TaskStatusBase):
    id: int

    class Config:
        orm_mode = True

# TaskHistory model
class TaskHistoryBase(BaseModel):
    task_id: int
    status_id: int

class TaskHistoryCreate(TaskHistoryBase):
    pass

class TaskHistory(TaskHistoryBase):
    id: int

    class Config:
        orm_mode = True
