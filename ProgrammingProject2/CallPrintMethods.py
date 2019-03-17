import re

def CallAllPrintMethods(classObject):

    methods = [getattr(classObject, i) for i in dir(classObject) if callable(getattr(classObject, i)) and re.search('Print*', i)]

    for x in methods:

        x()
