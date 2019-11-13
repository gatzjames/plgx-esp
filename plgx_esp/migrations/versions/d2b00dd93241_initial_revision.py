"""Initial revision for migrations going forward.

Revision ID: d2b00dd93241
Revises: None
Create Date: 2016-05-01 09:57:32.779107

"""

# revision identifiers, used by Alembic.
revision = 'd2b00dd93241'
down_revision = None

from alembic import op
import sqlalchemy as sa
import polylogyx.database
from sqlalchemy.dialects import postgresql


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###

    op.create_table('file_path',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('category', sa.String(), nullable=False),
                    sa.Column('target_paths', sa.String(), nullable=True),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('category')
                    )

    op.create_table('node_config',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(), nullable=True, unique=True),
                    sa.Column('type', sa.String(), nullable=True),
                    sa.Column('config', sa.String(), nullable=True),
                    sa.Column('apply_by_default', sa.Boolean(), nullable=True),

                    sa.Column('created_at', sa.DateTime(), nullable=True),
                    sa.Column('updated_at', sa.DateTime(), nullable=True),
                    sa.PrimaryKeyConstraint('id'), )
    op.create_table('options',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(), nullable=False, unique=True),
                    sa.Column('option', sa.String(), nullable=True),
                    sa.Column('created_at', sa.DateTime(), nullable=True),
                    sa.Column('updated_at', sa.DateTime(), nullable=True),
                    sa.PrimaryKeyConstraint('id'), )
    op.create_table('settings',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(), nullable=False, unique=True),
                    sa.Column('setting', sa.String(), nullable=True),
                    sa.Column('created_at', sa.DateTime(), nullable=True),
                    sa.Column('updated_at', sa.DateTime(), nullable=True),
                    sa.PrimaryKeyConstraint('id'), )
    op.create_table('node',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('os_info', postgresql.JSONB(), nullable=False),
                    sa.Column('network_info', postgresql.JSONB(), nullable=False),

                    sa.Column('node_key', sa.String(), nullable=False),
                    sa.Column('platform', sa.String(), nullable=True),
                    sa.Column('enroll_secret', sa.String(), nullable=True),
                    sa.Column('enrolled_on', sa.DateTime(), nullable=True),
                    sa.Column('host_identifier', sa.String(), nullable=True),
                    sa.Column('last_checkin', sa.DateTime(), nullable=True),
                    sa.Column('last_results_update_date', sa.DateTime(), nullable=True),
                    sa.Column('last_results_seen_date', sa.DateTime(), nullable=True),

                    sa.Column('config_id', sa.Integer(), nullable=True),
                    sa.PrimaryKeyConstraint('id'),
                    sa.ForeignKeyConstraint(['config_id'], ['node_config.id'], ),
                    sa.UniqueConstraint('node_key')
                    )

    op.create_table('alerts',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('message', postgresql.JSONB(), nullable=False),
                    sa.Column('sql', sa.String(), nullable=True),
                    sa.Column('query_name', sa.String(), nullable=True),
                    sa.Column('created_at', sa.DateTime(), nullable=False),
                    sa.Column('node_id', sa.Integer(), nullable=False),
                    sa.Column('message', postgresql.JSONB(), nullable=False),

                    sa.ForeignKeyConstraint(['node_id'], ['node.id'], ),

                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('pack',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.Column('platform', sa.String(), nullable=True),
                    sa.Column('version', sa.String(), nullable=True),
                    sa.Column('description', sa.String(), nullable=True),
                    sa.Column('shard', sa.Integer(), nullable=True),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('name')
                    )
    op.create_table('query',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.Column('sql', sa.String(), nullable=False),
                    sa.Column('interval', sa.Integer(), nullable=True),
                    sa.Column('platform', sa.String(), nullable=True),
                    sa.Column('version', sa.String(), nullable=True),
                    sa.Column('description', sa.String(), nullable=True),
                    sa.Column('value', sa.String(), nullable=True),
                    sa.Column('removed', sa.Boolean(), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('tag',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('value', sa.String(), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('value')
                    )
    op.create_table('distributed_query',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('guid', sa.String(), nullable=False),
                    sa.Column('status', sa.Integer(), nullable=False),
                    sa.Column('sql', sa.String(), nullable=False),
                    sa.Column('timestamp', sa.DateTime(), nullable=True),
                    sa.Column('not_before', sa.DateTime(), nullable=True),
                    sa.Column('retrieved', sa.DateTime(), nullable=True),
                    sa.Column('node_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['node_id'], ['node.id'], ),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('guid')
                    )
    op.create_table('file_path_tags',
                    sa.Column('tag.id', sa.Integer(), nullable=True),
                    sa.Column('file_path.id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['file_path.id'], ['file_path.id'], ),
                    sa.ForeignKeyConstraint(['tag.id'], ['tag.id'], )
                    )
    op.create_table('node_tags',
                    sa.Column('tag.id', sa.Integer(), nullable=True),
                    sa.Column('node.id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['node.id'], ['node.id'], ),
                    sa.ForeignKeyConstraint(['tag.id'], ['tag.id'], )
                    )
    op.create_table('pack_tags',
                    sa.Column('tag.id', sa.Integer(), nullable=True),
                    sa.Column('pack.id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['pack.id'], ['pack.id'], ),
                    sa.ForeignKeyConstraint(['tag.id'], ['tag.id'], )
                    )
    op.create_table('query_packs',
                    sa.Column('pack.id', sa.Integer(), nullable=True),
                    sa.Column('query.id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['pack.id'], ['pack.id'], ),
                    sa.ForeignKeyConstraint(['query.id'], ['query.id'], )
                    )
    op.create_table('query_tags',
                    sa.Column('tag.id', sa.Integer(), nullable=True),
                    sa.Column('query.id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['query.id'], ['query.id'], ),
                    sa.ForeignKeyConstraint(['tag.id'], ['tag.id'], )
                    )
    op.create_table('result_log',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.Column('timestamp', sa.DateTime(), nullable=True),
                    sa.Column('action', sa.String(), nullable=True),
                    sa.Column('columns', postgresql.JSONB(), nullable=True),
                    sa.Column('node_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['node_id'], ['node.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('status_log',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('line', sa.Integer(), nullable=True),
                    sa.Column('message', sa.String(), nullable=True),
                    sa.Column('severity', sa.Integer(), nullable=True),
                    sa.Column('filename', sa.String(), nullable=True),
                    sa.Column('created', sa.DateTime(), nullable=True),
                    sa.Column('node_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['node_id'], ['node.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('distributed_query_result',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('columns', postgresql.JSONB(), nullable=True),
                    sa.Column('timestamp', sa.DateTime(), nullable=True),
                    sa.Column('distributed_query_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['distributed_query_id'], ['distributed_query.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    ### end Alembic commands ###

    op.create_table('email_recipient',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('recipient', sa.String(), nullable=False),
                    sa.Column('status', sa.String(), nullable=True),
                    sa.Column('created_at', sa.DateTime(), nullable=True),
                    sa.Column('updated_at', sa.DateTime(), nullable=True),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('recipient')
                    )

    op.create_table('carve_session',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('session_id', sa.String(), nullable=True),
                    sa.Column('carve_guid', sa.String(), nullable=True),
                    sa.Column('archive', sa.String(), nullable=True),

                    sa.Column('carve_size', sa.Integer(), nullable=True),
                    sa.Column('block_size', sa.Integer(), nullable=True),

                    sa.Column('block_count', sa.Integer(), nullable=True),
                    sa.Column('created_at', sa.DateTime(), nullable=False),
                    sa.Column('created_at', sa.DateTime(), nullable=False),

                    sa.Column('node_id', sa.Integer(), nullable=False),

                    sa.ForeignKeyConstraint(['node_id'], ['node.id'], ),

                    sa.PrimaryKeyConstraint('id')
                    )

    op.create_table('node_data',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.Column('data', postgresql.JSONB(), nullable=True),
                    sa.Column('node_id', sa.Integer(), nullable=False),

                    sa.ForeignKeyConstraint(['node_id'], ['node.id'], ),
                    sa.Column('created_at', sa.DateTime(), nullable=False),
                    sa.Column('updated_at', sa.DateTime(), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    )





    def downgrade():
        ### commands auto generated by Alembic - please adjust! ###
        op.drop_table('distributed_query_result')
        op.drop_table('status_log')
        op.drop_table('result_log')
        op.drop_table('query_tags')
        op.drop_table('query_packs')
        op.drop_table('pack_tags')
        op.drop_table('node_tags')
        op.drop_table('file_path_tags')
        op.drop_table('distributed_query')
        op.drop_table('tag')
        op.drop_table('query')
        op.drop_table('pack')
        op.drop_table('node')
        op.drop_table('file_path')

        op.drop_table('alerts')
        ### end Alembic commands ###