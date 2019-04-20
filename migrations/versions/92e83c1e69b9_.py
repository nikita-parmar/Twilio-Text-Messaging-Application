"""empty message

Revision ID: 92e83c1e69b9
Revises: 
Create Date: 2019-04-08 18:12:18.474300

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '92e83c1e69b9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('keywords',
    sa.Column('key', sa.String(), nullable=False),
    sa.Column('correct_resp', sa.String(), nullable=True),
    sa.Column('incorrect_resp', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('key')
    )
    op.create_table('numbers',
    sa.Column('number', sa.String(length=15), nullable=False),
    sa.PrimaryKeyConstraint('number')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('numbers')
    op.drop_table('keywords')
    # ### end Alembic commands ###
