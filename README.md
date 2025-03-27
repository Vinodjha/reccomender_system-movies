# 🎬 Movie Suggestions Based on Last Watched Movie  

This is a **content-based movie recommendation system** built using **Python** and **Streamlit**. The system suggests similar movies based on the last watched movie using **TF-IDF vectorization** and **cosine similarity**.  

## 🚀 Features  
- **Movie Similarity**: Finds similar movies based on genres, keywords, cast, and crew.  
- **Content-Based Filtering**: Uses movie metadata to generate recommendations.  
- **Interactive UI**: Deployed with **Streamlit** for user-friendly interaction.  

---

## 🏗️ Project Structure  
The project consists of two main Python scripts:  

### **1. model.py** (Building the Recommender System)  
- Loads movie data from **TMDB 5000 Movies dataset**.  
- Extracts important features: **genres, keywords, cast, crew, and overview**.  
- Prepares data by **cleaning text, stemming words, and vectorizing with TF-IDF**.  
- Computes **cosine similarity** to find related movies.  
- Saves the processed data and similarity matrix as **pickle files**.  

### **2. app.py** (Streamlit Application)  
- Loads **processed data** and **similarity matrix**.  
- Provides a **dropdown menu** to select a movie.  
- Displays **top 4 recommended movies** when the user clicks "Recommend".  

---

## 🔧 Setup and Installation  

### **1. Clone the Repository**  
```bash
git clone https://github.com/Vinodjha/movie-recommendation.git
cd movie-recommendation
