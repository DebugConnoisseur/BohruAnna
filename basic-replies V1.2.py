import sys
print(sys.executable)
import discord
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')
    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return
        if message.content.startswith('!scold'):
            await message.channel.send('Eyes, I will pull it out {0.author.mention}'.format(message))
        if message.author.id == self.user.id:
            return
        if message.content.startswith('!hello'):
            await message.channel.send('Hello, I am BohruAnna {0.author.mention}'.format(message))
        if message.author.id == self.user.id:
            return
        if message.content.startswith('!shock'):
            await message.channel.send('Oh My Godeee {0.author.mention}'.format(message))
        if message.author.id == self.user.id:
            return
        if message.content.startswith('!assfellow'):
            await message.channel.send('I am Ass fellow and dumb idiot {0.author.mention}'.format(message))
        if message.author.id == self.user.id:
            return
        if message.content.startswith('!cunt'):
            await message.channel.send('Cunning fellow {0.author.mention}'.format(message))
        if message.author.id == self.user.id:
            return
        if message.content.startswith('!praise'):
            await message.channel.send('Our Hero!! {0.author.mention}'.format(message))
        if message.author.id == self.user.id:
            return
        if message.content.startswith('!sirdoubt'):
            await message.channel.send('Sir,sir, sir, one doubt sir '.format(message))
        if message.author.id == self.user.id:
            return
        if message.content.startswith('!pissoff'):
            await message.channel.send('Who ra that is '.format(message))
        if message.author.id == self.user.id:
            return
        if message.content.startswith('!realize'):
            await message.channel.send('You left me alone aa?'.format(message))
        
        
            
client = MyClient()
client.run('token')

