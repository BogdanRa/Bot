from urlparse2 import urlparse

def parse_url(url):
    parsed = urlparse(url)
    if parsed.scheme:
        return url
    else:
        pass

