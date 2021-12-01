import pandas as pd
import random

class create_related_movies_file: 
    # Load data, clear unnecessary columns and set data type
    cols1 = ['id', 'title']
    cols2 = ['userId', 'movieId', 'rating']
    df_movies = pd.read_csv('movies_metadata.csv', dtype={'id': int}, usecols=cols1, encoding='UTF-8')

    df_ratings_s = pd.read_csv('ratings_small.csv', dtype={'userId': int, 'movieId': int, 'rating': float}, usecols=cols2, encoding='UTF-8')

    # Rename id to movieId in order to merge
    df_movies.rename(columns={"id": "movieId"}, inplace=True)

    # Merge both tables by userId
    df_merged = df_ratings_s.merge(df_movies, on='movieId')

    # Generate pivot table in order to diplay all ratings per movie in columns
    df_pivot = df_merged.pivot_table(index='userId', columns='title', values='rating')

    # Create correlation and set to consider only movies with a certain amount of ratings
    corr_matrix = df_pivot.corr(method='pearson', min_periods=50)

    # Create .csv
    pd.DataFrame(corr_matrix).to_csv('related_movies.csv')
