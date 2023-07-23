"""add last few columns to posts table

Revision ID: 7771de138c64
Revises: 09aefbe0b809
Create Date: 2023-07-23 18:41:44.978342

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7771de138c64'
down_revision = '09aefbe0b809'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE'
    ))
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')
    ))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')

    pass
