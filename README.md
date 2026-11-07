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

Apply database migrations from the `backend` directory:

```powershell
$env:DATABASE_URL="postgresql+psycopg://irisvote:change_this_for_local_development@localhost:5433/irisvote"
python -m alembic upgrade head
```

The registration endpoint is `POST /api/v1/registrations`. It accepts synthetic
IDs in the `IV-XXXXXX` format and stores new applications with
`PENDING_REVIEW` status. Duplicate synthetic IDs return `409 Conflict`.

## Database setup

Copy `.env.example` to `.env` and set a local development password. Start
PostgreSQL with:

```powershell
docker compose up -d postgres
```

The database is configured for local development on host port `5433` (the
PostgreSQL container still listens on its internal port `5432`). Do not place
production credentials, real voter information, or biometric images in this
repository.

## Run the application

Run the frontend and backend in separate terminals. The frontend is currently a
landing page and navigation foundation; voter registration and iris processing
will be added in later stages.
