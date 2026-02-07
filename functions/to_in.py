from .safe_input import safe_input
from .get_current_time import get_current_time


def to_in(db_connection, cursor) -> None:
    print("--- ПРИХІД НА СКЛАД ---\n*Номенклатура товару*")
    name = safe_input(str)
    print("*Кількість товару*")
    quantity = safe_input(int)
    print("*Ціна товару*")
    price = safe_input(float)
    cursor.execute(f"SELECT goods_name FROM goods WHERE goods_name = '{name}'")
    try:
        if cursor.fetchone()[0] == name:
            update(cursor, name, quantity, price)
    except Exception as e:
        insert(cursor, name, quantity, price)
    db_connection.commit()


def update(cursor, name, quantity, price) -> None:
    cursor.execute(f"""
    UPDATE Goods SET 
    goods_quantity = goods_quantity + '{quantity}', 
    goods_price = '{price}' 
    WHERE goods_name = '{name}'""")


def insert(cursor, name, quantity, price) -> None:
    cursor.execute(
        "INSERT INTO Goods("
        "goods_name, "
        "goods_quantity, "
        "goods_price, "
        "action_date )"
        "VALUES (?, ?, ?, ?)",
        (name, quantity, price, get_current_time()),
    )
