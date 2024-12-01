function aaaa() {
    if (true) {
        var a = 1
        let b = "jifwoifj fj jfuoiefjoöeusrh"

        //b = 4
        console.log(b)
    }
    var a = 3
    console.log(a)

    let f = 1 === "1"
    let h = 2
    if (h >= 1) {
        console.log("true!")
    } else {
        console.log("false!")
    }

    function mult(a, b) {
        return a * b
    }

    c = mult(3, 4)
    console.log(c)
}
function season(month){
    if (month >= 1 && month <= 2 || month == 12){
        return "winter"
    }

    if (month >=3 && month <=5){
        return "spring"
    }

    if (month >=6 && month <=8){
        return "summer"
    }

    if (month >=9 && month <=11){
        return "autumn"
    }

    return "Invalid month number. Should be in range 1-12"
}

let a = [1,2,3,4]
let b = 1
function func(a, b){
    a[0]=0
    b = 0
}

func(a,b)
console.log("While loop:")
let x = 0
while (x < 10){
    console.log(x)
    x++
}

//while (school != false && day != "saturday"){
//    goToSchool()
//}
console.log("For loop:")
for (let y = 0; y < 10; y++){
    //console.log(y % 2 === 0)
    console.log(y)
}

let e = 0
++e
console.log(e)

const gh = [1,2,3]
console.log(gh)
gh.push(-45)
console.log(gh)
