import codecs
from lxml import html

import sys

archive = html.parse('http://thelocalteaparty.com/archive').getroot()
permalinks = [a.attrib['href'] for a in archive.cssselect("#content > a.regular.brick")]

output = codecs.open(sys.argv[1], "w", encoding="utf-8")

for permalink in permalinks:
    post = html.parse(permalink).getroot()
    content = post.cssselect(".bodytype")[0].text_content()
    output.write(content + "\n")
