"""empty message

Revision ID: f031a1ac2bc1
Revises: 6e9514db401f
Create Date: 2024-09-11 17:22:29.065541

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f031a1ac2bc1'
down_revision = '6e9514db401f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('trainings', schema=None) as batch_op:
        batch_op.alter_column('dept_target',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
        batch_op.alter_column('role_target',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('trainings', schema=None) as batch_op:
        batch_op.alter_column('role_target',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
        batch_op.alter_column('dept_target',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)

    # ### end Alembic commands ###