from functions.get_current_time import get_current_time
from functions.json_loader import open_json
from functions.menu_show import menu_show
from functions.safe_int_input import safe_input
from functions.show_all import show_all
import sqlite3

# text = open_json("functions/interface_texts/return_sale_buy_menu.json")
# menu_show(text)
# text = open_json("functions/interface_texts/main_menu.json")
# menu_show(text)
#
# print(safe_input(float))


def main() -> None:
    """
    first initial
    """
    db_connection = sqlite3.connect("warehouse.db")
    cursor = db_connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Goods(
        id INTEGER PRIMARY KEY,
        goods_name TEXT NOT NULL,
        goods_quantity INT NOT NULL,
        goods_price REAL NOT NULL,
        action_date TEXT NOT NULL DEFAULT current_timestamp,
        goods_description TEXT)
        """)
    db_connection.commit()

    while True:

        print(f"{'-' * 45}\n\tПрогама складського обліку 'КОМІРНИК'")
        menu_show(open_json("functions/interface_texts/main_menu.json"))
        choice = safe_input(int)
        match choice:
            case 1:
                cursor.execute(
                    "INSERT INTO Goods (goods_name, goods_quantity, goods_price, action_date, goods_description ) VALUES (?, ?, ?, ?, ?)",
                    ("newuser", 5, 12.3, get_current_time(), ""),
                )

                # Сохраняем изменения и закрываем соединение
                # connection.commit()
                # connection.close()
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                show_all(cursor)
            case 6:
                pass
            case 7:

                db_connection.commit()
                cursor.close()
                db_connection.close()
                break


if __name__ == "__main__":
    main()
