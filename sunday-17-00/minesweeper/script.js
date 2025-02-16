

function onFieldClick(event) {
	event.target.style.backgroundColor = "red";
}

function drawBoard(){
	let board = [];
	let rows = 8;
	let columns = 8;

	for(let i = 0; i < rows; i++) {
		let row = [];
		for(let j = 0; j < columns; j++) {
			let field = document.createElement("div");
			field.classList.add("closedField")
			field.classList.add("field")
			field.addEventListener("click", onFieldClick)
			document.getElementById("board").appendChild(field)
			row.push(field)
		}
		board.push(row)
	}
	//generateMines(board)
	console.log(board)
}

function newGame(){
	clearBoard()
	drawBoard()
}
function clearBoard(){
	document.getElementById("board").innerHTML = ""
	
}

function createButton(name){
	let newButton = document.createElement("button")
	newButton.innerText = name
	newButton.classList.add("newButton")
	document.body.appendChild(newButton)
	newButton.addEventListener("click", newGame)
}