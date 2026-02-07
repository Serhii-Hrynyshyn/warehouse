from .safe_int_input import safe_input


def to_out(db_connection, cursor):
    print("--- ПРОДАЖ ЗІ СКЛАДУ ---\n*Номер товару в базі*")
    name = safe_input(int)
    print("*Кількість товару*")
    quantity = safe_input(int)
    print("*Ціна товару*")
    price = safe_input(float)

    cursor.execute(f"SELECT goods_name FROM goods WHERE goods_name = '{name}'")

    try:

        if cursor.fetchone()[0] == name:
            update(cursor, db_connection, name, quantity, price)

    except Exception as e:
        insert(cursor, name, quantity, price)

    db_connection.commit()


def update(cursor, connection, name, quantity, price):
    cursor.execute(f"""
        UPDATE Goods SET 
        goods_quantity = goods_quantity + '{quantity}', 
        goods_price = '{price}' 
        WHERE goods_name = '{name}'""")
