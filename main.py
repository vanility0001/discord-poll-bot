#imports
import discord
from discord.ext import commands

#defining client
client = commands.Bot(command_prefix = "p!")

#on_ready event
@client.event
async def on_ready():
    print("Poll bot is ready.")

#removing default help command to replace it
client.remove_command("help")

#on_guild_join event to send a message on joining a server
@client.event
async def on_guild_join(guild):
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            embed=discord.Embed(color=0xcc0231)
            embed.set_thumbnail(url="https://images.discordapp.net/avatars/324631108731928587/7dbf4eec7a6c1f7f2d3969a5c7008bb9.png?size=512")
            embed.add_field(name="Thank you!", value="Thank you for adding me! The default prefix is `p!`. Run the `help` command to see a list of commands.")
            await channel.send(embed=embed)
        break

#poll command
@client.command()
async def poll(ctx, txt):
    author = ctx.message.author
    txt = str(txt)

    embed=discord.Embed(color=0xcc0231)
    embed.set_author(name="Poll Bot", url="https://github.com/vanility0104/discord-poll-bot", icon_url="https://images.discordapp.net/avatars/324631108731928587/7dbf4eec7a6c1f7f2d3969a5c7008bb9.png?size=512")
    embed.add_field(name="Member", value=author.mention, inline=False)
    embed.add_field(name="Poll", value=txt, inline=False)
    message = await ctx.send(embed=embed)

    await message.add_reaction("👍")
    await message.add_reaction("👎")

#suggestion command
@client.command()
async def suggest(ctx, txt):
    author = ctx.message.author
    txt = str(txt)

    embed=discord.Embed(color=0xcc0231)
    embed.set_author(name="Poll Bot", url="https://github.com/vanility0104/discord-poll-bot", icon_url="https://images.discordapp.net/avatars/324631108731928587/7dbf4eec7a6c1f7f2d3969a5c7008bb9.png?size=512")
    embed.add_field(name="Member", value=author.mention, inline=False)
    embed.add_field(name="Suggest", value=txt, inline=False)
    message = await ctx.send(embed=embed)

    await message.add_reaction("✅")
    await message.add_reaction("❌")

#help command
@client.command()
async def help(ctx):
    embed = discord.Embed(color=0xcc0231)
    embed.set_author(name="Poll Bot", url="https://github.com/vanility0104/discord-poll-bot", icon_url="https://images.discordapp.net/avatars/324631108731928587/7dbf4eec7a6c1f7f2d3969a5c7008bb9.png?size=512")
    embed.add_field(name="suggest TEXT", value="Puts your suggestion in an embed.", inline=False)
    embed.add_field(name="poll TEXT", value="Puts your poll in an embed.", inline=False)
    embed.add_field(name="help", value="Shows this message.", inline=False)
    await ctx.send(embed=embed)

#error handling
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        embed=discord.Embed(color=0xcc0231)
        embed.set_author(name="Poll Bot", url="https://github.com/vanility0104/discord-poll-bot", icon_url="https://images.discordapp.net/avatars/324631108731928587/7dbf4eec7a6c1f7f2d3969a5c7008bb9.png?size=512")
        embed.add_field(name="Failed", value="Unknown command!")
        await ctx.send(embed=embed)

    if isinstance(error, commands.MissingRequiredArgument):
        embed=discord.Embed(color=0xcc0231)
        embed.set_author(name="Poll Bot", url="https://github.com/vanility0104/discord-poll-bot", icon_url="https://images.discordapp.net/avatars/324631108731928587/7dbf4eec7a6c1f7f2d3969a5c7008bb9.png?size=512")
        embed.add_field(name="Failed", value="Missing required arguments!")
        await ctx.send(embed=embed)


#running the bot
client.run("token_here")
