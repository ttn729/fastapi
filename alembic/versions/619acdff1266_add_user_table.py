"""add user table

Revision ID: 619acdff1266
Revises: b107847f879c
Create Date: 2023-07-23 18:24:33.816655

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '619acdff1266'
down_revision = 'b107847f879c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email'))
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
