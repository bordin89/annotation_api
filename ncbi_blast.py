import logging
import sys
import time

import requests

__all__ = ['blast']

baseUrl = 'https://www.ebi.ac.uk/Tools/services/rest/ncbiblast/'


def _raiser(req: requests.Response) -> None:
    try:
        req.raise_for_status()
    except requests.HTTPError as err:
        logging.exception(f'HTTP request had error response. Message: {err}')
        sys.exit(1)


def _poll_id(job_id: str, polling_frequency) -> None:
    logging.debug('Polling start...')
    result = 'PENDING'
    while result == 'RUNNING' or result == 'PENDING':
        req = requests.get(baseUrl + 'status/' + job_id)
        _raiser(req)
        result = req.text

        if result == 'RUNNING' or result == 'PENDING':
            time.sleep(polling_frequency)
    logging.debug('Polling finished...')


def blast(email: str, title: str, sequence: str, expectation_value: str = '1e-5',
          polling_frequency=10) -> str:
    """ Please provide an email, title, and sequence.

        Optionally provide expectation_value (default='1e-5') and
        polling_frequency (default=10)

        Returns a string which contains the BLAST results in XML format
    """

    params = {'email': email,
              'title': title,
              'sequence': sequence,
              'program': 'blastp',
              'stype': 'protein',
              'database': 'uniprotkb',
              'exp': expectation_value
              }
    url = baseUrl + 'run/'

    # Set the HTTP User-agent.
    req = requests.post(url, data=params)
    _raiser(req)

    return get_result_for_id(req.text, polling_frequency)


def get_result_for_id(job_id: str, polling_frequency) -> str:

    print(f'Getting results for {job_id}')
    # Polls until job is complete
    _poll_id(job_id, polling_frequency)

    # Get the result
    req = requests.get(f'{baseUrl}/result/{job_id}/xml')
    _raiser(req)

    return req.text
