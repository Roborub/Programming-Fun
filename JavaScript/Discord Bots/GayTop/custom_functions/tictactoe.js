function tictactoe(){
	debugger;
	
	let _board = 	"123456789";
	let _player = 	"X";
	let _turn = 	0;
	let _channel = 	null;
	let _bot =		null;
	let _playing = 	false;

	const xWin = /x..x..x..|.x..x..x.|..x..x..x|xxx......|...xxx...|......xxx|x...x...x|..x.x.x../i;	
	const oWin = /o..o..o..|.o..o..o.|..o..o..o|ooo......|...ooo...|......ooo|o...o...o|..o.o.o../i;	// Matthias' Work

	return function(bot, message, channel){
		debugger;
		_playing = 	true;
		_channel = 	channel;
		_bot = 		bot;
		if (_turn === 0){
			_channel.send("Challenge me to a game of tictactoe huh? GET SET FAGGOT");
			_channel.send("Tell me where you want to put it. 1 to 9");
			printBoard(_channel);
		}else{
			if(!/[1-9]/.test(message)){
				_channel.send("Dude, type in 1 to 9. \nHave you ever played this game before? hah.");
				return;
			}else{
				makeMove(message);
				if(_playing){
					_bot.setTimeout(()=>{
						const positions = _board.split("").filter(c=>{
							return Number.isInteger(Number(c));
						});
						makeMove(positions[Math.floor(Math.random() * positions.length)]);
					}, 2000, null);
				}else{
					return;
				}
			}
		}	
	}
	
	function makeMove(pos){
		const posNum = Number(pos);
		if(Number.isInteger(Number(_board.charAt(posNum - 1)))){
			_board = _board.replace(pos, _player);
		}else{
			_channel.send("How about you choose a space that WE DIDN'T ALREADY PLAY.");
		}
		printBoard();
	}

	function printBoard(){
		if(xWin.test(_board) || oWin.test(_board)){
			return win();
		}else if (/\D{9}/.test(_board)){
			return tie();
		}
		_player = ((_player === "X") ? "X" : "O");
		_turn++;
		const boardArr = _board.split("");
		const message = boardArr.reduce((a,c,i)=>{
			c = c + " " + (((i + 1) % 3 === 0) ? "\n" : "| ");
			return a + c;
		}, "");
		_channel.send(message);
	}

	function win(){
		const winMessage = (_player === "X")? "You.. FUCKING CHEATED DUDE..." : "Hah I knew you were too weak to win." ;
		_channel.send(winMessage);
		initGame();
		return;
	}

	function tie(){
		_channel.send("Tie game.");
		initGame();
		return;
	}

	function initGame(){
		_board = 	"123456789";
		_player = 	"X";
		_turn = 	0;
		_channel = 	null;
		_bot =		null;
		_playing = 	false;
	}
}

module.exports = {
	name: 'TICTACTOE',
	fn: tictactoe
}