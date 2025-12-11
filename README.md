# DevOps CI/CD Project

**This project demonstrates a complete CI/CD pipeline using GitHub Actions, Docker, PostgreSQL, AWS EC2, and Nginx/Flask for deployment.
**---

## 🚀 Project Overview

This repository includes:

* A simple Python Flask API (Tic Tac Toe bot).
* Docker containerization.
* GitHub Actions CI pipeline running tests using `pytest`.
* Deployment over SSH to a remote server(EC2 instance).

---
## 📦 Project Structure

```
DevOps-CI-CD/
│
├── app.py
├── bot_logic.py
├── requirements.txt
├── docker-compose.yml
├── Dockerfile
├── tests/
│   └── test_api.py
└── .github/workflows/ci.yml
```
## 🧩 Architecture Diagram

**Simplified Flow (Arrows Diagram):**

```
Developer Pushes Code
          |
          v
   GitHub Actions CI
          |
          v
     Run Tests
     /      \
 Pass         Fail
  |             |
  v             v
Build Docker   Stop
    |
    v
Push to EC2 Server
    |
    v
Docker Compose Up
    |
    v
App Running on Port 5000
```
##  CI/CD Pipeline (GitHub Actions)

The pipeline runs automatically on every push o the main branch:

1. Install Python
2. Install dependencies
3. Run unit tests
4. Deploy via SSH if tests pass

---
---

## 🔧 Running Locally

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the app

```bash
python app.py
```

App runs at: `http://localhost:5000`

---

## 🐳 Running with Docker

```bash
docker compose up --build
```

App will be available at:

```
http://localhost:5000
```

---

##  Deployment to AWS EC2

The GitHub Actions pipeline also performs **automatic deployment** to an EC2 instance using SSH.

###  What the deployment step does

* Connects to your EC2 machine over SSH
* Pulls the latest code from GitHub
* Rebuilds Docker images
* Restarts the application using Docker Compose

After deployment, the app becomes available from your EC2 public IP.


####  Game Page (Tic Tac Toe)

```
http://YOUR-EC2-PUBLIC-IP:5000/
```

####  Game Results API

```
http://YOUR-EC2-PUBLIC-IP:5000//games
```

---

##  CI/CD Pipeline (GitHub Actions)

The pipeline runs automatically on every push o the main branch:

1. Install Python
2. Install dependencies
3. Run unit tests
4. Deploy via SSH if tests pass

---
## 📘 Additional Information

For questions, open an issue or message me on GitHub.

