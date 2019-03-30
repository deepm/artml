import os
import glob


recipes = glob.glob("recipes/*.txt")
removeFlag = False

for recipe in recipes:

    removeFlag = False
    with open(recipe,'r') as r:

        content = " ".join((r.read()).split()).strip()
        
        if "receipt" in recipe:
            newName = recipe.replace("receipt", "recipe")
            removeFlag = True
        else:
            newName = recipe
        
        with open(newName, 'w') as nr:

            nr.write(content)
    if removeFlag:  
        os.remove(recipe)
    break
    


        