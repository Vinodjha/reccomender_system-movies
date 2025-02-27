#This is the center of the project which implements a content based reccomender systemf for movies

#Importing the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import ast
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem.porter import PorterStemmer
import pickle


#reading the data from the two csv files containg all the details about the movie and credits
movies = pd.read_csv('C:/Users/vjha8/Downloads/tmdb_5000_movies/tmdb_5000_movies.csv')
credits = pd.read_csv('C:/Users/vjha8/Downloads/tmdb_5000_movies/tmdb_5000_credits.csv')

movies = movies.merge(credits, on  = 'title')
movies1 = movies.copy()

# There were lots of columns which were not a factor in deciding the similarity between the movies
#only the below columns are kept for this project
movies = movies[['movie_id', 'title', 'overview', 'genres', 'keywords', 'cast', 'crew']]

#movies.isnull().sum() # dropping the rows containing  the null values
movies.dropna(inplace = True) 
movies.duplicated().sum()

#The data in the genre column looks like a dictionary but it is actually a string
# the below function first converts the string into dictionary and then extract the name of genre to store it in a list
def convert_str2genre(x):
    genres = []
    for i in ast.literal_eval(x):
        genres.append(i['name'])
    return genres

movies['genres'] = movies['genres'].apply(convert_str2genre)
#movies.genres[:3]

movies['keywords'] = movies['keywords'].apply(convert_str2genre)
#movies.head(3)

#same issue with the cast column, also only keeping 3 casts

def convert_str2cast(x):
    cast = []
    counter = 0 #keeping only top 3 casts
    for i in ast.literal_eval(x):
        if counter != 3:
            cast.append(i['name'])
            counter += 1

    return cast
    
        
        
   


movies['cast']= movies['cast'].apply(convert_str2cast)


#similar problem witht the crew column as well, also we are only interested in director of the movie for reccomending similar movies

def convert_str2fetch_director(x):
    director = []
    for i in ast.literal_eval(x):
        if i['job'] == 'Director':
            director.append(i['name'])
            break
        
    return director

movies['crew'] = movies['crew'].apply(convert_str2fetch_director)
movies['overview'] = movies['overview'].apply(lambda x: x.split())

#we need to remove spaces between the words in the cast, crew, genres columns 
#so that the reccomender system can understand that the two words are one entity

movies['cast']=movies['cast'].apply(lambda x: [str.lower(i).replace(" ","") for i in x])
movies['crew']=movies['crew'].apply(lambda x: [str.lower(i).replace(" ","") for i in x])
movies['genres']=movies['genres'].apply(lambda x: [str.lower(i).replace(" ","") for i in x])
movies['keywords']=movies['keywords'].apply(lambda x: [str.lower(i).replace(" ","") for i in x])

#creating the tag column by combining overviews, genres, csat, crew and keywords

movies['tag'] = movies['overview'] + movies['genres'] +movies['keywords'] +movies['cast'] + movies['crew']


# Now we are ready. To find similar movie to the given movie, only the tag column is needed
df = movies[['movie_id', 'title', 'tag']]
#df.head()

#convert the list to string in the tag column
df['tag'] = df['tag'].apply(lambda x:" ".join(x))

#converting the string to lower case
df['tag'] = df['tag'].apply(lambda x: str.lower(x))

# Using TF-IDF to convert the tag column into a vector for similarity match
tfidf = TfidfVectorizer( max_features=5000)

# stemming the words in the tag column to remove redundancy.
#for example running, run, ran all will be converted to same word 'run'
ps = PorterStemmer()

def stem(text):
    x = []
    for i in text.split():
        x.append(ps.stem(i))
    return " ".join(x)

df['tag'] = df['tag'].apply(stem)

vectors = tfidf.fit_transform(df['tag']).toarray()
#vectors

similarity_matrix = cosine_similarity(vectors)  # 
similarity_matrix

def reccomend(movie):
    movie_index = df[df['title']==movie].index[0]
    similarity_score = similarity_matrix[movie_index] 
    movie_list = sorted(list(enumerate(similarity_score)), reverse = True, key = lambda x:x[1])[1:5]
    for i in movie_list:
        print(df.iloc[i[0]].title)
    return movie_list

reccomend('Batman')


pickle.dump(df.to_dict(), open('movie_dict.pkl', 'wb'))
pickle.dump(similarity_matrix, open('similarity.pkl', 'wb'))

