// 6! = 6*5*4*3*2*1

function fact(num){
    if (num === 0){
        return 1
    }else{
        return num * fact(num-1)
    }
}

let a = 1
let numbers = [1,2,3,4,5,6] 


function add(numbers){
    if (numbers.lenght === 0) {
        return 0;
    }
    let first = numbers.splice(1)
    return first + add(numbers);
}