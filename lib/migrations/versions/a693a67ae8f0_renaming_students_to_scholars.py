"""Renaming students to scholars

Revision ID: a693a67ae8f0
Revises: 791279dd0760
Create Date: 2023-09-01 00:44:36.760112

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a693a67ae8f0'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')




def downgrade() -> None:
      op.rename_table('scholars', 'students')