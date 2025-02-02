"""initial commit, again..

Revision ID: 34c85795e3b3
Revises: 
Create Date: 2020-08-24 16:58:44.358184

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '34c85795e3b3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('use_in_budget', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_category'))
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_user'))
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_user_username'), ['username'], unique=True)

    op.create_table('transaction',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('account_id', sa.String(length=64), nullable=True),
    sa.Column('transaction_id', sa.String(length=250), nullable=True),
    sa.Column('transaction_date', sa.Date(), nullable=True),
    sa.Column('amount', sa.Float(), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.Column('description', sa.String(length=250), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], name=op.f('fk_transaction_category_id_category')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_transaction'))
    )
    with op.batch_alter_table('transaction', schema=None) as batch_op:
        batch_op.create_index('account_id_transaction_id', ['account_id', 'transaction_id'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('transaction', schema=None) as batch_op:
        batch_op.drop_index('account_id_transaction_id')

    op.drop_table('transaction')
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_user_username'))

    op.drop_table('user')
    op.drop_table('category')
    # ### end Alembic commands ###
