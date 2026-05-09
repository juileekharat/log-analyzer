# 📊 Log Analyzer

A modern log analytics dashboard built using FastAPI, Jinja2, Chart.js, Tailwind CSS, and Docker.

This project parses application log files, extracts operational insights, visualizes analytics, and exports reports in CSV format.

---

# 🚀 Features

- Upload and analyze `.log` files
- Parse INFO / WARNING / ERROR logs
- Interactive analytics dashboard
- Pie chart visualization
- Error-per-hour bar chart
- Search and filter logs
- Pagination support
- CSV export support
- Dockerized application
- Docker Compose setup

---

# 🛠️ Tech Stack

- Python
- FastAPI
- Jinja2
- Chart.js
- Tailwind CSS
- Pandas
- Docker
- Docker Compose

---

# 📂 Project Structure

```plaintext
log-analyzer/
│
├── app/
│   ├── main.py
│   ├── log_parser.py
│   └── templates/
│
├── uploads/
├── reports/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
