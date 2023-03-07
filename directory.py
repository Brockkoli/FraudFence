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


async def main():
    while True:
        base_url = input("Enter your URL: ")
        if not base_url.endswith('/'):
            base_url += '/'
        if not base_url.startswith(('http://', 'https://')):
            print(colorama.Fore.RED + "Please include the protocol, https:// or http://" + colorama.Style.RESET_ALL)
        else:
            break

    wordlist_file = "directory-list-lowercase-2.3-medium.txt" # 220560 lines
    # wordlist_file = "common.txt" # 4616 lines
    tasks = []
    rate_limit = 10  # Requests per second
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

if __name__ == "__main__":
    asyncio.run(main())