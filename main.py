from functions.json_loader import open_json
from functions.menu_show import menu_show

text = open_json("functions/interface_texts/return_sale_buy_menu.json")
menu_show(text)
text = open_json("functions/interface_texts/main_menu.json")
menu_show(text)
