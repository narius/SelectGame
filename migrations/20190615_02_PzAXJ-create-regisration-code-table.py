"""
Create regisration code table
"""

from yoyo import step

__depends__ = {'20190615_01_HOmLx-create-users-table'}

steps = [
    step("""
    -- Sequence and defined type
    CREATE SEQUENCE IF NOT EXISTS registration_codes_id_seq;

    -- Table Definition
    CREATE TABLE "public"."registration_codes" (
    "id" int4 NOT NULL DEFAULT nextval('registration_codes_id_seq'::regclass),
    "code" varchar NOT NULL,
    "description" varchar,
    "valid_to" date,
    "valid" bool,
    PRIMARY KEY ("id")
);""")
]
