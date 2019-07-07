"""
new game_rating
"""

from yoyo import step

__depends__ = {'20190704_01_5zbkY-make-game-categories-nullable'}

steps = [
    step("""-- This script only contains the table creation statements and does not fully represent the table in the database. It's still missing: indices, triggers. Do not use it as a backup.

-- Sequence and defined type
CREATE SEQUENCE IF NOT EXISTS game_rating_id_seq;

-- Table Definition
CREATE TABLE "public"."game_rating" (
    "id" int4 NOT NULL DEFAULT nextval('game_rating_id_seq'::regclass),
    "user_id" int4 NOT NULL,
    "rating" int4 NOT NULL DEFAULT 0,
    "game_id" int4 NOT NULL,
    CONSTRAINT "game_rating_user_id_fkey" FOREIGN KEY ("user_id") REFERENCES "public"."users"("id") ON DELETE CASCADE,
    CONSTRAINT "game_rating_game_id_fkey" FOREIGN KEY ("game_id") REFERENCES "public"."game"("id"),
    PRIMARY KEY ("id")
);""")
]
