# AI Resume Ranking System

## 📌 Project Overview
The **AI Resume Ranking System** is a Streamlit-based web application that ranks uploaded resumes based on their relevance to a given job description. It utilizes **TF-IDF Vectorization** and **Cosine Similarity** from **Scikit-learn** to compare and evaluate resumes against the job description.

---
## 🚀 Features
- Upload multiple **PDF resumes**
- Enter or paste a **job description**
- AI-powered **resume ranking** based on relevance
- **User-friendly** UI with a two-column layout
- Runs **locally** with Streamlit

---
## 🛠️ Setup Instructions

### 1️⃣ Prerequisites
Ensure your system has the following installed:
- **Python** (>=3.8 recommended)
- **pip** (Python package manager)

### 2️⃣ Clone the Repository
```sh
# Clone this project (if using GitHub)
git clone https://github.com/your-username/resume-ranker.git
cd resumeScanning
```

### 3️⃣ Activate the Virtual Environment
A virtual environment (`env`) is already included with all necessary dependencies.

```sh
# Activate Virtual Environment (Windows)
env\Scripts\activate

# Activate Virtual Environment (Mac/Linux)
source env/bin/activate
```

*Alternatively, if you want to install dependencies manually, run:*
```sh
pip install -r requirements.txt
```

### 4️⃣ Run the Application
```sh
streamlit run app.py
```
After running the command, a new **browser window** will open automatically with the app.

---
## 📦 Dependencies
This project already includes a virtual environment with the necessary dependencies:
- **Streamlit**
- **PyPDF2**
- **pandas**
- **scikit-learn**

If needed, you can reinstall dependencies using:
```sh
pip install -r requirements.txt
```

---
## 📷 Screenshots
![Resume Ranker] https://github.com/sgr-8426/resumeScanning/blob/main/Screenshot%202025-03-10%20143625.png

---
## 🤝 Contributing
Feel free to contribute by forking this repository and submitting a pull request!

---
## 📜 License
This project is licensed under the **MIT License**.

