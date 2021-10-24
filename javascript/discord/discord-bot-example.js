/**
 * A simple Discord.js-based Bot demonstrating as simple message
 * based event handling logic whereby server members can say
 * "hello alphabot!" and be greeted in kind.
 *
 * @version 10/24/2021
 * @author @alpazwest
 */
// Load token from .env file
// Note: requires valid Discord application token to be 
// present in a file named .env in project root.
require('dotenv').config()

// Import necessary Discord.js classes
const { Client, Intents } = require('discord.js');

// Instantiate new client object with desired Intents
const client = new Client(
    { intents: [Intents.FLAGS.GUILDS, Intents.FLAGS.GUILD_MESSAGES] });

// Authenticate via environment variable having been loaded
// via the dotenv.config() call earlier.
client.login(process.env.DISCORD_TOKEN)

// Notify successful connection via console
client.on('ready', function(e){
    console.log(`Logged in as ${client.user.tag}!`)
})

// Wait for message events, check content for match,
// respond cordially to user via reply.
client.on('message',
    function(msg){
        if(msg.content === "Hello!"){
            msg.reply("Howdy!")
        }
    })
