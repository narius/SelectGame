"""
Creates session table
"""

from yoyo import step

__depends__ = {'20190620_01_IwAbL-creates-table-locations'}

steps = [
    step("""-- This script only contains the table creation statements and does not fully represent the table in the database. It's still missing: indices, triggers. Do not use it as a backup.

-- Sequence and defined type
CREATE SEQUENCE IF NOT EXISTS session_id_seq;

-- Table Definition
CREATE TABLE "public"."session" (
    "id" int4 NOT NULL DEFAULT nextval('session_id_seq'::regclass),
    "user_id" int4 NOT NULL,
    "hashed_session" text NOT NULL,
    "created" date NOT NULL DEFAULT now(),
    CONSTRAINT "session_user_id_fkey" FOREIGN KEY ("user_id") REFERENCES "public"."users"("id") ON DELETE CASCADE,
    PRIMARY KEY ("id")
);""")
]
