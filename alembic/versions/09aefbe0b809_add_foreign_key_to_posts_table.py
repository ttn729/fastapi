"""add foreign key to posts table

Revision ID: 09aefbe0b809
Revises: 619acdff1266
Create Date: 2023-07-23 18:35:15.525743

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '09aefbe0b809'
down_revision = '619acdff1266'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users",
                          local_cols=['owner_id'], remote_cols=['id'], ondelete='CASCADE')
    pass


def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
