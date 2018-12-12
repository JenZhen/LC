#!/usr/local/bin/python3

# https://www.lintcode.com/problem/url-parser/description?_from=ladder&&fromId=8
# Example
# 分析一段html语言中的网址
#
# 样例
# <html>
#   <body>
#     <div>
#       <a href="http://www.google.com" class="text-lg">Google</a>
#       <a href="http://www.facebook.com" style="display:none">Facebook</a>
#     </div>
#     <div>
#       <a href="https://www.linkedin.com">Linkedin</a>
#       <a href = "http://github.io">LintCode</a>
#     </div>
#   </body>
# </html>
# 需要返回
#
# [
#   "http://www.google.com",
#   "http://www.facebook.com",
#   "https://www.linkedin.com",
#   "http://github.io"
# ]

"""
Solution:
正则表达式

Corner cases:
"""
class HtmlParser:
    """
    @param: content: content source code
    @return: a list of links
    """
    def parseUrls(self, content):
        # write your code here
        import re
        # re.I -- ignoring cases
        links = re.findall(r'\s*(?i)href\s*=\s*("|\')+([^"\'>\s]*)', content, re.I)
        print(links)
        links = [link[1] for link in links if len(link[1]) and not link[1].startswith('#')]
        return links


# Test Cases
if __name__ == "__main__":
    solution = Solution()
