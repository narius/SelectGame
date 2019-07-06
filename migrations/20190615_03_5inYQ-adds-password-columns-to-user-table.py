"""
Adds password columns to user table
"""

from yoyo import step

__depends__ = {'20190615_02_PzAXJ-create-regisration-code-table'}

steps = [
    step("ALTER TABLE users ADD COLUMN password VARCHAR")
]
