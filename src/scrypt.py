"""Job scraper."""

from bs4 import BeautifulSoup
import requests



def stack_jobs():
    """Use requests and BS to find public twitter profile and harvest information from HTML."""

    job_list = []
    url = 'https://stackoverflow.com/jobs'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    jobs = soup.find_all(class_='-title g-row')
    for idx in jobs:
        # import pdb; pdb.set_trace()
        job_list.append(jobs[idx].text)
    return job_list

if __name__ == '__main__':
    print(stack_jobs())
