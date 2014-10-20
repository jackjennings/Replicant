import os
from vanilla.dialogs import message
from replicant.helpers import createArchiveYesNo
from replicant.models import Replicant

replicant = Replicant(CurrentFont())
if not replicant.font:
    message("No open font", "You must have an open, saved font to replicate.")
elif os.path.exists(replicant.path) or createArchiveYesNo():
    replicant.replicate()
