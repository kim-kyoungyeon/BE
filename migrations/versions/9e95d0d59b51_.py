"""empty message

Revision ID: 9e95d0d59b51
Revises: 898466442e99
Create Date: 2024-09-17 12:38:12.817072

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9e95d0d59b51'
down_revision = '898466442e99'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('departments', schema=None) as batch_op:
        batch_op.add_column(sa.Column('trainings', sa.String(length=255), nullable=True))
        batch_op.alter_column('dept_target',
               existing_type=sa.VARCHAR(length=255),
               type_=sa.Text(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('departments', schema=None) as batch_op:
        batch_op.alter_column('dept_target',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=255),
               existing_nullable=True)
        batch_op.drop_column('trainings')

    # ### end Alembic commands ###
