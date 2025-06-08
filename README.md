# ❄️ Distributed Snowflake ID Generator (FastAPI)

This is a Python implementation of a **Snowflake ID Generator**, wrapped in a FastAPI API. It generates unique, time-ordered 64-bit IDs, ideal for distributed systems that require scalable, collision-free identifiers.

---

## 🚀 Features

- Unique 64-bit IDs based on:
  - Timestamp
  - Node ID
  - Sequence number
- Thread-safe
- Lightweight FastAPI wrapper for easy integration
- Ready for horizontal scaling with multiple nodes

---

## 📁 Project Structure

snowflake-unique-id-gen/
├── snowfalke.py # Core Snowflake ID logic
├── api.py # FastAPI wrapper
├── requirements.txt
└── README.md


## 🔧 Requirements

- Python 3.8+
- `fastapi`
- `uvicorn`

Install dependencies:

pip install -r requirements.txt
🧠 How Snowflake Works (Simplified)
Each ID is a 64-bit integer:

| 41 bits timestamp | 10 bits node ID | 12 bits sequence |
Timestamp: Time in milliseconds since a custom epoch

Node ID: Identifies the generator machine (max 1024 nodes)

Sequence: Counts requests per millisecond (max 4096 per ms)

▶️ Running the API
Start the FastAPI server:

uvicorn api:app --reload
Then access:

GET http://localhost:8000/generate-id
Example response:

{
  "id": 469128249589370880
}

📦 Future Enhancements
Add node registration service
gRPC version
Metrics and rate-limiting
Docker support
