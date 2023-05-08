import re

def domain_name(url: str):
    url = re.sub(r'^https?://', '', url)
    url = re.sub(r'www.', '', url)
    url = re.split(r'[.]', url)
    return url[0]


domain_names = ["http://github.com/carbonfive/raygun", "http://www.zombie-bites.com", "https://www.cnet.com", "http://google.co.jp"]
for dname in domain_names:
    domain = domain_name(dname)
    print(domain)