"""empty message

Revision ID: c12c89ea65c4
Revises: 6910676c8735
Create Date: 2022-07-01 17:32:58.238142

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c12c89ea65c4'
down_revision = '6910676c8735'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('admins', sa.Column('first_name', sa.String(length=200), nullable=True))
    op.drop_index('ix_admins_firstName', table_name='admins')
    op.create_index(op.f('ix_admins_first_name'), 'admins', ['first_name'], unique=False)
    op.drop_column('admins', 'firstName')
    op.add_column('students', sa.Column('first_name', sa.String(length=200), nullable=True))
    op.drop_index('ix_students_firstName', table_name='students')
    op.create_index(op.f('ix_students_first_name'), 'students', ['first_name'], unique=False)
    op.drop_column('students', 'firstName')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('students', sa.Column('firstName', sa.VARCHAR(length=200), autoincrement=False, nullable=True))
    op.drop_index(op.f('ix_students_first_name'), table_name='students')
    op.create_index('ix_students_firstName', 'students', ['firstName'], unique=False)
    op.drop_column('students', 'first_name')
    op.add_column('admins', sa.Column('firstName', sa.VARCHAR(length=200), autoincrement=False, nullable=True))
    op.drop_index(op.f('ix_admins_first_name'), table_name='admins')
    op.create_index('ix_admins_firstName', 'admins', ['firstName'], unique=False)
    op.drop_column('admins', 'first_name')
    # ### end Alembic commands ###
