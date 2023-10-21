from menu import MENU

for key, val in MENU['espresso'].items():
    if isinstance(val, dict):
        for k, v in val.items():
            print(k)