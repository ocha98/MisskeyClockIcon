import datetime
import logging

import azure.functions as func

import MisskeyClockIcon.main 


def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    if mytimer.past_due:
        logging.info('The timer is past due!')

    logging.info("Changing icon...")
    try :
        MisskeyClockIcon.main.main()
    except Exception as e:
        logging.error("Faild change icon")
        logging.error(e)
    else:
        logging.info("Finish icon...")

    logging.info('Python timer trigger function ran at %s', utc_timestamp)
