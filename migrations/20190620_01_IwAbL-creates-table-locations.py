"""
Creates table locations
"""

from yoyo import step

__depends__ = {'20190615_04_0npAF-creares-friends-table'}

steps = [
    step("""-- This script only contains the table creation statements and does not fully represent the table in the database. It's still missing: indices, triggers. Do not use it as a backup.

-- Sequence and defined type
CREATE SEQUENCE IF NOT EXISTS locations_id_seq;

-- Table Definition
CREATE TABLE "public"."locations" (
    "id" int4 NOT NULL DEFAULT nextval('locations_id_seq'::regclass),
    "owner" int4,
    "public" bool,
    "name" varchar,
    "street" varchar,
    "postalcode" varchar,
    "city" varchar,
    CONSTRAINT "locations_owner_fkey" FOREIGN KEY ("owner") REFERENCES "public"."users"("id") ON DELETE CASCADE ON UPDATE CASCADE,
    PRIMARY KEY ("id")
);""")
]
