"""init

Revision ID: 98e09689d4d9
Revises: 
Create Date: 2022-01-05 23:00:34.063133

"""
from alembic import op
import sqlmodel
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '98e09689d4d9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('period',
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('start_time', sa.Time(), nullable=False),
    sa.Column('end_time', sa.Time(), nullable=False),
    sa.Column('id', sqlmodel.sql.sqltypes.GUID(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('role',
    sa.Column('permissions', sa.JSON(), nullable=True),
    sa.Column('ar_name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('en_name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('id', sqlmodel.sql.sqltypes.GUID(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('type', sa.Enum('employee', 'teacher', 'teacher_employee', 'student', 'other', name='usertype'), nullable=True),
    sa.Column('gender', sa.Enum('male', 'female', name='usergender'), nullable=True),
    sa.Column('scrape_from', sa.Enum('uot', 'asc', 'uot_asc', name='userscrapefrom'), nullable=True),
    sa.Column('id', sqlmodel.sql.sqltypes.GUID(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('color', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('en_name', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('email', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('uot_url', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('image', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('asc_job_title', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('asc_name', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('role_id', sqlmodel.sql.sqltypes.GUID(), nullable=True),
    sa.Column('hashed_password', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['role.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_index(op.f('ix_user_en_name'), 'user', ['en_name'], unique=False)
    op.create_index(op.f('ix_user_name'), 'user', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_name'), table_name='user')
    op.drop_index(op.f('ix_user_en_name'), table_name='user')
    op.drop_table('user')
    op.drop_table('role')
    op.drop_table('period')
    # ### end Alembic commands ###
