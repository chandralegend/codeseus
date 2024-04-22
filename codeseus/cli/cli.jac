"""CLI Implementation."""

import:py os ;
import:py from codeseus.cli.utils, select_file_or_dir ;
import:py from prompt_toolkit.shortcuts, radiolist_dialog ;
import:py from prompt_toolkit.styles, Style ;

"""CLI Implementation."""
can jac_main() -> None {
    options=[('Refactor', 'refactor'), ('Repair', 'repair'), ('Test', 'test'), ('Review', 'review')];    
    action=radiolist_dialog(title='Welcome to Codeseus', 
    text="Your odyssey to pristine code ends here. Simply provide instructions, and codeseus will refactor,repair, test, and review your codebase with divine precision.Select what you want to do",
    values=options,
    style=Style.from_dict(
        {
            'dialog': 'bg:#D6D1D1', 
        'checkbox': '#DD31EB', 
        'dialog.body': 'bg:#F1EDED', 
        'button': 'bg:#E0CEBD', 
        'frame.label': '#2881F2', 
        'dialog.body label': '#31AAEB'
        })).run();    
    if action {
        current_dir=os.getcwd();    
        select_path=current_dir;    
        collected_files_dir: list[str]=[];    
        while True {
            selected_path=select_file_or_dir(select_path, action, collected_files_dir);    
            if selected_path is None {
                break ;}
            
            select_path=os.path.join(select_path, selected_path);    
            if os.path.isfile(select_path) {
                break ;}
        }
        
        print(f"List of files :{collected_files_dir}");    
        radiolist_dialog(title='Codeseus',
         text='You have selected the following files and folders to work on'+''.join(collected_files_dir),
         values=[('Continue', 'continue'), ('Cancel', 'cancel')],
        
        style=Style.from_dict({
            'dialog': 'bg:#D6D1D1', 
            'checkbox': '#DD31EB', 
            'dialog.body': 'bg:#F1EDED', 
            'button': 'bg:#E0CEBD', 
            'frame.label':' #2881F2', 
           ' dialog.body label' : '#31AAEB'
            }
            )).run() ;
            
    } 

    else {
            print('No option selected') ;
     }
}

with entry {
        jac_main();
}
