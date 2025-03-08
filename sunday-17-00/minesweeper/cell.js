class Cell{

    #element;
    #hasMine;
    #isRevealed;
    #isFlagged;
    #neighbouringBombs;
    

    constructor(){
        this.#element = document.createElement("div");
        this.#element.addEventListener("click", this.#onFieldClick)
        this.#element.classList.add("closedField")
        this.#hasMine = false;
        this.#isRevealed = false;
        this.#isFlagged = false;
        this.#neighbouringBombs = 0
    }

    #onFieldClick(event) {
        event.target.style.backgroundColor = "red";
        if (this.#hasMine ){
            event.target.style.backgroundColor = "yellow";
        } else {
            event.target.innedHTML = `<p>${this.#neighbouringBombs}</p>`;
        }
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

}

export default Cell
