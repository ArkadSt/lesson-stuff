import Cell from "./cell";

let minesCount = 10;

// board = [
//     [Cell, Cell, Cell, Cell, Cell, Cell, Cell, Cell],
//     [Cell, Cell, Cell, Cell, Cell, Cell, Cell, Cell],   
//     [Cell, Cell, Cell, Cell, Cell, Cell, Cell, Cell],   
//     [Cell, Cell, Cell, Cell, Cell, Cell, Cell, Cell],   
//     [Cell, Cell, Cell, Cell, Cell, Cell, Cell, Cell],   
//     [Cell, Cell, Cell, Cell, Cell, Cell, Cell, Cell],   
//     [Cell, Cell, Cell, Cell, Cell, Cell, Cell, Cell],   
//     [Cell, Cell, Cell, Cell, Cell, Cell, Cell, Cell],   
// ]

function generateMines(board) {
    let minesLeft = minesCount;

    while (minesLeft > 0) {
        let r = Math.floor(Math.random() * 8);
        let c = Math.floor(Math.random() * 8);
        let id = r.toString() + "-" + c.toString();
        
    }
}

generateMines();

console.log("Mines generated:", minesLocation)
