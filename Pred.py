from flask import Flask, render_template, request, jsonify
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64

app = Flask(__name__)

# Generate synthetic training data
np.random.seed(42)
num_samples = 1000

# Simulated feature data
X_train = pd.DataFrame({
    'Hour_Posted': np.random.randint(0, 24, num_samples),
    'Post_Length': np.random.randint(1, 500, num_samples),
    'Hashtag_Count': np.random.randint(0, 10, num_samples),
    'followers': np.random.randint(1, 10000, num_samples),
    'num_comments': np.random.randint(0, 200, num_samples),
    'video_play_count': np.random.randint(0, 10000, num_samples)
})

# Simulate target variable (likes) with a realistic relationship
y_train = (
    X_train['Hour_Posted'] * 100 +  # Impact of hour posted
    (X_train['Post_Length'] * 2) +  # Impact of post length
    (X_train['Hashtag_Count'] * 50) +  # Impact of hashtag count
    (X_train['followers'] / 100) +  # Impact of followers
    (X_train['num_comments'] * 10) +  # Impact of comments
    (X_train['video_play_count'] / 100) +  # Impact of video play count
    np.random.normal(0, 50, num_samples)  # Add noise
)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Route for Home Page
@app.route('/')
def index():
    return render_template('index.html')

# Route to make predictions
@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    hour_posted = data['hour_posted']
    post_length = data['post_length']
    hashtag_count = data['hashtag_count']
    followers = data['followers']
    num_comments = data['num_comments']
    video_play_count = data['video_play_count']

    X_new = pd.DataFrame({
        'Hour_Posted': [hour_posted],
        'Post_Length': [post_length],
        'Hashtag_Count': [hashtag_count],
        'followers': [followers],
        'num_comments': [num_comments],
        'video_play_count': [video_play_count]
    })

    likes_prediction = model.predict(X_new)[0]
    return jsonify({'prediction': round(likes_prediction, 2)})

# Route to show graph
@app.route('/show_graph')
def show_graph():
    y_pred = model.predict(X_train)

    plt.figure(figsize=(10, 6))

    # Scatter plot for actual likes in blue
    sns.scatterplot(x=y_train, y=y_train, color='blue', label='Actual Likes')

    # Scatter plot for predicted likes in orange
    sns.scatterplot(x=y_train, y=y_pred, color='orange', label='Predicted Likes')

    # Add labels and title
    plt.xlabel('Likes')
    plt.ylabel('Predicted Likes')
    plt.title('Actual vs Predicted Likes')
    plt.xlim(0, max(y_train.max(), y_pred.max()) * 1.1)
    plt.ylim(0, max(y_train.max(), y_pred.max()) * 1.1)
    plt.plot([0, max(y_train.max(), y_pred.max())], [0, max(y_train.max(), y_pred.max())], 'k--')

    # Add legend
    plt.legend()

    # Save plot to a string in base64 format
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode('utf8')

    return render_template('graph.html', plot_url=plot_url)

if __name__ == '__main__':
    app.run(debug=True)
