/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isSubsequence = function(s, t) {
    
    let indexofT=0
    for (let i of t){
        
        if(i===s.charAt(indexofT)) indexofT+=1
    }
    
    if(indexofT===s.length) return true
    
    return false
    
};