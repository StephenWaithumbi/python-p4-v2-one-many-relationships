"""Initial migration

Revision ID: e00d19efaccd
Revises: 
Create Date: 2025-01-19 17:29:59.129042

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e00d19efaccd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('employees',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('hire_date', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('onboardings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('orientation', sa.DateTime(), nullable=True),
    sa.Column('forms_complete', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('reviews',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.Column('summary', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reviews')
    op.drop_table('onboardings')
    op.drop_table('employees')
    # ### end Alembic commands ###
