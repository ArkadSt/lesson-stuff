function getRandomArbitrary(min, max) {
    return Math.floor(Math.random() * (max - min) + min);
}
  
function guess_a_number(){
    let random_number = getRandomArbitrary(0,100)

    for (let i = 7; i > 0; i--){
        user_number = prompt("Enter your guess: ")
        if (user_number > random_number){
            alert("Your number is too big")
        }else if (user_number < random_number){
            alert("Your number is too small")
        }
        if (user_number == random_number){
            alert("You win!")
            break
        }
    }
}

