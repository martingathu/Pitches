"""Initial Migration

Revision ID: 9753a4dfa1df
Revises: 843ed267ff31
Create Date: 2020-05-07 11:12:45.732731

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9753a4dfa1df'
down_revision = '843ed267ff31'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('comment', sa.Text(), nullable=True))
    op.drop_column('comments', 'description')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('description', sa.TEXT(), autoincrement=False, nullable=True))
    op.drop_column('comments', 'comment')
    # ### end Alembic commands ###