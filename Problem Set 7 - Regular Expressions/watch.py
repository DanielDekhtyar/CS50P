# Learning Python with CS50
# Watch on YouTube
# https://cs50.harvard.edu/python/2022/psets/7/watch/


import re


def main():
    print(parse(input("HTML: ")))


def parse(html):
    html.strip()
    url = re.search(r'src="https?://(?:www\.)?youtube.com/embed/([^"]+)"', html)
    if url:
        return f"https://youtu.be/{url.group(1)}"
    else:
        return None


if __name__ == "__main__":
    main()