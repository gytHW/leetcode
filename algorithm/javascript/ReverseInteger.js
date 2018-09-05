/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
    var arr = x.toString().split('')
    if(arr[0] == "-")
    {
        newarr = arr.slice(1).reverse().join('')
        newarr = "-" + newarr
    }
    else
    {
        newarr = arr.reverse().join('')
    }
    
    newarr = parseInt(newarr)
    if(newarr > 2**31-1 || newarr < -(2**31))
        return 0
    else
        return newarr
    
};
