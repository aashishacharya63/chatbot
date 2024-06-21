import numpy as np

def recommend_movie(user_input, df):
    user_preferences = preprocess_input(user_input)
    
    # Find movies that match user preferences
    matches = []
    for index, row in df.iterrows():
        if (user_preferences in row['genre'].lower() or
            user_preferences in row['director'].lower() or
            user_preferences in row['star'].lower() or
            user_preferences in row['country'].lower()):
            matches.append(row['name'])
    
    if matches:
        return matches[0]  # Return the first match found
    else:
        return "No matching movies found"
