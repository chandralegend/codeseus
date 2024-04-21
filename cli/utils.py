import os
from typing import List, Tuple, Optional
from prompt_toolkit.shortcuts import radiolist_dialog



def list_to_options(lst: List[str]) -> List[Tuple[str, str]]:
    """Converts a list of strings into a list of tuples for radiolist_dialog options."""
    return [(item, item) for item in lst]

def select_file_or_dir(select_path: str, action: str) -> Optional[str]:
    """Prompts the user to select a file or directory from the given path using a radiolist_dialog."""
    options = os.listdir(select_path)
    select_file_or_dir = radiolist_dialog(
        title="Codeseus",
        text=f"Select a file or folder to {action} in {select_path}",
        values=list_to_options(options)
    ).run()

    if select_file_or_dir is None:
        return None

    select_file_or_dir = os.path.join(select_path, select_file_or_dir)
    if os.path.isdir(select_file_or_dir):
        return select_file_or_dir
    else:
        radiolist_dialog(
            title="Codeseus",
            text=f"Are you sure you want to {action} {select_file_or_dir}",
            values=list_to_options(["Yes", "No"])
        ).run()
        return select_file_or_dir