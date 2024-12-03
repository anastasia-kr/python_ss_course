import requests
import tiktoken

# url = 'https://www.credit-land.com/grocery-rewards-credit-cards.php'
# input_html = requests.get(url).text


def count_tokens(html):
    encoding = tiktoken.encoding_for_model('gpt-4o')
    num_tokens = len(encoding.encode(html))
    return num_tokens


r = count_tokens('Hello, world!')
print(r)
