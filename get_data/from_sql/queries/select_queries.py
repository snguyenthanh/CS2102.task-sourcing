SELECT_ALL_PERSON_QUERY = r"""SELECT "person"."username" FROM "person";"""

SELECT_ALL_EMAIL_QUERY = r"""SELECT "person"."email" FROM "person";"""

SELECT_ONE_PERSON_QUERY = r"""
SELECT
    "person"."username"
FROM "person"
WHERE 1=1
    AND "person"."username" = '{}'
LIMIT 1;"""

SELECT_ONE_EMAIL_QUERY = r"""
SELECT "person"."email"
FROM "person"
WHERE 1=1
    AND "person"."email" = '{}'
LIMIT 1;"""

SELECT_PERSON_WITH_PWD_QUERY = r"""
SELECT "person"."username"
FROM "person"
WHERE 1=1
    AND "person"."username" = '{}'
    AND "person"."password" = '{}'
LIMIT 1;"""
