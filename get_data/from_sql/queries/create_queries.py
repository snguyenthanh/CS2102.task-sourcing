CREATE_TABLE_PERSON_QUERY = r"""
CREATE TABLE IF NOT EXISTS "person" (
	"id"			SERIAL			PRIMARY KEY,
	"username"		VARCHAR(25) 	UNIQUE NOT NULL,
	"password" 		CHAR(100) 		NOT NULL,
	"email" 		TEXT 			UNIQUE NOT NULL,
	"created_dt" 	TIMESTAMP 		NOT NULL,
	"role" 			VARCHAR(10) 	DEFAULT 'member' NOT NULL
);
"""

CREATE_TABLE_CATEGORY_QUERY = r"""
CREATE TABLE IF NOT EXISTS "category" (
	"id"		SERIAL				PRIMARY KEY,
	"name"		TEXT				UNIQUE NOT NULL
);
"""

CREATE_TABLE_TASK_QUERY = r"""
CREATE TABLE IF NOT EXISTS "task" (
	"id" 			CHAR(6)			PRIMARY KEY,
	"title" 		TEXT 			NOT NULL,
	"description"	TEXT			NOT NULL,
	"category_id"	INTEGER			NOT NULL 					REFERENCES "category" ("id") ON DELETE NO ACTION,
	"location"		TEXT			NOT NULL,
	"requester"		VARCHAR(25)		NOT NULL					REFERENCES "person" ("username") ON DELETE CASCADE,
	"start_dt"		TIMESTAMP		NOT NULL,
	"end_dt"		TIMESTAMP		NOT NULL,
	"price"			MONEY			NOT NULL,
	"status_task"	VARCHAR(8)		DEFAULT 'open' NOT NULL,
	"assignee"		VARCHAR(25)		DEFAULT NULL 				REFERENCES "person" ("username") ON DELETE SET NULL
);
"""

CREATE_TABLE_OFFER_QUERY = r"""
CREATE TABLE IF NOT EXISTS "offer" (
	"id"			CHAR(6)			PRIMARY KEY,
	"task_id"		CHAR(6)			NOT NULL					REFERENCES "task" ("id") ON DELETE CASCADE,
	"price"			MONEY			NOT NULL,
	"assignee"		VARCHAR(25)		NOT NULL					REFERENCES "person" ("username") ON DELETE CASCADE,
	"offered_dt"	TIMESTAMP		NOT NULL,
	"status_offer"	VARCHAR(8)		DEFAULT 'pending' NOT NULL
);
"""
