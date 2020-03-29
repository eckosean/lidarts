"""empty message

Revision ID: 9f8355316c4d
Revises: 3f1057c5e16e
Create Date: 2020-03-28 18:53:01.440048

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9f8355316c4d'
down_revision = '3f1057c5e16e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('x01_presettings', sa.Column('public_challenge', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('x01_presettings', 'public_challenge')
    # ### end Alembic commands ###