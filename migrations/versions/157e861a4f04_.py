"""empty message

Revision ID: 157e861a4f04
Revises: 485ffc01d843
Create Date: 2022-07-01 16:36:15.742908

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '157e861a4f04'
down_revision = '485ffc01d843'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Students',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('firstName', sa.String(length=200), nullable=True),
    sa.Column('last_name', sa.String(length=200), nullable=True),
    sa.Column('student_email', sa.String(length=200), nullable=True),
    sa.Column('matric_no', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_Students_firstName'), 'Students', ['firstName'], unique=False)
    op.create_index(op.f('ix_Students_last_name'), 'Students', ['last_name'], unique=False)
    op.create_index(op.f('ix_Students_matric_no'), 'Students', ['matric_no'], unique=False)
    op.drop_index('ix_students_firstName', table_name='students')
    op.drop_index('ix_students_last_name', table_name='students')
    op.drop_index('ix_students_matric_no', table_name='students')
    op.drop_table('students')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('students',
    sa.Column('id', postgresql.UUID(), autoincrement=False, nullable=False),
    sa.Column('firstName', sa.VARCHAR(length=200), autoincrement=False, nullable=True),
    sa.Column('last_name', sa.VARCHAR(length=200), autoincrement=False, nullable=True),
    sa.Column('student_email', sa.VARCHAR(length=200), autoincrement=False, nullable=True),
    sa.Column('matric_no', sa.VARCHAR(length=200), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='students_pkey')
    )
    op.create_index('ix_students_matric_no', 'students', ['matric_no'], unique=False)
    op.create_index('ix_students_last_name', 'students', ['last_name'], unique=False)
    op.create_index('ix_students_firstName', 'students', ['firstName'], unique=False)
    op.drop_index(op.f('ix_Students_matric_no'), table_name='Students')
    op.drop_index(op.f('ix_Students_last_name'), table_name='Students')
    op.drop_index(op.f('ix_Students_firstName'), table_name='Students')
    op.drop_table('Students')
    # ### end Alembic commands ###