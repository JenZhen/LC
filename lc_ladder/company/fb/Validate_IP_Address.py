#! /usr/local/bin/python3

# https://www.lintcode.com/problem/validate-ip-address/description
# Example
# 实现一个函数来检查输入字符串是一个合法的IPv4地址，还是一个合法的IPv6地址，抑或是两者都不是。
#
# IPv4地址被规范地表示为点分十进制，包含四个取值为0到255的十进制数，其间使用点号(".")来进行分隔，例如，172.16.254.1；
#
# 此外，前导零在IPv4地址中是非法的。例如，地址172.16.254.01就是非法的。
#
# IPv6地址被表示为十六进制数位，每4个十六进制数位归为一组，共八组，每组可表示16个二进制位。每组之间使用冒号(":")来进行分隔。例如，地址2001:0db8:85a3:0000:0000:8a2e:0370:7334是合法的。同时，去掉每组十六进制数位中的一些前导零，或是将表示十六进制数位的小写字母写作大写字母，也都是合法的，所以2001:db8:85a3:0:0:8A2E:0370:7334同样是一个合法的IPv6地址（它忽略了前导零同时使用了大写字母）。
#
# 然而，我们不能为了追求简洁就使用两个冒号("::")将连续的值为0的组替换为一个空组。例如，2001:0db8:85a3::8A2E:0370:7334就是一个非法的IPv6地址。
#
# 此外，额外的前导零在IPv6中也是非法的。例如，地址02001:0db8:85a3:0000:0000:8a2e:0370:7334就是非法的。
#
# 样例
# 例1:
#
# 输入："172.16.254.1"
#
# 输出："IPv4"
#
# 说明：这是一个合法的IPv4地址，因此返回"IPv4"。
# 例2:
#
# 输入："2001:0db8:85a3:0:0:8A2E:0370:7334"
#
# 输出："IPv6"
#
# 说明：这是一个合法的IPv6地址，因此返回"IPv6"。
# 例3:
#
# 输入："256.256.256.256"
#
# 输出："Neither"
#
# 说明：这既不是一个合法的IPv4地址，也不是一个合法的IPv6地址，因此返回"Neither"。
# 注意事项
# 你可以假设输入字符串中没有多余的空格或其他特殊字符。
"""
Algo: string manipulation
D.S.:

Solution:

if else corner case,
巧用 try catch


Corner cases:
"""

class Solution:
    """
    @param IP: the given IP
    @return: whether an input string is a valid IPv4 address or IPv6 address or neither
    """
    def validIPAddress(self, IP):
        # Write your code here
        ip = IP.split('.')
        if len(ip) == 4:
            # ipv4 candidate now validate
            for octet_s in ip:
                try:
                    octet = int(octet_s)
                except ValueError:
                    return 'Neither'
                if octet < 0 or octet > 255 or (octet_s != '0' and octet_s[0] == '0'):
                    return 'Neither'
            return 'IPv4'
        else:
            # not ipv4 try to split as ipv6
            ip = IP.split(':')
            if len(ip) == 8:
                # ipv6 candidate, validate it
                for hexa_s in ip:
                    if not hexa_s or len(hexa_s) > 4 or not hexa_s[0].isalnum():
                        return 'Neither'
                    try:
                        hexa = int(hexa_s, base=16)
                    except ValueError:
                        return 'Neither'
                    # hexa_redo = '{:x}'.format(hexa)
                    if hexa < 0 or hexa > 65535:
                        return 'Neither'
                return 'IPv6'
        return 'Neither'


# Test Cases
if __name__ == "__main__":
    solution = Solution()
