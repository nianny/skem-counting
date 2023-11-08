import config
import discord
from discord.ext import commands
from discord import app_commands
import random

def run():
    
    username = int(config.user_id)
    print(username, type(username))
    intents = discord.Intents.all()
    bot = commands.Bot(command_prefix = "?", intents=intents)
    
    @bot.event
    async def on_ready():
        print(f"Hallooooo :D")
        await bot.tree.sync()
    
    @bot.event
    async def on_message(msg):
        if (msg.author.id == username):
            await msg.add_reaction('✅')
    
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
    
    
    def isAdmin(interaction: discord.Interaction):
        return interaction.user.guild_permissions.administrator
    
    def isNianny(interaction: discord.Interaction):
        return interaction.user.id == 782247763542016010
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