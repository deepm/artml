import glob

recipes = glob.glob("../recipes/*.txt")
stringSeg = "ALL RIGHTS RESERVED"
for recipe in recipes:

    with open(recipe, 'r+') as r:
        content = r.read()
        pos = content.find(stringSeg)
        if pos != -1:
            r.truncate(0)
            with open(recipe, 'w') as nr:

                nr.write(content[:pos])
            