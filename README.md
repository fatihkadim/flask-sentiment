# Flask NLP Sentiment Analysis 

A production-ready Flask web app for sentiment analysis using HuggingFace Transformers.  
Users can register, log in, analyze text, and view their history + overall mood on a dashboard.

---

## Features
- **Authentication**: Register, Login, Logout   
- **Sentiment Analysis**: Analyze text for positive, negative, or neutral sentiment with a score.  
- **Dashboard**: View per-user history and overall mood.   
- **Persistence**: SQLite database to store user and analysis data.  
- **Clean Design**: Simple and intuitive Flask/Jinja templates.  

---

## Getting Started 

### 1. Clone & Set Up Environment
First, clone the repository and navigate into the project directory.

```bash
git clone https://github.com/fatihkadim/flask-sentiment.git
cd flask-sentiment
```
Next, create a virtual environment and install the required packages.

```
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate

pip install -r requirements.txt
```
### 2. Configure Environment Variables
Create a .env file in the project root and add the following:
```
FLASK_APP=run.py
FLASK_ENV=development
SECRET_KEY="your_secret_key"

# SQLite in /instance
SQLALCHEMY_DATABASE_URI="sqlite:///<choose_name_for_your_db>.db"
example : "sqlite:///nlp.db"
SQLALCHEMY_TRACK_MODIFICATIONS=False

```
### 3. Initialize the Database
Use Flask-Migrate to set up the database. This only needs to be done once.
```
flask db init # only once
flask db migrate -m "init"
flask db upgrade
```
### 4. Run the App
Start the Flask application with the following command:
```
python run.py
```
Open your browser and navigate to http://127.0.0.1:5000 to access the app.

## Usage
- `/`: Home page  
- `/register`: Create a new account  
- `/login`: Sign in to an existing account  
- `/sentiment`: Enter text and get a sentiment analysis  
- `/dashboard`: View your overall mood and analysis history  
- `/logout`: Sign out of your account  

---

## Sample Texts for Testing
- `"I absolutely love this movie!"`  
- `"The product quality is disappointing."`  
- `"The weather is okay today."`  

---

## Technologies Used
- **Flask 3**: Web framework  
- **Flask-SQLAlchemy**: ORM for database interactions  
- **Flask-Login**: User session management  
- **Flask-WTF**: Forms handling  
- **Flask-Migrate**: Database migrations  
- **Transformers 4**: NLP model  
- **TensorFlow 2**: Backend for the model  
- **python-dotenv**: Environment variables  
- **bcrypt**: Password hashing  

See requirements.txt for the full list of dependencies and their versions.

### License
This project is licensed under the MIT License.
See the LICENSE file for more details.
