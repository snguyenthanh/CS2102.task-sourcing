INSERT_PERSON_QUERY = r"""INSERT INTO "person" ("username", "password", "email", "created_dt")
                            VALUES ('{}', '{}', '{}', '{}');""" # username, password, email, created_dt

INSERT_CATEGORY_QUERY = r"""INSERT INTO "category" ("name") VALUES ('{}');""" # Category name
