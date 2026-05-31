from datetime import date
import sqlite3
import time
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()
create_table_query = '''
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data DATE,
    category TEXT,
    summ INTEGER
);    
'''
cursor.execute(create_table_query)
connection.commit()
def main():
    a = 1
    while a == 1:
        print("Expense Tracker CLI")
        print(' 1. Добавить расход', '\n', '2. Показать расходы', '\n', '3. Сохранить и выйти')
        try:
            a = int(input('Выберите действие (1-3):'))
        except ValueError():
            print()
        if a == 1:
            vvod()
        elif a == 2:
            pokaz()
        elif a == 3:
            save()
            a = 2
def vvod():
    print("\n--- Добавление расхода ---")
    while True:
        expenses_date = input("Дата (ГГГГ-ММ-ДД, Enter - сегодня): ")
        if not expenses_date:
            expenses_date = date.today().isoformat()
            break
        try:
            datetime.strptime(expenses_date, "%Y-%m-%d")
            break
        except ValueError:
            print("Ошибка: используйте формат ГГГГ-ММ-ДД")
    expenses_category = input("Категория: ").strip()
    while True:
        try:
            expenses_summa = float(input("Сумма: "))
            if expenses_summa <= 0:
                print("Сумма должна быть положительной")
                continue
            break
        except ValueError:
            print("Ошибка: введите число")
    insert_query = "INSERT INTO expenses (data, category, summ) VALUES (?, ?, ?)"
    cursor.execute(insert_query, (expenses_date, expenses_category, expenses_summa))
    connection.commit()  # Явный commit
    print("Расход добавлен")
    time.sleep(1)
def pokaz(): 
    summa = 0
    select_query = "SELECT id, data, category, summ FROM expenses"
    cursor.execute(select_query)
    all_users = cursor.fetchall()
    print("\nсписко всез расходов:")
    for user in all_users:
        print(f"ID: {user[0]}, date: {user[1]}, category: {user[2]}, summ: {user[3]}")
        summa += user[3]
    print(f'Итоговый расход {summa}')
    time.sleep(2)
def save():
    connection.commit()





main()
