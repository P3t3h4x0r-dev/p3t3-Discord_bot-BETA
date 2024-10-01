import discord 
from discord.ext import commands
from collections import defaultdict

class AntiCreateRoles(commands.Cog): #Define a classe.
    def __init__(self, bot): #Inicia a classe.
        self.bot = bot
        self.ROLE_CREATE_THRESHOLD = 5
        self.TIME_WINDOW = 3
        self.role_create_log = defaultdict(list)

    def get_log_channel(self, guild):
      #Procura um canal de texto com o nome definido de 'logs'.
        return discord.utils.get(guild.text_channels, name='logs')
    
    
    @commands.command() #Define como um comando.
    @commands.has_permissions(administrator=True) #Necessário ter perm de ADM
    async def ConfigurarCR(self, ctx, tempo:int, quantidade:int):
        try:
            self.TIME_WINDOW = tempo
            self.CHANNEL_CREATE_THRESHOLD = quantidade
            await ctx.send(f"habitado com sucesso com {self.TIME_WINDOW} segundos com a quandidade de {self.CHANNEL_CREATE_THRESHOLD} canais")
        except:
            await ctx.send("ocorreu um erro")
            
    @commands.Cog.listener()
    async def on_guild_role_create(self, role):
        # Recupera o log de auditoria para identificar quem deletou o canal
        guild = role.guild
        async for entry in guild.audit_logs(limit=1, action=discord.AuditLogAction.role_create):
            user = entry.user
            now = discord.utils.utcnow()

        # Registra a deleção do canal
            self.role_create_log[user.id].append(now)

        # Remove entradas antigas que estão fora da janela de tempo
            self.role_create_log[user.id] = [
            timestamp for timestamp in self.role_create_log[user.id]
            if (now - timestamp).total_seconds() <= self.TIME_WINDOW
        ]

        # Verifica se o usuário excedeu o limite de deleções
        if len(self.role_create_log[user.id]) > self.ROLE_CREATE_THRESHOLD:
            try:
                await guild.ban(user, reason="criou muitos cargos em um curto período de tempo.")
                print(f'{user} foi expulso por criar muitos cargos.')
            except discord.Forbidden:
                print(f'Não tenho permissão para expulsar {user}.')
            except discord.HTTPException as e:
                print(f'Ocorreu um erro ao tentar expulsar {user}: {e}')