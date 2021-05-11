import os

def execute(code):
    #code = code.replace("\n","\\n").replace("\t","\\t").replace("\r","\\r")
    file = open("agent.py","w",encoding="utf-8")
    file.write(code)
    file.close()
    os.system("python executor.py > output.txt")
    data = open("output.txt",encoding="utf-8").read()
    if data != "":
        return data if len(data) <= 2000 else "Output too big, returning first 4000 characters\n"+data[:4000]
    else:
        return "No output statement provided"
