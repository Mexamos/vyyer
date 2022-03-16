"""Add Identities table

Revision ID: 474fc6acd35c
Revises: 076b9fa96466
Create Date: 2022-03-16 17:59:59.854994

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '474fc6acd35c'
down_revision = '076b9fa96466'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('identities',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('user_ids', sa.JSON(), nullable=True),
    sa.Column('ban', mysql.INTEGER(display_width=1), nullable=True),
    sa.Column('start', sa.TIMESTAMP(), nullable=True),
    sa.Column('end', sa.TIMESTAMP(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('identities')
    # ### end Alembic commands ###