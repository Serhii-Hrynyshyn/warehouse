import sqlite3
from .get_current_time import get_current_time


def show_all(cursor) -> None:
    print(f"{'-' * 45}\n\tЗАЛИШОК ТОВАРУ ПО БАЗІ НА: {get_current_time()}")
    cursor.execute("SELECT * FROM Goods")
    for good in cursor.fetchall():
        params = []
        for param in range(5):
            params.append(good[param])
        print(
            f"№{params[0]}|Назва: {params[1]}|Кількість: {params[2]}"
            f"|Вартість(грн.): {params[3]}|Час операції: {params[4]}"
        )
