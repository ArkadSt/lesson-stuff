// script.js

// 1. Поле +
// 2  Генерация рандомных мин по карте +
// 3. Логика нажатия на клетки +
//     1. Открыть клетку +
//         Сосчитать мины и показать число.
//     2. Взорвать бомбу и закончить игру.
//     3. Поставить флажок (правая кнопка мыши)
// 4. Завершить игру если все безопасные поля открыты или если нажал на мину. -
// 5. Автоматически открывать пустые зоны. -
// 6. Кнопка начать новую игру +
import  NewGame  from "./newgame.js"
import Cell from "./cell.js";
//import generateMines from "./randombombs.js";
function generateMines(board, minesCount, rows, columns) {
    let minesLeft = minesCount;

    while (minesLeft > 0) {
        let r = Math.floor(Math.random() * rows);
        let c = Math.floor(Math.random() * columns);

        let cell = board[r][c]
        if (!cell.hasMine()){
            cell.setMine()
            minesLeft -= 1
        } 

    }

    
}

function drawBoard(rows, columns, mines) {
    let board = [];
    // console.log("ROWS:" + rows)
    // console.log("Columns:" + columns)
    // console.log("Mines:" + mines)

    document.getElementById("board").style = `grid-template-columns: repeat(${columns}, 50px)`

    
    for(let i = 0; i < rows; i++) {
        let row = [];
        for(let j = 0; j < columns; j++) {
            let field = new Cell(board, j, i);
            document.getElementById("board").appendChild(field.getElement());
            row.push(field);
        }
        board.push(row);
    }
    generateMines(board, mines, rows, columns);
    calculationAroundBombs(board)

    // for(let i = 0; i < rows; i++) {
    //     for(let j = 0; j < columns; j++) {
    //         let cell = board[i][j]
    //         console.log(cell.hasMine())
    //         if (cell.hasMine()){
    //             cell.getElement().innerHTML = `<p>*</p>`
    //         } else {
    //             cell.getElement().innerHTML = `<p>${cell.getNeighbouringBombs()}</p>`
    //         }
                
    //     }
    // }

    console.log(board);
}

// function newGame() {
//     clearBoard();
//     drawBoard();
// }

function clearBoard() {
    document.getElementById("board").innerHTML = "";
}

function createButton(text) {
    let newButton = document.createElement("button");
    newButton.innerText = text;
    newButton.classList.add("newButton");
    document.body.appendChild(newButton);
    newButton.addEventListener("click", NewGame);
}

// Initialize the game when the module loads
function InitGame() {
    createButton("New Game");
    drawBoard();
}

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



function calculationAroundBombs(board){
    for(let i=0; board.length > i; i++){
        for(let j=0; board[i].length > j; j++){
            if(board[i][j].hasMine()){
                const cords = [
                    [i-1, j-1], [i-1, j],  [i-1, j+1],
                    [i, j-1],              [i, j+1],
                    [i+1, j-1], [i+1, j],  [i+1, j+1]
                ];
                for (let k = 0; k < cords.length; k++){
                    let r = cords[k][0];
                    let c = cords[k][1];
                    // TODO check if r and c are in the board (try-catch)
                    try{
                        board[r][c].addNeighbouringBomb();
                    } catch (e) {}
                }

            }

        }

    }
}

export { InitGame, createButton, drawBoard, clearBoard };