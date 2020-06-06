const Discord = require("discord.js");
const bot = new Discord.Client();
const Auth = require("./auth.json");
const fs = require("fs");
const commandPath = "./custom_functions";
const prefix = "!GT_";


const commandFiles = fs.readdirSync(commandPath).filter(f=>f.endsWith(".js"));
bot.commands = new Discord.Collection();

for (const file of commandFiles){
	const command = require(`${commandPath}/${file}`);
	bot.commands.set(command.name, command.fn);
}

let ticTacToe = bot.commands.get("TICTACTOE")(); // Closure to keep track of data in tictactoe board

bot.on("ready", ()=>{
	console.log("logged in.");
});

bot.on('message', msg => {
  	if(msg.content.toUpperCase().startsWith(prefix) & !msg.author.bot){
  		const message =	msg.content.trim();
  		const com = message.toUpperCase().split(" ")[0].replace(prefix, "");
  		const args = message.replace(/^\!gt_.*\s|^\!gt_.*\s*/i, "");

  		switch(com.toUpperCase()){
  			case "TICTACTOE":
				ticTacToe(bot, args.trim(), msg.channel);
  				break;
			default:
				msg.channel.send("That's not a correct command my dude.");
  		}
  	}
});

bot.login(Auth.token);