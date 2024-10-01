import discord 
from discord.ext import commands
from Log.Logs import Logs #Puxa o arquivo de logs e sua classe.
from Administração.ChannelDelete import DeleteChannels #Puxa o arquivo para deletar canais e sua classe.
from Administração.ChannelCreate import CreateChannels #Puxa o arquivo para criar canais e sua classe.
from Administração.RoleCreate import CreateRoles #Puxa o arquivo para criar cargos e sua classe.
from Administração.RoleDelete import DeleteRoles #Puxa o arquivo para deletar canais e sua classe.
from Help.Help import Help #Puxa o arquivo Help e sua classe.
from Segurança.Spam import spam #Puxa o arquivo Anti spam e sua classe.
from Segurança.UserChannelDelete import AntiDeleteChannel
from Segurança.UserChannelCreate import AntiCreateChannel
from Segurança.UserRoleCreate import AntiCreateRoles
from Segurança.UserRoleDelete import AntiDeleteRoles
from Segurança.UserMemberBan import AntiBan
from Segurança.UserMemberKick import AntiKick
from Diversao.entrarnacall import VoiceJoiner

import asyncio
from decouple import config

prefixo = "!" #Prefixo do bot.

#Cria o objeto bot.
bot = commands.Bot(command_prefix=prefixo, intents=discord.Intents.all(), case_insensitive=True, self_bot=True)
bot.remove_command('help')

@bot.event
async def on_ready(): #Quando o bot é iniciado.
    print(f'Bot está online como {bot.user}')
    await bot.change_presence(activity=discord.Game(name="Aceita um cafézinho?"))

async def setup(): #Carrega as classes dos  comandos.
    await bot.add_cog(Logs(bot))
    await bot.add_cog(DeleteChannels(bot))
    await bot.add_cog(CreateChannels(bot))
    await bot.add_cog(CreateRoles(bot))
    await bot.add_cog(DeleteRoles(bot))
    await bot.add_cog(Help(bot))
    await bot.add_cog(spam(bot))
    await bot.add_cog(AntiDeleteChannel(bot))
    await bot.add_cog(AntiCreateChannel(bot))
    await bot.add_cog(AntiCreateRoles(bot))
    await bot.add_cog(AntiDeleteRoles(bot))
    await bot.add_cog(AntiBan(bot))
    await bot.add_cog(AntiKick(bot))
    await bot.add_cog(VoiceJoiner(bot))

asyncio.run(setup()) #Inicia as classes dos comandos.

TOKEN = config("TOKEN")
bot.run(TOKEN)




