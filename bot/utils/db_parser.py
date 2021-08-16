import os
from typing import Union, Any

import psycopg2


CONN = psycopg2.connect(os.environ.get("DATABASE_URL"))
CUR = CONN.cursor()

MATCHING = {
    "ASCII Art":                  ("ascii", "ascii art", "art"),
    "Text to Handwriting":        ("ascii", "ascii" "art", "art"),
    "Shutdown":                   ("shutdown",),
    "Cancel Shutdown":            ("Cancel Shutdown",),
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


def execute(sql: str, mode: str = "r") -> Union[bool, list[tuple[Any, ...]], None]:
    """Execute a SQL statement"""

    if mode == "w":
        try:
            CUR.execute(sql)
            CONN.commit()
            return True
        except psycopg2.Error as e:
            CONN.rollback()
            return False

    elif mode == "r":
        CUR.execute(sql)
        return CUR.fetchall()


def match_string(string: str) -> Union[str, None]:
    """Match the String with the Command """
    for k, v in MATCHING.items():
        if string.lower() in v:
            return k
    else:
        for key in MATCHING:
            if string.lower() in key.lower():
                return key

    return None


def search_for_docs(search_string: str) -> tuple:
    """Get Docs for a particular Function"""

    function = match_string(search_string)
    if function:
        function = function.strip()
        sql = f"SELECT topic, description, args, returns, link FROM command WHERE topic='{function}'"
        data = execute(sql)
        return data[0]
    else:
        return ()


def search_for_example(search_string: str) -> tuple:
    """Get the Example for a Particular"""

    function = match_string(search_string)
    if function:
        function = function.strip()
        sql = f"SELECT example, comment FROM example WHERE function='{function}'"
        data = execute(sql)
        return function, data
    else:
        return None, (())


def search_for_exception(search_string: str) -> tuple:
    """Get details about an Exception"""

    sql = f"SELECT topic, description, fix FROM exception WHERE topic='{search_string}'"
    data = execute(sql)
    if data:
        return data[0]
    else:
        return ()
