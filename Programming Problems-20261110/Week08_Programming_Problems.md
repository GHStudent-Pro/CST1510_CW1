# Week 8 – Pulling Real Data – Programming Problems

## Task 1: First API Request

Install `requests` (`pip install requests`). Send a GET request to `https://jsonplaceholder.typicode.com/posts/1` and print the status code and the `title` of the post (use `response.json()`).

## Task 2: Parsing a JSON List

Request `https://jsonplaceholder.typicode.com/users`. Print the name and email of every user and the total number of users.

## Task 3: Query Parameters

Request `https://jsonplaceholder.typicode.com/posts` passing `params={"userId": 1}`. Print how many posts that user has and the title of each one.

## Task 4: Handling Failed Requests

Request `https://httpbin.org/status/404` and `https://httpbin.org/status/500`. Use `response.raise_for_status()` inside `try`/`except requests.exceptions.HTTPError` and print a friendly message that includes the status code.

## Task 5: Slow Requests and Retries

Request `https://httpbin.org/delay/5` with `timeout=2` and catch `requests.exceptions.Timeout`. Then write a function `get_with_retry(url, attempts=3)` that tries again after a timeout and gives up with a message after the last attempt.

## Task 6: Downloading Files

Download `https://httpbin.org/image/png` and save it as `downloaded.png`, and download `https://httpbin.org/robots.txt` and save it as `robots.txt`. Use `response.content` and `'wb'` mode for the image. Print the size in bytes of each file.

## Task 7: Regex Basics

Using the `re` module on the text below:
1. `re.search` – print the first phone number (format `07xxx xxxxxx`).
2. `re.findall` – print all email addresses.
3. `re.sub` – replace every digit with `*` and print the masked text.

```python
text = "Contact Ann on 07123 456789 or ann@mail.com. Bob: bob@work.org, 07987 654321."
```

## Task 8: Pure Python EDA – Text Extractor
You are given a messy string containing a log report. Extract all the valid IP addresses from it using Regular Expressions, and print a count of how many unique IP addresses were found.

```python
import re

log_data = 'User 192.168.1.1 logged in. Failed login from 10.0.0.55. Connection closed by 192.168.1.1.'
```

## Task 9: Refactor into a Class

Refactor your API code into a class `PostClient`:
- `__init__(self, base_url)` stores the base URL (`https://jsonplaceholder.typicode.com`).
- `get_post(self, post_id)` returns one post as a dictionary.
- `get_user_posts(self, user_id)` returns a list of posts.
- Both methods handle errors and timeouts and return `None` (with a message) on failure.

Write a short main program that creates a `PostClient`, prints one post, and prints how many posts user 3 has.
