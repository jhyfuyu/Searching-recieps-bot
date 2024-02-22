import sqlite3
from typing import List, Any

DATABASE: str = 'database/main.db'
#  1) Используйте относительные пути вместо абсолютных, это практичнее - проект будет работать на разных компьютерах/серверах
#  2) это константа, а имена констант пишутся заглавными (прописными) буквами
table: str = 'customers'
    
    
def set_data(countries: str, user_id: str, user_name: str) -> None:
    """ Вносим полученные данные в базу данных"""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute('INSERT INTO customers (tg_id, name, countries) VALUES (?, ?, ?)', (user_id, user_name, countries))

    conn.commit() 
    conn.close()


def get_cuisines_by_tg_id(tg_id: str) -> str:
    """ Достаем данные из таблицы"""
    with sqlite3.connect(DATABASE) as connection:
        cursor = connection.cursor()
        cursor.execute(f'SELECT countries FROM {table} WHERE tg_id={tg_id}')
        result = cursor.fetchall()
    return result


def save_request(tg_id: str, request_data: str) -> Any:
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute('INSERT INTO req_history (tg_id, req) VALUES (?, ?)', (tg_id, request_data))

    conn.commit() 
    conn.close()


def get_requests_history_by_id(tg_id: str, table: str, k: int=10) -> Any:
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute(f'SELECT req FROM {table} WHERE tg_id={tg_id}')
        history_data = cursor.fetchall()
    return history_data
