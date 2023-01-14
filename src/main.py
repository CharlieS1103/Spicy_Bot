import discord
from discord import app_commands
from embeds import find_config_embed, uninstall_embed, path_embed, keyword_embed

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

guild_id = "755866816038961175"

# Events
@client.event
async def on_ready():
    """Sync the command tree with the guild and print the bot's username"""
    await tree.sync(guild=discord.Object(id=guild_id))
    print(f'We have logged in as {client.user}')

# commands
@tree.command()
async def find_config(ctx):
    """Show the solutions for finding config file"""
    await ctx.send(embed=find_config_embed)

@tree.command()
async def uninstall(ctx):
    """Show the solutions for uninstalling spicetify"""
    await ctx.send(embed=uninstall_embed)

@tree.command()
async def path(ctx):
    """Show the solutions for resolving prefs/spotify path error"""
    await ctx.send(embed=path_embed)

@tree.command()
async def keyword(ctx):
    """Show the solutions for resolving keyword error"""
    await ctx.send(embed=keyword_embed)

client.run("<YOUR_BOT_TOKEN>")
