"""create posts table

Revision ID: 65839838ccaa
Revises: 
Create Date: 2023-07-23 18:15:55.305817

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '65839838ccaa'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
