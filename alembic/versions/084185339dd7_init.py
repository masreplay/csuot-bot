"""init

Revision ID: 084185339dd7
Revises: 
Create Date: 2022-01-16 22:14:37.727891

"""
from alembic import op
import sqlmodel
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '084185339dd7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('building',
    sa.Column('lng', sa.Float(), nullable=True),
    sa.Column('lat', sa.Float(), nullable=True),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('color', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('id', sqlmodel.sql.sqltypes.GUID(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_building_name'), 'building', ['name'], unique=False)
    op.create_table('day',
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('id', sqlmodel.sql.sqltypes.GUID(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('department',
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('en_name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('abbr', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('vision', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('id', sqlmodel.sql.sqltypes.GUID(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('floor',
    sa.Column('id', sqlmodel.sql.sqltypes.GUID(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('job_title',
    sa.Column('type', sa.Enum('employee', 'teacher', 'student', 'other', name='usertype'), nullable=True),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('en_name', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('id', sqlmodel.sql.sqltypes.GUID(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
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
    op.create_table('subject',
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('color', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('id', sqlmodel.sql.sqltypes.GUID(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_subject_name'), 'subject', ['name'], unique=False)
    op.create_table('branch',
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('en_name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('abbr', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('vision', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('department_id', sqlmodel.sql.sqltypes.GUID(), nullable=True),
    sa.Column('id', sqlmodel.sql.sqltypes.GUID(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['department_id'], ['department.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('room',
    sa.Column('type', sa.Enum('classroom', 'employee', 'other', name='roomtype'), nullable=True),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('color', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('building_id', sqlmodel.sql.sqltypes.GUID(), nullable=True),
    sa.Column('floor_id', sqlmodel.sql.sqltypes.GUID(), nullable=True),
    sa.Column('id', sqlmodel.sql.sqltypes.GUID(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['building_id'], ['building.id'], ),
    sa.ForeignKeyConstraint(['floor_id'], ['floor.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_room_name'), 'room', ['name'], unique=False)
    op.create_table('user',
    sa.Column('gender', sa.Enum('male', 'female', name='usergender'), nullable=True),
    sa.Column('scrape_from', sa.Enum('uot', 'asc', 'uot_asc', name='userscrapefrom'), nullable=True),
    sa.Column('id', sqlmodel.sql.sqltypes.GUID(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('color', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
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
    op.create_table('ascversion',
    sa.Column('created_by', sqlmodel.sql.sqltypes.GUID(), nullable=False),
    sa.Column('file_name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('id', sqlmodel.sql.sqltypes.GUID(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['created_by'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('lesson',
    sa.Column('subject_id', sqlmodel.sql.sqltypes.GUID(), nullable=True),
    sa.Column('teacher_id', sqlmodel.sql.sqltypes.GUID(), nullable=True),
    sa.Column('id', sqlmodel.sql.sqltypes.GUID(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['subject_id'], ['subject.id'], ),
    sa.ForeignKeyConstraint(['teacher_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('stage',
    sa.Column('shift', sa.Enum('morning', 'evening', 'both', name='collageshifts'), nullable=True),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('level', sa.Integer(), nullable=True),
    sa.Column('branch_id', sqlmodel.sql.sqltypes.GUID(), nullable=True),
    sa.Column('id', sqlmodel.sql.sqltypes.GUID(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['branch_id'], ['branch.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_stage_level'), 'stage', ['level'], unique=False)
    op.create_table('user_job_title',
    sa.Column('job_title_id', sqlmodel.sql.sqltypes.GUID(), nullable=True),
    sa.Column('user_id', sqlmodel.sql.sqltypes.GUID(), nullable=True),
    sa.ForeignKeyConstraint(['job_title_id'], ['job_title.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('job_title_id', 'user_id')
    )
    op.create_table('card',
    sa.Column('period_id', sqlmodel.sql.sqltypes.GUID(), nullable=False),
    sa.Column('day_id', sqlmodel.sql.sqltypes.GUID(), nullable=False),
    sa.Column('lesson_id', sqlmodel.sql.sqltypes.GUID(), nullable=False),
    sa.Column('id', sqlmodel.sql.sqltypes.GUID(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['day_id'], ['day.id'], ),
    sa.ForeignKeyConstraint(['lesson_id'], ['lesson.id'], ),
    sa.ForeignKeyConstraint(['period_id'], ['period.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('period_id', 'day_id', 'lesson_id', name='card_ids')
    )
    op.create_table('stage_lesson',
    sa.Column('lesson_id', sqlmodel.sql.sqltypes.GUID(), nullable=True),
    sa.Column('stage_id', sqlmodel.sql.sqltypes.GUID(), nullable=True),
    sa.ForeignKeyConstraint(['lesson_id'], ['lesson.id'], ),
    sa.ForeignKeyConstraint(['stage_id'], ['stage.id'], ),
    sa.PrimaryKeyConstraint('lesson_id', 'stage_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('stage_lesson')
    op.drop_table('card')
    op.drop_table('user_job_title')
    op.drop_index(op.f('ix_stage_level'), table_name='stage')
    op.drop_table('stage')
    op.drop_table('lesson')
    op.drop_table('ascversion')
    op.drop_index(op.f('ix_user_name'), table_name='user')
    op.drop_index(op.f('ix_user_en_name'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_room_name'), table_name='room')
    op.drop_table('room')
    op.drop_table('branch')
    op.drop_index(op.f('ix_subject_name'), table_name='subject')
    op.drop_table('subject')
    op.drop_table('role')
    op.drop_table('period')
    op.drop_table('job_title')
    op.drop_table('floor')
    op.drop_table('department')
    op.drop_table('day')
    op.drop_index(op.f('ix_building_name'), table_name='building')
    op.drop_table('building')
    # ### end Alembic commands ###
