import requests

def in_english(text):
    status = requests.get(f"http://pywhatkit.pythonanywhere.com/is_english?text={text}").text
    return False if status == "False" else True
