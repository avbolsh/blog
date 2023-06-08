"""empty message

Revision ID: 34f61eb2bd42
Revises: 
Create Date: 2023-06-07 08:30:23.413307

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '34f61eb2bd42'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=140), nullable=True),
    sa.Column('slug', sa.String(length=140), nullable=True),
    sa.Column('body', sa.Text(), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('slug')
    )
    op.create_table('tag',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=140), nullable=True),
    sa.Column('slug', sa.String(length=140), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('slug')
    )
    op.create_table('posts_tags',
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.Column('tag_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tag.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('posts_tags')
    op.drop_table('tag')
    op.drop_table('post')
    # ### end Alembic commands ###