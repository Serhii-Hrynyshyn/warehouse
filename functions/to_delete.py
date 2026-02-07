from .safe_input import safe_input
def to_delete(db_connection, cursor):
    print("Введіть номер номенклатури на видалення")
    delete_id = safe_input(int)
    db_connection.commit()
    try:
        cursor.execute(f"DELETE FROM Goods WHERE ID = '{delete_id}'")
        db_connection.commit()
    except Exception as e:
        print(f"Видалення не можливе: {e}")
