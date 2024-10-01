import discord
from discord.ext import commands

class VoiceJoiner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.voice_channel_id = 1254542293881585724  # Substitua pelo ID do canal de voz desejado

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Bot {self.bot.user} está pronto.')
        guild = discord.utils.get(self.bot.guilds)
        channel = self.bot.get_channel(self.voice_channel_id)
        if guild and channel and isinstance(channel, discord.VoiceChannel):
            if guild.voice_client is None:
                await channel.connect()
                print(f'Conectado ao canal de voz {channel.name}')
            else:
                print(f'Já estou conectado a um canal de voz.')

    @commands.command()
    async def leave(self, ctx):
        if ctx.voice_client:
            await ctx.guild.voice_client.disconnect()
            await ctx.send('Desconectado do canal de voz.')
        else:
            await ctx.send('Eu não estou em um canal de voz.')


