// import Cell from "./cell";

// let minesCount = 10;

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
// let cell = board[r][c] - как получать объект клетки по координатам r, c
// cell.setMine() - установить мину
// cell.hasMine() -> true/false - проверить есть ли мина

// function generateMines(board) {
//     let minesLeft = minesCount;

//     while (minesLeft > 0) {
//         let r = Math.floor(Math.random() * 8);
//         let c = Math.floor(Math.random() * 8);

//         let cell = board[r][c]
//         if (!cell.hasMine()){
//             cell.setMine()
//             minesLeft -= 1
//         } 

//     }

    
// }

// export default generateMines;

