from datetime import date, timedelta
from unittest.mock import MagicMock

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.main import app
from app.database.base import Base
from app.database.session import get_db
from app.routes.registrations import create_registration
from app.schemas.registration import RegistrationCreate

engine = create_engine(
    "sqlite+pysqlite:///:memory:",
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base.metadata.create_all(bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)

VALID_PAYLOAD = {
    "synthetic_voter_id": "IV-ABC123",
    "full_name": "Asha Prototype",
    "date_of_birth": "1990-04-12",
    "address": "Synthetic testing address",
    "contact_number": "+91 90000 00000",
}


def test_missing_required_fields() -> None:
    response = client.post("/api/v1/registrations", json={"synthetic_voter_id": "IV-ABC123"})
    assert response.status_code == 422


def test_invalid_synthetic_voter_id() -> None:
    payload = {**VALID_PAYLOAD, "synthetic_voter_id": "EPIC-123"}
    response = client.post("/api/v1/registrations", json=payload)
    assert response.status_code == 422


def test_invalid_date_of_birth() -> None:
    payload = {**VALID_PAYLOAD, "date_of_birth": (date.today() + timedelta(days=1)).isoformat()}
    response = client.post("/api/v1/registrations", json=payload)
    assert response.status_code == 422


def test_successful_registration() -> None:
    response = client.post("/api/v1/registrations", json=VALID_PAYLOAD)
    assert response.status_code == 201
    assert response.json()["status"] == "PENDING_REVIEW"
    assert response.json()["synthetic_voter_id"] == "IV-ABC123"


def test_duplicate_voter_id() -> None:
    response = client.post("/api/v1/registrations", json=VALID_PAYLOAD)
    assert response.status_code == 409


def test_database_error_handling() -> None:
    from sqlalchemy.exc import SQLAlchemyError

    db = MagicMock()
    db.query.return_value.filter_by.return_value.first.return_value = None
    db.commit.side_effect = SQLAlchemyError("database unavailable")
    with pytest.raises(Exception) as error:
        create_registration(RegistrationCreate(**VALID_PAYLOAD), db)
    assert getattr(error.value, "status_code", None) == 500
