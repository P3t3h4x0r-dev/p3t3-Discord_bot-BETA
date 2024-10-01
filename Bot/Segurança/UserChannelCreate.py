import discord 
from discord.ext import commands
from collections import defaultdict
from discord import Embed 

class AntiCreateChannel(commands.Cog): #Define a classe.
    def __init__(self, bot): #Inicia a classe.
        self.bot = bot
        self.CHANNEL_CREATE_THRESHOLD = 5
        self.TIME_WINDOW = 3
        self.channel_create_log = defaultdict(list)

    def get_log_channel(self, guild):
      #Procura um canal de texto com o nome definido de 'logs'.
        return discord.utils.get(guild.text_channels, name='logs')
    

    
    
    @commands.command() #Define como um comando.
    async def check(self, ctx):
       await ctx.send(f"o valor de time é de {self.TIME_WINDOW} e o valor de quantidade é de {self.CHANNEL_CREATE_THRESHOLD}")



    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel):
    # Recupera o log de auditoria para identificar quem deletou o canal
        guild = channel.guild
        async for entry in guild.audit_logs(limit=1, action=discord.AuditLogAction.channel_create):
            user = entry.user
            now = discord.utils.utcnow()

        # Registra a deleção do canal
            self.channel_create_log[user.id].append(now)

        # Remove entradas antigas que estão fora da janela de tempo
            self.channel_create_log[user.id] = [
            timestamp for timestamp in self.channel_create_log[user.id]
            if (now - timestamp).total_seconds() <= self.TIME_WINDOW
        ]

        # Verifica se o usuário excedeu o limite de deleções
        if len(self.channel_create_log[user.id]) > self.CHANNEL_CREATE_THRESHOLD:
            try:
                await guild.ban(user, reason="criou muitos canais em um curto período de tempo.")
                print(f'{user} foi expulso por criar muitos canais.')
            except discord.Forbidden:
                print(f'Não tenho permissão para expulsar {user}.')
            except discord.HTTPException as e:
                print(f'Ocorreu um erro ao tentar expulsar {user}: {e}')