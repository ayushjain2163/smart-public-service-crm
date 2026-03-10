# 🚀 Smart Public Service CRM with AI Co-Pilot

> AI-powered governance platform that helps administrators manage citizen complaints, analyze public sentiment, and make data-driven decisions.

---

## 🎥 Project Demo

Watch the working demo here:

[![Project Demo](https://img.youtube.com/vi/eRUuRrhMugc/0.jpg)](https://youtu.be/eRUuRrhMugc)

🔗 https://youtu.be/eRUuRrhMugc

---

# 📌 Problem Statement

Public service grievance systems often face:

- ❌ Fragmented complaint management
- ❌ Slow resolution times
- ❌ Administrative overload
- ❌ Lack of real-time citizen sentiment insights

Government departments struggle to **prioritize and analyze complaints effectively**.

---

# 💡 Our Solution

**Smart Public Service CRM + AI Co-Pilot**

An AI-driven system that:

- Collects citizen complaints
- Automatically categorizes them
- Detects sentiment
- Provides analytics dashboards
- Assists administrators with AI insights

This creates a **Smart Governance Decision Support System**.

---

# 🧠 Key Features

### 📝 Complaint Management

Citizens can submit complaints with location.

Example:

```
"The road near my house is broken"
Location: Pimpri
```

AI automatically detects:

```
Category: Road Infrastructure
Sentiment: Negative
```

---

### 🤖 AI Complaint Analysis

Uses **NLP models** to detect:

- Complaint category
- Citizen sentiment
- Issue trends

---

### 📊 Admin Analytics Dashboard

Administrators can view:

- Complaint list
- Sentiment distribution
- Category distribution
- AI insights

Built with **Streamlit + Plotly**.

---

### 🧭 Location-Based Complaints

Each complaint stores:

```
text
location
category
sentiment
status
timestamp
```

This enables **geo-based governance analytics**.

---

### 🤖 AI Co-Pilot for Administrators

Admins can paste:

- policy documents
- meeting notes
- reports

AI generates:

- concise summary
- key insights

---

# 🏗 System Architecture

```
Citizen Interface
       │
       ▼
 FastAPI Backend
       │
       ├── AI Engine
       │     ├ Sentiment Analysis
       │     ├ Complaint Categorization
       │     └ AI Summarization
       │
       ▼
     MongoDB
       │
       ▼
 Streamlit Dashboard
       │
       ├ Complaint Analytics
       ├ Sentiment Charts
       └ Admin Insights
```

---

# ⚙️ Technology Stack

| Layer          | Technology               |
| -------------- | ------------------------ |
| Backend API    | FastAPI                  |
| Dashboard      | Streamlit                |
| Database       | MongoDB                  |
| AI Models      | HuggingFace Transformers |
| Visualization  | Plotly                   |
| Authentication | JWT                      |

---

# 📂 Project Structure

```
smart-public-service-crm
│
├── backend
│   ├── main.py
│   ├── ai_engine.py
│   ├── crud.py
│   ├── database.py
│   ├── auth.py
│   ├── schemas.py
│   └── utils.py
│
├── dashboard
│   └── app.py
│
├── data
│
├── requirements.txt
└── README.md
```

---

# 🚀 Installation Guide

## Clone Repository

```
git clone https://github.com/your-repo/smart-public-service-crm
cd smart-public-service-crm
```

---

## Create Virtual Environment

```
python -m venv venv
```

Activate:

### Windows

```
venv\Scripts\activate
```

### Mac / Linux

```
source venv/bin/activate
```

---

## Install Dependencies

```
pip install -r requirements.txt
```

---

# ▶ Running the System

## Start Backend

```
cd backend
uvicorn main:app --reload
```

Backend runs at:

```
http://127.0.0.1:8000
```

Swagger API Docs:

```
http://127.0.0.1:8000/docs
```

---

## Start Dashboard

Open another terminal:

```
cd dashboard
streamlit run app.py
```

Dashboard runs at:

```
http://localhost:8501
```

---

# 📡 API Endpoints

### Submit Complaint

```
POST /submit-complaint
```

Example:

```json
{
  "text": "The road near school is broken",
  "location": "Pimpri"
}
```

---

### Get Complaints

```
GET /complaints
```

---

### Admin Signup

```
POST /admin/signup
```

---

### Admin Login

```
POST /admin/login
```

Returns:

```
JWT access token
```

---

### AI Summary

```
POST /summarize
```

Input:

```
meeting notes / policy text
```

Output:

```
AI summary
```

---

# 📊 Dashboard Features

Admin dashboard shows:

- Complaint table
- Sentiment distribution
- Complaint categories
- AI summaries

---

# 🔮 Future Scope

This system can be extended into a **Smart City Governance Platform**.

Possible upgrades:

### 📍 Complaint Heatmap

Visualize complaints geographically.

### 🚨 AI Priority Detection

Example:

```
Electric pole sparking near school
→ Priority: Critical
```

### 🏢 Department Auto Assignment

```
Road complaint → PWD
Water complaint → Water Department
```

### 🎤 Voice Complaint Submission

```
Speech → Text → AI analysis
```

Using **OpenAI Whisper**.

### 🤖 AI Governance Assistant

Admins can ask:

```
Which area has the most road complaints?
```

AI provides insights using complaint data.

---

# 🎯 Impact

This platform enables:

- Faster grievance resolution
- Data-driven governance
- Better citizen satisfaction
- Smart city analytics

---

# 👨‍💻 Team

Team Name: **[Add Your Team Name]**

Members:

- Ayush Jain
- A S Laxman Babu

Affiliation:

Pimpri Chinchwad College of Engineering

---

# ⭐ If you like this project

Give the repository a star ⭐
