${imports if imports else ""}
"""${message}

Revision ID: ${up_revision}
Revises: ${down_revision if down_revision else None}
Create Date: ${create_date}

"""
from alembic import op
import sqlalchemy as sa
${render_imports() if render_imports else ""}

# revision identifiers, used by Alembic.
revision = '${up_revision}'
down_revision = '${down_revision if down_revision else None}'
branch_labels = ${repr(branch_labels) if branch_labels else None}
depends_on = ${repr(depends_on) if depends_on else None}

def upgrade():
${upgrades if upgrades else "    pass"}

def downgrade():
${downgrades if downgrades else "    pass"}
