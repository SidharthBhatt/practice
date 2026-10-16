from collections import Counter
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        my_dict = {}
        for index, word in enumerate(strs):
            countedWord = tuple(sorted(Counter(word).items()))
            small_list = []
            if countedWord in my_dict:
                small_list = my_dict[countedWord]
                small_list.append(index)
            else:
                small_list.append(index)
            my_dict[countedWord] = small_list
        big_list = []
        for key, value in my_dict.items():
            group_anagram = []
            for pos in value:
                group_anagram.append(strs[pos])
            big_list.append(group_anagram)
        return big_list



        