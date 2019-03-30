import glob


recipes = glob.glob("../recipes/*.txt")

authorFile = "../recipes/authors/authors.txt"
quoteFile = "../recipes/quotes/quotes.txt"
ingredientFile = "../recipes/ingredients/ingredients.txt"
directionFile = "../recipes/directions/directions.txt"

ingredientStr = "Ingredients"
directionStr = "Directions"
quoteStr = "\""

authors = []
quotes = []
ingredients = []
directions = []

for recipe in recipes:

    with open(recipe,'r') as r:
        content = r.read()
        quotePos = content.find(quoteStr)
        ingPos = content.find(ingredientStr)
        dirPos = content.find(directionStr)

        authors.append(content[:quotePos])
        quotes.append(content[quotePos:ingPos])
        ingredients.append(content[ingPos + len(ingredientStr) + 1:dirPos - 1])
        directions.append(content[dirPos + len(directionStr) + 1:])


with open(authorFile, "w") as a:

    a.write("\n".join(authors))

with open(quoteFile, "w") as q:

    q.write("\n".join(quotes))

with open(ingredientFile, "w") as i:

    i.write("\n".join(ingredients))

with open(directionFile, "w") as d:

    d.write("\n".join(directions))



