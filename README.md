# 🔐 SQL Injection Vulnerability Demonstration System

## 📌 Project Overview
This project demonstrates a **SQL Injection vulnerability** in a web application.  
It shows how improper handling of user input can allow attackers to manipulate SQL queries and access unauthorized data.

The application is built using Flask and deployed on cloud, making it accessible globally.

## 🎯 Objective
- To understand SQL Injection attacks  
- To demonstrate how user input can manipulate SQL queries  
- To highlight risks of insecure coding practices  
- To deploy the application on cloud  

## 🛠️ Technologies Used
- Backend: Python (Flask)
- Frontend: HTML, CSS
- Database: SQLite
- Cloud: Render

## ⚙️ How It Works
1. User enters a product name in the search box  
2. Input is directly used in SQL query (vulnerable)  
3. Database executes query  
4. Results are displayed  

## 💣 SQL Injection Demonstration

### 🔹 Normal Input
Laptop ➡ Shows only matching product  

### 🔹 Malicious Input
' OR '1'='1

➡ Modified Query: SELECT * FROM products WHERE name LIKE '%' OR '1'='1%'
➡ Result:
- All products are displayed  
- Demonstrates unauthorized access  

## ⚠️ Error Handling
The application uses exception handling to prevent crashes and display user-friendly error messages.

## ☁️ Cloud Deployment
The application is deployed on cloud using Render.

### 🌍 Live Demo: 
https://sql-injection-project.onrender.com

## 📂 Project Structure
miniProject/
│── app.py
│── init_db.py
│── products.db
│── requirements.txt
│── Procfile
│
├── templates/
│ └── index.html
│
└── static/
└── styles.css

---
## ▶️ How to Run Locally

### 1. Clone repository
git clone <your-repo-link>
cd miniProject

### 2. Create virtual environment
python3 -m venv venv
source venv/bin/activate

### 3. Install dependencies
pip install -r requirements.txt

### 4. Initialize database
python init_db.py

### 5. Run application
python app.py

### 6. Open in browser
http://127.0.0.1:8000

---

## 🔐 Prevention (Secure Version)
SQL Injection can be prevented by:
- Using parameterized queries  
- Validating user input  
- Using ORM frameworks  

## 🚀 Future Improvements
- Add secure mode (toggle)  
- Implement login system  
- Use cloud database (MongoDB Atlas)  
- Add logging and monitoring  

## 🧠 Key Learning
This project demonstrates how small coding mistakes can lead to major security vulnerabilities.

## 📚 References
- Flask Documentation  
- OWASP SQL Injection Guide  
- Render Documentation  

## 👨‍💻 Author
Anurag Mendhe
