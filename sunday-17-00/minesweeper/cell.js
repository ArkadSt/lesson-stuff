import  NewGame  from "./newgame.js"

class Cell{

    #element;
    #hasMine;
    #isRevealed;
    #neighbouringBombs;
    #board;
    #x;
    #y;


    constructor(board, x, y){
        this.#element = document.createElement("div");
        this.#element.addEventListener("click", (e) => this.onFieldClick(e))
        this.#element.addEventListener("contextmenu", (e) => {
            e.preventDefault()
            if (!this.#isRevealed) {
                if (this.#element.innerHTML === "<p>🚩</p>") {
                    this.#element.innerHTML = ""; 
                }else{
                    this.#element.innerHTML = "<p>🚩</p>"; 
                }
            }
        })
        this.#element.classList.add("closedField")
        this.#hasMine = false;
        this.#isRevealed = false;
        this.#neighbouringBombs = 0
        this.#board = board
        this.#x = x
        this.#y = y

    }
   

    onFieldClick(e) {
        console.log(`Cell ${this.#x} ${this.#y} clicked!`)

        if (this.#hasMine){
            // debugger;
            for(let i = 0; i < this.#board.length; i++) {
                for(let j = 0; j < this.#board[i].length; j++) {
                    let cell = this.#board[i][j]
                    if (cell.hasMine()){
                        cell.getElement().style.backgroundColor = "yellow";
                    }   
                }
            }
            this.#element.style.backgroundColor = "yellow";
            
            setTimeout(() => {
                alert("You lost!")
                NewGame()
              }, 50); 
            return
        } 


        if (this.#neighbouringBombs === 0){
            
            this.revealEmptySpace(this.#x, this.#y)
        } else {
            this.openCell()
        }
        
    }
    openCell(){
        this.#element.style.backgroundColor = "red";
        this.#isRevealed = true

        if (this.#neighbouringBombs === 0) {
            this.#element.innerHTML = "";
        }else {
            this.#element.innerHTML = `<p>${this.#neighbouringBombs}</p>`;
        }

        console.log()
        if (this.#board.flat().every((cell) => cell.isRevealed() || cell.hasMine())){
            setTimeout(() => {
                alert("Victory!")
                NewGame()
              }, 50); 
        }
        
    }



    revealEmptySpace(x,y){
        //debugger;
        console.log(`Revealing emply space around cell ${x} ${y}`)
        let cell = this.#board[y][x]
        if (cell.hasMine() || cell.isRevealed()){
            console.log(cell.hasMine())
            console.log(cell.isRevealed())
            console.log(`Exiting at ${x} ${y}`)
            return
        }
        cell.openCell()
        const CORDS = [
            [y-1, x-1], [y-1, x],  [y-1, x+1],
            [y, x-1],              [y, x+1],
            [y+1, x-1], [y+1, x],  [y+1, x+1]
        ];
    
        if (cell.getNeighbouringBombs() > 0){
            return
        }

        for(let [r, c] of CORDS){
            if (r >= 0 && c >= 0 && r < this.#board.length && c < this.#board[y].length) {
                this.revealEmptySpace(c, r)
        }
    }
    
    }

    isRevealed(){
        return this.#isRevealed
    }


    setMine(){
        this.#hasMine = true;
    }
    getElement(){
        return this.#element;
    }
    hasMine(){
        return this.#hasMine;
    }
    addNeighbouringBomb(){
        this.#neighbouringBombs++
    }

    getNeighbouringBombs(){
        return this.#neighbouringBombs
    }

}

export default Cell
