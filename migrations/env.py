from __future__ import with_statement
from alembic import context
from sqlalchemy import engine_from_config, pool
from logging.config import fileConfig
import logging



config = context.config


fileConfig(config.config_file_name)
logger = logging.getLogger("alembic.env")

from flask import current_app

config.set_main_option('sqlalchemy.url', current_app.config.get('SQLALCHEMY_DATABASE_URI'))

target_metadata = current_app.extensions['migrate'].db.metadata



def run_migrations_offline():
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url, 
        target_metadata=target_metadata,
        literal_binds=True
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():

    def process_version_directives(context, revision, directives):
        if getattr(config.cmd_opts, 'autogenerate', False):
            script = directives[0]
            if script.upgrade_ops.is_empty():
                directives[:] = []
                logger.info("No changes in schema detected.")

    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, 
                          target_metadata=target_metadata,
                          process_revision_directives=process_version_directives,
                          **current_app.extensions['migrate'].configure_args)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()