from pathlib import Path
import re
import os

FILE_NAME_PATTERN = re.compile(r'(\D*)(\d*)\.py')
MAX_DUPLICATES=100
def main():
    me = Path(__file__)
    cloneName = me.name
    needNewName = True
    while needNewName:
        cloneName, index = makeNewName(cloneName)
        if index > MAX_DUPLICATES:
            print("That's all folks")
            return
        clone = me.parent / cloneName
        needNewName = clone.exists()
    
    duplicate(clone)
    os.system('start python "' + str(clone) + '"')
    
    
    
def makeNewName(oldName:str) -> tuple:
    matcher = FILE_NAME_PATTERN.fullmatch(oldName)
    if matcher == None:
        raise ValueError("The format of my name is unexpected!" )
    baseName = matcher.group(1)
    indexStr = matcher.group(2)
    if indexStr:
        index = int(indexStr) + 1
    else:
        index = 1
    
    return (baseName + str(index) + ".py", index)

def duplicate(target: Path) -> None:
    with open(__file__, 'rb') as s, open(target, 'xb') as t:
        t.write(s.read())

if __name__ == "__main__":
    main()
    
        