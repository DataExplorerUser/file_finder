# create list of files using pathlib, but without glob
# advantage should be that you can just skip folders and 
# files that go beyond the maximum name length of 258 on 
# windows.

from pathlib import Path

def walk(path): 
    for p in Path(path).iterdir(): 
        if p.is_dir(): 
            yield from walk(p)
            continue
        yield p.resolve()

# recursively traverse all files from current directory
for p in walk(Path('.')): 
    print(p)

# the function returns a generator so if you need a list you need to build one
all_files = list(walk(Path('.'))) 


source: https://stackoverflow.com/questions/6639394/what-is-the-python-way-to-walk-a-directory-tree
