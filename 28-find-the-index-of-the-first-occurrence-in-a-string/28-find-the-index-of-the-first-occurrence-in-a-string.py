class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        needleIndex=0
        
        # needleFoundIndex=-1
        index=0
        while(index<=(len(haystack)-1)):
            if haystack[index]==needle[needleIndex]:
                needleIndex+=1
                
                if needleIndex==(len(needle)):
                    return (index-(needleIndex-1))
                index+=1
            else:
                index=index-(needleIndex)+1
                needleIndex=0
                
                
        return -1        
                
        