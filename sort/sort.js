let myFunc = (arr) => {
    let newArr = [Infinity]
    for (let p = 0; p < arr.length; p++) {
        for (let i = 0; i < arr.length; i++) {
            if (arr[p] < newArr[i]) {
                newArr.splice(i, 0, arr[p])
                break;
            } 
        }
    }
    newArr.pop()
    return newArr
}
es6 = (arr) => {
    return ar
}

console.log(myFunc([1, 3, 5, 6]))