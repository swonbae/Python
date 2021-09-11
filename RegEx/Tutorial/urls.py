import re

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

subbed_urls = pattern.sub(r'\2\3', urls)    # root domain (e.g., google.com)

print(subbed_urls)

# matches = pattern.finditer(urls)

# for match in matches:
#     # print(match.group(0))     # entire match
#     # print(match.group(1))     # www. = subdomain
#     print(match.group(2))       # domain name
#     # print(match.group(3))     # top-level domain