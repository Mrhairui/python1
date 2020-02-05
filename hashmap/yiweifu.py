class Solution:
    def groupAnagrams(self, strs):
        from collections import defaultdict
        ans = defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()


if __name__ == '__main__':
    solution = Solution()
    strs = ["hos","boo","nay","deb","wow","bop","bob","brr","hey","rye","eve","elf","pup","bum","iva","lyx","yap","ugh",
            "hem","rod","aha","nam","gap","yea","doc","pen","job","dis","max","oho","jed","lye","ram","pup","qua","ugh",
            "mir","nap","deb","hog","let","gym","bye","lon","aft","eel","sol","jab"]
    p = solution.groupAnagrams(strs)
    print(p)






