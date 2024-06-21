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
    # Implement chatbot logic here based on `processed_input` and `movie_df`
    # For demonstration, returning a simple response
    response = f"Chatbot received: {processed_input}"
    return render_template('index.html', response=response)

if __name__ == '__main__':
    app.run(debug=True)
