let minesCount = 10;
let minesLocation = [];

function generateMines(board) {
    let minesLeft = minesCount;

    while (minesLeft > 0) {
        let r = Math.floor(Math.random() * 8);
        let c = Math.floor(Math.random() * 8);
        let id = r.toString() + "-" + c.toString();
        
        if (!minesLocation.includes(id)/*board[r][c].classList*/) {
            minesLocation.push(id);//board[r][c].classList.add()
            minesLeft -= 1;
        }
    }
}

generateMines();

console.log("Mines generated:", minesLocation)
