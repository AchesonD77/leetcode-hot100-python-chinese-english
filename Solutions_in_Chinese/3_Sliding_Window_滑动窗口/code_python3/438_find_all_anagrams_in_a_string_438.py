class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # left滑动窗口左边、result[]我们需要的返回索引list、right滑动窗口右边、Counter字典哈希表=我们需要的need，sliding window 
        left = 0
        result = []

        need = Counter(p)
        window = Counter()

        # 知道长度 -> 用 for 循环
        for right in range(len(s)):
            # 窗口右边 开始滑动
            window[s[right]] += 1 
            # 滑动到 遇到 长度 超过 固定的需要判断的长度 的情况
            if right - left + 1 > len(p):
                # 删除窗口最左边，并窗口左边 右滑
                window[s[left]] -= 1
                # 判断左边去除的值 是否 value为0，字母数为0
                if window[s[left]] == 0:
                    del window[s[left]]
                # 窗口左边 右滑，保持长度
                left += 1
            
            # 如果长度相等：如果字典的 键值都相等
            if right - left + 1 == len(p):
                if window == need:
                    # 存入此时的左边的left值 为该异位词的起始索引
                    result.append(left)
        return result
            


