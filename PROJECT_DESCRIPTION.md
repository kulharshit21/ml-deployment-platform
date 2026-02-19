# 📘 Project Description — Cloud Product & Platform Engineering

## 🎓 Course: Professional Elective — Cloud Product and Platform Engineering
**Student:** B.Tech CSE | SRM Institute of Science and Technology  
**Project Title:** End-to-End Scalable ML Model Deployment Platform with Automated CI/CD Pipeline

---

## 🧠 What This Project Does

This project builds a **production-ready cloud platform** that takes a trained 
Machine Learning model and deploys it as a fully automated, scalable, 
cloud-native service — accessible to anyone on the internet, completely free.

A user opens the web interface, adjusts flower measurements using sliders, 
clicks Predict, and instantly receives a prediction from an ML model running 
on the cloud — all without the user or developer managing any servers manually.

---

## ☁️ Cloud Platform Engineering Concepts Used

### 1. Containerization (Docker)
- The entire ML model + API is packaged into a Docker container
- This ensures the app runs identically on any machine or cloud provider
- Eliminates "works on my machine" problems
- **File:** `Dockerfile`

### 2. Microservices Architecture
- Backend (FastAPI on Render) and Frontend (Streamlit on Hugging Face) 
  are completely decoupled services
- Each service can be updated, scaled, or replaced independently
- Frontend communicates with backend only via REST API calls

### 3. CI/CD Pipeline (Continuous Integration & Continuous Deployment)
- Every `git push` to the `main` branch automatically triggers the pipeline
- GitHub Actions runs tests, validates the model, and triggers deployment
- Zero manual deployment steps needed
- **File:** `.github/workflows/deploy.yml`

### 4. API-First Design
- Backend exposes a clean REST API with `/predict` endpoint
- Any frontend (web, mobile, CLI) can consume the API
- Auto-generated interactive API documentation via FastAPI/Swagger
- **Endpoint:** `https://ml-deployment-platform.onrender.com/docs`

### 5. Infrastructure as Code (IaC)
- `Dockerfile` defines the entire runtime environment as code
- `requirements.txt` declares all dependencies explicitly
- Any developer can reproduce the exact environment with one command
- No manual server configuration needed

### 6. Cloud-Native Deployment
- Backend hosted on **Render** (free tier, auto-scaling enabled)
- Frontend hosted on **Hugging Face Spaces** (free tier, global CDN)
- Both services are stateless — can scale horizontally
- Zero infrastructure management by the developer

### 7. Platform Engineering Principle — Self-Service
- Developer pushes code → platform handles everything automatically
- No manual SSH, no manual server setup, no manual restarts
- This is the core principle of modern Platform Engineering (like Netflix, Spotify)

---

## 🏗️ System Architecture

```
Developer writes code
        ↓
    Git Push to GitHub
        ↓
GitHub Actions triggers CI/CD Pipeline
        ↓
    ┌─────────────────────────┐
    │  Tests run automatically │
    │  Model integrity checked │
    └─────────────────────────┘
        ↓
    ┌─────────────────────────────────────┐
    │  Render (Backend)                   │
    │  FastAPI + Docker Container         │
    │  → REST API /predict endpoint       │
    │  → Auto-scales with traffic         │
    └─────────────────────────────────────┘
              ↑ API calls
    ┌─────────────────────────────────────┐
    │  Hugging Face Spaces (Frontend)     │
    │  Streamlit Web Interface            │
    │  → User-friendly prediction UI      │
    │  → Accessible globally              │
    └─────────────────────────────────────┘
              ↑ opens in browser
           End Users (Anyone)
```

---

## 🛠️ Tech Stack

| Layer | Technology | Cloud PE Concept |
|---|---|---|
| ML Model | scikit-learn RandomForest | Core service logic |
| API Framework | FastAPI | API-First Design |
| Containerization | Docker | IaC + Portability |
| CI/CD | GitHub Actions | Automation |
| Backend Hosting | Render (free) | Cloud-Native Deployment |
| Frontend | Streamlit | Self-Service UI |
| Frontend Hosting | Hugging Face Spaces | Cloud-Native Deployment |
| Version Control | GitHub | Source of Truth |

---

## 🔗 Live Demo Links

| Service | URL |
|---|---|
| 🌸 Frontend UI | https://huggingface.co/spaces/harshitrk07/ml-deployment-platform |
| ⚙️ Backend API | https://ml-deployment-platform.onrender.com |
| 📄 API Docs | https://ml-deployment-platform.onrender.com/docs |
| 🔄 CI/CD Pipeline | https://github.com/kulharshit21/ml-deployment-platform/actions |
| 💻 Source Code | https://github.com/kulharshit21/ml-deployment-platform |

---

## 💰 Total Infrastructure Cost: ₹0.00

| Service | Free Limit | Usage |
|---|---|---|
| Render | 750 hrs/month | ~50 hrs/month |
| Hugging Face Spaces | Unlimited public apps | 1 app |
| GitHub Actions | 2000 mins/month | ~5 mins/month |
| Docker | Free | Local only |

---

## 🎯 Key Takeaway

This project demonstrates that **modern platform engineering removes the burden 
of infrastructure from developers**. A developer only writes code and pushes to 
GitHub — the platform automatically tests, builds, and deploys everything. 
This is exactly how teams at Google, Netflix, and Spotify operate at scale.
