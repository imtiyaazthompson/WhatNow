import re
import urlfetch as uf

def get_headline_divs(html):
    hdivs = []

    # (.*) vs (.*?)
    regex = '<h3\sclass=\"ipQwMb\sekueJc\sRD0gLb\">(.*?)</h3>'
    match = re.findall(regex, html)

    return match


def extract_headlines(hdivs):
    headlines = []
    regex = '<a\s+href=\"(.*?)\"\s+class=\"DY5T1d RZIKme\"\s?>(.*?)</a>'

    for i in range(10):
        match = re.search(regex, hdivs[i])

        # Process Link
        gnews = "news.google.com"
        link = match.group(1)
        gnews += link[1:]

        head = re.sub('&#39;','\'',match.group(2))
        headlines.append((gnews, head))

    return headlines


def main():
    html = uf.extract_html(uf.get_request("https://news.google.com/search?q=london&hl=en-ZA&gl=ZA&ceid=ZA%3Aen"))
    print(extract_headlines(get_headline_divs(html)))


if __name__ == "__main__":
    main()
