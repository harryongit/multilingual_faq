# Multilingual FAQ API

## Overview
This project is a Django-based REST API for managing a multilingual FAQ system. It allows users to retrieve frequently asked questions (FAQs) in English, Hindi, and Bengali. The API automatically translates questions and answers using Google Translate.

## Features
- REST API for FAQs
- Supports multiple languages (English, Hindi, Bengali)
- Automatic translation using Google Translate
- Redis caching for optimized performance
- CKEditor for rich text formatting
- Dockerized setup for easy deployment

## Tech Stack
- **Backend:** Django, Django REST Framework (DRF)
- **Database:** SQLite (can be replaced with PostgreSQL/MySQL)
- **Caching:** Redis
- **Containerization:** Docker, Docker Compose

## Installation

### 1. Clone the Repository
```sh
git clone https://github.com/harryongit/multilingual_faq.git
cd multilingual_faq
```

### 2. Create a Virtual Environment
```sh
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Run Database Migrations
```sh
python manage.py migrate
```

### 5. Create a Superuser
```sh
python manage.py createsuperuser
```

### 6. Run the Server
```sh
python manage.py runserver
```

## API Endpoints

### Get FAQs
**URL:** `/api/faqs/`

**Query Parameters:**
- `lang` (optional) - Language preference (`en`, `hi`, `bn`). Default is English.

**Example Requests:**
```sh
curl http://localhost:8000/api/faqs/  # English (default)
curl http://localhost:8000/api/faqs/?lang=hi  # Hindi
curl http://localhost:8000/api/faqs/?lang=bn  # Bengali
```

## Docker Setup
### 1. Build and Run the Containers
```sh
docker-compose up --build
```
### 2. Stop the Containers
```sh
docker-compose down
```

## Running Tests
```sh
python manage.py test
```

## Deployment
- Deploy on AWS/GCP/Azure using Docker
- Use PostgreSQL for production
- Configure Redis caching properly

## License
MIT License

