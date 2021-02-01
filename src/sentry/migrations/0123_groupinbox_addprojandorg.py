# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-11-05 16:10

from django.db import migrations
import django.db.models.deletion
import sentry.db.models.fields.foreignkey


class Migration(migrations.Migration):
    # This flag is used to mark that a migration shouldn't be automatically run in
    # production. We set this to True for operations that we think are risky and want
    # someone from ops to run manually and monitor.
    # General advice is that if in doubt, mark your migration as `is_dangerous`.
    # Some things you should always mark as dangerous:
    # - Large data migrations. Typically we want these to be run manually by ops so that
    #   they can be monitored. Since data migrations will now hold a transaction open
    #   this is even more important.
    # - Adding columns to highly active tables, even ones that are NULL.
    is_dangerous = True

    # This flag is used to decide whether to run this migration in a transaction or not.
    # By default we prefer to run in a transaction, but for migrations where you want
    # to `CREATE INDEX CONCURRENTLY` this needs to be set to False. Typically you'll
    # want to create an index concurrently when adding one to an existing table.
    atomic = False

    dependencies = [
        ("sentry", "0122_add_release_status"),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=[
                migrations.RunSQL(
                    """
                    ALTER TABLE "sentry_groupinbox" ADD COLUMN "organization_id" bigint NULL;
                    ALTER TABLE "sentry_groupinbox" ADD COLUMN "project_id" bigint NULL;
                    """,
                    reverse_sql="""
                        ALTER TABLE "sentry_groupinbox" DROP COLUMN "organization_id";
                        ALTER TABLE "sentry_groupinbox" DROP COLUMN "project_id";
                        """,
                ),
                migrations.RunSQL(
                    """
                    CREATE INDEX CONCURRENTLY "sentry_groupinbox_organization_id_7b67769a" ON "sentry_groupinbox" ("organization_id");
                    """,
                    reverse_sql="""
                        DROP INDEX CONCURRENTLY "sentry_groupinbox_organization_id_7b67769a";
                        """,
                ),
                migrations.RunSQL(
                    """
                    CREATE INDEX CONCURRENTLY "sentry_groupinbox_project_id_ef8f034d" ON "sentry_groupinbox" ("project_id");
                    """,
                    reverse_sql="""
                        DROP INDEX CONCURRENTLY "sentry_groupinbox_project_id_ef8f034d";
                        """,
                ),
            ],
            state_operations=[
                migrations.AddField(
                    model_name="groupinbox",
                    name="organization",
                    field=sentry.db.models.fields.foreignkey.FlexibleForeignKey(
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="sentry.Organization",
                    ),
                ),
                migrations.AddField(
                    model_name="groupinbox",
                    name="project",
                    field=sentry.db.models.fields.foreignkey.FlexibleForeignKey(
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="sentry.Project",
                    ),
                ),
            ],
        )
    ]
