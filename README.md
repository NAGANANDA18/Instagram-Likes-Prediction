# Instagram-Likes-Prediction

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Instagram Engagement Predictor</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            background-color: #f8f9fa;
            font-family: Arial, sans-serif;
        }

        .container {
            margin-top: 30px;
        }

        h1 {
            color: #ff5733;
            font-weight: bold;
            text-align: center;
            margin-bottom: 20px;
        }

        h2 {
            color: #343a40;
            font-weight: bold;
            margin-top: 20px;
        }

        ul {
            list-style-type: disc;
            margin-left: 20px;
        }

        .feature-section {
            margin-bottom: 30px;
        }

        footer {
            margin-top: 30px;
            text-align: center;
            color: #6c757d;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Instagram Engagement Predictor</h1>
        <p>This project is a <strong>web-based application</strong> that predicts the number of likes an Instagram post may receive based on several input factors. It uses a machine learning model integrated into a user-friendly web interface, allowing users to input key metrics and receive predictions.</p>

        <div class="feature-section">
            <h2>Features</h2>
            <h3>Input Factors:</h3>
            <ul>
                <li>Hour the post is published</li>
                <li>Length of the post</li>
                <li>Number of hashtags used</li>
                <li>Follower count</li>
                <li>Number of comments</li>
                <li>Video play count</li>
            </ul>

            <h3>Prediction:</h3>
            <p>Outputs the estimated number of likes for the given inputs.</p>

            <h3>User Interface:</h3>
            <ul>
                <li>A responsive, visually appealing design built with HTML, CSS, and Bootstrap.</li>
                <li>A transparent input form with semi-transparent fields.</li>
                <li>Integrated background image for aesthetics.</li>
            </ul>

            <h3>Graph:</h3>
            <p>Option to display a graphical representation of predictions.</p>
        </div>

        <div class="feature-section">
            <h2>Technology Stack</h2>
            <h3>Frontend:</h3>
            <ul>
                <li>HTML5, CSS3, JavaScript</li>
                <li>Bootstrap 5 for responsive design</li>
            </ul>

            <h3>Backend:</h3>
            <ul>
                <li>Flask (Python) or similar web framework to handle predictions</li>
                <li>Machine Learning model (e.g., Random Forest Regressor) for prediction logic</li>
            </ul>

            <h3>Deployment:</h3>
            <p>Can be hosted on platforms like Heroku or AWS.</p>
        </div>
    </div>

    <footer>
        <p>&copy; 2024 Instagram Engagement Predictor. All Rights Reserved.</p>
    </footer>
</body>
</html>
