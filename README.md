<div class="hero-icon" align="center">
  <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
</div>

<h1 align="center">
AI Request Handler MVP
</h1>
<h4 align="center">A streamlined backend service for seamless integration with the OpenAI API.</h4>
<h4 align="center">Developed with the software and tools below.</h4>
<div class="badges" align="center">
  <img src="https://img.shields.io/badge/Framework-FastAPI-blue" alt="Framework used for building APIs">
  <img src="https://img.shields.io/badge/Backend-Python_3.9+-blue" alt="Backend programming language">
  <img src="https://img.shields.io/badge/Database-PostgreSQL-DB4437" alt="Database used">
  <img src="https://img.shields.io/badge/AI_Customization-OpenAI-black" alt="Usage of OpenAI API">
</div>
<div class="badges" align="center">
  <img src="https://img.shields.io/github/last-commit/coslynx/ai-request-handler-mvp?style=flat-square&color=5D6D7E" alt="git-last-commit" />
  <img src="https://img.shields.io/github/commit-activity/m/coslynx/ai-request-handler-mvp?style=flat-square&color=5D6D7E" alt="GitHub commit activity" />
  <img src="https://img.shields.io/github/languages/top/coslynx/ai-request-handler-mvp?style=flat-square&color=5D6D7E" alt="GitHub top language" />
</div>

## 📑 Table of Contents
- 📍 Overview
- 📦 Features
- 📂 Structure
- 💻 Installation
- 🏗️ Usage
- 🌐 Hosting
- 📜 License
- 👏 Authors

## 📍 Overview
The AI Request Handler is a backend service designed to simplify the integration of the OpenAI API, allowing developers and businesses to leverage AI capabilities in their applications with minimal complexity. The system acts as a middleware, encapsulating the complexities of API requests and responses while enhancing the user experience.

## 📦 Features
|    | Feature                | Description                                                                                                       |
|----|------------------------|-------------------------------------------------------------------------------------------------------------------|
| ⚙️ | **Simplified API**    | Streamlines requests to OpenAI through a dedicated API endpoint.                                                 |
| ✅ | **Request Validation** | Validates incoming requests to ensure they meet the expected format prior to processing.                         |
| 🔄 | **Response Formatting**| Reformats responses from OpenAI into a standardized JSON format for easier consumption.                          |
| 🚨 | **Error Handling**     | Captures errors during API interactions, providing meaningful feedback to users in a well-defined format.        |
| 🏥 | **Health Check**       | Endpoint to monitor the application’s status, ensuring it is operational at all times.                           |
| ⏱️ | **Rate Limiting**      | Implements controls to manage the frequency of requests made to the OpenAI API.                                 |
| 📖 | **Comprehensive Logging**| Tracks all interactions and errors for easier debugging and monitoring.                                         |

## 📂 Structure
```text
.
├── .env
├── .gitignore
├── requirements.txt
├── main.py
├── startup.sh
├── api
│   └── v1
│       ├── routes.py
│       └── controllers
│           └── aiController.py
├── models
│   ├── requestModel.py
│   └── responseModel.py
├── services
│   └── aiService.py
├── database
│   └── db.py
├── utils
│   ├── logger.py
│   └── validation.py
└── tests
    ├── unit
    │   └── test_ai_service.py
    └── integration
        └── test_routes.py
```

## 💻 Installation
### 🔧 Prerequisites
- Python 3.9+
- PostgreSQL Database
- OpenAI API Key

### 🚀 Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/coslynx/ai-request-handler-mvp.git
   cd ai-request-handler-mvp
   ```

2. Create a `.env` file and add your environment configurations:
   ```bash
   OPENAI_API_KEY=your_openai_api_key
   DATABASE_URL=postgresql://username:password@localhost/dbname
   JWT_SECRET=your_jwt_secret
   PORT=8000
   ```

3. Install the necessary dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000 --reload
   ```

## 🏗️ Usage
### 🏃‍♂️ Running the MVP
1. Start the application:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port $PORT
   ```
2. Access the application through the following endpoints:
   - Health Check: [http://localhost:8000/health](http://localhost:8000/health)
   - AI Request: [http://localhost:8000/ai/request](http://localhost:8000/ai/request)

### ⚙️ Configuration
- Modify the `.env` file for different environment settings, ensuring your database and API keys are correctly set.

### 📚 Examples
#### Making a Request to the OpenAI API:
```http
POST http://localhost:8000/ai/request
Content-Type: application/json

{
  "prompt": "Translate the following English text to French: 'Hello, world!'",
  "max_tokens": 50
}
```

#### Sample Response:
```json
{
  "output": "Bonjour le monde!",
  "status_code": 200,
  "message": null
}
```

## 🌐 Hosting
### 🚀 Deployment Instructions
Deploy this application on any platform supporting ASGI applications (like Heroku, AWS, etc.)

1. Use a service like Heroku for hosting:
   - Install the Heroku CLI:
     ```bash
     heroku login
     heroku create ai-request-handler
     ```
   - Set environment variables:
     ```bash
     heroku config:set OPENAI_API_KEY=your_key
     heroku config:set DATABASE_URL=your_url
     ```

2. Deploy the app:
   ```bash
   git push heroku main
   ```

### 🔑 Environment Variables
- `DATABASE_URL`: Connection string for PostgreSQL.
- `JWT_SECRET`: Secret key used for JWT encoding.
- `OPENAI_API_KEY`: Key for accessing OpenAI services.

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👏 Authors
This Minimum Viable Product (MVP) is created by [Drix10](https://drix10.com) and [Kais Radwan](https://www.linkedin.com/in/kais-radwan).

---

###  🌐 CosLynx.com
Create Your Custom MVP in Minutes With CosLynxAI!
```