"""
Event
"""

from yoyo import step

__depends__ = {'20190707_02_hJbQg-game-library'}

steps = [
    step("""-- This script only contains the table creation statements and does not fully represent the table in the database. It's still missing: indices, triggers. Do not use it as a backup.

-- Sequence and defined type
CREATE SEQUENCE IF NOT EXISTS event_id_seq;

-- Table Definition
CREATE TABLE "public"."event" (
    "id" int4 NOT NULL DEFAULT nextval('event_id_seq'::regclass),
    "owner" int4,
    "creator" int4,
    "location" int4,
    "name" varchar,
    "createddate" date DEFAULT now(),
    "eventdate" date,
    CONSTRAINT "event_creator_fkey" FOREIGN KEY ("creator") REFERENCES "public"."users"("id") ON DELETE CASCADE,
    CONSTRAINT "event_owner_fkey" FOREIGN KEY ("owner") REFERENCES "public"."users"("id") ON DELETE CASCADE,
    CONSTRAINT "event_location_fkey" FOREIGN KEY ("location") REFERENCES "public"."locations"("id") ON DELETE CASCADE,
    PRIMARY KEY ("id")
); """)
]
