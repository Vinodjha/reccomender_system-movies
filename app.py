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



import streamlit as st

st.title('Similar Movie Predictor')

# Display the logo properly
st.sidebar.image("./static/logo_vj.png", width=200)  # Increase width if needed

# Footer with name & links
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: #222; /* Dark background */
        color: #fff; /* White text */
        text-align: center;
        padding: 10px;
        font-size: 16px;
        font-weight: bold;
    }
    .footer a {
        color: #1E90FF; /* Bright blue links */
        text-decoration: none;
        font-weight: bold;
        margin: 0 10px;
    }
    </style>
    <div class="footer">
        <p>Created by <b>Vinod Jha</b> |  
        <a href="https://linkedin.com/in/yourprofile" target="_blank">LinkedIn</a> |  
        <a href="https://vinodjha.github.io/" target="_blank">Website</a></p>
    </div>
    """,
    unsafe_allow_html=True
)

# Dropdown & button
selected_movie_name = st.selectbox('For which movie do you want to find similar movies?', movie_list['title'].values)

if st.button('Recommend'):
    recommended_movies = recommend(selected_movie_name)
    for i in recommended_movies:
        st.write(i)
