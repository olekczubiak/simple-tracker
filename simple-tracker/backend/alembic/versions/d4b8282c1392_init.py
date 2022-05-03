"""init

Revision ID: d4b8282c1392
Revises: 
Create Date: 2021-10-24 15:08:25.745815

"""
from sqlalchemy.sql.expression import true
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import String
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "d4b8282c1392"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("email", sa.String, unique=True, index=True),
        sa.Column("hashed_password", sa.String),
        sa.Column("is_active", sa.Boolean, default=True),
        sa.Column("company", sa.String),
    )
    op.create_table(
        "device",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("device_name", sa.String),
        sa.Column("gps_name", sa.String),
        sa.Column("owner_id", sa.Integer, ForeignKey("users.id")),
        sa.Column("description", sa.String, index=True),
    )
    op.create_table(
        "position",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("owner_id", sa.Integer, ForeignKey("users.id")),
        sa.Column("my_date", sa.Date),
        sa.Column("time", sa.String),
        sa.Column("latitude", sa.Float),
        sa.Column("longitude", sa.Float),
    )


def downgrade():
    op.drop_table("users")
    op.drop_table("device")
    op.drop_table("position")
