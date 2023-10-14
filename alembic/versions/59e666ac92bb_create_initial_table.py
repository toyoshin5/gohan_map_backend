"""create initial table

Revision ID: 59e666ac92bb
Revises: 
Create Date: 2023-10-14 14:53:25.186754

"""
from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "59e666ac92bb"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "anonymous_post",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("user_id", sa.String(length=200), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        comment="Swipe UIに使用する匿名投稿用のテーブル",
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("anonymous_post")
    # ### end Alembic commands ###
