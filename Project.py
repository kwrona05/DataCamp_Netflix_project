# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")
print(netflix_df)

# Set movies from 1990s
netflix_subset = netflix_df[netflix_df["type"] == "Movie"]
subset = netflix_subset[(netflix_subset['release_year'] >= 1990)]
netflix_movies_1990 = subset[(subset['release_year'] < 2000)]

# Count movies from each country
country_movie_counts = netflix_movies_1990['country'].value_counts()
country_movie_counts

#Chart - Movies Distribution by country
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
bars = plt.bar(country_movie_counts.index, country_movie_counts.values, color='skyblue', edgecolor='black')

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, int(yval), ha='center', va='bottom', fontsize=12)
    
plt.xlabel('Country')
plt.ylabel('Number of movies')
plt.title('Movies distribution by country')
plt.xticks(rotation=45)
plt.show()

#Most pupular genre
most_popular_genre = netflix_movies_1990['genre'].value_counts()
most_popular_genre

#Chart - Most popular genre in 1990
plt.bar(most_popular_genre.index, most_popular_genre.values, color='orange', edgecolor='black')
plt.title('Most popular genre in 1990')
plt.xlabel('Genre')
plt.ylabel('Number of movies')
plt.xticks(rotation=45)
plt.show()

# Movies types
movie_type = netflix_movies_1990['type'].value_counts()
movie_type

#Movies duration
duration = netflix_movies_1990['duration'].fillna(0).astype(int)
duration

plt.hist(netflix_movies_1990['duration'])
plt.title('Distribution of Movie Duration')
plt.xlabel('Duration')
plt.ylabel('Number of Movies')
plt.show()

duration = 100

#Count Movies less than 90 minutes in Action movies
action_movies = netflix_movies_1990[netflix_movies_1990['genre'] == 'Action']
short_movie_count = (action_movies['duration'] < 90).sum()