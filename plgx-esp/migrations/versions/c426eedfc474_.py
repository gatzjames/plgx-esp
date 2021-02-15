"""empty message

Revision ID: c426eedfc474
Revises: 27ac66cfa860
Create Date: 2020-10-15 22:20:51.436752

"""

# revision identifiers, used by Alembic.
revision = 'c426eedfc474'
down_revision = '27ac66cfa860'

from alembic import op
import sqlalchemy as sa
import polylogyx.database
from sqlalchemy.dialects import postgresql


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('osquery_schema',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('platform', postgresql.ARRAY(sa.String()), nullable=False),
    sa.Column('schema', postgresql.JSONB(astext_type=sa.Text()), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('osquery_schema')
    # ### end Alembic commands ###