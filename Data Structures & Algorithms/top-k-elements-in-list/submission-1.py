class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        seen = {}

        for num in nums:
            if num in seen:
                seen[num] +=1
            else:
                seen[num] = 1

        liste_couples = list(seen.items())

        liste_triee = sorted(liste_couples, key=lambda x: x[1], reverse=True)

        top_k_couples = liste_triee[:k]

        resultat = [paire[0] for paire in top_k_couples]

        return resultat




        