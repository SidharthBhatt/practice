from collections import Counter
class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        counts = Counter(words)
        arr = []
        for item, frequency in counts.items():
            arr.append((item,frequency))
        arr = sorted(arr, key=self.sorter)
        result = []
        for item in arr[:k]:
            result.append(item[0])
        return result

    def sorter(self, pair):
        return (-pair[1], pair[0])
        