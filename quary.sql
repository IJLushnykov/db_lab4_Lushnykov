SELECT v.name, Year_of_Release as Release_Year, SUM(Global_Sales_in_Millions) as Total_Global_Sales
FROM Video_Game v
JOIN Global_Sales g ON v.Indexx = g.Indexx
GROUP BY Year_of_Release, name
ORDER BY Release_Year;

SELECT Genre, COUNT(*) as Genre_Count
FROM Video_Game
GROUP BY Genre;

SELECT Name, Critic_Score, User_Score
FROM Video_Game;
