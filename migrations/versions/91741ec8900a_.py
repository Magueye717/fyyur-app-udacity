"""empty message

Revision ID: 91741ec8900a
Revises: f198558bb3cd
Create Date: 2022-08-20 21:23:57.797010

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '91741ec8900a'
down_revision = 'f198558bb3cd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('artists', sa.Column('website_link', sa.String(length=120), nullable=True))
    op.drop_column('artists', 'website')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('artists', sa.Column('website', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
    op.drop_column('artists', 'website_link')
    # ### end Alembic commands ###