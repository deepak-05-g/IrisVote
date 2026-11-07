from datetime import date, datetime
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StringConstraints, field_validator

VoterId = Annotated[str, StringConstraints(pattern=r"^IV-[A-Z0-9]{6}$")]


class RegistrationCreate(BaseModel):
    synthetic_voter_id: VoterId
    full_name: Annotated[str, Field(min_length=2, max_length=120)]
    date_of_birth: date
    address: Annotated[str, Field(min_length=5, max_length=500)]
    contact_number: Annotated[str | None, Field(default=None, max_length=20)]

    @field_validator("synthetic_voter_id", "full_name", "address", "contact_number")
    @classmethod
    def strip_text(cls, value: str | None) -> str | None:
        return value.strip() if value is not None else None

    @field_validator("date_of_birth")
    @classmethod
    def validate_birth_date(cls, value: date) -> date:
        if value >= date.today():
            raise ValueError("Date of birth must be in the past")
        return value

    @field_validator("contact_number")
    @classmethod
    def validate_contact_number(cls, value: str | None) -> str | None:
        if value == "":
            return None
        if value is not None and not value.replace("+", "").replace(" ", "").replace("-", "").isdigit():
            raise ValueError("Contact number contains invalid characters")
        return value


class RegistrationResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    synthetic_voter_id: str
    full_name: str
    date_of_birth: date
    address: str
    contact_number: str | None
    status: str
    created_at: datetime
