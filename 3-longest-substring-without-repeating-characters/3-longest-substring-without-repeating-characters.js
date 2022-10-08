/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    
    let length=s.length
    
    let maxLength= s!==""?1:0
    
    let i =0
    let newSet= new Set()
    while (i<= length){
    
        if(newSet.size>maxLength) maxLength=newSet.size
        if (!newSet.has(s.charAt(i))){
            newSet.add(s.charAt(i))
            i++
        }
        else {
            // if(newSet.size>maxLength) maxLength=newSet.size
            
            let repeatedCharIndex=Array.from(newSet).indexOf(s.charAt(i))
             i = i - (newSet.size - repeatedCharIndex) + 1;
            newSet=new Set()               
        }
        
    }
    
    
    return maxLength
    
};