import discord 
from discord import app_commands
from discord.ext import commands



class DeleteRoles(commands.Cog):
    def __init__(self, bot): #Inicia a classe.
        self.bot = bot
        super().__init__()


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def DR(self, ctx, cargo_nome: str):
     role = discord.utils.get(ctx.guild.roles, name=cargo_nome)
     if role:
            try:

                await role.delete()
                embed = discord.Embed(
                title="cargo Deletado",
                description="O cargo foi apagado",
                color=discord.Color.purple())
                embed.add_field(name="", value=f"o cargo {cargo_nome} foi deletado com sucesso", inline=False)
                await ctx.send(embed=embed)

            except discord.Forbidden:
                embed = discord.Embed(
                title="Permissoes insuficientes",
                description="",
                color=discord.Color.purple())
                embed.add_field(name="", value=f"Voce não tem permissões ", inline=False)
                await ctx.send(embed=embed)

            except:
              await ctx.send(f'O cargo "{cargo_nome}" não foi encontrado.')
     


    @DR.error
    async def DR_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
        title="Falta de permissões",
        description="Voce não tem permissões suficientes para executar este comando",
        color=discord.Color.purple())
        await ctx.send(embed=embed)