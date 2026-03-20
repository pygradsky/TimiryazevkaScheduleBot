import os

from src.configs.config import DataConfig
from src.db.db_operations import create_table

data_config = DataConfig()

db_file = os.path.join(data_config.db_dir, 'users.db')
dirs_to_create = [
    data_config.data_dir,
    data_config.downloads_dir,
    data_config.db_dir,
]


async def create_dirs() -> None:
    for d in dirs_to_create:
        os.makedirs(d, exist_ok=True)


async def setup() -> None:
    await create_dirs()
    await create_table()
