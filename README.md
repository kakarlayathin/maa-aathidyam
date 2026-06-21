# Shipyard Client Dashboard

A full-stack SaaS Client Dashboard built with FastAPI and React.

## Project Structure

```
maa-aathidyam/
├── backend/          # FastAPI app
│   ├── app/
│   │   ├── models/
│   │   ├── routes/
│   │   ├── schemas/
│   │   └── auth/
│   ├── tests/
│   └── alembic/
├── frontend/         # Vite + React app
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── api/
│   │   └── lib/
│   └── tests/
├── .github/
│   └── workflows/    # CI
└── README.md
```

## Tech Stack

- **Backend:** Python FastAPI, SQLAlchemy (SQLite via Turso), Pydantic, pytest
- **Frontend:** React, Vite, TailwindCSS, Vitest
- **CI/CD:** GitHub Actions

## Setup

### Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

## License

MIT
