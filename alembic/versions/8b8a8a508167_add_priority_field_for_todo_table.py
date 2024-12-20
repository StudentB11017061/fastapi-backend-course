"""add priority field for todo table

Revision ID: 8b8a8a508167
Revises: a0ee89127682
Create Date: 2024-12-19 14:41:23.802295

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8b8a8a508167'
down_revision: Union[str, None] = 'a0ee89127682'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('priority', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'priority')
    # ### end Alembic commands ###
