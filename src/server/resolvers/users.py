from drug_store.src.server.database.db_manager import db_manager
from drug_store.src.server.database.models import Users

def login(username: str, password: str) -> dict:
    res = db_manager.execute(
        query="""SELECT id, username, email, role
                  FROM Users
                  WHERE username = ? AND password = ?""",
        args=(username, password)
    )

    return res

def change_password(user_id: int, new_password: str) -> dict:
    res = db_manager.execute(
        query="""UPDATE Users
                  SET password = ?
                  WHERE id = ?
                  RETURNING id""",
        args=(new_password, user_id)
    )

    return res
