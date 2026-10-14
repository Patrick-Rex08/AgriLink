# AgriLink — AI & Blockchain-Powered Agricultural Marketplace

> **Smart India Hackathon (SIH) 2026 Project**  
> Direct farm-to-buyer platform enabling fair prices, verifiable supply chain provenance, and optimized agricultural logistics.

---

## 🏗️ Architecture Overview

AgriLink employs a decoupled monorepo architecture:

* **Frontend (`/frontend`)**: React 19 + TypeScript + Vite + TailwindCSS.
* **Backend (`/backend`)**: Python 3.14 + FastAPI + Pydantic v2 + SQLAlchemy 2.0.
* **Database**: PostgreSQL (configured via `.env`).
* **Planned Modules**:
  * **AI Intelligence**: scikit-learn for Mandi market price forecasting and fair MSP recommendations.
  * **Logistics Optimization**: Google OR-Tools for multi-farm collection routing and load aggregation.
  * **Trust & Traceability**: Solidity smart contract with testnet deployment and QR batch verification.

---

## 📁 Repository Structure

```
HackArena/
├── backend/
│   ├── app/
│   │   ├── main.py                  # FastAPI application entrypoint
│   │   ├── core/
│   │   │   ├── config.py            # Pydantic v2 settings & database configuration
│   │   │   └── database.py          # SQLAlchemy 2.0 engine & connection verification
│   │   └── api/v1/
│   │       ├── api.py               # API router aggregator
│   │       └── endpoints/
│   │           └── health.py        # /health diagnostic check
│   ├── tests/
│   │   └── test_health.py           # Integration tests
│   ├── requirements.txt             # Python dependencies
│   ├── check_health.py              # CLI diagnostic health script
│   └── .env.example                 # Backend environment variable template
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   └── HealthStatusCard.tsx # Real-time API & DB status card
│   │   ├── services/
│   │   │   └── api.ts               # Backend API client
│   │   ├── types/
│   │   │   └── index.ts             # TypeScript definitions
│   │   ├── App.tsx                  # Foundation dashboard
│   │   ├── main.tsx
│   │   └── index.css
│   ├── package.json
│   ├── tsconfig.json
│   ├── vite.config.ts               # Proxy configuration to FastAPI
│   └── .env.example
│
├── legacy/                          # Preserved previous work (Project Sakhi / Saha AI)
│   └── project-sakhi/
│
├── .gitignore                       # Multi-stack gitignore
├── .env.example                     # Root environment variable template
└── README.md
```

---

## 🚀 Quickstart: Local Development

### 1. Backend (FastAPI)

1. Open PowerShell and navigate to the backend directory:
   ```powershell
   cd backend
   ```
2. Activate the pre-configured virtual environment:
   ```powershell
   .\venv\Scripts\Activate.ps1
   ```
   *(Or run commands directly with `.\venv\Scripts\python.exe`)*
3. Create your `.env` file from the template:
   ```powershell
   Copy-Item .env.example .env
   ```
4. Run automated tests:
   ```powershell
   .\venv\Scripts\pytest.exe -v
   ```
5. Start the backend development server:
   ```powershell
   .\venv\Scripts\uvicorn.exe app.main:app --reload --port 8000
   ```
   * Interactive API docs: [http://localhost:8000/docs](http://localhost:8000/docs)
   * Health endpoint: [http://localhost:8000/health](http://localhost:8000/health)

---

### 2. Frontend (React + Vite)

1. Open a second PowerShell terminal and navigate to `frontend`:
   ```powershell
   cd frontend
   ```
2. Start the Vite development server:
   ```cmd
   npm.cmd run dev
   ```
3. Open your browser at [http://localhost:5173](http://localhost:5173).

---

## 🔒 Security Best Practices

* **No Hardcoded Secrets**: Passwords, API keys, and blockchain private keys are strictly loaded via `.env`.
* **Zero Secret Leakage to Client**: The React frontend bundle only accesses non-sensitive parameters prefixed with `VITE_`.
* **Database Isolation**: The database connection string is constructed and consumed solely on the backend server.
