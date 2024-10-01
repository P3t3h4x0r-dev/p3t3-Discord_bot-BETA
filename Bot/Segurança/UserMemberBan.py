import discord
from discord.ext import commands
from collections import defaultdict, deque
from datetime import datetime, timedelta


class AntiBan(commands.Cog): #Define a classe.
    def __init__(self, bot):
        self.bot = bot
        self.ban_counter = defaultdict(lambda: deque())
        self.BAN_LIMIT = 5  # Limite de bans permitido
        self.TIME_LIMIT = timedelta(seconds=3)  # Intervalo de tempo permitido para os bans
    

    
    def get_log_channel(self, guild):
      #Procura um canal de texto com o nome definido de 'logs'.
        return discord.utils.get(guild.text_channels, name='logs')
    

    @commands.Cog.listener()
    async def on_member_ban(self, guild, user):
       async for entry in guild.audit_logs(limit=1, action=discord.AuditLogAction.ban):
            if entry.target == user:
                moderator = entry.user
                if moderator == self.bot.user:
                    return  # Ignora se o bot for o moderador

                # Adiciona o timestamp do banimento ao deque do moderador
                now = datetime.utcnow()
                self.ban_counter[moderator.id].append(now)

                # Remove timestamps antigos fora do limite de tempo
                while self.ban_counter[moderator.id] and now - self.ban_counter[moderator.id][0] > self.TIME_LIMIT:
                    self.ban_counter[moderator.id].popleft()

                # Verifica se os bans ultrapassam o limite no tempo definido
                if len(self.ban_counter[moderator.id]) >= self.BAN_LIMIT:
                    await guild.ban(moderator, reason="Baniu muitos membros em pouco tempo")
                    del self.ban_counter[moderator.id]  # Reseta o contador do moderador
                    print(f'{moderator} foi banido por banir muitos membros em pouco tempo.')