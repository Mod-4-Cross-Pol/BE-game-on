"""empty message

Revision ID: ffcd3d4964cd
Revises: a6a385f05ea9
Create Date: 2020-04-13 17:31:50.110948

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ffcd3d4964cd'
down_revision = 'a6a385f05ea9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('events', sa.Column('skill_level', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('events', 'skill_level')
    # ### end Alembic commands ###
