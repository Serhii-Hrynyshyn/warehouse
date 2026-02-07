from .safe_input import safe_input


def to_out(db_connection, cursor):
    print("--- ПРОДАЖ ЗІ СКЛАДУ ---\n*Номер товару в базі*")
    number = safe_input(int)
    print("*Кількість товару*")
    sale_quantity = safe_input(int)
    try:
        cursor.execute(f"""SELECT goods_quantity 
        FROM goods WHERE ID = '{number}'""")
        warehouse_quantity = int(cursor.fetchone()[0])
        if warehouse_quantity >= sale_quantity:
            cursor.execute(f"""
            UPDATE Goods SET 
            goods_quantity = goods_quantity - '{sale_quantity}'
            WHERE ID = '{number}'
            """)
            db_connection.commit()
        else:
            print("Списання не можливе, недостатньо товару на складі")
    except Exception as e:
        print(f"Не успішно, помилка вводу: {e}")
