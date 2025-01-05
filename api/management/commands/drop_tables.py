from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    help = "Drops all tables and schemas (except system schemas) in the database."

    def handle(self, *args, **kwargs):
        with connection.cursor() as cursor:
            # Drop all tables
            cursor.execute("""
            DO $$ DECLARE
                r RECORD;
            BEGIN
                FOR r IN (SELECT tablename FROM pg_tables WHERE schemaname = 'public') LOOP
                    EXECUTE 'DROP TABLE IF EXISTS ' || quote_ident(r.tablename) || ' CASCADE';
                END LOOP;
            END $$;
            """)

            # Drop all schemas except system schemas
            cursor.execute("""
            DO $$ DECLARE
                s RECORD;
            BEGIN
                FOR s IN (SELECT schema_name FROM information_schema.schemata WHERE schema_name NOT IN ('pg_catalog', 'information_schema', 'public')) LOOP
                    EXECUTE 'DROP SCHEMA ' || quote_ident(s.schema_name) || ' CASCADE';
                END LOOP;
            END $$;
            """)

            # Reset the public schema
            cursor.execute("""
            DROP SCHEMA public CASCADE;
            CREATE SCHEMA public;
            GRANT ALL ON SCHEMA public TO public;
            GRANT ALL ON SCHEMA public TO CURRENT_USER;
            """)
        self.stdout.write(self.style.SUCCESS("Successfully dropped all tables and schemas."))