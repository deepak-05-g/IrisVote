"""create registrations table

Revision ID: 20261107_0001
Revises:
Create Date: 2026-11-07
"""

from alembic import op
import sqlalchemy as sa

revision = "20261107_0001"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "registrations",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("synthetic_voter_id", sa.String(length=9), nullable=False),
        sa.Column("full_name", sa.String(length=120), nullable=False),
        sa.Column("date_of_birth", sa.Date(), nullable=False),
        sa.Column("address", sa.Text(), nullable=False),
        sa.Column("contact_number", sa.String(length=20), nullable=True),
        sa.Column("status", sa.String(length=32), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("synthetic_voter_id"),
    )
    op.create_index("ix_registrations_synthetic_voter_id", "registrations", ["synthetic_voter_id"], unique=False)


def downgrade() -> None:
    op.drop_index("ix_registrations_synthetic_voter_id", table_name="registrations")
    op.drop_table("registrations")
