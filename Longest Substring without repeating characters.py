# LeetCode3 https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        max_length = start = 0
        # 포인터 2개 사용: 포인터1은 start, 포인터2는 index(enumerate함수에 따라서 증가)
        for index, char in enumerate(s):
            # 이미 등장했던 문자라면 start 위치 갱신(쓰인 문자열 다음 위치로)
            if char in used and start <= used[char]:
                start = used[char] + 1
            else:  # 반복문자가 아니라면 최대 부분 문자열 길이 갱신
                max_length = max(max_length, index - start + 1)

            # 현재 문자의 위치 삽입
            used[char] = index

        return max_length