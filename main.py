import discord
from discord.ext import *

intents = discord.Intents.default()
intents.message_content = True



bot = discord.Bot(intents=intents)


@bot.event
async def on_ready():
    print('Online. Name: {0.user}'.format(bot))
    await bot.change_presence(status=discord.Status.online)


guild = 755866816038961175



help_words = ["help", "install", "stuck"]

@bot.event
async def on_message(ctx):

    if ctx.author == bot.user:
        return

    for i in ctx.content.split(" "):
        if i in help_words:
            await ctx.reply("Do you need help? Open a ticket in #support-tickets, or type in / and look if you see a solution for your problem. If not just ignore this message <3")





find_config_e=discord.Embed(title="find your config (config-xpui.ini) file", description="very helpful for helper", color=0x0400ff)
find_config_e.add_field(name="Solution 1:", value="run ```spicetify config-dir``` in a terminal of your choice (this opens your file explorer at the right location)", inline=False)
find_config_e.add_field(name="Solution 2: ", value="run ```spicetify config``` in a terminal of your choice. What comes back is your config file", inline=False)
find_config_e.add_field(name="Solution 3: ", value='''Search it by yourself:
Pathes:
Windows: `C:/Users/YOUR NAME/AppData/Roaming/spicetify`
Linux: `~/.config/spicetify/config-xpui.ini`
mac: `~/.config/spicetify/config-xpui.ini`''', inline=True)


uninstall_e=discord.Embed(title="Uninstall spicetify", description="D:", color=0x4400ff)
uninstall_e.add_field(name="How 2:", value='''
**First Step (all platforms):**
run ```spicetify restore``` in a terminal
**Second Step (win):**
run each command one after another:
```cd %appdata%```
```rmdir spicetify / /S```
```cd %localappdata%```
```rmdir spicetify /s /S```
''', inline=False)
uninstall_e.add_field(name="Linux + Mac", value='''just run ```rm -rf ~/.spicetify``` and ```rm -rf ~/.config/spicetify```''')


path=discord.Embed(title="prefs/spotify path error", color=0x0033ff)
path.add_field(name="prefs path:", value="open your config file and replace whatever is after ```prefs_path =``` with (win) ```C:/Users/<YOUR USERNAME>/appdata/Roaming/Spotify/prefs``` or (mac) ```/Users/YOUR_USERNAME/Library/Application Support/Spotify/prefs``` or (linux) ```/home/YOUR_USERNAME/.config/spotify/prefs```", inline=False)
path.add_field(name="spotify path:", value='''same thing. But instead of ```prefs_path =``` ```spotify_path =``` and ```C:/Users/<YOUR USERNAME>/appdataRoaming/Spotify``` (for mac its `spotify_path = /Applications/Spotify.app/Contents/Resources`. Linux depends on how you installed spotify''', inline=True)


keyword=discord.Embed(title="Keyword 'Spicetify' Not Recognized In Terminals", description="annoying tbh", color=0x0033ff)
keyword.add_field(name="Step 1:", value="restart your pc (maybe even fixes it)", inline=False)
keyword.add_field(name="Step 2 (windows):", value='''In your search bar type the word ```environment``` an application should appear that says ```edit environment variables for your account``` once opened double click on the "path" header, select new in the right side of the window, and type the path ```C:/Users/USERNAME/appdata/local/spicetify``` make sure to press okay in both windows and not cancel!''', inline=False)
keyword.add_field(name="alternative:", value="cd into your ```%localappdata%``` or  directory", inline=False)
keyword.add_field(name="Linux + Mac", value='''Add the spicetify install directory (e.g. ~/.spicetify) to your $PATH. You can google how to do that for your shell. Modern macOS uses zsh, but you might still be on bash.''')


update=discord.Embed(title="Spotify has blank screen", description="if you see black or sth", color=0x0033ff)
update.add_field(name="Solution:", value="Update your spotify and spicetify to the newest version", inline=False)
update.add_field(name="How excactly:", value="spicetify: run: ```spicetify upgrade``` then ```spicetify backup apply``` Spotify should update automatically", inline=True)


restart_e=discord.Embed(title="Spicetify gone after restart", description="I dont like this one", color=0x0033ff)
restart_e.add_field(name="Solution (both only win):", value="find your spotify shortcut you most often use (this can be on your taskbar, start menu, or desktop, as-long as its a .lnk file) You'll need to right click on this shorcut and press properties, inside of the ```target``` text box, press ```ctrl + a``` then delete. Replace the now removed text with ```spicetify auto```", inline=False)
restart_e.add_field(name="if you have Spotify setup to run on startup:", value="navigate to this entry in regedit: ```HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run``` find the ```spotify``` key and edit its value to say ```spicetify auto``` aswell", inline=True)






@bot.slash_command(guild_ids=[guild], name="find_config", description="Helps you and the helpers")
async def find_config(ctx):
    await ctx.respond(embed=find_config_e)

@bot.slash_command(guild_ids=[guild], name="uninstall", description="Helps you to uninstall this really cool spicetify")
async def uninstall(ctx):
    await ctx.respond(embed=uninstall_e)

@bot.slash_command(guild_ids=[guild], name="path_error", description="How 2 fix the prefs path not found error")
async def pathError(ctx):
    await ctx.respond(embed=path)

@bot.slash_command(guild_ids=[guild], name="keyword_not_found", description="Helps you to find it")
async def keywordNotFound(ctx):
    await ctx.respond(embed=keyword)

@bot.slash_command(guild_ids=[guild], name="blank_screen", description="Helps you to see everything again")
async def blank_screen(ctx):
    await ctx.respond(embed=update)

@bot.slash_command(guild_ids=[guild], name="gone_after_restart", description="When you restart and your spotify is boring again")
async def restart(ctx):
    await ctx.respond(embed=restart_e)

@bot.slash_command(guild_ids=[guild], name="install", description="Hot to install spicetify")
async def installS(ctx):
    await ctx.respond("https://letmegooglethat.com/?q=Spicetify")






bot.run("")
