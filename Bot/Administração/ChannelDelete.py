import discord 
from discord import app_commands
from discord.ext import commands

class DeleteChannels(commands.Cog): #Define a classe.
    def __init__(self, bot): #Inicia a classe.
        self.bot = bot
        super().__init__()

    @commands.command() #Define como um comando.
    @commands.has_permissions(administrator=True) #Necessário o usuario possuir permissões de Administrador.
    async def CDT(self, ctx, canal: discord.TextChannel): #O usuário utiliza o comando CDT (Deleta canal de texto) definindo o nome do canal.
          await canal.delete()
          embed = discord.Embed( #Cria uma mensagem em embed.
        title="Canal Criado",
        description="o canal de texto foi deletado",
        color=discord.Color.purple())
          embed.add_field(name="", value=f"o canal {canal} foi deletado com sucesso", inline=False)
          await ctx.send(embed=embed) #Encaminha a mensagem em embed para o canal onde foi utilizado o prefixo.

    @commands.command() #Define como um comando.
    @commands.has_permissions(administrator=True) #Necessário o usuario possuir permissões de Administrador.
    async def CDV(self, ctx, canal: discord.VoiceChannel): #O usuário utiliza o comando CDV (Deleta canal de texto) definindo o nome do canal.
          await canal.delete()
          embed = discord.Embed( #Cria uma mensagem em embed.
        title="Canal deletado ",
        description="o canal de voz foi deletado",
        color=discord.Color.purple())
          embed.add_field(name="", value=f"o canal {canal} foi deletado com sucesso", inline=False)
          await ctx.send(embed=embed)  #Encaminha a mensagem em embed para o canal onde foi utilizado o prefixo.

    
    @CDV.error #Define como um Event de erro.
    async def CDV_error(self, ctx, error): #Caso ocorra um erro.
        if isinstance(error, commands.MissingPermissions): #Quando o usuário tem falta de permissões(ADM).
            embed = discord.Embed( #Cria uma mensagem em embed.
        title="Falta de permissões",
        description="Voce não tem permissões suficientes para executar este comando",
        color=discord.Color.purple())
        await ctx.send(embed=embed)  #Envia a mensagem da embed para o canal onde foi utilizado o prefixo.

    @CDT.error #Define como um Event de erro.
    async def CDT_error(self, ctx, error): #Caso ocorra um erro.
        if isinstance(error, commands.MissingPermissions):  #Quando o usuário tem falta de permissões(ADM).
            embed = discord.Embed( #Cria uma mensagem em embed.
        title="Falta de permissões",
        description="Voce não tem permissões suficientes para executar este comando",
        color=discord.Color.purple())
        await ctx.send(embed=embed)  #Encaminha a mensagem em embed para o canal onde foi utilizado o prefixo.