#! /usr/local/bin/python3

# https://www.lintcode.com/problem/department-statistics/description?_from=ladder&&fromId=156
# Example
# 公司给你提供了所有员工的信息，包括其ID，姓名和所属部门。
# 以及他们之间的朋友关系，每个关系中由2个ID组成，如 "1, 2" 代表1号员工和2号员工是朋友。
# 朋友关系不具有传递性，即B、C都是A的朋友，但B和C不一定是朋友。
# 请计算每个部门中与其它部门的员工有朋友关系的员工个数。
#
# 样例
# 样例输入:
# employees = [
#   "1, Bill, Engineer",
#   "2, Joe, HR",
#   "3, Sally, Engineer",
#   "4, Richard, Business",
#   "6, Tom, Engineer"
# ]
#
# friendships = [
#   "1, 2",
#   "1, 3",
#   "3, 4"
# ]
# 样例输出:
# "Engineer: 2 of 3"
# "HR: 1 of 1"
# "Business: 1 of 1"
# 说明
# 样例中，Engineer的1号员工和HR的2号员工是朋友关系，3号员工和Business的4号员工是朋友关系，所以Engineer有2个人和其它部门有朋友关系，输出"Engineer: 2 of 3“。
#
# 注意事项
# 所有的输入中逗号后都跟有一个空格，而且你的程序输出也要和样例格式相同。
# 返回的列表对顺序没有要求。
# 员工信息数量 N <= 50 条。
# 朋友关系的数量 M <= 1000 条。
# 员工ID都是100以内的数字。
# 部门数 K <= 20。
"""
Algo: hashmap
D.S.:

Solution:


Corner cases:
"""

class Solution:
    """
    @param employees: information of the employees
    @param friendships: the friendships of employees
    @return: return the statistics
    """
    def departmentStatistics(self, employees, friendships):
        # write your code here.
        dept2id = {}
        id2dept = {}
        deptfriends = {}
        for e in employees:
            info = e.split(',')
            id, dept = info[0].strip(), info[2].strip()
            if dept not in dept2id:
                dept2id[dept] = set()
            dept2id[dept].add(id)
            id2dept[id] = dept

        for dept in dept2id:
            deptfriends[dept] = set()

        for f in friendships:
            info = f.split(',')
            id1, id2 = info[0].strip(), info[1].strip()
            dept1, dept2 = id2dept[id1], id2dept[id2]
            if dept1 == dept2:
                continue
            deptfriends[dept1].add(id1)
            deptfriends[dept2].add(id2)
        res = []
        for dept, ids in dept2id.items():
            res.append(dept + ': ' + str(len(deptfriends[dept])) + ' of ' + str(len(ids)))
        return res

# Test Cases
if __name__ == "__main__":
    solution = Solution()
