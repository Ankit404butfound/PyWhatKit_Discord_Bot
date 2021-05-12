import os

def execute(code):
    #code = code.replace("\n","\\n").replace("\t","\\t").replace("\r","\\r")
    file = open("bot/agent.py","w",encoding="utf-8")
    file.write(code)
    file.close()
    os.system("python bot/executor.py > bot/output.txt")
    data = open("bot/output.txt",encoding="utf-8").read()
    if data != "":
        return data if len(data) <= 2000 else "Output too big, returning first 4000 characters\n"+data[:4000]
    else:
        return "No output statement provided"
