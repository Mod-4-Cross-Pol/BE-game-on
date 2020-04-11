"""empty message

Revision ID: a6a385f05ea9
Revises: 
Create Date: 2020-04-11 19:24:09.728065

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a6a385f05ea9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('events',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('start_time', sa.String(), nullable=True),
    sa.Column('duration', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('location', sa.String(), nullable=True),
    sa.Column('lat_long', sa.String(), nullable=True),
    sa.Column('current_participant_count', sa.Integer(), nullable=True),
    sa.Column('max_participant_count', sa.Integer(), nullable=True),
    sa.Column('activity', sa.String(), nullable=True),
    sa.Column('equipment', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('events')
    # ### end Alembic commands ###
