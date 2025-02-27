import pickle
import streamlit as st
import pandas as pd


movie_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movie_list = pd.DataFrame(movie_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

def reccomend(movie):
    
    movie_index = movie_list[movie_list['title']==movie].index[0]
    similarity_score = similarity[movie_index] 
    similar_movie = sorted(list(enumerate(similarity_score)), reverse = True, key = lambda x:x[1])[1:5]
    reccomended = []
    for i in similar_movie:
        reccomended.append(movie_list.iloc[i[0]].title)
    return reccomended



st.title('Similar Movie Predictor')

selected_movie_name = st.selectbox('for which movie you want to find similar movies?',movie_list['title'].values)

if st.button('Reccomend'):
    reccomended_movies = reccomend(selected_movie_name)
    for i in reccomended_movies:
        st.write(i)