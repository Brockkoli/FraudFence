import httpx
import asyncio
from itertools import product
from tqdm import tqdm 
import colorama

colorama.init()

async def make_request(url, sem, word):
    async with sem:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            return response, word


async def directory(base_url):
    try:
        if base_url.startswith("https://"):
                base_url = base_url.strip("https://")
        elif base_url.startswith("http://"):
                base_url = base_url.strip("http://")
        elif base_url.startswith("www"):     
                base_url = base_url.strip("www")
        elif base_url.startswith("https://www"):     
                base_url = base_url.strip("https://www")
        elif base_url.startswith("http://www"):     
                base_url = base_url.strip("http://www")
        base_url = "https://www." + base_url

        if not base_url.endswith('/'):
            base_url += '/'

        print("-" * 50)
        print("Directory busting for: " + colorama.Fore.YELLOW + base_url + colorama.Style.RESET_ALL)

        # wordlist_file = "directory-list-lowercase-2.3-medium.txt" # 220560 lines
        wordlist_file = "common.txt" # 4616 lines
        tasks = []
        rate_limit = 10  # Requests per second
        # limit rate limit to be less sus
        sem = asyncio.Semaphore(rate_limit)

        with open(wordlist_file, 'r') as f:
            wordlist = [line.strip() for line in f]

        total = len(wordlist)
        progress_bar = tqdm(total=total, desc='Progress', position=0, leave=False)

        success_count = 0
        successes = []

        for word in wordlist:
            url = base_url + word
            tasks.append((url, sem, word))

        for task in asyncio.as_completed([make_request(*t) for t in tasks]):
            try:
                response, word = await task
                if response.status_code < 400:
                    # check for custom page not found 
                    if "404 Not Found" or "does not exit" in response.text:
                        tqdm.write("Failure (Custom Error): " + colorama.Fore.RED + f"{response.url}"  + colorama.Style.RESET_ALL + f"   Word: {word}")
                        success_count = 0
                    else:
                        tqdm.write("Success: " + colorama.Fore.GREEN + f"{response.url}"  + colorama.Style.RESET_ALL + f"   Word: {word}")
                        success_count += 1
                        # append found directories to successes list
                        successes.append(response.url)
                        if success_count == 20:
                            print("20 consecutive successful scan. Like FALSE POSITIVES due to custom error page or server configuration. Edit response text in line 40 to attempt bypassing of custom error page.")
                            break
                else:
                    tqdm.write("Failure: " + colorama.Fore.RED + f"{response.url}"  + colorama.Style.RESET_ALL + f"   Word: {word}")
                progress_bar.update(1)
            except httpx.HTTPError:
                progress_bar.update(1)
                print(httpx.HTTPError)
                pass

        progress_bar.close()

        print("\nFound URLs:")
        for url in successes:
            print(colorama.Fore.GREEN + url + colorama.Style.RESET_ALL)

        checker = input("Do you wish to continue? (Y/N) ")
        if checker == "y":
            return True
        else:
            return False
        
    except KeyboardInterrupt:
            print("\nExiting program...")
            exit()