"""empty message

Revision ID: 678ce982f425
Revises: 0c8f63591525
Create Date: 2024-06-04 11:27:43.150826

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '678ce982f425'
down_revision: Union[str, None] = '0c8f63591525'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('notifications',
    sa.Column('telegram_id', sa.String(), nullable=False),
    sa.Column('coin_name', sa.String(), nullable=False),
    sa.Column('target_price', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('telegram_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('notifications')
    # ### end Alembic commands ###
