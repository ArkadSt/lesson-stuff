// script.js
import Cell from "./cell.js";

function drawBoard() {
    let board = [];
    let rows = 8;
    let columns = 8;
    
    for(let i = 0; i < rows; i++) {
        let row = [];
        for(let j = 0; j < columns; j++) {
            let field = new Cell();
            document.getElementById("board").appendChild(field.getElement());
            row.push(field.getElement());
        }
        board.push(row);
    }
    generateMines(board);
    console.log(board);
}

function newGame() {
    clearBoard();
    drawBoard();
}

function clearBoard() {
    document.getElementById("board").innerHTML = "";
}

function createButton(text) {
    let newButton = document.createElement("button");
    newButton.innerText = text;
    newButton.classList.add("newButton");
    document.body.appendChild(newButton);
    newButton.addEventListener("click", newGame);
}

// Initialize the game when the module loads
function InitGame() {
    createButton("New Game");
    drawBoard();
}

export { InitGame, newGame, createButton };