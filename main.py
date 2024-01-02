import psycopg2


db_params = {
    'host': 'localhost',
    'database': 'db_lab3',
    'user': 'postgres',
    'password': 'byebye'
}

def execute_query(query):
    conn = None
    try:
        conn = psycopg2.connect(**db_params)
        cursor = conn.cursor()

        cursor.execute(query)
        result = cursor.fetchall()

        for row in result:
            print(row)

        cursor.close()

    except psycopg2.Error as e:
        print(f"Error: {e}")

    finally:
        if conn is not None:
            conn.close()


if __name__ == "__main__":
    #Перший запит: виведення глобальних продажів ігор відсортованих за роком виходу
    query1 = """
    SELECT v.name, Year_of_Release as Release_Year, SUM(Global_Sales_in_Millions) as Total_Global_Sales
    FROM Video_Game v
    JOIN Global_Sales g ON v.Indexx = g.Indexx
    GROUP BY Year_of_Release, name
    ORDER BY Release_Year;
    """

    #Другий запит: підрахунок скільки різних ігор відповідають різним жанрам
    query2 = """
    SELECT Genre, COUNT(*) as Genre_Count
    FROM Video_Game
    GROUP BY Genre;
    """

    #Третій запит: вивід ігор і їх оцінок від критиків і гравців
    query3 = """
    SELECT Name, Critic_Score, User_Score
    FROM Video_Game;
    """

    print("Query 1 Results:")
    execute_query(query1)

    print("\nQuery 2 Results:")
    execute_query(query2)

    print("\nQuery 3 Results:")
    execute_query(query3)
