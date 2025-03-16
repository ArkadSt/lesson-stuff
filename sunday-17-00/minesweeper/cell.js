

class Cell{

    #element;
    #hasMine;
    #isRevealed;
    #isFlagged;
    #neighbouringBombs;
    #board;
    #x;
    #y;
    

    constructor(board, x, y){
        this.#element = document.createElement("div");
        this.#element.addEventListener("click", () => this.onFieldClick())
        this.#element.classList.add("closedField")
        this.#hasMine = false;
        this.#isRevealed = false;
        this.#isFlagged = false;
        this.#neighbouringBombs = 0
        this.#board = board
        this.#x = x
        this.#y = y
    }
    


    onFieldClick() {
        console.log(`Cell ${this.#x} ${this.#y} clicked!`)
        if(this.#isRevealed) return
        //this.#isRevealed = true

        if (this.#hasMine){
            this.#element.style.backgroundColor = "yellow";
            // Game over alert + newGame()
            return
        } 
        this.#element.style.backgroundColor = "red";
        this.#element.innerHTML = `<p>${this.#neighbouringBombs}</p>`;

        

        if (this.#neighbouringBombs === 0){
            
            this.revealEmptySpace(this.#x, this.#y)
        } else {
            this.openCell()
        }
        
    }
    openCell(){
        //if (this.#isRevealed) return 
        this.#element.style.backgroundColor = "red";
        this.#isRevealed = true
        this.#element.innerHTML = `<p class="">${this.#neighbouringBombs}</p>`;
        
    }



    revealEmptySpace(x,y){
        //debugger;
        console.log(`Revealing emply space around cell ${x} ${y}`)
        let cell = this.#board[y][x]
        if (cell.hasMine() /*|| cell.getNeighbouringBombs() > 0*/ || cell.isRevealed()){
            console.log(cell.hasMine())
            //console.log(cell.getNeighbouringBombs())
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
            // let nearCell = this.#board[r][c]
            // if (nearCell.isRevealed()){
            //     nearCell.openCell()
            // }
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
