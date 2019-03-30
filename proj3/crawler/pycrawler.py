import urllib.request
import time
from html.parser import HTMLParser


class RecipeParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.flag = False
        self.stack = []
        self.data = []
        

    def handle_starttag(self, tag, attrs):
        if tag == 'div' and (('class','recipe-print__container2') in attrs):
            self.flag = True
        
        if self.flag:
            self.stack.append(tag)

    def handle_data(self, data):
        
        if self.flag:
            self.data.append(data.strip())

    def handle_endtag(self, tag):
        if self.flag:
            self.stack.pop()
            if len(self.stack) == 0:
                self.flag = False




def sendRequest(url):
    request = urllib.request.Request(url,None, {})
    return urllib.request.urlopen(request).read().decode('utf8')

def writeFile(output, filename):

    with open("recipes/recipe"+filename+".txt",'w') as f:

        f.write(output)


failCount = 0
pageID = 8128

while failCount < 100:
    filename = str(pageID)
    print(pageID, failCount)
    try:
        result = sendRequest("https://www.allrecipes.com/recipe/{}/dirt-cake-i/print/?recipeType=Recipe&servings=10&isMetric=false".format(pageID))
    except urllib.error.HTTPError as err:
        if err.code == 404:
            failCount += 1
            continue
        else:
            raise
    
    pageID += 1
      
    failCount = 0
    parser = RecipeParser()
    parser.feed(result)
    parser.close()
    writeFile(''.join(parser.data), filename)
    time.sleep(1.5)
    
    
