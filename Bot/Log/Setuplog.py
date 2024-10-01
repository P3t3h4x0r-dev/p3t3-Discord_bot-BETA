import discord 
from discord import app_commands
from discord.ext import commands
import logging
from discord import Embed 
from datetime import datetime

class Logs(commands.Cog): #Define a classe.
    def __init__(self, bot): #Inicia a classe.
        self.bot = bot
        super().__init__()


    @commands.command() #Define como um comando.
    @commands.has_permissions(administrator=True) #Necessário ter perm de ADM
    async def setuplog(self, ctx): #O usuário utiliza o comando "setuplog" (Cria o canal de 'logs') definindo aonde sera encaminhado os logs.
        guild = ctx.guild
        overwrites = { #Permissões do canal.
        guild.default_role: discord.PermissionOverwrite(read_messages=False), #@everyone Pessoas sem ADM não podem ver o canal.
        guild.me: discord.PermissionOverwrite(read_messages=True, send_messages=True) #Pessoas com ADM podem ler e escrever no canal.
    }
        log_channel = await guild.create_text_channel('logs', overwrites=overwrites)  #Cria o canal com as permsissões no "overwrites".
        await log_channel.send('Canal de log criado com sucesso.') #Envia a mensagem de confirmação da criação do canal logs no "logs".