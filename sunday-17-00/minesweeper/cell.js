

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
        console.log("sdfsd")
        if(this.#isRevealed) return
        this.#isRevealed = true

        if (this.#hasMine){
            this.#element.style.backgroundColor = "yellow";
            // newGame()
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
        this.#element.innerHTML = `<p>${this.#neighbouringBombs}</p>`;
        
    }



    revealEmptySpace(x,y){
        let cell = this.#board[y][x]
        if (cell.hasMine() || cell.getNeighbouringBombs() > 0 || cell.isRevealed()){
            return
        }

        const CORDS = [
            [x -1, y-1], [x-1, y],  [x-1, y+1],
            [x, y-1],              [x, y+1],
            [x+1,y-1], [x+1, y],  [x+1, y+1]
        ];
    
        for(let [x, y] of CORDS){
            if (x >= 0 && y >= 0 && y < this.#board.length && x < this.#board[y].length) {
            let nearCell = this.#board[y][x]
            if (nearCell.isRevealed()){
                nearCell.openCell()
            }

            this.revealEmptySpace(x,y)
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
