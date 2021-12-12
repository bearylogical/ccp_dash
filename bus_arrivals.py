import logging
from dotenv import load_dotenv
import os
import datetime
from parsers import SGBusParser
from utils import update_svg, configure_logging

# load our env vars
load_dotenv()
configure_logging()

LTA_API_KEY = os.getenv("LTA_CREDENTIALS")

def get_travel_time():

    logging.info("Retrieving LTA Data")
    res = SGBusParser(LTA_API_KEY).get_timings("84619")
    logging.info(f"Retrieved {len(res)} bus services")
    return res

if __name__ == "__main__":
    get_travel_time()
