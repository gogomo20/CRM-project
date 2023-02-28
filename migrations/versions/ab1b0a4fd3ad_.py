"""empty message

Revision ID: ab1b0a4fd3ad
Revises: c0578658e445
Create Date: 2023-02-22 19:20:43.766723

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ab1b0a4fd3ad'
down_revision = 'c0578658e445'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('usuarios',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nome', sa.String(length=84), nullable=False),
    sa.Column('email', sa.String(length=84), nullable=False),
    sa.Column('senha', sa.String(length=128), nullable=False),
    sa.Column('classe', sa.String(length=1), server_default='F', nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('usuarios')
    # ### end Alembic commands ###