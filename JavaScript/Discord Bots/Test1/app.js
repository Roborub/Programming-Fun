const Discord = 		require('discord.io');
const Auth = 			require('./auth.json');
const Data = 			require('./data.json');
const CustomFunctions = require('./customFunctions.js');

// Initialize Bot
const bot = new Discord.Client({
    token: Auth.token,
    autorun: true
});
bot.on('ready', ()=>{
	console.log("Bot has started.\n\n");
});

// Bot Behaviour
bot.on('message', (user, userID, channelID, message, event)=>{
	if (userID !== Auth.bot.id){
		switch(message.split(" ")[0].toUpperCase()){
			case Data.prefixes.talk:
				CustomFunctions.talk(message, bot, channelID);
				break;
			case Data.prefixes.music:
				CustomFunctions.playSong(bot, message.replace(/\!gaybott_music/gi, ""), channelID);
				break;
			case Data.prefixes.leave:
				bot.disconnect();
				break;
			case Data.prefixes.game:
				CustomFunctions.playGame(bot, message);
				break;
			case Data.prefixes.dog:
				CustomFunctions.getDog(bot, message, channelID);
				break;
			case Data.prefixes.help:
				CustomFunctions.getHelp(bot, channelID);
				break;
			case Data.prefixes.avatar:
				CustomFunctions.setAvatar(bot, message);
				break;
			default:
				console.error("No prefix was matched");
		}
	}
});