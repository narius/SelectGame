"""
Creares friends table
"""

from yoyo import step

__depends__ = {'20190615_03_5inYQ-adds-password-columns-to-user-table'}

steps = [
    step("""CREATE TABLE friends (
        id              SERIAL PRIMARY KEY,
        sender int references users(id),
        receiver int references users(id),
        friendship_status varchar,
        date_sent      date DEFAULT timezone('UTC'::text, now()),
        date_rejected      date,
        date_accepted      date
)""")
]
