# Flask NLP Sentiment Analysis

A production-ready Flask web app for sentiment analysis using HuggingFace Transformers. Users can register, log in, analyze text, and view their history + overall mood on a dashboard.
<img src="https://github.com/user-attachments/assets/42cd7ccb-557c-49e8-9146-75e7d4d6d2da" width="600" height="250" alt="Ekran görüntüsü 1" />
<img src="https://github.com/user-attachments/assets/dee41ee0-ded4-4942-9e80-f6d53198e052" width="400" height="180" alt="Ekran görüntüsü 2" />
<img src="https://github.com/user-attachments/assets/278f2824-e14c-49d6-85d0-feb0d2fef51b" width="500" height="450" alt="Ekran görüntüsü 3" />


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
SECRET_KEY="your_secret_key_here"
SQLALCHEMY_DATABASE_URI="sqlite:///nlp.db"
SQLALCHEMY_TRACK_MODIFICATIONS=False
```

**Important**: 
- Generate a strong SECRET_KEY for production
- Never commit your `.env` file to version control
- For production, set `FLASK_ENV=production`

### 3. Run Locally (Recommended for Development)

Create and activate virtual environment:

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Initialize database (first time only):

```bash
flask db init      # only once
flask db migrate -m "Initial migration"
flask db upgrade
```

Run the application:

```bash
python run.py
```

**Access**: http://127.0.0.1:5000

### 4. Run with Docker

Build the Docker image:

```bash
docker build -t sentiment-analysis-project .
```

Run the container:

```bash
docker run -p 5000:5000 --name sentiment-analysis-container --env-file .env --rm sentiment-analysis-project
```

**Access**: http://localhost:5000

### 5. Run with Docker Compose (Recommended for Production)

```yaml
# docker-compose.yml
version: '3.8'
services:
  web:
    build: .
    ports:
      - "5000:5000"
    env_file:
      - .env
    volumes:
      - ./instance:/app/instance
    restart: unless-stopped
```

Run with:

```bash
docker-compose up -d
```

## Usage

### Routes

- `/` - Home page
- `/register` - Create a new account
- `/login` - Sign in to an existing account
- `/sentiment` - Enter text and get a sentiment analysis
- `/dashboard` - View your overall mood and analysis history
- `/logout` - Sign out

### Sample Texts for Testing

- **Positive**: "I absolutely love this movie!"
- **Negative**: "The product quality is disappointing."
- **Neutral**: "The weather is okay today."

## Technologies Used

- **Flask 3** - Web framework
- **Flask-SQLAlchemy** - Database ORM
- **Flask-Login** - User authentication
- **Flask-WTF** - Form handling and CSRF protection
- **Flask-Migrate** - Database migrations
- **Transformers 4** - HuggingFace sentiment analysis models
- **TensorFlow 2** - Machine learning backend
- **python-dotenv** - Environment variable management
- **bcrypt** - Password hashing

## Required Dependencies

Create `requirements.txt` with:

```txt
Flask==3.0.0
Flask-SQLAlchemy==3.1.1
Flask-Login==0.6.3
Flask-WTF==1.2.1
Flask-Migrate==4.0.5
transformers==4.35.2
tensorflow==2.15.0
python-dotenv==1.0.0
bcrypt==4.1.1
WTForms==3.1.1
```

## Security Notes

- **Never commit your `.env` file** to version control
- Use a **strong, unique SECRET_KEY** in production
- Set **FLASK_ENV=production** for production deployment
- Consider using **PostgreSQL** instead of SQLite for production
- Regularly update dependencies for security patches
- Use HTTPS in production environments

## Production Deployment

### Environment Variables for Production

```env
FLASK_APP=run.py
FLASK_ENV=production
SECRET_KEY="your_very_strong_secret_key_here"
SQLALCHEMY_DATABASE_URI="postgresql://user:password@localhost/sentiment_db"
SQLALCHEMY_TRACK_MODIFICATIONS=False
```


### Deployment Steps

#### 1. Use a production WSGI server like **Gunicorn**:
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:5000 run:app
   ```

#### 2. Set up reverse proxy with **Nginx**
#### 3. Configure SSL certificates
#### 4. Set up monitoring and logging

## Troubleshooting

### Common Issues

**Database Migration Errors:**
```bash
# Reset migrations
rm -rf migrations/
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

**Port Already in Use:**
```bash
# Find and kill process using port 5000
lsof -ti:5000 | xargs kill -9
```

**Docker Permission Issues:**
```bash
# On Linux, you might need to use sudo
sudo docker build -t sentiment-analysis-project .
```

## Contributing

#### 1. Fork the repository
#### 2. Create a feature branch (`git checkout -b feature/amazing-feature`)
#### 3. Commit your changes (`git commit -m 'Add some amazing feature'`)
#### 4. Push to the branch (`git push origin feature/amazing-feature`)
#### 5. Open a Pull Request

## License

MIT License. See [LICENSE](LICENSE) file for details.

## Contact

For questions or issues, please open an issue on GitHub or contact the maintainer.
