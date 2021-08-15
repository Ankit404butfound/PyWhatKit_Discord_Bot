import sqlite3 #psycopg2

import os

from typing import Union


CONN = sqlite3.connect(":memory:")#psycopg2.connect(os.environ.get("DATABASE_URL"))
CUR = CONN.cursor()

MATCHING = {
    "ASCII Art":                  ("ascii", "ascii art", "art"),
    "Text to Handwriting":        ("ascii", "ascii" "art", "art"),
    "Shutdown":                   ("shutdown",),
    "Cancel Shutdown":            ("sancel Shutdown",),
    "Send Mail":                  ("mail", "send mail"),
    "Send HTML Mail":             ("send hmail", "html mail"),
    "Info":                       ("info", "wikipedia"),
    "Play on YT":                 ("playonyt", "youtube", "search on yt"),
    "Search Google":              ("google", "search"),
    "Show History":               ("history",),
    "Close Tab":                  ("close tab",),
    "Send WhatsApp Message":      ("sendwhatmsg", "send message"),
    "Sending Message Instantly":  ("sendwhatmsg_instantly", "send message instantly"),
    "Sending Message to a Group": ("sendwhatmsg_to_group", "group message"),
    "Sending WhatsApp Media":     ("sendwhats_image", "send image", "send media"),
}


def execute(sql: str, mode: str = "r") -> Union[bool, tuple]:
    """
    Execute a SQL statement
    :param sql: SQL statement
    :param mode: 'w' or 'r'
    :return: bool or dict
    """

    if mode == "w":
        try:
            CUR.execute(sql)
            CONN.commit()
            return True
        except:#psycopg2.Error as e:
            CONN.rollback()
            return False

    elif mode == "r":
        CUR.execute(sql)
        return CUR.fetchall()


def match_string(string: str) -> str:
    """
    Match the string with the command
    """
    for k, v in MATCHING.items():
        if string.lower() in v:
            return k
    else:
        for key in MATCHING:
            if string.lower() in key.lower():
                return key
        
    return None


def search_for_docs(search_string: str) -> tuple:
    """
    Get information from DB for particular function
    :param function: function name
    :return: str
    """

    function = match_string(search_string)
    if function:
        function = function.strip()
        sql = f"SELECT topic, description, args, returns, link FROM command WHERE topic='{function}'"
        data = execute(sql)#("SELECT topic, description, args, returns, link FROM command WHERE topic='Sending WhatsApp Media'")
        return data[0]
    else:
        return ()


def search_for_example(search_string: str) -> tuple:
    """
    Get information from DB for particular function
    :param function: function name
    :return: str
    """

    function = match_string(search_string)
    if function:
        function = function.strip()
        sql = f"SELECT example, comment FROM example WHERE function='{function}'"
        data = execute(sql)
        return function, data
    else:
        return None, (())


def search_for_exception(search_string: str) -> tuple:
    """
    Get exception's information from DB for particular function
    :param function: function name
    :return: str
    """

    sql = f"SELECT topic, description, fix FROM exception WHERE topic='{search_string}'"
    data = execute(sql)
    if data:
        return data[0]
    else:
        return ()
