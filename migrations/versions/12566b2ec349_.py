"""empty message

Revision ID: 12566b2ec349
Revises: 31430f5e8390
Create Date: 2022-07-01 17:57:00.827469

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '12566b2ec349'
down_revision = '31430f5e8390'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admins_table',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('first_name', sa.String(length=200), nullable=True),
    sa.Column('last_name', sa.String(length=200), nullable=True),
    sa.Column('password_hash', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_admins_table_first_name'), 'admins_table', ['first_name'], unique=False)
    op.create_index(op.f('ix_admins_table_last_name'), 'admins_table', ['last_name'], unique=False)
    op.drop_index('ix_Admins_first_name', table_name='Admins')
    op.drop_index('ix_Admins_last_name', table_name='Admins')
    op.drop_table('Admins')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Admins',
    sa.Column('id', postgresql.UUID(), autoincrement=False, nullable=False),
    sa.Column('first_name', sa.VARCHAR(length=200), autoincrement=False, nullable=True),
    sa.Column('last_name', sa.VARCHAR(length=200), autoincrement=False, nullable=True),
    sa.Column('password_hash', sa.VARCHAR(length=200), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='Admins_pkey')
    )
    op.create_index('ix_Admins_last_name', 'Admins', ['last_name'], unique=False)
    op.create_index('ix_Admins_first_name', 'Admins', ['first_name'], unique=False)
    op.drop_index(op.f('ix_admins_table_last_name'), table_name='admins_table')
    op.drop_index(op.f('ix_admins_table_first_name'), table_name='admins_table')
    op.drop_table('admins_table')
    # ### end Alembic commands ###