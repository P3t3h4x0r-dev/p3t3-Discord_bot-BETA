import discord 
from discord import app_commands
from discord.ext import commands
from discord import Embed 


class Help(commands.Cog): #Define a classe.
    def __init__(self, bot): #Inicia a classe.
        self.bot = bot
        super().__init__()

    @commands.command() #Define como um comando.
    async def Help(self, ctx): #O usuário utiliza o comando HELP para ver os comandos do bot.
            embed = discord.Embed( #Cria uma mensagem em embed.
                title="Lista de comandos ",
                description=f"Guia para usar o bot.",
                color=discord.Color.purple())
            embed.add_field(name="!CCT", value="Cria canais de texto: [!CCT um_simples_canal] ", inline=False)
            embed.add_field(name="!CCV", value="Cria canais de voz: [!CCV um_simples_canal] ", inline=False)
            embed.add_field(name="!CDT", value="Deleta canais de texto: [!CDT um_simples_canal] ", inline=False)
            embed.add_field(name="!CDV", value="Deleta canais de Voz: [!CDV um_simples_canal] ", inline=False)
            embed.add_field(name="!CR", value="Cria cargos: [!CR Membro] ", inline=False)
            embed.add_field(name="!DR", value="Deleta cargos: [!DR Membro] ", inline=False)
            embed.add_field(name="!SETUPLOG", value="Habilita os logs no servidor", inline=False)
            await ctx.send(embed=embed) #Envia a mensagem da embed para o canal onde foi utilizado o prefixo.