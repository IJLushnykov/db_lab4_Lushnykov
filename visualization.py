import psycopg2
import  matplotlib.pyplot as plt
import pandas as pd

db_params = {
    'host': 'localhost',
    'database': 'db_lab3',
    'user': 'postgres',
    'password': 'byebye'
}

conn = psycopg2.connect(**db_params)
cursor = conn.cursor()



if __name__ == "__main__":
    #Перший запит: виведення глобальних продажів ігор відсортованих за роком виходу
    query1 = """
   SELECT v.name, Year_of_Release as Release_Year, SUM(Global_Sales_in_Millions) as Total_Global_Sales
    FROM Video_Game v
    JOIN Global_Sales g ON v.Indexx = g.Indexx
    GROUP BY Year_of_Release, name
    ORDER BY Release_Year;
    """
    

    cursor.execute(query1)
    result1 = cursor.fetchall()

    #Другий запит: підрахунок скільки різних ігор відповідають різним жанрам
    query2 = """
    SELECT Genre, COUNT(*) as Genre_Count
    FROM Video_Game
    GROUP BY Genre;
    """
    cursor.execute(query2)
    result2 = cursor.fetchall()

    #Третій запит: вивід ігор і їх оцінок від критиків і гравців
    query3 = """
    SELECT Name, Critic_Score, User_Score
    FROM Video_Game;
    """
    
    cursor.execute(query3)
    result3 = cursor.fetchall()
    cursor.close()
    conn.close()

names = [item[0] for item in result1]
years = [item[1] for item in result1]
sales = [float(item[2]) for item in result1]  

# Побудова стовпчикової діаграми для запиту 1
plt.figure(figsize=(10, 6))  
plt.bar(names, sales, color='skyblue')  
plt.xlabel('Game Name')
plt.ylabel('Total Global Sales (Millions)')
plt.title('Total Global Sales per Game')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()  
plt.show()
genre_counts = [item[1] for item in result2]
genres = [item[0] for item in result2]



# Побудова кругової діаграми для запиту 2
plt.figure(figsize=(8, 8))
plt.pie(genre_counts, labels=genres, autopct='%1.1f%%') 

plt.title('Distribution of Games by Genre')  
plt.axis('equal')  
plt.tight_layout()  
plt.show()



# Підготовка даних для побудови діаграми 3 запиту
names = [item[0] for item in result3]
critic_scores = [float(item[1]) / 10 for item in result3]  # Ділимо на 10 для наглядності
user_scores = [float(item[2]) for item in result3]  

# Побудова стовпчикової діаграми для третього запиу
plt.figure(figsize=(12, 6))

plt.bar(names, critic_scores, color='orange', label='Critic Score')
plt.bar(names, user_scores, color='blue', alpha=0.5, label='User Score')

plt.xlabel('Game Name')
plt.ylabel('Scores')
plt.title('Comparison of Critic and User Scores for Each Game')
plt.xticks(rotation=45, ha='right')
plt.legend()
plt.tight_layout()

plt.show()
