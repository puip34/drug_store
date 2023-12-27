from drug_store.src.server.database.db_manager import db_manager

def calculate_performance_statistics() -> dict:
    res = db_manager.execute(
        query="""SELECT COUNT(*) AS num_completed_applications,
                        AVG(DATEDIFF(completed_date, date_added)) AS avg_time_to_complete,
                        drug_id,
                        COUNT(DISTINCT drug_id) AS num_drug_types
                  FROM Applications
                  WHERE status = 'completed'
                  GROUP BY drug_id"""
    )

    return res
