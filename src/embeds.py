import discord

EMBED_COLOR = 0x0400ff

find_config_embed = discord.Embed(
    title="Find Your Config (config-xpui.ini) File", 
    description="This is very helpful for troubleshooting", 
    color=EMBED_COLOR
)
find_config_embed.add_field(
    name="Solution 1:", 
    value="Run ```spicetify config-dir``` in a terminal of your choice (this opens your file explorer at the right location)", 
    inline=False
)
find_config_embed.add_field(
    name="Solution 2: ", 
    value="Run ```spicetify config``` in a terminal of your choice. The output will be the path to your config file", 
    inline=False
)
find_config_embed.add_field(
    name="Solution 3: ", 
    value='''Search for it by yourself:
Pathes:
Windows: `C:/Users/YOUR_NAME/AppData/Roaming/spicetify`
Linux: `~/.config/spicetify/config-xpui.ini`
Mac: `~/.config/spicetify/config-xpui.ini`''', 
    inline=True
)

install_embed = discord.Embed(
    title="Installing Spicetify", 
    description="Here are the steps to installing Spicetify", 
    color=EMBED_COLOR
)
install_embed.add_field(
    name="Step 1:", 
    value="Make sure you have Node.js and Git installed on your computer", 
    inline=False
)
install_embed.add_field(
    name="Step 2: ", 
    value="Run the command ```npm install -g spicetify-cli``` in your terminal", 
    inline=False
)
install_embed.add_field(
    name="Step 3: ", 
    value="Run ```spicetify``` to configure and install Spicetify", 
    inline=True
)

uninstall_embed = discord.Embed(
    title="Uninstall Spicetify", 
    description="Instructions for uninstalling Spicetify", 
    color=EMBED_COLOR
)
uninstall_embed.add_field(
    name="Step 1:", 
    value="Run ```spicetify restore``` in a terminal", 
    inline=False
)
uninstall_embed.add_field(
    name="Step 2 (Windows):", 
    value='''Run each command one after another:
```cd %appdata%```
```rmdir spicetify / /S```
```cd %localappdata%```
```rmdir spicetify /s /S```''', 
    inline=False
)
uninstall_embed.add_field(
    name="Step 2 (Linux + Mac):", 
    value='''Run the command ```rm -rf ~/.spicetify``` and ```rm -rf ~/.config/spicetify```''', 
    inline=True
)

path_embed = discord.Embed(
    title="prefs/spotify path error", 
    color=EMBED_COLOR
)
path_embed.add_field(
    name="prefs path:", 
    value="Open your config file and replace whatever is after ```prefs_path =``` with (Windows) ```C:/Users/<YOUR_USERNAME>/appdata/Roaming/Spotify/prefs``` or (Mac) ```/Users/YOUR_USERNAME/Library/Application Support/Spotify/prefs``` or (Linux) ```/home/YOUR_USERNAME/.config/spotify/prefs```", 
    inline=False
)
path_embed.add_field(
    name="spotify path:", 
    value='''Same thing. But instead of ```prefs_path =``` use ```spotify_path =``` and for Windows use ```C:/Users/<YOUR_USERNAME>/appdata/Roaming/Spotify```, for Mac use ```/Applications/Spotify.app/Contents/Resources``` and for Linux it depends on how you installed Spotify''', 
    inline=True
)

keyword_embed = discord.Embed(
    title="Keyword 'Spicetify' Not Recognized In Terminals", 
    description="Instructions for resolving this issue", 
    color=EMBED_COLOR
)
keyword_embed.add_field(
    name="Step 1:", 
    value="Restart your PC (this may fix the issue)", 
    inline=False
)
keyword_embed.add_field(
    name="Step 2 (Windows):", 
    value='''In your search bar, type the word ```environment``` an application should appear that says ```Edit environment variables for your account```. Once opened, double click on the "Path" header, select new in the right side of the window, and type the path ```C:/Users/USERNAME/appdata/local/spicetify```. Make sure to press OK in both windows and not cancel!''', 
    inline=False
)
keyword_embed.add_field(
    name="Step 2 (Linux + Mac):", 
    value='''Edit your bash profile file (usually located at `~/.bash_profile`, `~/.bashrc` or `~/.zshrc`) and add the following line:
```export PATH=$PATH:/path/to/spicetify```
Make sure to replace `/path/to/spicetify` with the actual path to the Spicetify folder on your system''', 
    inline=True
)

blank_screen_embed = discord.Embed(
    title="Blank screen after installing Spicetify", 
    description="Instructions for resolving this issue", 
    color=EMBED_COLOR
)
blank_screen_embed.add_field(
    name="Step 1:", 
    value="Try running ```spicetify upgradey``` and ```spicetify restore backup apply```, if the terminal/powershell prompts you to do something else, do that instead. If it still doesn't work, wait for a new update to Spicetify", 
    inline=True
)

gone_after_restart_embed = discord.Embed(
    title="Spicetify settings gone after restarting PC", 
    description="Instructions for resolving this issue", 
    color=EMBED_COLOR
)
gone_after_restart_embed.add_field(
    name="Step 1:", 
    value="Check if you have the latest version of Spicetify installed", 
    inline=False
)
gone_after_restart_embed.add_field(
    name="Step 2:", 
    value="Make sure your config file is located in the correct location", 
    inline=False
)
gone_after_restart_embed.add_field(
    name="Step 3:", 
    value="Run ```spicetify config``` and make sure the path to your Spotify client is correct", 
    inline=False
)
gone_after_restart_embed.add_field(
    name="Step 4:", 
    value="Try running ```spicetify backup apply``` and ```spicetify update```", 
    inline=True
)



