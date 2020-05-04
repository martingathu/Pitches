"""Add password

Revision ID: 2701d19344eb
Revises: 2dd321a3252b
Create Date: 2020-05-04 16:31:28.053859

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2701d19344eb'
down_revision = '2dd321a3252b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password', sa.String(length=255), nullable=True))
    op.drop_column('users', 'pass_secure')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('pass_secure', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_column('users', 'password')
    # ### end Alembic commands ###
