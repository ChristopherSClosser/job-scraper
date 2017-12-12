"""Job scraper."""

from bs4 import BeautifulSoup
import requests



def stack_jobs():
    """Use requests and BS to find public twitter profile and harvest information from HTML."""
    try:
        url = 'https://stackoverflow.com/jobs'
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'lxml')
        import pdb; pdb.set_trace()

    except:
        return {'site': 'stackoverflow',
                'empty': 'Not found'
                }


if __name__ == '__main__':
    stack_jobs()
