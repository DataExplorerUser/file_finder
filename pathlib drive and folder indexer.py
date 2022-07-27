from pathlib import Path
import datetime
from prettytable import PrettyTable

def get_files(folder_str):
    folder = Path(folder_str)
    items = folder.iterdir()  # folders and files
    # extensions = ['.FLAC', '.MP3', '.WAV']
    # return [item.name for item in items if item.is_file() and item.suffix.upper() in extensions]
    extensions = ['.FLAC', '.MP3', '.WAV']
    return [item.name for item in items if item.is_file()]

def globbing(folder_str):
    path = Path(folder_str)

    for e in path.rglob('*.*'):
        print(e)

def files_table(folder_str):
    path = Path(folder_str)

    pt = PrettyTable()
    pt.field_names = ["Folder", "File name", "Size", "Created", "Modified"]

    pt.align["Folder"] = "l"
    pt.align["File name"] = "l"
    pt.align["Size"] = "r"
    pt.align["Created"] = "l"
    pt.align["Modified"] = "l"

    for e in path.glob('*.*'):
        created = datetime.datetime.fromtimestamp(e.stat().st_ctime)
        modified = datetime.datetime.fromtimestamp(e.stat().st_mtime)
        size = e.stat().st_size
        pt.add_row([e.parent, e.name, size, f"{created:%Y-%m-%d %H:%M:%S}", f"{modified:%Y-%m-%d %H:%M:%S}"])
        print('parent:', e.parent)
        # print('parts:', e.parts)

    print(pt)

if __name__ == '__main__':
    # files = get_files('P:\My Documents')
    # print(files)

    # files = globbing('P:\My Documents\04. Kerndocumenten')

    files_table('P:\My Documents\quick_salary')