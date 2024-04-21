import os

from prompt_toolkit import prompt
from prompt_toolkit.shortcuts import radiolist_dialog
from prompt_toolkit.styles import Style

from utils import  select_file_or_dir

def main():
    """
    The main function that prompts the user to select an action and a file or directory
    to perform the selected action on.
    """
    options = [
        ("Refactor", "refactor"),
        ("Repair", "repair"),
        ("Test", "test"),
        ("Review", "review")
    ]
    action = radiolist_dialog(
        title="Welcome to Codeseus",
        text="Your odyssey to pristine code ends here. \nSimply provide instructions, and codeseus will refactor, repair, test, and review your codebase with divine precision.\nSelect what you want to do",
        values=options,
        style=Style.from_dict({
        'dialog': 'bg:#D6D1D1',
         'checkbox': '#DD31EB',
         'dialog.body': 'bg:#F1EDED',
        'button': 'bg:#E0CEBD',
         'frame.label': '#2881F2',
        'dialog.body label': '#31AAEB',
        })
    ).run()

    if action:
        current_dir = os.getcwd()
        select_path = current_dir
        while True:
            selected_path = select_file_or_dir(select_path, action)
            if selected_path is None:
                break
            select_path = selected_path
            if os.path.isfile(select_path):
                break
            #selected path is the file that we want to work on
            # TODO: Implement the logic to refactor, repair, test, or review the file here
    else:
        print("No option selected.")

if __name__ == "__main__":
    main()
