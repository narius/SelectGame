"""
Make game categories nullable
"""

from yoyo import step

__depends__ = {'20190702_02_TmK2Z-creates-game-game-rating-roles-roles-users'}

steps = [
    step("ALTER TABLE game ALTER COLUMN categories DROP NOT NULL;")
]
