from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.registration import Registration
from app.schemas.registration import RegistrationCreate, RegistrationResponse

router = APIRouter(prefix="/api/v1/registrations", tags=["registrations"])


@router.post("", response_model=RegistrationResponse, status_code=status.HTTP_201_CREATED)
def create_registration(payload: RegistrationCreate, db: Session = Depends(get_db)) -> Registration:
    try:
        existing = db.query(Registration).filter_by(synthetic_voter_id=payload.synthetic_voter_id).first()
        if existing:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Synthetic voter ID is already registered",
            )

        registration = Registration(**payload.model_dump(), status="PENDING_REVIEW")
        db.add(registration)
        db.commit()
        db.refresh(registration)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Synthetic voter ID is already registered",
        ) from None
    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Registration could not be saved",
        ) from None
    return registration
