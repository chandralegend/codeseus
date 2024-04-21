"""Utility functions for CLI."""

import os
from typing import List, Optional, Tuple

from prompt_toolkit.shortcuts import checkboxlist_dialog
from prompt_toolkit.styles import Style


def list_to_options(lst: List[str]) -> List[Tuple[str, str]]:
    """Convert the list of strings into a list of tuples for radiolist_dialog Options."""
    return (
        [("Select All", "*")]
        + [("Back", "..")]
        + [(item, item) for item in lst]
        + [("Done", "Done")]
    )


def select_file_or_dir(
    select_path: str, action: str, collected_files_dir: List[str]
) -> Optional[str]:
    """Prompts the user to select a file or directory from the given path using a radiolist_dialog."""
    options = os.listdir(select_path)
    select_file_or_dir = checkboxlist_dialog(
        title="Codeseus",
        text="selected:"
        + "".join(collected_files_dir)
        + f"\n\n Select a file or folder to {action} in {select_path}",
        values=list_to_options(options),
        style=Style.from_dict(
            {
                "dialog": "bg:#D6D1D1",
                "checkbox": "#DD31EB",
                "dialog.body": "bg:#F1EDED",
                "button": "bg:#E0CEBD",
                "frame.label": "#2881F2",
                "dialog.body label": "#31AAEB",
            }
        ),
    ).run()
    if select_file_or_dir is None:
        return None
    elif len(select_file_or_dir) == 1:
        if select_file_or_dir[0] == "Back":
            return os.path.dirname(select_path)
        elif select_file_or_dir[0] == "Select All":
            extra_options = ["Back", "Select All", "Done"]
            for file_or_dir in options:
                if file_or_dir not in extra_options:
                    inner_collected = os.path.join(select_path, file_or_dir)
                    collected_files_dir.append(inner_collected)
            return select_path
        elif select_file_or_dir[0] == "Done":
            return None
        else:
            if os.path.isdir(os.path.join(select_path,select_file_or_dir[0])):
                return select_file_or_dir[0]
            else:
                collected_files_dir.append(
                    os.path.join(select_path, select_file_or_dir[0])
                )
                return os.path.dirname(select_path)
    else:
        extra_options = ["Back", "Select All", "Done"]
        for file_or_dir in select_file_or_dir:
            if file_or_dir not in extra_options:
                inner_collected = os.path.join(select_path, file_or_dir)
                collected_files_dir.append(inner_collected)
        return os.path.dirname(select_path)
