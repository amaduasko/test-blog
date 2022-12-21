"""create users table

Revision ID: 636d10dac8c6
Revises: 
Create Date: 2022-12-20 19:19:44.202771

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '636d10dac8c6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
            'roles',
            sa.Column('id', sa.INT, primary_key=True),
            sa.Column('name', sa.VARCHAR(50), nullable=False)
        )
    op.create_table(
            'users',
            sa.Column('id', sa.BIGINT, primary_key=True),
            sa.Column('fio', sa.TEXT, nullable=False),
            sa.Column('datar', sa.DATE),
            sa.Column('id_role',sa.INT, sa.ForeignKey("roles.id")),
            sa.Column('created_on', sa.DATE),
        )
    
    op.execute("INSERT INTO roles(id,name) VALUES (1,'Грузчик'),(2,'Дворник') ")
    pass


def downgrade() -> None:
    op.drop_table('roles')
    op.drop_table('users')
    pass
