#this function will make sure that all the environment variable are read everytime when the code is executed.
# since this is __init__.py file, whenever sensor file is imported, this function (load_dotenv()) will get automatically called & all the environment variables will bbe read out

from dotenv import load_dotenv
print(f"Loading environment variable from .env file")
load_dotenv()