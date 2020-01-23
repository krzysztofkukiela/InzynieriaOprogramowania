import re
from pathlib import Path

def findFunctions(file):
    fileContent = open(file).read()
    regex = r"def[\s]+([a-zA-Z_0-9]+)\(.*\)[ ]*\:"
    matches = re.findall(regex, fileContent, re.MULTILINE)
    return matches

def findFunctionCalls(functionsInFiles, files):
    calls = {}
    for functionsInFile in functionsInFiles:
        moduleTo = Path(functionsInFile).stem
        for functionToCheck in functionsInFiles[functionsInFile]:
            for file in files:
                moduleFrom = Path(file).stem
                if moduleTo == moduleFrom:
                    continue
                fileContent = open(file).read()
                functionsRegex = r"def(?! " + functionToCheck + r")[\s]+(.*)\(.*\).*(\n(\t|[\s]{4}).*)*"
                functions = re.finditer(functionsRegex, fileContent, re.MULTILINE)
                for function in functions:
                    functionCallRegex = r"[^a-zA-z_0-9]" + functionToCheck + r"\(.*\)"
                    isCalled = re.findall(functionCallRegex, function.group(), re.MULTILINE)
                    if len(isCalled) == 0:
                        continue
                    if (function.group(1) + ':' + moduleFrom in calls):
                        calls[function.group(1) + ':' + moduleFrom] = calls[function.group(1) + ':' + moduleFrom] + 1
                    else:
                        calls[function.group(1) + ':' + moduleFrom] = 1
                    if (moduleFrom + ':' + moduleTo in calls):
                        calls[moduleFrom + ':' + moduleTo] = calls[moduleFrom + ':' + moduleTo] + 1
                    else:
                        calls[moduleFrom + ':' + moduleTo] = 1
                    if (functionToCheck + ':' + moduleTo in calls):
                        calls[functionToCheck + ':' + moduleTo] = calls[functionToCheck + ':' + moduleTo] + 1
                    else:
                        calls[functionToCheck + ':' + moduleTo] = 1
    return calls

