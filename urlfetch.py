import urllib.request as ur

def get_request(url):
    """Make a get request to a specific url"""
    response = ur.urlopen(url)
    status = response.getcode()

    if status != 200:
        # raise an error
        pass
    else:
        # return response
        return response


def extract_html(response):
    """Extract the html from the given response"""
    html = response.read().decode("utf-8")

    return html

def main():
    resp = get_request("https://news.google.com/search?q=london&hl=en-ZA&gl=ZA&ceid=ZA%3Aen")
    print(extract_html(resp))


if __name__ == "__main__":
    main()
