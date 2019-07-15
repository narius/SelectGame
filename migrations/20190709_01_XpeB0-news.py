"""
news
"""

from yoyo import step

__depends__ = {'20190708_02_nh7BY-event-participants'}

steps = [
    step("""
-- This script only contains the table creation statements and does not fully represent the table in the database. It's still missing: indices, triggers. Do not use it as a backup.

-- Sequence and defined type
CREATE SEQUENCE IF NOT EXISTS news_id_seq;

-- Table Definition
CREATE TABLE "public"."news" (
    "id" int4 NOT NULL DEFAULT nextval('news_id_seq'::regclass),
    "writer_id" int4,
    "header" text,
    "text" text,
    "created" timestamp DEFAULT now(),
    "publish_from" timestamp,
    "publish_to" timestamp,
    CONSTRAINT "news_writer_id_fkey" FOREIGN KEY ("writer_id") REFERENCES "public"."users"("id"),
    PRIMARY KEY ("id")
); """)
]
