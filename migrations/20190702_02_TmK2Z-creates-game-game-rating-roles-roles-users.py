"""
Creates game, game_rating, roles, roles_users

"""

from yoyo import step

__depends__ = {'20190702_01_NdaA4-creates-session-table'}

steps = [
    step("""-- This script only contains the table creation statements and does not fully represent the table in the database. It's still missing: indices, triggers. Do not use it as a backup.

-- Sequence and defined type
CREATE SEQUENCE IF NOT EXISTS game_id_seq;

-- Table Definition
CREATE TABLE "public"."game" (
    "id" int4 NOT NULL DEFAULT nextval('game_id_seq'::regclass),
    "name" text NOT NULL,
    "categories" text NOT NULL,
    PRIMARY KEY ("id")
);
-- This script only contains the table creation statements and does not fully represent the table in the database. It's still missing: indices, triggers. Do not use it as a backup.

-- Sequence and defined type
CREATE SEQUENCE IF NOT EXISTS game_rating_id_seq;

-- Table Definition
CREATE TABLE "public"."game_rating" (
    "id" int4 NOT NULL DEFAULT nextval('game_rating_id_seq'::regclass),
    "user_id" int4 NOT NULL,
    "raing" int4 NOT NULL DEFAULT 0,
    CONSTRAINT "game_rating_user_id_fkey" FOREIGN KEY ("user_id") REFERENCES "public"."users"("id") ON DELETE CASCADE,
    PRIMARY KEY ("id")
);

-- This script only contains the table creation statements and does not fully represent the table in the database. It's still missing: indices, triggers. Do not use it as a backup.

-- Sequence and defined type
CREATE SEQUENCE IF NOT EXISTS roles_id_seq;

-- Table Definition
CREATE TABLE "public"."roles" (
    "id" int4 NOT NULL DEFAULT nextval('roles_id_seq'::regclass),
    "name" text NOT NULL,
    "description" text,
    PRIMARY KEY ("id")
);

-- This script only contains the table creation statements and does not fully represent the table in the database. It's still missing: indices, triggers. Do not use it as a backup.

-- Sequence and defined type
CREATE SEQUENCE IF NOT EXISTS roles_user_id_seq;

-- Table Definition
CREATE TABLE "public"."roles_user" (
    "id" int4 NOT NULL DEFAULT nextval('roles_user_id_seq'::regclass),
    "role_id" int4,
    "user_id" int4,
    CONSTRAINT "roles_user_role_id_fkey" FOREIGN KEY ("role_id") REFERENCES "public"."roles"("id") ON DELETE CASCADE,
    CONSTRAINT "roles_user_user_id_fkey" FOREIGN KEY ("user_id") REFERENCES "public"."users"("id") ON DELETE CASCADE,
    PRIMARY KEY ("id")
);
""")
]
