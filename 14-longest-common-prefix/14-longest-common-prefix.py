class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        minStr=min(strs)
        maxStr=max(strs)
        
        # if minStr==maxStr:
        #     return minStr
        
        for i in range(len(minStr)):
            if minStr[i]!=maxStr[i]:
                return minStr[:i]
            
        return minStr  
#         limit=min(strs)
        
#         stringSet=set()
        
#         for i in range(len(limit)):
#             for str in strs:
                
#                 stringSet.add(str[i])
             
            
#             if len(stringSet)==(i+1):
#                 continue
#             else:
#                 return limit[:i]
         
#         if len(stringSet)==0:
#             return ''
#         return limit
        
        