import discord
from discord.ext import commands
from collections import defaultdict, deque
from datetime import datetime, timedelta

class AntiKick(commands.Cog): #Define a classe.
    def __init__(self, bot):
        self.bot = bot
        self.kick_counter = defaultdict(lambda: deque())
        self.KICK_LIMIT = 5  # Limite de kicks permitido
        self.TIME_LIMIT = timedelta(seconds=3)  # Intervalo de tempo permitido para os kicks
    
    def get_log_channel(self, guild):
      #Procura um canal de texto com o nome definido de 'logs'.
        return discord.utils.get(guild.text_channels, name='logs')
    
    
    @commands.command() #Define como um comando.
    @commands.has_permissions(administrator=True) #Necessário ter perm de ADM
    async def ConfigurarDR(self, ctx, tempo:int, quantidade:int):
        try:
            self.TIME_WINDOW = tempo
            self.CHANNEL_CREATE_THRESHOLD = quantidade
            await ctx.send(f"habitado com sucesso com {self.TIME_WINDOW} segundos com a quandidade de {self.CHANNEL_CREATE_THRESHOLD} canais")
        except:
            await ctx.send("ocorreu um erro")
    

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        guild = member.guild
        async for entry in guild.audit_logs(limit=1, action=discord.AuditLogAction.kick):
            if entry.target == member:
                moderator = entry.user
                if moderator == self.bot.user:
                    return  # Ignora se o bot for o moderador

                # Adiciona o timestamp do kick ao deque do moderador
                now = datetime.utcnow()
                self.kick_counter[moderator.id].append(now)

                # Remove timestamps antigos fora do limite de tempo
                while self.kick_counter[moderator.id] and now - self.kick_counter[moderator.id][0] > self.TIME_LIMIT:
                    self.kick_counter[moderator.id].popleft()

                # Verifica se os kicks ultrapassam o limite no tempo definido
                if len(self.kick_counter[moderator.id]) >= self.KICK_LIMIT:
                    await guild.ban(moderator, reason="Kickou muitos membros em pouco tempo")
                    del self.kick_counter[moderator.id]  # Reseta o contador do moderador
                    print(f'{moderator} foi banido por kickar muitos membros em pouco tempo.')