from urllib import parse

# data = '{"p": 10000000, "jl": "489", "kw": "java", "kt": "3"}'
# print(data)
#
# """"%7b%22p%22%3a+1%2c+%22jl%22%3a+%22489%22%2c+%22kw%22%3a+%22java%22%2c+%22kt%22%3a+%223%22%7d
# """
# print(parse.quote(string=data, encoding="utf-8"))
# print("%7b%22p%22%3a+1%2c+%22jl%22%3a+%22489%22%2c+%22kw%22%3a+%22java%22%2c+%22kt%22%3a+%223%22%7d")
def url_encode(url):
    return parse.quote(string=url, encoding="utf-8")