
"""empty message

Revision ID: 3c1a0b158a2d
Revises: 854bec9e1c34
Create Date: 2024-03-20 19:44:40.367009

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3c1a0b158a2d'
down_revision: Union[str, None] = '854bec9e1c34'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
