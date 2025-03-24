import { clearBoard, drawBoard } from "./script.js"

function NewGame() {


    let rows = document.getElementById("number_of_rows").value
    let columns = document.getElementById("number_of_columns").value
    let mines = document.getElementById("number_of_mines").value

    // console.log(rows, columns, mines)
    // document.getElementById("board")
    
    clearBoard();
    drawBoard(rows, columns, mines);
}

export default NewGame