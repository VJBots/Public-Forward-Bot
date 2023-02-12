import os
import logging
class Config:                                                                   
    API_ID = int(os.environ.get("API_ID", "19134188"))
    API_HASH = os.environ.get("API_HASH", "91587601a5d898e3341b7e4a9e1c2537")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5815403978:AAHWjMNEPswgMfaqvvPSjw3OtoOFvbFyLgU")
    BOT_SESSION = os.environ.get("BOT_SESSION", "forwardbot")
    OWNER_ID = os.environ.get("OWNER_ID", "1802523258")                             
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://Multibot123:Multibot123@cluster0.qnuoqak.mongodb.net/?retryWrites=true&w=majority")  
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Clujgj")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Data')
    SESSION = os.environ.get("SESSION", "")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001899524586"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "ForwardVJbot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
