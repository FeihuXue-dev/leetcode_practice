from typing import List
def longestCommonPrefix(self, strs:List[str]) -> str:
    """Find the longest common prefix among a list of strings."""
    prefix = strs[0]

    for string in strs[1:]:
        while not string.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""

    return prefix
