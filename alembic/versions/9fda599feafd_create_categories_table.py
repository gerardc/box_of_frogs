"""create categories table

Revision ID: 9fda599feafd
Revises: 
Create Date: 2019-11-25 13:08:55.342753

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9fda599feafd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'categories',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('display_name', sa.String(50), nullable=False)
    )


def downgrade():
    op.drop_table('categories')
