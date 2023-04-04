"""Initial migration

Revision ID: 455ffe80fc27
Revises: 
Create Date: 2023-04-04 21:28:30.938463

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '455ffe80fc27'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('author',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('bio', sa.String(length=600), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_author_id'), 'author', ['id'], unique=False)
    op.create_index(op.f('ix_author_name'), 'author', ['name'], unique=True)
    op.create_table('book',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('summary', sa.String(length=600), nullable=False),
    sa.Column('publication_date', sa.Date(), nullable=False),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['author.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_book_id'), 'book', ['id'], unique=False)
    op.create_index(op.f('ix_book_title'), 'book', ['title'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_book_title'), table_name='book')
    op.drop_index(op.f('ix_book_id'), table_name='book')
    op.drop_table('book')
    op.drop_index(op.f('ix_author_name'), table_name='author')
    op.drop_index(op.f('ix_author_id'), table_name='author')
    op.drop_table('author')
    # ### end Alembic commands ###