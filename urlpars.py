from urlparse2 import urlparse

def parse_url(url):
    parsed = urlparse(url)
    if parsed.scheme:
        return url
    else:
        pass

def parse_domain(url):
    parsed = urlparse(url)
    if parsed.scheme:
        return parsed.hostname

