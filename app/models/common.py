import re

def slugify(s):
    return re.sub(r'[^\w+]', "-", s)