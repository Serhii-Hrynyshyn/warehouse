from functions.json_loader import open_json
from functions.menu_show import menu_show
from functions.safe_input import safe_input
from functions.show_all import show_all
from functions.to_in import to_in
from functions.to_out import to_out
from functions.to_delete import to_delete
from functions.to_print_report import to_print_report
from functions.get_current_time import get_current_time
import sqlite3


def main() -> None:
    """
    Ініціалізація таблиці
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
                """
                Прихід товару на склад
                """
                to_in(db_connection, cursor)
            case 2:
                """
                Видача товару зі складу
                """
                to_out(db_connection, cursor)
            case 3:
                """
                Друк звіту всієї наявної номенклатури на складі
                """
                to_print_report(cursor)
            case 4:
                """
                Видалення номенклатури з складу
                """
                to_delete(db_connection, cursor)
            case 5:
                """
                Перегляд всієї наявної номенклатури на складі
                """
                show_all(cursor)
            case 6:
                """
                Списання всієї наявної номенклатури на складі
                """
                cursor.execute(f"DELETE FROM Goods")
                db_connection.commit()
            case 7:
                """
                Вихід з складської програми
                """
                db_connection.commit()
                cursor.close()
                db_connection.close()
                break


if __name__ == "__main__":
    main()
