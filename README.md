# Building a REST API with Django REST Framework
### A Beginner's Toolkit for Modern API Development with JWT Authentication

---

##  Table of Contents
- [Title & Objective](#title--objective)
- [Quick Summary](#quick-summary-of-django-rest-framework)
- [System Requirements](#system-requirements)
- [Installation & Setup](#installation--setup-instructions)
- [Minimal Working Example](#minimal-working-example)
- [AI Prompt Journal](#ai-prompt-journal)
- [Common Issues & Fixes](#common-issues--fixes)
- [API Endpoints](#api-endpoints)
- [References](#references)

---

## Title & Objective

**Technology:** Django REST Framework (DRF) with JWT Authentication

**Why I chose it:**  
- Django REST Framework is one of the most powerful and widely-used frameworks for building web APIs in Python.
- Companies like Instagram, Mozilla, Spotify, and Red Bull use Django in production. 
- I wanted to learn how to build secure, scalable APIs with modern authentication patterns.

**End Goal:**  
Create a fully functional Book Tracker API with:
- User registration and JWT authentication
- Custom user profiles with reading goals
- Token refresh and blacklist functionality
- Auto-generated interactive API documentation
- Production-ready project structure

---

##  Quick Summary of Django REST Framework

**What is it?**  
Django REST Framework (DRF) is a powerful toolkit for building Web APIs in Python. It's built on top of Django and provides features like serialization, authentication, permissions, and automatic API documentation.

**Where is it used?**  
- Building backend APIs for mobile apps
- Creating microservices architectures
- Developing SaaS platforms
- Internal company APIs and data services

**Real-world example:**  
Instagram uses Django to serve over 1 billion users daily. Their API handles photo uploads, comments, likes, and user authentication - all built with Django REST Framework.

---

## System Requirements

### Operating System
-  Linux (Ubuntu 20.04+ recommended)
-  macOS (10.15+)
-  Windows 10/11 (with WSL2 recommended)

### Required Tools
```
Python 3.11+
PostgreSQL 14+
Git
Text Editor (VS Code recommended)
Terminal/Command Line
```

### Python Packages
All packages are listed in `requirements.txt` and `requirements-dev.txt`

---

## Installation & Setup Instructions

### Step 1: Clone the Repository
```bash
git clone https://github.com/WanjikuN/book-tracker-api.git
cd book-tracker-api
```

### Step 2: Create Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate it
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
# Install production packages
pip install -r requirements.txt

# Install development packages (for testing and linting)
pip install -r requirements-dev.txt
```

### Step 4: Set Up PostgreSQL Database
```bash
# Access PostgreSQL
psql -U postgres

# Create database and user
CREATE DATABASE book_tracker_db;
CREATE USER book_tracker_user WITH PASSWORD 'yourpassword';
GRANT ALL PRIVILEGES ON DATABASE book_tracker_db TO book_tracker_user;

# Exit PostgreSQL
\q
```

### Step 5: Configure Environment Variables
```bash
# Copy the example environment file
cp .env.example .env

# Edit .env with your values
nano .env
```

**Your .env file should contain:**
```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=postgres://book_tracker_user:yourpassword@localhost:5432/book_tracker_db
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://127.0.0.1:3000
```

### Step 6: Run Migrations
```bash
python manage.py migrate
```

### Step 7: Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

### Step 8: Run the Development Server
```bash
python manage.py runserver
```

**Server will start at:** `http://localhost:8000`

### Step 9: View API Documentation
Visit: `http://localhost:8000/api/docs/`

---

## Minimal Working Example

### What This Example Does
Demonstrates the complete authentication flow:
1. Register a new user
2. Login to get JWT tokens
3. Access a protected endpoint with the token
4. Refresh the token before it expires
5. Logout by blacklisting the refresh token

### Code Example: Register and Login
```bash
# 1. Register a new user
curl -X POST http://localhost:8000/api/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "bookworm",
    "email": "bookworm@example.com",
    "password": "securepass123",
    "password_confirm": "securepass123"
  }'
```

**Expected Output:**
```json
{
  "user": {
    "id": 1,
    "username": "bookworm",
    "email": "bookworm@example.com",
    "first_name": "",
    "last_name": "",
    "full_name": "",
    "bio": "",
    "profile_picture": null,
    "reading_goal": null,
    "created_at": "2026-02-19T10:30:00Z"
  },
  "message": "User registered successfully"
}
```
```bash
# 2. Login to get tokens
curl -X POST http://localhost:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "bookworm",
    "password": "securepass123"
  }'
```

**Expected Output:**
```json
{
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```
```bash
# 3. Access protected endpoint (replace YOUR_ACCESS_TOKEN)
curl -X GET http://localhost:8000/api/auth/profile/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

**Expected Output:**
```json
{
  "id": 1,
  "username": "bookworm",
  "email": "bookworm@example.com",
  "first_name": "",
  "last_name": "",
  "full_name": "",
  "bio": "",
  "profile_picture": null,
  "reading_goal": null,
  "created_at": "2026-02-19T10:30:00Z"
}
```

---

## AI Prompt Journal

### Prompt 1: Initial Project Setup
**Prompt Used:**  
*"I'm currently building a book tracker for my 2026 reads. I'm using Django. What are the naming conventions in Python?"*

**AI Response Summary:**  
The AI explained PEP 8 naming conventions including snake_case for variables/functions, PascalCase for classes, UPPER_SNAKE_CASE for constants, and Django-specific patterns for models, views, and URLs.

**Evaluation:**  
✅ Extremely helpful - provided clear examples with tables and Django-specific guidance that I referenced throughout the project.

---

### Prompt 2: Package Selection
**Prompt Used:**  
*"I'm going to use django rest framework. So I'm thinking the first packages and libraries I should use include Django, django-rest-framework, django-environ. Is this right and which ones do you think I missed in order to kickstart my project?"*

**AI Response Summary:**  
The AI recommended adding:
- `psycopg2-binary` for PostgreSQL
- `djangorestframework-simplejwt` for JWT auth
- `django-cors-headers` for CORS
- `ruff` and `black` for code quality
- `pytest-django` and `factory-boy` for testing

**Evaluation:**  
✅ Critical guidance - caught missing packages early and explained why each was needed. This saved hours of troubleshooting later.

---

### Prompt 3: Custom User Model
**Prompt Used:**  
*"At what point should I initialize a git repo for tracking and committing? Also, since this is a single-user project for now, do you want a custom user model?"*

**AI Response Summary:**  
The AI strongly recommended:
1. Initialize git immediately before writing code
2. Always create a custom user model at the start (even if not needed now) because changing it later is extremely difficult
3. Provided a complete custom user model with fields for profile pictures, reading goals, and bio

**Evaluation:**  
✅ Critical advice - The custom user model recommendation was crucial. The AI explained this is a "now or never" decision and provided a future-proof implementation.

---

### Prompt 4: Environment Variables
**Prompt Used:**  
*"I want to setup my environmental variables first as the settings.py file often has secret Key. Would you recommend this as a standard practice?"*

**AI Response Summary:**  
The AI confirmed this is best practice and provided:
- How to use `django-environ`
- Creating `.env` and `.env.example` files
- What should never be committed (`.env`) vs what should (`.env.example`)
- Complete configuration example for `settings.py`

**Evaluation:**  
✅ Security-focused guidance prevented me from accidentally committing secrets to GitHub.

---

### Prompt 5: Understanding Serializers
**Prompt Used:**  
*"Let's move to serializer - userSerializer. What does this mean? What definitions do I need to understand the workflow?"*

**AI Response Summary:**  
The AI provided:
- Clear analogy: serializers are "translators" between Python objects and JSON
- Explained serialization (Python → JSON) and deserialization (JSON → Python)
- Detailed breakdown of serializer responsibilities: field selection, validation, read-only vs write-only fields
- Complete working examples for UserSerializer and UserRegistrationSerializer

**Evaluation:**  
✅ Excellent teaching - The translator analogy and workflow diagrams made a complex concept immediately understandable.

---

### Prompt 6: JWT Configuration
**Prompt Used:**  
*"Explain this SIMPLE_JWT configuration: ACCESS_TOKEN_LIFETIME, REFRESH_TOKEN_LIFETIME, ROTATE_REFRESH_TOKENS, BLACKLIST_AFTER_ROTATION, ALGORITHM, SIGNING_KEY, AUTH_HEADER_TYPES"*

**AI Response Summary:**  
The AI explained each setting with analogies:
- Access token = "visitor pass" (short-lived)
- Refresh token = "ID card" (long-lived)
- Token rotation = security feature that invalidates old tokens
- Blacklist = ensures rotated tokens can never be reused
- HS256 = the cryptographic algorithm
- Provided timeline diagrams showing token lifecycle

**Evaluation:**  
✅ Perfect explanations - The visitor pass vs ID card analogy made JWT token mechanics crystal clear.

---

### Prompt 7: Fixing Migration Issues
**Prompt Used:**  
*"I'm getting this error: 'Migration admin.0001_initial is applied before its dependency book_tracker.0001_initial on database'. Is this because I ran migrate before adding the custom user model?"*

**AI Response Summary:**  
The AI:
- Confirmed this is a classic error from adding custom user model after initial migration
- Provided step-by-step recovery instructions (drop database, delete migrations, recreate)
- Explained why custom user model must be set before first migration
- Included commands to safely reset everything

**Evaluation:**  
✅ Saved the project - Without this guidance, I would have had to start over completely. The step-by-step recovery process worked perfectly.

---

### Prompt 8: API Documentation Setup
**Prompt Used:**  
*"Configure drf-spectacular for this project"*

**AI Response Summary:**  
The AI provided:
- Installation instructions
- Complete SPECTACULAR_SETTINGS configuration
- How to add JWT Bearer authentication to docs
- URL configuration for Swagger UI and ReDoc
- Examples of decorating views with `@extend_schema`

**Evaluation:**  
✅ Professional touch - Added interactive API documentation that makes the project demo-ready and professional.

---

### Prompt 9: Git Workflow
**Prompt Used:**  
*"What's the difference between using feat/auth vs feature/authentication? Are there any conventional preferences?"*

**AI Response Summary:**  
The AI explained:
- Both work, but conventions matter for consistency
- `feat/` prefix mirrors conventional commits style
- Descriptive names more important than prefix choice
- Recommended using `feat/` consistently with commit messages
- Provided examples of good vs bad branch names

**Evaluation:**  
✅ Professional practices - Helped establish clean git workflow used throughout the project.

---


## Common Issues & Fixes

### Issue 1: InconsistentMigrationHistory Error
**Error:**
```
django.db.migrations.exceptions.InconsistentMigrationHistory: Migration admin.0001_initial is applied before its dependency book_tracker.0001_initial
```

**Why it happened:**  
I ran migrations before adding the custom user model to settings.

**Solution:**
```bash
# Drop and recreate database
psql -U postgres
DROP DATABASE book_tracker_db;
CREATE DATABASE book_tracker_db;
GRANT ALL PRIVILEGES ON DATABASE book_tracker_db TO book_tracker_user;
\q

# Delete migration files
find . -path "*/migrations/0*.py" -delete

# Recreate migrations
python manage.py makemigrations
python manage.py migrate
```

**Lesson Learned:**  
Always set `AUTH_USER_MODEL` before running your first migration.

---

### Issue 2: "Token has wrong type" Error
**Error:**
```json
{
  "error": "Token has wrong type"
}
```

**Why it happened:**  
I was sending the access token where a refresh token was expected (or vice versa).

**Solution:**  
JWT tokens have two types:
- **Access token** - use in `Authorization: Bearer <token>` header for API requests
- **Refresh token** - use in request body to `/api/auth/refresh/` or `/api/auth/logout/`

Always check which token type the endpoint expects.

**Verification:**
```bash
# Decode token to check type (without verification)
echo "YOUR_TOKEN" | cut -d. -f2 | base64 -d | python -m json.tool
# Look for "token_type": "access" or "refresh"
```

---

### Issue 3: CORS Errors in Browser
**Error:**
```
Access to fetch at 'http://localhost:8000/api/auth/login/' from origin 'http://localhost:3000' has been blocked by CORS policy
```

**Why it happened:**  
Django blocks cross-origin requests by default for security.

**Solution:**  
Install and configure `django-cors-headers`:
```python
# settings.py
INSTALLED_APPS = [
    ...
    'corsheaders',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # Must be at top
    ...
]

CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
    'http://127.0.0.1:3000',
]

CORS_ALLOW_CREDENTIALS = True
```

---

### Issue 4: Password Validation Method Not Working
**Error:**  
My `has_reading_goal()` validation method in the serializer wasn't being called.

**Why it happened:**  
Wrong method name. Django expects `validate_<field_name>()` pattern.

**Solution:**
```python
#  Wrong
def has_reading_goal(self, value):
    ...

# Correct
def validate_reading_goal(self, value):
    if value and value < 12:
        raise serializers.ValidationError("Reading goal must be at least 12 books")
    return value
```

---


##  API Endpoints

### Authentication Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/api/auth/register/` | Register new user | No |
| POST | `/api/auth/login/` | Get access & refresh tokens | No |
| POST | `/api/auth/refresh/` | Refresh access token | No |
| POST | `/api/auth/verify/` | Verify token validity | No |
| GET | `/api/auth/profile/` | Get current user profile | Yes |
| PUT | `/api/auth/profile/` | Update profile (full) | Yes |
| PATCH | `/api/auth/profile/` | Update profile (partial) | Yes |
| POST | `/api/auth/logout/` | Blacklist refresh token | Yes |

### Documentation Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/docs/` | Swagger UI (interactive docs) |
| GET | `/api/redoc/` | ReDoc (clean read-only docs) |
| GET | `/api/schema/` | OpenAPI schema (JSON) |

---

##  References

### Official Documentation
- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/)
- [drf-spectacular](https://drf-spectacular.readthedocs.io/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)

### Tutorials & Guides
- [DRF Tutorial Series](https://www.django-rest-framework.org/tutorial/quickstart/)
- [JWT Authentication in DRF](https://simpleisbetterthancomplex.com/tutorial/2018/12/19/how-to-use-jwt-authentication-with-django-rest-framework.html)
- [Python PEP 8 Style Guide](https://pep8.org/)

### Video Resources
- [Django REST Framework Full Course](https://www.youtube.com/watch?v=c708Nf0cHrs) by freeCodeCamp
- [JWT Authentication Tutorial](https://www.youtube.com/watch?v=xjMP0hspNLE) by Very Academy

### Community & Support
- [Django Forum](https://forum.djangoproject.com/)
- [DRF GitHub Discussions](https://github.com/encode/django-rest-framework/discussions)
- [Stack Overflow - Django Tag](https://stackoverflow.com/questions/tagged/django)
- [Reddit r/django](https://www.reddit.com/r/django/)

### Tools Used
- [Postman](https://www.postman.com/) - API testing
- [pgAdmin](https://www.pgadmin.org/) - PostgreSQL management

---

## What I Learned

Through this AI-assisted learning journey, I gained hands-on experience with:

1. **Modern API Architecture** - RESTful design principles, proper HTTP methods, status codes
2. **Security Best Practices** - JWT authentication, token rotation, environment variables, never committing secrets
3. **Django Patterns** - Custom user models, serializers, class-based views, URL routing
4. **Database Design** - PostgreSQL integration, migrations, model relationships
5. **Code Quality** - Linting with ruff, formatting with black, git workflow with feature branches
6. **Documentation** - Auto-generated API docs with drf-spectacular
7. **Problem Solving** - Debugging migration issues, CORS errors, token authentication

**Key Takeaway:**  
Using AI as a learning partner accelerated my understanding dramatically. Instead of reading documentation for hours, I could ask specific questions and get contextual explanations with working examples. The AI helped me avoid common pitfalls and learn industry best practices from day one.

---

##  License

This project is open source and available under the [MIT License](LICENSE).

---

##  Author

**Your Name**  
- GitHub: [@WanjikuN](https://github.com/WanjikuN)
- Email: wanjikunpatricia@gmail.com

---

## Acknowledgments

- Moringa School for the capstone project framework
- Claude AI for guidance throughout the development process
- Django and DRF communities for excellent documentation

---

**Happy coding!**