# Flask NLP Sentiment Analysis

A production-ready Flask web app for sentiment analysis using HuggingFace Transformers. Users can register, log in, analyze text, and view their history + overall mood on a dashboard.

## Features

- **Authentication**: Register, Login, Logout
- **Sentiment Analysis**: Analyze text for positive, negative, or neutral sentiment with a score
- **Dashboard**: View per-user history and overall mood
- **Persistence**: SQLite database to store user and analysis data
- **Clean Design**: Simple and intuitive Flask/Jinja templates

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/fatihkadim/flask-sentiment.git
cd flask-sentiment
```

### 2. Configure Environment Variables

Create a `.env` file based on `example.env`:

```bash
cp example.env .env
```

Example `.env` content:

```env
FLASK_APP=run.py
FLASK_ENV=development
SECRET_KEY="your_secret_key"
SQLALCHEMY_DATABASE_URI="sqlite:///nlp.db"
SQLALCHEMY_TRACK_MODIFICATIONS=False
```

**Note**: Do not commit your `.env` file to GitHub.

### 3. Run Locally (Optional)

If you want to test without Docker:

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Initialize database
flask db init      # only once
flask db migrate -m "init"
flask db upgrade

# Run the app
python run.py
```

**Access**: http://127.0.0.1:5000

### 4. Run with Docker (Recommended)

Build the Docker image:

```bash
docker build -t sentiment-analysis-project .
```

Run the container:

```bash
docker run -p 5000:5000 --name sentiment-analysis-container --env-file .env sentiment-analysis-project
```

**Access**: http://localhost:5000

With Docker, `app.run(host="0.0.0.0", port=5000, debug=True)` ensures Flask is accessible outside the container.

## Usage

- `/`: Home page
- `/register`: Create a new account
- `/login`: Sign in to an existing account
- `/sentiment`: Enter text and get a sentiment analysis
- `/dashboard`: View your overall mood and analysis history
- `/logout`: Sign out

## Sample Texts for Testing

- "I absolutely love this movie!"
- "The product quality is disappointing."
- "The weather is okay today."

## Technologies Used

- **Flask 3**
- **Flask-SQLAlchemy**
- **Flask-Login**
- **Flask-WTF**
- **Flask-Migrate**
- **Transformers 4**
- **TensorFlow 2**
- **python-dotenv**
- **bcrypt**

## License

MIT License. See LICENSE file for details.
