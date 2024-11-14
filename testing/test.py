import requests
import re
import time

def get_title_from_web(url, retries=3, delay=2):
    for attempt in range(retries):
        try:
            response = requests.get(url, timeout=5)  # Adding a timeout to avoid hanging
            response.raise_for_status()

            title_match = re.search(r'<title>(.*?)</title>', response.text, re.IGNORECASE)
            if title_match:
                title = title_match.group(1).strip()
                return title
            else:
                return "No title found"
        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt + 1 == retries:
                return f"An error occurred: {e}"
            time.sleep(delay)  # Delay before retrying


web_url = "http://localhost:5000"
title = get_title_from_web(web_url)
# print(title)
try:
    assert title == "Form Absensi Mahasiswa"
except AssertionError:
    print(f"Assertion failed. Expected: 'Form Absensi Mahasiswa', but got: '{title}'")
    raise
assert title == "Form Absensi Mahasiswa"
print("Testing success")