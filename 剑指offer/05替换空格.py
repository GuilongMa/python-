class Solution:
    def replaceSpace(self, s: str) -> str:
        str_list = s.split(" ")
        return "%20".join(str_list)