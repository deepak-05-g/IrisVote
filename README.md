# IrisVote

IrisVote is a prototype for detecting potentially duplicate voter registrations
using iris biometric recognition. A biometric similarity signal creates an alert
for human investigation; it never automatically rejects a voter.

## Technology

- **Frontend:** React, TypeScript, Vite, Tailwind CSS, and shadcn/ui
- **Backend:** Python, FastAPI, SQLAlchemy, and Alembic
- **Database:** PostgreSQL
- **Infrastructure:** Docker Compose

## Project structure

```text
frontend/          React and TypeScript application
backend/app/       FastAPI application modules
backend/            Python dependencies and migration configuration
docker-compose.yml PostgreSQL development service
```

## Frontend setup

```powershell
cd frontend
npm install
npm run dev
```

The development server is available at `http://localhost:5173`.

## Backend setup

Create a virtual environment and install the dependencies:

```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
```

The API is available at `http://localhost:8000`.
The health endpoint is `GET http://localhost:8000/health`.

## Database setup

Copy `.env.example` to `.env` and set a local development password. Start
PostgreSQL with:

```powershell
docker compose up -d postgres
```

The database is configured for local development on port `5432`. Do not place
production credentials, real voter information, or biometric images in this
repository.

## Run the application

Run the frontend and backend in separate terminals. The frontend is currently a
landing page and navigation foundation; voter registration and iris processing
will be added in later stages.
