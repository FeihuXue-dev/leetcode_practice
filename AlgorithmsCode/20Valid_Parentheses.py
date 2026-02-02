
def isValid(self, s:str) -> bool:
    """判断字符串中的括号是否有效匹配"""
    stack = ['(', ')', '[', ']', '{', '}']

    for string in s[:-1]:
