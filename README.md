# Real-Time E-Commerce Data Pipeline

## 🚀 Tech Stack
- Apache Kafka
- Apache Spark Structured Streaming
- Python (Kafka Producer)
- MySQL
- Apache Airflow

## 📌 Architecture
Python Producer → Kafka → Spark Streaming → MySQL → Airflow Orchestration

## 📂 Features
- Real-time order generation using Kafka Producer
- Stream processing using Spark Structured Streaming
- JSON parsing and schema enforcement
- DAG scheduling using Airflow (daily job)
- End-to-end ETL pipeline

## ⚙️ How to Run

### 1. Start Kafka
```bash
bin/kafka-server-start.sh config/server.properties
