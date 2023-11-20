

import config
import discord
from discord.ext import commands
from discord import app_commands
import random

def run():
    
    
    usernames = [948474333381156924, 1034734742270128159, 782247763542016010]
    intents = discord.Intents.all()
    bot = commands.Bot(command_prefix = "?", intents=intents)
    
    
    bot.fake_count = []
    bot.fake_error = {}
    
    def isAdmin(interaction: discord.Interaction):
        return interaction.user.guild_permissions.administrator
    
    def isNianny(interaction: discord.Interaction):
        return interaction.user.id in usernames
    
    
    @bot.event
    async def on_ready():
        # avatar = bot.get_user(298661966086668290).avatar.url;
        # print(avatar)
        await bot.tree.sync()
        print(f"Hallooooo :D")
    
    @bot.event
    async def on_message(msg):
        if (msg.author.id in bot.fake_count):
            await msg.add_reaction('✅')
        elif(msg.author.id in bot.fake_error):
            print(msg.author.global_name, msg.content)
            await msg.add_reaction('❌')
            embed = discord.Embed(description="Vote [here](https://countingbot.com/vote) to earn saves so you can continue counting next time. See `c!help`.", color=0x8965d6)
            await msg.channel.send(f"{msg.author.mention} RUINED IT AT **{bot.fake_error[msg.author.id]}**!! Next number is **1**. **Wrong number.**", embed=embed)
            bot.fake_error.pop(msg.author.id)
    
    
    @bot.tree.command(name="startskem", description="Starts counting autoreactions :D")
    @app_commands.check(isNianny)
    async def startskem(interaction: discord.Interaction):
        bot.fake_count.append(interaction.user.id)
        await interaction.response.send_message(f"Started counting autoreactions :D")
    
    @bot.tree.command(name="stopskem", description="Stops counting autoreactions :D")
    @app_commands.check(isNianny)
    async def stopskem(interaction: discord.Interaction):
        if (interaction.user.id in bot.fake_count):
            bot.fake_count.remove(interaction.user.id)
            await interaction.response.send_message(f"Stopped counting autoreactions :D")
        else:
            await interaction.response.send_message(f"Autoreactions wasn't on for you :O")
    
    
    @bot.tree.command(name="startskemerror", description="Next count will be fake!")
    @app_commands.check(isNianny)
    async def startskemerror(interaction: discord.Interaction, current_count: int):
        bot.fake_error[interaction.user.id] = current_count
        if (interaction.user.id in bot.fake_count):
            bot.fake_count.remove(interaction.user.id)
        await interaction.response.send_message(f"Next count will be faked as an error :D")
    
    # @bot.tree.command(description="Makes someone a boruoi :O", name = "boruoi")
    # @app_commands.describe(mem="Who do you want to make a boruoi?")
    # @app_commands.rename(mem="person")
    # async def boruoi(interaction: discord.Interaction, mem: discord.Member):
    #     await make_boruoi(interaction, mem)
    
    # @bot.tree.context_menu(name="boruoi")
    # async def boruoi_app(interaction: discord.Interaction, mem: discord.Member):
    #     await make_boruoi(interaction, mem)
    
    # async def make_boruoi(interaction: discord.Interaction, mem: discord.Member):
    #     try:
    #         await mem.edit(nick="boruoi")
    #         try:
    #             for role in interaction.guild.roles:
    #                 if role.name == "boruoi":
    #                     await mem.add_roles(role)
    #         except:
    #             pass
    #         await interaction.response.send_message(f"{interaction.user.mention} has made {mem.mention} a boruoi :O\nHallooo {mem.mention} :D")
    #     except:
    #         await interaction.response.send_message(f"Welp something went wrong (prob no perms) :(")
    
    # @bot.tree.command(description="Unboruoi yourself :O", name = "unboruoi")
    # async def unboruoi(interaction: discord.Interaction):
    #     await un_boruoi(interaction)
    
    # async def un_boruoi(interaction: discord.Interaction):
    #     if interaction.user.nick == "boruoi":
    #         try:
    #             options = []
    #             for member in interaction.guild.members:
    #                 if member.nick != "boruoi":
    #                     options.append(member)
    #             nick = random.choice(options).display_name
    #             await interaction.user.edit(nick=nick)
    #             await interaction.response.send_message(f"Halloo {interaction.user.mention} :O")
    #         except:
    #             await interaction.response.send_message(f"Welp something went wrong (prob no perms) :(")
    #     else:
    #         await interaction.response.send_message(f"Skem how do you expect to be able to unboruoi yourself when you aren't even a boruoi?!?!?! :O")
    
    
    
    @bot.tree.context_menu(name="unboruoi")
    # @app_commands.check(isAdmin)
    @app_commands.check(isNianny)
    async def unboruooi(interaction: discord.Interaction, mem: discord.Member):
        try:
            options = []
            for member in interaction.guild.members:
                if member.nick != "boruoi":
                    options.append(member)
            nick = random.choice(options).display_name
            await mem.edit(nick=nick)
            await interaction.response.send_message(f"Halloo {mem.mention} :O")
        except:
            await interaction.response.send_message(f"Welp something went wrong (prob no perms) :(")
            
    bot.run(config.discord_api_token)
    
if __name__ == "__main__":
    run()