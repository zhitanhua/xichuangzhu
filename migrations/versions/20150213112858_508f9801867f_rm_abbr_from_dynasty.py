"""Rm abbr from dynasty.

Revision ID: 508f9801867f
Revises: 51bcea7b942c
Create Date: 2015-02-13 11:28:58.513476

"""

# revision identifiers, used by Alembic.
revision = '508f9801867f'
down_revision = '51bcea7b942c'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql


def upgrade():
    # ## commands auto generated by Alembic - please adjust! ###
    op.drop_column('dynasty', 'abbr')
    # ## end Alembic commands ###


def downgrade():
    # ## commands auto generated by Alembic - please adjust! ###
    op.add_column('dynasty', sa.Column('abbr', mysql.VARCHAR(length=50), nullable=True))
    op.create_unique_constraint(u'abbr', 'dynasty', ['abbr'])
    # ## end Alembic commands ###
