from drug_store.src.server.database.db_manager import db_manager
from drug_store.src.server.database.models import Applications

def add_application(application: Applications) -> dict:
    res = db_manager.execute(
        query="""INSERT INTO Applications (application_number, date_added, drug_id, customer_data, status)
                  VALUES (?, ?, ?, ?, ?)
                  RETURNING id""",
        args=(application.application_number, application.date_added, application.drug_id,
              application.customer_data, application.status)
    )

    return res

def edit_application(application_id: int, new_status: str, new_drug_id: int) -> dict:
    res = db_manager.execute(
        query="""UPDATE Applications
                  SET status = ?, drug_id = ?
                  WHERE id = ?
                  RETURNING id""",
        args=(new_status, new_drug_id, application_id)
    )

    return res

def track_application_status(application_id: int) -> dict:
    res = db_manager.execute(
        query="""SELECT id, application_number, date_added, drug_id, customer_data, status
                  FROM Applications
                  WHERE id = ?""",
        args=(application_id,)
    )

    return res

def assign_responsible(application_id: int, seller_id: int, comment: str) -> dict:
    res = db_manager.execute(
        query="""UPDATE Applications
                  SET seller_id = ?, comment = ?
                  WHERE id = ?
                  RETURNING id""",
        args=(seller_id, comment, application_id)
    )

    return res
