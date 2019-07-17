"""
Create users table
"""

from yoyo import step

__depends__ = {}

steps = [
    step("""CREATE TABLE users (
  id              SERIAL PRIMARY KEY,
  username           VARCHAR(100) NOT NULL,
  firstname  VARCHAR(100) NULL,
  surname  VARCHAR(100) NULL,
  email  VARCHAR(100) NULL
)
""")
]
