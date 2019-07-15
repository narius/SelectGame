"""
Event participants
"""

from yoyo import step

__depends__ = {'20190708_01_oqgg0-event'}

steps = [
    step("""-- This script only contains the table creation statements and does not fully represent the table in the database. It's still missing: indices, triggers. Do not use it as a backup.

-- Sequence and defined type
CREATE SEQUENCE IF NOT EXISTS event_participant_id_seq;

-- Table Definition
CREATE TABLE "public"."event_participant" (
    "id" int4 NOT NULL DEFAULT nextval('event_participant_id_seq'::regclass),
    "event_id" int4 NOT NULL,
    "user_id" int4 NOT NULL,
    "status" varchar,
    "invited_by" int4,
    CONSTRAINT "event_participant_invited_by_fkey" FOREIGN KEY ("invited_by") REFERENCES "public"."users"("id"),
    CONSTRAINT "event_participant_user_id_fkey" FOREIGN KEY ("user_id") REFERENCES "public"."users"("id"),
    CONSTRAINT "event_participant_event_id_fkey" FOREIGN KEY ("event_id") REFERENCES "public"."event"("id"),
    PRIMARY KEY ("id")
); """)
]
