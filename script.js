function aaaa(g) {

    if (0 === '0') {
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
    } else if (h < 50){
        console.log("h is less than 50")
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


//while (school != false && day != "saturday"){
//    goToSchool()
//}
function stuff1(){
    console.log("While loop:")
    let x = 0
    while (x < 10){
        console.log(x)
        x++
    }
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
}


function even(num){
    const arr = []
    for (let x = num; x >= 0; x--){
        if (x % 2 === 0){
            arr.push(x)
        }
    }
    return arr
}

//console.log(even(20))
let isHuman = 0
let x = 0
document.addEventListener("DOMContentLoaded", ()=>{
    let btn = document.getElementById("btn")
    btn.addEventListener("mousemove", ()=>{
        isHuman++
        console.log(isHuman)
    })

    btn.addEventListener("click", ()=>{
        if (isHuman >= 4){
            alert("Human")
        }else{
            alert("Bot")
        }
        isHuman = 0

        x++
        console.log("Clicked " + x + " times.")
    })
})






function sum(a,b){
    return a+b
}

function mult(a,b){
    return a*b
}

console.log(mult(5, sum(2,3)) === mult(5, sum(3,2)))

console.log(true)

function loop(){
    let input = prompt("Type command (a,b,c,q): ")
    if (input === 'a'){
        alert("You have chosen a")
    } else if (input === 'b'){
        alert("You have chosen b")
    } else if (input === 'c'){
        alert("You have chosen c")
    } else if (input === 'q'){
        return
    } else {
        alert("invalid command. try again")
    }
    loop()
}

loop()







