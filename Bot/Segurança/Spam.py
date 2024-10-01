import discord
from discord.ext import commands
from collections import defaultdict
import asyncio
from discord import Embed 

class spam(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.spam_count = defaultdict(int)
        self.spam_threshold = 5
        self.spam_interval = 3  # Intervalo em segundos

    def get_log_channel(self, guild):
        
      #Procura um canal de texto com o nome definido de 'logs'.
        return discord.utils.get(guild.text_channels, name='logs')
    
    @commands.command() #Define como um comando.
    @commands.has_permissions(administrator=True) #Necessário ter perm de ADM
    async def ConfigurarSpam(self, ctx, tempo:int, quantidade:int):
        try:
            self.spam_threshold = tempo
            self.spam_interval = quantidade
            await ctx.send(f"habitado com sucesso com {self.spam_threshold} segundos com a quandidade de {self.spam_interval} canais")
        except:
            await ctx.send("ocorreu um erro")

    async def check_spam(self, message):
        log_channel = discord.utils.get(message.guild.channels, name='logs')
        author_id = message.author.id #Autor da mensagem
        self.spam_count[author_id] += 1
        if self.spam_count[author_id] > self.spam_threshold:
            try:
                await message.author.ban(reason="Spamming")
                embed = discord.Embed( #Cria uma mensagem em embed.
                title="Banido",
                color=discord.Color.purple())
                embed.add_field(name=f"", value=f"O usuário {message.author.mention} foi banido por spam!!", inline=False)
                await log_channel.send(embed=embed) #Envia a mensagem em embed para o canal 'logs'.
            except: 
                print("algum erro ocorreu")
        
        return True
        await asyncio.sleep(self.spam_interval)
        self.spam_count[author_id] -= 1
        return False

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        if await self.check_spam(message):
            return

