"""empty message

Revision ID: 6b5881fedb30
Revises: 
Create Date: 2021-04-06 00:23:24.476649

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6b5881fedb30'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('country',
                    sa.Column('id', sa.String(length=50), nullable=False),
                    sa.Column('object_id', sa.String(
                        length=50), nullable=True),
                    sa.Column('name', sa.VARCHAR(length=100), nullable=True),
                    sa.Column('remark', sa.String(length=50), nullable=True),
                    sa.Column('created_date', sa.BIGINT(), nullable=True),
                    sa.Column('updated_date', sa.BIGINT(), nullable=True),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('name')
                    )
    op.create_index(op.f('ix_country_id'), 'country', ['id'], unique=False)
    op.create_index(op.f('ix_country_object_id'),
                    'country', ['object_id'], unique=True)
    op.create_table('state',
                    sa.Column('id', sa.String(length=50), nullable=False),
                    sa.Column('object_id', sa.String(
                        length=50), nullable=True),
                    sa.Column('name_mm_uni', sa.String(
                        length=50), nullable=True),
                    sa.Column('name_mm_zawgyi', sa.String(
                        length=50), nullable=True),
                    sa.Column('country_id', sa.String(
                        length=255), nullable=True),
                    sa.Column('created_date', sa.BIGINT(), nullable=True),
                    sa.Column('updated_date', sa.BIGINT(), nullable=True),
                    sa.ForeignKeyConstraint(
                        ['country_id'], ['country.object_id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_state_id'), 'state', ['id'], unique=False)
    op.create_index(op.f('ix_state_object_id'),
                    'state', ['object_id'], unique=True)
    op.create_table('day',
                    sa.Column('id', sa.String(length=50), nullable=False),
                    sa.Column('object_id', sa.String(
                        length=50), nullable=True),
                    sa.Column('day', sa.Integer(), nullable=True),
                    sa.Column('day_mm', sa.String(length=10), nullable=True),
                    sa.Column('sehri_time_desc_mm_uni',
                              sa.String(length=30), nullable=True),
                    sa.Column('sehri_time_desc_mm_zawgyi',
                              sa.String(length=30), nullable=True),
                    sa.Column('iftari_time_desc_mm_zawgyi',
                              sa.String(length=30), nullable=True),
                    sa.Column('iftari_time_desc_mm_uni',
                              sa.String(length=30), nullable=True),
                    sa.Column('dua_ar', sa.String(length=1000), nullable=True),
                    sa.Column('dua_mm_uni', sa.String(
                        length=2000), nullable=True),
                    sa.Column('dua_mm_zawgyi', sa.String(
                        length=2000), nullable=True),
                    sa.Column('calendar_day', sa.String(
                        length=30), nullable=True),
                    sa.Column('hijari_day', sa.String(
                        length=30), nullable=True),
                    sa.Column('sehri_time_desc', sa.String(
                        length=30), nullable=True),
                    sa.Column('iftari_time_desc', sa.String(
                        length=30), nullable=True),
                    sa.Column('dua_en', sa.String(length=1000), nullable=True),
                    sa.Column('sehri_time', sa.String(
                        length=30), nullable=True),
                    sa.Column('iftari_time', sa.String(
                        length=30), nullable=True),
                    sa.Column('is_kadir', sa.Boolean(), nullable=True),
                    sa.Column('is_Eid', sa.Boolean(), nullable=True),
                    sa.Column('country_id', sa.String(
                        length=255), nullable=True),
                    sa.Column('state_id', sa.String(
                        length=255), nullable=True),
                    sa.Column('created_date', sa.BIGINT(), nullable=True),
                    sa.Column('updated_date', sa.BIGINT(), nullable=True),
                    sa.ForeignKeyConstraint(
                        ['country_id'], ['country.object_id'], ),
                    sa.ForeignKeyConstraint(
                        ['state_id'], ['state.object_id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_day_country_id'), 'day',
                    ['country_id'], unique=False)
    op.create_index(op.f('ix_day_id'), 'day', ['id'], unique=False)
    op.create_index(op.f('ix_day_object_id'), 'day',
                    ['object_id'], unique=True)
    op.create_index(op.f('ix_day_state_id'), 'day', ['state_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_day_state_id'), table_name='day')
    op.drop_index(op.f('ix_day_object_id'), table_name='day')
    op.drop_index(op.f('ix_day_id'), table_name='day')
    op.drop_index(op.f('ix_day_country_id'), table_name='day')
    op.drop_table('day')
    op.drop_index(op.f('ix_state_object_id'), table_name='state')
    op.drop_index(op.f('ix_state_id'), table_name='state')
    op.drop_table('state')
    op.drop_index(op.f('ix_country_object_id'), table_name='country')
    op.drop_index(op.f('ix_country_id'), table_name='country')
    op.drop_table('country')
    # ### end Alembic commands ###
