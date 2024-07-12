import requests
from time import sleep

def download_with_retry(urls):
    results = []
    for url in urls:
        attempts = 3
        while attempts > 0:
            try:
                response = requests.get(url)
                response.raise_for_status()
                results.append(response.content)
                break
            except requests.exceptions.RequestException as e:
                print(f"Error downloading {url}: {e}")
                attempts -= 1
                sleep(1)
                if attempts == 0:
                    results.append(None)
    return results

urls = input("Enter URLs separated by commas: ").split(',')
results = download_with_retry(urls)
for i, content in enumerate(results):
    if content:
        print(f"Content of URL {urls[i]} downloaded successfully.")
    else:
        print(f"Failed to download content of URL {urls[i]}.")
