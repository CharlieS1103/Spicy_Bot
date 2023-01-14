import discord
from discord import app_commands
from embeds import *
from threadResolver import check_common_issues
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

guild_id = "842219447716151306"
forum_channel_id = "1010665630837526588"
# Events
@client.event
async def on_ready():
    """Sync the command tree with the guild and print the bot's username"""
    await tree.sync(guild=discord.Object(id=guild_id))
    print(f'We have logged in as {client.user}')

# Handle the thread_create event
@client.event
async def on_thread_create(thread):
    if str(thread.parent_id) == forum_channel_id:
        first_message = await thread.fetch_message(thread.id)
        print(first_message)
        matching_issue = await check_common_issues(first_message.content)
#        if matching_issue:
      #      if matching_issue == find_config_embed.title:
    # PRint the matching issue
        print(matching_issue)
        await thread.send(embed=find_config_embed)
           

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

client.run("")
