class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        sorted_list = []
        sublist_position = {}

        for word in strs:

            sort_word = sorted(word)
            mot = "".join(sort_word)

            if mot in sublist_position:
                sorted_list[sublist_position[mot]].append(word)
            else:
                sorted_list.append([word])
                sublist_position[mot] = len(sorted_list) - 1

        return sorted_list