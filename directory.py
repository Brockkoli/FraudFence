import httpx
import asyncio
from itertools import product
from tqdm import tqdm 
import colorama

colorama.init()
results = {}

async def make_request(url, sem, word):
    async with sem:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            return response, word


async def directory(base_url):
    try:
        if base_url.startswith("https://www."):     
            base_url = base_url.replace("https://www.", "", 1)
        elif base_url.startswith("http://www."):     
            base_url = base_url.replace("http://www.", "", 1)
        elif base_url.startswith("https://"):
            base_url = base_url.replace("https://", "", 1)
        elif base_url.startswith("http://"):
            base_url = base_url.replace("http://", "", 1)
        elif base_url.startswith("www."):     
            base_url = base_url.replace("www.", "", 1)
        base_url = "https://www." + base_url

        if not base_url.endswith('/'):
            base_url += '/'

        print("-" * 50)
        print("Directory busting for: " + colorama.Fore.YELLOW + base_url + colorama.Style.RESET_ALL)
        print("\n")

        wordlist_file = "y8domain.txt" 
        #wordlist_file = "directory-list-lowercase-2.3-medium.txt" # 220560 lines
        #wordlist_file = "common.txt" # 4616 lines
        tasks = []
        rate_limit = 10  # Requests per second
        # limit rate limit to be less sus
        sem = asyncio.Semaphore(rate_limit)

        with open(wordlist_file, 'r') as f:
            wordlist = [line.strip() for line in f]

        total = len(wordlist)
        progress_bar = tqdm(total=total, desc='Progress', position=0, leave=False)

        success_count = 0
        success_custom_count = 0
        blocked_count = 0
        successes = []
        successes_custom = []
        blocked = []

        for word in wordlist:
            url = base_url + word
            tasks.append((url, sem, word))

        for task in asyncio.as_completed([make_request(*t) for t in tasks]):
            try:
                response, word = await task
                if response.status_code < 400:
                    # check for custom page not found 
                    if response.status_code == 302:
                        success_count = 0
                        tqdm.write("Redirect (Custom Page): " + colorama.Fore.MAGENTA + f"{response.url}"  + colorama.Style.RESET_ALL + f"   Word: {word}")
                        success_custom_count += 1
                        successes_custom.append(response.url)
                    elif response.status_code == 200 and ("Page not found" or "404 not found" or "does not exist" in response.text):
                        tqdm.write("Page not found (Custom Page): " + colorama.Fore.MAGENTA + f"{response.url}"  + colorama.Style.RESET_ALL + f"   Word: {word}")
                        success_custom_count += 1
                        successes_custom.append(response.url)
                    elif response.status_code == 200:
                        tqdm.write("Success: " + colorama.Fore.GREEN + f"{response.url}"  + colorama.Style.RESET_ALL + f"   Word: {word}")
                        success_count += 1
                        results[response.url]="Success"
                        # append found directories to successes list
                        successes.append(response.url)
                        if success_count == 10:
                            print(colorama.Fore.RED + "\n\n10 consecutive successful scan.")
                            print("!!! Likely FALSE POSITIVES due to custom error page or server configuration !!!\n" + colorama.Style.RESET_ALL)
                            break
                    else:
                        tqdm.write("Redirect (Likely to exist): " + colorama.Fore.YELLOW + f"{response.url}"  + colorama.Style.RESET_ALL + f"   Word: {word}")
                        results[response.url] = "Redirect (Likely to exist)"
                        blocked_count += 1
                        blocked.append(response.url)
                else:
                    tqdm.write("Failure: " + colorama.Fore.RED + f"{response.url}"  + colorama.Style.RESET_ALL + f"   Word: {word}")
                progress_bar.update(1)
            except httpx.HTTPError:
                progress_bar.update(1)
                pass

        progress_bar.close()

        if len(successes) != 0 and success_count != 20:
            print("\nFound directories:")
            for url in successes:
                print(colorama.Fore.GREEN + str(url) + colorama.Style.RESET_ALL)

        # if len(successes_custom) != 0:
        #     print("\nPage not found (customised page):")
        #     for url in successes_custom:
        #         print(colorama.Fore.MAGENTA + str(url) + colorama.Style.RESET_ALL)

        if len(blocked) != 0:
            print("\nRedirected directories found (likely to exist):")
            for url in blocked:
                print(colorama.Fore.YELLOW + str(url) + colorama.Style.RESET_ALL)
        
        print("Directory scanning completed!")
        sorted_results = dict(sorted(results.items(), key=lambda x: x[1], reverse=True))
        return sorted_results

    except KeyboardInterrupt:
            print("\nExiting program...")
            exit()

    except:
        print(" Directory scanning not available.")
    