# Job Discovery Agent

A GitHub-ready job discovery tool that searches multiple job sources and ranks opportunities for a candidate profile.

## Target countries
- Italy
- Germany
- Netherlands
- Spain

## Features
- Multi-provider job search
- Profile-based matching
- Job scoring
- Duplicate removal
- FastAPI backend
- HTML dashboard
- GitHub Actions daily automation

## Quick start
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload
```

Open http://localhost:8000

## API
- `GET /api/jobs` - search and return ranked jobs
- `GET /api/health` - health check

## Notes
Use official APIs or sources that permit automated access. Add API credentials to `.env`, never commit secrets.
