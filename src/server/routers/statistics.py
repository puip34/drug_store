import fastapi
from drug_store.src.server.resolvers import statistics

statistics_router = fastapi.APIRouter(prefix='/statistics', tags=["Statistics"])

@statistics_router.get(path='/calculate_performance', response_model=dict)
def calculate_performance_statistics() -> dict:
    return statistics.calculate_performance_statistics()
