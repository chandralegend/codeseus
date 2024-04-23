"""CLI for codeseus."""

import os

from jaclang import jac_import

main = jac_import("cli", base_path=os.path.dirname(__file__)).main
