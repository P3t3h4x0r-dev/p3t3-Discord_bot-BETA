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


    def get_log_channel(self, guild):
      #Procura um canal de texto com o nome definido de 'logs'.
        return discord.utils.get(guild.text_channels, name='logs')
    
    
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

    @commands.Cog.listener() #Define como um Event.
    async def on_member_remove(self, member): #Quando um membro sai do servidor.
              log_channel = discord.utils.get(member.guild.channels, name='logs') #Pega o canal chamado 'logs'.
              if log_channel: #Caso tenha o canal de 'Logs'.
                
                embed = discord.Embed( #Cria uma mensagem em embed.
                title="Membro saiu",
                description=f"Sentiremos sua falta.",
                color=discord.Color.purple())
                embed.set_thumbnail(url=f"{member.display_avatar.url}")
                embed.add_field(name=f"", value=f"o usuário {member.mention} saiu do servidor 😢", inline=False)
                await log_channel.send(embed=embed) #Envia a mensagem em embed para o canal 'logs'.


    @commands.Cog.listener() #Define como um Event.
    async def on_member_join(self, member): #Quando um usuário entra.'
          log_channel = discord.utils.get(member.guild.channels, name='logs') #Pega o canal chamado 'Logs'.
          if log_channel: #Caso tenha o canal de 'Logs'.
            embed = discord.Embed( #Cria uma mensagem em embed.
                title="Novo membro",
                description=f"Seja bem vindo ao nosso servidor",
                color=discord.Color.purple())
            
            embed.set_thumbnail(url=f"{member.display_avatar.url}")
            embed.add_field(name=f"", value=f"O usuário {member.mention} Entrou em nosso servidor. 🎉", inline=False)
            
            await log_channel.send(embed=embed) #Envia a mensagem em embed para o canal 'logs'.

      
    @commands.Cog.listener() #Define como um Event.
    async def on_message_delete(self, message): #Quando o Usuário apaga a mensagem.
              log_channel = discord.utils.get(message.guild.channels, name='logs') #Puxa o canal com o nome 'logs'.
              if not message.author.bot: #Caso a mensagem não seja do bot.
                 if log_channel: #Caso tenha o canal de 'Logs'.
                    embed = discord.Embed( #Cria uma mensagem em embed.
                    title="Mensagem Deletada",
                    description=f"A mensagem de {message.author.mention} Foi deletada no canal {message.channel.mention}.",
                    color=discord.Color.purple())

                
                    embed.add_field(name="Conteúdo", value=message.content, inline=False)
                    embed.set_footer(text=f"Autor: {message.author} | ID da mensagem: {message.id}")

                    await log_channel.send(embed=embed) #Envia a mensagem em embed para o canal 'logs'.








    @commands.Cog.listener() #Define como um Event.   
    async def on_message_edit(self, before, after): #Quando a mensagem for editada.
        channel_name = before.channel.name #Puxa o canal que a mensagem foi editada.
        log_channel = discord.utils.get(before.guild.channels, name='logs') #Puxa o canal com o nome 'logs'.
        if log_channel: #Caso tenha o canal de 'Logs'.
          if not after.author.bot: #Caso a mensagem não seja do bot.
            if log_channel: #Caso tenha o canal de 'Logs'.
                embed = discord.Embed( #Cria uma mensagem em embed.
                title="Mensagem editada",
                description=f"A mensagem foi editada por {after.author.mention}.",
                color=discord.Color.purple())

           
                embed.add_field(name="Conteúdo Original:", value=before.content, inline=False)
                embed.add_field(name="Conteúdo Alterado:", value=after.content, inline=False)

                await log_channel.send(embed=embed) #Envia a mensagem em embed para o canal 'logs'.

            
          

    @commands.Cog.listener() #Define como um Event.
    async def on_user_update(self, before, after): #Quando o usuario mudar o perfil.
        if before.avatar != after.avatar:
            for guild in self.bot.guilds: #Caso o avatar seja diferenque que antes.
                log_channel = self.get_log_channel(guild) #Puxa o canal 'logs'.
                if log_channel: #Caso tenha o canal de 'Logs'.
                    embed = discord.Embed( #Cria uma mensagem em embed.
                        title="Avatar Atualizado",
                        description=f"{after.display_name} atualizou seu avatar.",
                        color=discord.Color.purple())
                    if after.avatar: 
                        embed.set_thumbnail(url=after.avatar.url)
                    await log_channel.send(embed=embed) #Envia a mensagem em embed para o canal 'logs'.
        
        if before.name != after.name: #Quando o nome de usuario foi diferente que antes
            for guild in self.bot.guilds: #para todos servidores (vou arrumar essa desgraça)
                log_channel = self.get_log_channel(guild)
                if log_channel: #caso tenha o canal de logs
                    embed = discord.Embed( #cria a mensagem em embed
                        title="Nome de Usuário Atualizado",
                        description=f"{before.name} mudou seu nome para {after.name}.",
                        color=discord.Color.purple()
                       
                    )
                    await log_channel.send(embed=embed) #Envia a mensagem em embed para o canal 'logs'.

       