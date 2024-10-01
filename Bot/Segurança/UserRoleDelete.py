import discord 
from discord.ext import commands
from collections import defaultdict

class AntiDeleteRoles(commands.Cog): #Define a classe.
    def __init__(self, bot): #Inicia a classe.
        self.bot = bot
        self.ROLE_DELETE_THRESHOLD = 5 
        self.TIME_WINDOW = 3
        self.role_delete_log = defaultdict(list)
    
    def get_log_channel(self, guild):
      #Procura um canal de texto com o nome definido de 'logs'.
        return discord.utils.get(guild.text_channels, name='logs')
    



    @commands.Cog.listener()
    async def on_guild_role_delete(self, role):
        # Recupera o log de auditoria para identificar quem deletou o canal
        guild = role.guild
        async for entry in guild.audit_logs(limit=1, action=discord.AuditLogAction.role_delete):
            user = entry.user
            now = discord.utils.utcnow()

        # Registra a deleção do canal
            self.role_delete_log[user.id].append(now)

        # Remove entradas antigas que estão fora da janela de tempo
            self.role_delete_log[user.id] = [
            timestamp for timestamp in self.role_delete_log[user.id]
            if (now - timestamp).total_seconds() <= self.TIME_WINDOW
        ]

        # Verifica se o usuário excedeu o limite de deleções
        if len(self.role_delete_log[user.id]) > self.ROLE_DELETE_THRESHOLD:
            try:
                await guild.ban(user, reason="deletou muitos cargos em um curto período de tempo.")
                print(f'{user} foi expulso por criar muitos cargos.')
            except discord.Forbidden:
                print(f'Não tenho permissão para expulsar {user}.')
            except discord.HTTPException as e:
                print(f'Ocorreu um erro ao tentar expulsar {user}: {e}')