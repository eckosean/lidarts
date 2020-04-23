"""empty message

Revision ID: e38a7a6adc5a
Revises: 377228bb1f36
Create Date: 2020-04-19 10:51:49.800149

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e38a7a6adc5a'
down_revision = '377228bb1f36'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('games_cricket',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('hashid', sa.String(length=10), nullable=True),
    sa.Column('bo_sets', sa.Integer(), nullable=False),
    sa.Column('bo_legs', sa.Integer(), nullable=False),
    sa.Column('two_clear_legs', sa.Boolean(), nullable=True),
    sa.Column('p1_sets', sa.Integer(), nullable=True),
    sa.Column('p2_sets', sa.Integer(), nullable=True),
    sa.Column('p1_legs', sa.Integer(), nullable=True),
    sa.Column('p2_legs', sa.Integer(), nullable=True),
    sa.Column('p1_next_turn', sa.Boolean(), nullable=True),
    sa.Column('closest_to_bull', sa.Boolean(), nullable=True),
    sa.Column('closest_to_bull_json', sa.JSON(), nullable=True),
    sa.Column('status', sa.String(length=20), nullable=True),
    sa.Column('type', sa.Integer(), nullable=True),
    sa.Column('match_json', sa.JSON(), nullable=True),
    sa.Column('begin', sa.DateTime(), nullable=True),
    sa.Column('end', sa.DateTime(), nullable=True),
    sa.Column('opponent_type', sa.String(length=10), nullable=True),
    sa.Column('public_challenge', sa.Boolean(), nullable=True),
    sa.Column('score_input_delay', sa.Integer(), nullable=True),
    sa.Column('webcam', sa.Boolean(), nullable=True),
    sa.Column('jitsi_hashid', sa.String(length=10), nullable=True),
    sa.Column('tournament', sa.String(length=10), nullable=True),
    sa.Column('player1', sa.Integer(), nullable=True),
    sa.Column('player2', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['player1'], ['users.id'], name=op.f('fk_games_cricket_player1_users')),
    sa.ForeignKeyConstraint(['player2'], ['users.id'], name=op.f('fk_games_cricket_player2_users')),
    sa.ForeignKeyConstraint(['tournament'], ['tournaments.hashid'], name=op.f('fk_games_cricket_tournament_tournaments')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_games_cricket')),
    sa.UniqueConstraint('hashid', name=op.f('uq_games_cricket_hashid')),
    sa.UniqueConstraint('jitsi_hashid', name=op.f('uq_games_cricket_jitsi_hashid'))
    )
    op.create_index(op.f('ix_games_cricket_player1'), 'games_cricket', ['player1'], unique=False)
    op.create_index(op.f('ix_games_cricket_player2'), 'games_cricket', ['player2'], unique=False)
    op.create_index(op.f('ix_games_cricket_status'), 'games_cricket', ['status'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_games_cricket_status'), table_name='games_cricket')
    op.drop_index(op.f('ix_games_cricket_player2'), table_name='games_cricket')
    op.drop_index(op.f('ix_games_cricket_player1'), table_name='games_cricket')
    op.drop_table('games_cricket')
    # ### end Alembic commands ###