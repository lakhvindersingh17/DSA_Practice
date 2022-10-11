class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        carry=0
        aReveresed=a[::-1]
        breserved=b[::-1]
        index=0
        result=""
        while(True):
            if index<len(a) and index<len(b):
                
                sum=int(aReveresed[index])+int(breserved[index])+carry
                result+=str(sum%2)
                carry=sum//2
                index+=1
                
            elif index<len(a):
                sum=int(aReveresed[index])+carry
                result+=str(sum%2)
                carry=sum//2
                index+=1
            elif index<len(b):
                sum=int(breserved[index])+carry
                result+=str(sum%2)
                carry=sum//2
                index+=1
            else:
                if carry!=0:
                    result+=str(carry)
                return result[::-1]
            
        return ""
                    
                
        