import logging

logging.basicConfig(
    level=logging.DEBUG, filename='log.txt', filemode='w',
    format="%(asctime)s - %(levelname)s - %(message)s"
                    )

logging.debug("it's debug")
logging.info("it's info")
logging.warning("it's warning")
logging.error("it's error")
logging.critical("it's critical")

try:
    a=1/0
except ZeroDivisionError as e:
    logging.exception(f"An error occurred: {e}")
