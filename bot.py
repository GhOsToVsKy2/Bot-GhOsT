import discord
from discord.ext.commands import Bot

przeklenstwa = ["KURWA", "SPIERDALAJ", "FUCK", "IDIOTO", "DEBILU", "STARA", "STARY"]
ms = []
bypass_list = []

Client = discord.Client()
client = discord.ext.commands.Bot(command_prefix = "$")

@client.event
async def on_ready():
    print("Bot jest gotowy!")

@client.event
async def on_message(message):
    contents = message.content.split(" ")
    chat_off = False
    if message.content == "$chat.off":
        await client.send_message(message.channel, "Chat wyłączony!")
        if client.send_message(message.channel):
            await client.delete_message(message)
            chat_off = True
    if message.content == "$cookie":
        await client.send_message(message.channel, ":cookie:")
    if message.content == "$python":
        await client.send_message(message.channel, "python czy to wąż? :joy:")
    if message.content =="$fajny":
        await client.send_message(message.channel, "no i fajnie :D")
    if message.content == "$help":
        await client.send_message(message.channel, "'$say' słowa do powtórzenia \n $zdj \n $autor \n $www \n komendy do interrakcji z botem: \n '$cookie' \n '$python' \n '$fajny'")
    if message.content.upper().startswith("$SAY"):
        args = message.content.split(" ")
        #args[0] = SAY
        #args[1] = Witam
        #args[2] = nowego!
        #args[1:] = Witam nowego!
        await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
    if message.content == "$zdj":
        await client.send_message(message.channel, "")
    if message.content == "$autor":
        await client.send_message(message.channel, "Moim autorem jest: GhOsToVsKy!")
    if message.content == "$www":
        await client.send_message(message.channel, "http://ghoforum.cba.pl")
    for word in contents:
        if word.upper() in przeklenstwa:
            if not message.author.id in bypass_list:
                 try:
                     await client.delete_message(message)
                     await client.send_message(message.channel, "Nie przeklinaj!")
                 except discord.errors.NotFound:
                      return
client.run("NDQ5OTI2MDc4NDY3OTMyMTYw.Des8bA.u9thXhH1DkrpZpGQGOhr3GBQ18M")

