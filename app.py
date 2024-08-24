<<<<<<< HEAD
# app.py

from flask import Flask, render_template, request
from preprocessor import preprocess_input, load_dataset, preprocess_dataset

app = Flask(__name__)

# Load and preprocess dataset
dataset_path = 'D:/movie/chatbot/movies.csv'
movie_df = load_dataset(dataset_path)
movie_df = preprocess_dataset(movie_df)
=======
from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load the dataset
movies_df = pd.read_csv('movies.csv')

def recommend_movies(user_input):
    user_input = user_input.strip().lower()
    
    matches = movies_df[
        movies_df['title'].str.lower().str.contains(user_input) |
        movies_df['genre'].str.lower().str.contains(user_input) |
        movies_df['original language'].str.lower().str.contains(user_input)
    ]
    
    if not matches.empty:
        recommendations = matches[['title', 'genre', 'overview', 'vote_average']].head(5).to_dict(orient='records')
        return recommendations
    else:
        return None
>>>>>>> cb47b97 (Initial commit)

@app.route('/')
def index():
    return render_template('index.html')

<<<<<<< HEAD
@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_input = request.form['user_input']
    processed_input = preprocess_input(user_input)
    
    # Example: Retrieve movies matching the user input
    matched_movies = movie_df[movie_df['name'].str.contains(processed_input, case=False)]

    if len(matched_movies) == 0:
        response = "No movies found matching your query."
    else:
        response = "Movies matching your query:\n"
        for idx, movie in matched_movies.iterrows():
            response += f"{movie['name']} ({movie['genre']}) - Directed by {movie['director']}\n"

    return render_template('index.html', response=response)
=======
@app.route('/recommend', methods=['POST'])
def recommend():
    user_input = request.json.get('message')
    recommendations = recommend_movies(user_input)
    
    if recommendations:
        return jsonify({'status': 'success', 'data': recommendations})
    else:
        return jsonify({'status': 'fail', 'message': 'No matching movies found.'})
>>>>>>> cb47b97 (Initial commit)

if __name__ == '__main__':
    app.run(debug=True)
