"""empty message

Revision ID: 3d6cf41c8d90
Revises: 
Create Date: 2019-07-13 15:36:22.801273

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3d6cf41c8d90'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('leads',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('first_name', sa.String(), nullable=False),
    sa.Column('last_name', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('phone', sa.String(), nullable=True),
    sa.Column('experience', sa.String(), nullable=True),
    sa.Column('qualification', sa.String(), nullable=True),
    sa.Column('address', sa.String(), nullable=True),
    sa.Column('landmark', sa.String(), nullable=True),
    sa.Column('gender', sa.String(), nullable=True),
    sa.Column('date_of_birth', sa.DateTime(), nullable=True),
    sa.Column('college_name', sa.String(), nullable=True),
    sa.Column('referral', sa.String(), nullable=True),
    sa.Column('resume', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('phone')
    )
    op.create_index(op.f('ix_leads_id'), 'leads', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_leads_id'), table_name='leads')
    op.drop_table('leads')
    # ### end Alembic commands ###
