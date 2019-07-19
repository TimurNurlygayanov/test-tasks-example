Introduction
------------

This is a simple Python script which helps to find all unactive slack
channels, send message to these channels and archive them.

How To Use The Bot
------------------

 * Create your slack Application and grand all required access to it.
   The bot required access to read and write to channels, and get history
   of each channel.
 * Add the token of your application to "headers" dict. The Token should 
   start with 'xox' text.
 * Run the script and enjoy.
 
Features
--------

 * You can add "do-not-archive" word to topic or purpose of channel to 
   avoid archiving the channel
 * You can add "archive-asap" word to topic or purpose of channel to
   automatically archive it as soon as possible
 * You can find channels with little number of people or without "fresh"
   messages and send notices to these channels that this channel is going to
   be archived soon.
