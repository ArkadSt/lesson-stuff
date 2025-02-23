class Cell{

    #element;
    #hasMine;
    #isRevealed;
    #isFlagged;
    

    constructor(){
        this.#element = document.createElement("div");
        this.#element.addEventListener("click", this.#onFieldClick)
        this.#element.classList.add("closedField")
        this.#hasMine = false;
        this.#isRevealed = false;
        this.#isFlagged = false;
    }

    #onFieldClick(event) {
        event.target.style.backgroundColor = "red";
    }
    setMine(){
        this.#hasMine = true
    }
    getElement(){
        return this.#element;
    }
    hasMine(){
        return this.#hasMine
    }

}

export default Cell
