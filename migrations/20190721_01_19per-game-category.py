"""
game_category
"""

from yoyo import step

__depends__ = {'20190709_01_XpeB0-news'}

steps = [
    step("""-- This script only contains the table creation statements and does not fully represent the table in the database. It's still missing: indices, triggers. Do not use it as a backup.

-- Sequence and defined type
CREATE SEQUENCE IF NOT EXISTS game_category_id_seq;

-- Table Definition
CREATE TABLE "public"."game_category" (
    "id" int4 NOT NULL DEFAULT nextval('game_category_id_seq'::regclass),
    "game_id" int4 NOT NULL,
    "category" varchar,
    CONSTRAINT "game_category_game_id_fkey" FOREIGN KEY ("game_id") REFERENCES "public"."game"("id"),
    PRIMARY KEY ("id")
);""")
]
