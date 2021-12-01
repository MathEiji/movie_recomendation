import pandas as pd
from movies_dataprep import create_related_movies_file

# Create similarities.csv
create_related_movies_file()

# Load similarities file
df_related_movies = pd.read_csv('related_movies.csv')

# Recommend 10 movies based on previously liked title

liked = ['20,000 Leagues Under the Sea', 'Rocky IV', '2001: A Space Odyssey', '48 Hrs.', 'A Nightmare on Elm Street']

i = 0
for movie in liked:
    print(f'\nUser {i+1}, we see you liked {liked[i]}, here are some recommendations: \n')
    print(df_related_movies.corr()[liked[i]].sort_values(ascending=False).iloc[:10])
    i+=1