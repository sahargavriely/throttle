import random
import threading
import time

import requests

from ..utils import (
    setup_logging,
    REQUEST_HOST,
    SERVER_PORT,
)


import logging
logger = setup_logging(__name__, logging.DEBUG, stream_to_screen=True)
run = False
minimal_time_between_request = 0
maximal_time_between_request = 1
sleep_range = minimal_time_between_request, maximal_time_between_request


def run_users(users_amount, host=REQUEST_HOST, port=SERVER_PORT):
    logger.info('executing for %s users over %s:%s', users_amount, host, port)
    global run
    run = True
    threads: list[threading.Thread] = list()
    for i in range(users_amount):
        thread = threading.Thread(target=exec_user, args=(i, host, port))
        threads.append(thread)
        thread.start()
    logger.info('all users started')
    input('Once you press enter it is over\n')
    logger.info('enter was pressed - exiting gracefully')
    run = False
    for thread in threads:
        thread.join()
    logger.info('all threads were exited gracefully')
    return 'done'


def exec_user(user_id, host, port):
    url = f'http://{host}:{port}/?clientId={user_id}'
    logger.info('user %s initialized %s', user_id, url)
    while run:
        try:
            logger.debug('user %s requesting', user_id)
            response = requests.get(url)
            logger.debug('user %s received back %s',
                         user_id, response.status_code)
        except Exception as e:
            logger.error('user %s failed to request with %s', user_id, e)
        time_to_sleep = random.uniform(*sleep_range)
        logger.debug('user %s sleeping for %s', user_id, time_to_sleep)
        time.sleep(time_to_sleep)
