"""add content column to posts table

Revision ID: b107847f879c
Revises: 65839838ccaa
Create Date: 2023-07-23 18:21:40.279073

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b107847f879c'
down_revision = '65839838ccaa'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String, nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
