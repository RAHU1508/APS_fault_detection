#each & every step during the execution of the project will be logged

import logging
import os
from datetime import datetime
import os

#log file name
LOG_FILE_NAME = f"{datetime.now().strftime('%m%d%Y__%H%M%S')}.log" #every time you do some execution, new file will get created for each time stamp

#log directory
LOG_FILE_DIR = os.path.join(os.getcwd(),"logs") #getcwd means 'get current directory', folder called 'logs' is created

#create folder if not available
os.makedirs(LOG_FILE_DIR,exist_ok=True)

#log file path

LOG_FILE_PATH = os.path.join(LOG_FILE_DIR,LOG_FILE_NAME)

logging.basicConfig( #in which file you are going to create log, how logging message will get displayed (format) & logging level
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
)