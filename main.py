from functions.get_current_time import get_current_time
from functions.json_loader import open_json
from functions.menu_show import menu_show
from functions.safe_int_input import safe_input
from functions.show_all import show_all
from functions.to_in import to_in
from functions.to_out import to_out
import sqlite3


def main() -> None:
    """
    first initial
    """
    db_connection = sqlite3.connect("db.db")
    cursor = db_connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Goods(
        id INTEGER PRIMARY KEY,
        goods_name TEXT NOT NULL,
        goods_quantity INT NOT NULL,
        goods_price REAL NOT NULL,
        action_date datetime NOT NULL DEFAULT current_timestamp
        )
        """)
    db_connection.commit()

    while True:

        print(f"{'-' * 45}\n\tПрогама складського обліку 'КОМІРНИК'")
        menu_show(open_json("functions/interface_texts/main_menu.json"))
        choice = safe_input(int)
        match choice:
            case 1:
                to_in(db_connection, cursor)
            case 2:
                to_out(db_connection, cursor)

            case 3:
                pass
            case 4:
                print("Введіть номер номенклатури на видалення")
                delete_id = safe_input(int)
                db_connection.commit()
                try:
                    cursor.execute(f"DELETE FROM Goods WHERE ID = '{delete_id}'")
                    db_connection.commit()
                except Exception as e:
                    print(e)
            case 5:
                show_all(cursor)
            case 6:
                cursor.execute(f"DELETE FROM Goods")
                db_connection.commit()
            case 7:

                db_connection.commit()
                cursor.close()
                db_connection.close()
                break


if __name__ == "__main__":
    main()
