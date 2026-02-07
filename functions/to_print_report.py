import os
from functions.get_current_time import get_current_time


def to_print_report(cursor) -> None:
    report_text = f"\t\t\tЗалишок по складу станом на:\n\t\t\t*{get_current_time()}*\n"
    cursor.execute("SELECT * FROM Goods")
    for good in cursor.fetchall():
        params = []
        for param in range(5):
            params.append(good[param])
        report_text += f"Назва: {params[1]}|Кількість: {params[2]} |Вартість(грн.): {params[3]}|Час операції: {params[4]}\n"
    print(report_text)
    with open("./report.txt", "w", encoding="utf-8") as report:
        report.write(report_text)
    report.close()
    os.startfile("report.txt", "print")
