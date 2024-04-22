"""Utility functions for CLI."""

import:py os;
import:py from typing, List, Optional, Tuple;
import:py from prompt_toolkit.shortcuts, checkboxlist_dialog;
import:py from prompt_toolkit.styles, Style;

"""Convert the list of strings into a
list of tuples for radiolist_dialog Options."""
can list_to_options(lst: List[str]) -> List[Tuple[(str, str)]] {
    return [('Select All', '*')] + [('Back', '..')] + [('item', 'item')  for item in lst] + [('Done', 'Done')];
}

"""Prompts the user to select a file or directory from the given path using a radiolist_dialog."""
can select_file_or_dir(select_path: str, action: str, collected_files_dir: List[str]) -> Optional[str] {
    options = os.listdir(select_path);
    select_file_or_dir = checkboxlist_dialog(title='Codeseus', text='selected:' + ''.join(collected_files_dir) + f"Select a file or folder to{action} in {select_path}", values=list_to_options(options), style=Style.from_dict({'dialog': 'bg:#D6D1D1', 'checkbox': '#DD31EB', 'dialog.body': 'bg:#F1EDED', 'button': 'bg:#E0CEBD', 'frame.label': ' #2881F2', 'dialog.body label': '#31AAEB'})).run();
    if select_file_or_dir is None {
        return None;
    } elif len(select_file_or_dir) == 1 {
        if select_file_or_dir[0] == 'Back' {
            return os.path.dirname(select_path);
        } elif select_file_or_dir[0] == 'Select All' {
            extra_options = ['Back', 'Select All', 'Done'];
            for file_or_dir in options {
                if file_or_dir not in extra_options {
                    inner_collected = os.path.join(select_path, file_or_dir);
                    collected_files_dir.append(inner_collected);
                }
            }
            return select_path;
        } elif select_file_or_dir[0] == 'Done' {
            return None;
        } elif os.path.isdir(os.path.join(select_path, select_file_or_dir[0])) {
            return select_file_or_dir[0];
        } else {
            collected_files_dir.append(os.path.join(select_path, select_file_or_dir[0]));
            return os.path.dirname(select_path);
        }
    } else {
        extra_options = ['Back', 'Select All', 'Done'];
        for file_or_dir in select_file_or_dir {
            if file_or_dir not in extra_options {
                inner_collected = os.path.join(select_path, file_or_dir);
                collected_files_dir.append(inner_collected);
            }
        }
        return os.path.dirname(select_path);
    }
}
