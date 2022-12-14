"""empty message

Revision ID: 0af2c2e286a7
Revises: a20aeb9b0eac
Create Date: 2020-12-13 19:20:18.250786

"""
import sqlalchemy_utils
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0af2c2e286a7'
down_revision = 'a20aeb9b0eac'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('can_use_coinbase', sa.Boolean(), server_default='0', nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'can_use_coinbase')
    # ### end Alembic commands ###
