"""
Game library
"""

from yoyo import step

__depends__ = {'20190707_01_JVd8l-new-game-rating'}

steps = [
    step(""" 
-- This script only contains the table creation statements and does not fully represent the table in the database. It's still missing: indices, triggers. Do not use it as a backup.

-- Sequence and defined type
CREATE SEQUENCE IF NOT EXISTS game_library_id_seq;

-- Table Definition
CREATE TABLE "public"."game_library" (
    "id" int4 NOT NULL DEFAULT nextval('game_library_id_seq'::regclass),
    "user_id" int4 NOT NULL,
    "game_id" int4 NOT NULL,
    CONSTRAINT "game_library_user_id_fkey" FOREIGN KEY ("user_id") REFERENCES "public"."users"("id"),
    CONSTRAINT "game_library_game_id_fkey" FOREIGN KEY ("game_id") REFERENCES "public"."game"("id"),
    PRIMARY KEY ("id")
);""")
]
