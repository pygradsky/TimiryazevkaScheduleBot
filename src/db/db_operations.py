import os
import aiosqlite

from src.configs.config import DataConfig

data_config = DataConfig()
db_file = os.path.join(data_config.db_dir, 'users.db')
users_cache = {}


async def create_table() -> None:
    async with aiosqlite.connect(db_file) as conn:
        await conn.execute(
            """CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            group_id INTEGER NOT NULL,
            faculty TEXT NOT NULL,
            join_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
            )
            """
        )
        await conn.commit()


async def save_user_info(user_id: int, username: str) -> None:
    async with aiosqlite.connect(db_file) as conn:
        await conn.execute(
            "INSERT OR IGNORE INTO users (user_id, username, group_id, faculty) VALUES (?, ?, ?, ?)",
            (user_id, username, 0, '')
        )
        await conn.commit()


async def get_user_info(user_id: int) -> dict | None:
    async with aiosqlite.connect(db_file) as conn:
        cur = await conn.execute(
            "SELECT user_id, username, group_id, faculty, join_date FROM users WHERE user_id = ?",
            (user_id,)
        )
        row = await cur.fetchone()

        if row:
            return {
                'user_id': row[0],
                'username': row[1],
                'group_id': row[2],
                'faculty': row[3],
                'join_date': row[4]
            }
        return None


async def get_cached_user_info(user_id: int) -> dict:
    if user_id not in users_cache:
        user_data = await get_user_info(user_id)
        users_cache[user_id] = user_data

    print(users_cache)
    return users_cache[user_id]
