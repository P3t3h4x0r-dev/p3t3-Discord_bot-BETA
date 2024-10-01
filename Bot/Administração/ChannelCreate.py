import discord
from discord.ext import commands

class CreateChannels(commands.Cog): #Define a classe.
    def __init__(self, bot): #Inicia a classe.
        self.bot = bot
        super().__init__()

    @commands.command() #Define como um comando.
    @commands.has_permissions(administrator=True) #Necessário o usuario possuir permissões de Administrador.
    async def CCT(self,ctx, nome: str): #O usuário utiliza o comando CCT (Criar canal de texto) definindo o nome do canal.
     guild = ctx.guild
     texto_channel = await guild.create_text_channel(f'{nome}')

     embed = discord.Embed( #Cria uma mensagem em embed.
        title="Canal Criado",
        description="Um novo canal de texto foi criado",
        color=discord.Color.purple())
     embed.add_field(name="", value=f"o canal {nome} foi criado com sucesso", inline=False)
     await ctx.send(embed=embed) #Encaminha a mensagem em embed para o canal onde foi utilizado o prefixo.

    @commands.command() #Define como um comando.
    @commands.has_permissions(administrator=True) #Necessário o usuario possuir permissões de Administrador.
    async def CCV(self,ctx, nome: str): #O usuário utiliza o comando CCV (Criar canal de voz) definindo o nome do canal de voz.
       guild = ctx.guild
       voz_channel = await guild.create_voice_channel(f'{nome}')

       embed = discord.Embed( #Cria uma mensagem em embed.
        title="Canal Criado",
        description="Um novo canal de voz foi criado",
        color=discord.Color.purple())
       embed.add_field(name="", value=f"o canal {nome} foi criado com sucesso", inline=False)
       await ctx.send(embed=embed) #Encaminha a mensagem em embed para o canal onde foi utilizado o prefixo.

    @CCV.error #Define como um Event de erro.
    async def CCV_error(self, ctx, error): #Caso ocorra um erro.
        if isinstance(error, commands.MissingPermissions): #Quando o usuário tem falta de permissões(ADM).
            embed = discord.Embed( #Cria uma mensagem em embed.
        title="Falta de permissões",
        description="Você não tem permissões suficientes para executar este comando",
        color=discord.Color.purple())
        await ctx.send(embed=embed) #Encaminha a mensagem em embed para o canal onde foi utilizado o prefixo.

    @CCT.error  #Define como um Event de erro.
    async def CCT_error(self, ctx, error): #Caso ocorra um erro.
        if isinstance(error, commands.MissingPermissions): #Quando o usuário tem falta de permissões(ADM).
            embed = discord.Embed( #Cria uma mensagem em embed.
        title="Falta de permissões",
        description="Voce não tem permissões suficientes para executar este comando",
        color=discord.Color.purple())
        await ctx.send(embed=embed) #Encaminha a mensagem em embed para o canal onde foi utilizado o prefixo.