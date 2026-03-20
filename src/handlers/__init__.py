from .start_cmd import router as start_cmd_router
from .schedule_cmd import router as schedule_cmd_router

__all_routers__ = [
    start_cmd_router,
    schedule_cmd_router,
]
