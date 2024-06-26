# app.py

from flask import Flask, render_template, request
from preprocessor import preprocess_input, load_dataset, preprocess_dataset

app = Flask(__name__)

# Load and preprocess dataset
dataset_path = 'D:/movie/chatbot/movies.csv'
movie_df = load_dataset(dataset_path)
movie_df = preprocess_dataset(movie_df)

@app.route('/')
def index():
    return render_template('index.html')

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

if __name__ == '__main__':
    app.run(debug=True)
