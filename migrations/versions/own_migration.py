"""added new field

Revision ID: a45cb4560be8
Revises: a5f6ea9ad79a
Create Date: 2020-11-26 20:30:59.982450

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
from sqlalchemy import text

revision = 'a45cb4560be9'
down_revision = 'a45cb4560be8'
branch_labels = None
depends_on = None


def upgrade():
    conn = op.get_bind()
    conn.execute(
        text(
            """
                UPDATE films
                SET test = 100
                WHERE title like '%Deathly%'
            """
        )
    )


def downgrade():
    conn = op.get_bind()
    conn.execute(
        text(
            """
                UPDATE films
                SET test = NULL
                WHERE title like '%Deathly%'
            """
        )
    )
