class math:
    def max(self, a, b):
        if a >= b:
            return a
        return b

class test(math):
    def __init__(self):
        super().__init__()
obj = test()
print(obj.max(2,3))



class my_iter:  # iterator
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        if self.a == 20:
            raise StopIteration
        x = self.a
        self.a += 1
        return x



x = iter(my_iter())

for i in x:
    print(i)


#####################
import json

x = '''{
    "glossary": {
        "title": "example glossary",
		"GlossDiv": {
            "title": "S",
			"GlossList": {
                "GlossEntry": {
                    "ID": "SGML",
					"SortAs": "SGML",
					"GlossTerm": "Standard Generalized Markup Language",
					"Acronym": "SGML",
					"Abbrev": "ISO 8879:1986",
					"GlossDef": {
                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
						"GlossSeeAlso": ["GML", "XML"]
                    },
					"GlossSee": "markup"
                }
            }
        }
    }
}'''
y = '''{"widget": {
    "debug": "on",
    "window": {
        "title": "Sample Konfabulator Widget",
        "name": "main_window",
        "width": 500,
        "height": 500
    },
    "image": { 
        "src": "Images/Sun.png",
        "name": "sun1",
        "hOffset": 250,
        "vOffset": 250,
        "alignment": "center"
    },
    "text": {
        "data": "Click Here",
        "size": 36,
        "style": "bold",
        "name": "text1",
        "hOffset": 250,
        "vOffset": 100,
        "alignment": "center",
        "onMouseUp": "sun1.opacity = (sun1.opacity / 100) * 90;"
    }
}}'''

print(json.loads(x))
print(json.loads(y))

print(json.dumps(json.loads(y), indent=4, separators=(',', ' = ')))

import numpy as np

x = np.array([1,2,3], ndmin=5, dtype='i')
x.reshape(-1)
print(x)


print(np.frompyfunc(lambda x,y: x * y, 2, 1)([3,4,5],[4,5,6]))
print(np.cumsum([1,2,3]))

import seaborn as sns
import pandas as pd

iris = sns.load_dataset('iris')
iris.head()

print(iris)