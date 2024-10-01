import discord 
from discord import app_commands
from discord.ext import commands
from discord import Embed 


class CreateRoles(commands.Cog):
    def __init__(self, bot): #Inicia a classe.
        self.bot = bot
        super().__init__()


    @commands.command() #Cria um comando
    @commands.has_permissions(administrator=True) #Necessário ter perm de ADM
    async def CR(self, ctx, cargo_nome): #!CR (Cria um cargo)  <nome do cargo>
      guild = ctx.guild 
      novo_cargo = await guild.create_role(name=cargo_nome)
      embed = discord.Embed( #Cria embeds em mensagens
                title="cargo criado ",
                description="Um novo cargo foi criado",
                color=discord.Color.purple())
      embed.add_field(name="", value=f"o cargo {cargo_nome} criado com sucesso", inline=False)
      await ctx.send(embed=embed) #Envia a mensagem em embed para o canal 'logs'.


    @CR.error #.
    async def CR_error(self, ctx, error): 
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
        title="Falta de permissões",
        description="Voce não tem permissões suficientes para executar este comando",
        color=discord.Color.purple())
        await ctx.send(embed=embed) #Envia a mensagem em embed para o canal 'logs'.
















