import discord
from discord.ext import commands
import os
import requests
import json
import random

client = commands.Bot(command_prefix = "a.")
client.remove_command('help')

@client.command(aliases=["DogFacts","Dogfacts","dogFacts","dogefacts","dog-facts","dog_facts","dogfact","dog_fact","dog-fact"])
async def dogfacts(ctx):
  try:
    response = requests.get('https://some-random-api.ml/facts/dog')
    data = response.json()
    embed = discord.Embed(
        title = 'Random Dog Fact 🐶',
        description = data['fact'],
        colour = discord.Colour.purple()
        )
    embed.set_footer(text=f"AnimalBot • UTC {ctx.message.created_at.hour}:{ctx.message.created_at.minute}")
    await ctx.send(embed=embed)
  except:
    await ctx.send("We cant reach the randomfact api\nIt will possibly be active again in 5-10 minutes until then you can use a.cat or a.dog")

@client.command()
async def ping(ctx):
  await ctx.send("Bot's ping': **{0:.1f}**ms".format(ctx.bot.latency * 1000))


@client.command(aliases=["davet","add"])
async def invite(ctx):
  await ctx.message.add_reaction("📩")
  embed = discord.Embed(
    title = 'Click Here To Add The Bot!',
    url= "https://discord.com/oauth2/authorize?client_id=800873059262660649&permissions=85056&scope=bot",
    description = None,
    color = 0xa9d9ce
    )
  await ctx.author.send(embed=embed)
  await ctx.author.send("Thanks for using AnimalBot!\nFor further information visit our website!:\nhttp://animalbot.netlify.app")


@client.command(aliases=["ElephantFact","Elephantfact","Elephantfacts","elephantfacts","ElephantFacts"])
async def elephantfact(ctx):
  try:
    response = requests.get('https://some-random-api.ml/facts/elephant')
    data = response.json()
    embed = discord.Embed(
        title = 'Random Elephant Fact 🐘',
        description = data['fact'],
        colour = discord.Colour.purple()
        )
    embed.set_footer(text=f"AnimalBot • UTC {ctx.message.created_at.hour}:{ctx.message.created_at.minute}")
    await ctx.send(embed=embed)
  except:
    await ctx.send("We cant reach the randomfact api\nIt will possibly be active again in 5-10 minutes until then you can use a.cat or a.dog")

@client.command(aliases=["GiraffeFact","Giraffefact","Giraffefacts","GiraffeFacts","giraffefacts"])
async def giraffefact(ctx):
  try:
    response = requests.get('https://some-random-api.ml/facts/giraffe')
    data = response.json()
    embed = discord.Embed(
        title = 'Random Giraffe Fact 🦒',
        description = data['fact'],
        colour = discord.Colour.purple()
        )
    embed.set_footer(text=f"AnimalBot • UTC {ctx.message.created_at.hour}:{ctx.message.created_at.minute}")
    await ctx.send(embed=embed)
  except:
    await ctx.send("We cant reach the randomfact api\nIt will possibly be active again in 5-10 minutes until then you can use a.cat or a.dog")

@client.command(aliases=["CatFacts","Catfacts","catFacts","kittenfacts","cat-facts","cat_facts","catfact","cat_fact","cat-fact"])
async def catfacts(ctx):
  try:
    response = requests.get('https://some-random-api.ml/facts/cat')
    data = response.json()
    embed = discord.Embed(
        title = 'Random Cat Fact 😸',
        description = data['fact'],
        colour = discord.Colour.purple()
        )
    embed.set_footer(text=f"AnimalBot • UTC {ctx.message.created_at.hour}:{ctx.message.created_at.minute}")
    await ctx.send(embed=embed)
  except:
    await ctx.send("We cant reach the randomfact api\nIt will possibly be active again in 5-10 minutes until then you can use a.cat or a.dog")

@client.command(aliases=["Pandafacts","pandafact","Pandafact"])
async def pandafacts(ctx):
  try:
    response = requests.get('https://some-random-api.ml/facts/panda')
    data = response.json()
    embed = discord.Embed(
        title = 'Random Panda Fact 🐼',
        description = data['fact'],
        colour = discord.Colour.purple()
        )
    embed.set_footer(text=f"AnimalBot • UTC {ctx.message.created_at.hour}:{ctx.message.created_at.minute}")
    await ctx.send(embed=embed)
  except:
    await ctx.send("We cant reach the randomfact api\nIt will possibly be active again in 5-10 minutes until then you can use a.cat or a.dog")

@client.command(aliases=["Foxfacts","foxfact","Foxfact"])
async def foxfacts(ctx):
  try:
    response = requests.get('https://some-random-api.ml/facts/fox')
    data = response.json()
    embed = discord.Embed(
        title = 'Random Fox Fact 🦊',
        description = data['fact'],
        colour = discord.Colour.purple()
        )
    embed.set_footer(text=f"AnimalBot • UTC {ctx.message.created_at.hour}:{ctx.message.created_at.minute}")
    await ctx.send(embed=embed)
  except:
    await ctx.send("We cant reach the randomfact api\nIt will possibly be active again in 5-10 minutes until then you can use a.cat or a.dog")

@client.command(aliases=["Birdfacts","birdfact","Birdfact"])
async def birdfacts(ctx):
  try:
    response = requests.get('https://some-random-api.ml/facts/bird')
    data = response.json()
    embed = discord.Embed(
        title = 'Random Bird Fact 🐦',
        description = data['fact'],
        colour = discord.Colour.purple()
        )
    embed.set_footer(text=f"AnimalBot • UTC {ctx.message.created_at.hour}:{ctx.message.created_at.minute}")
    await ctx.send(embed=embed)
  except:
    await ctx.send("We cant reach the randomfact api\nIt will possibly be active again in 5-10 minutes until then you can use a.cat or a.dog")

@client.command(aliases=["Koalafacts","koalafact","Koalafact"])
async def koalafacts(ctx):
  try:
    response = requests.get('https://some-random-api.ml/facts/koala')
    data = response.json()
    embed = discord.Embed(
        title = 'Random Koala Fact 🐨',
        description = data['fact'],
        colour = discord.Colour.purple()
        )
    embed.set_footer(text=f"AnimalBot • UTC {ctx.message.created_at.hour}:{ctx.message.created_at.minute}")
    await ctx.send(embed=embed)
  except:
    await ctx.send("We cant reach the randomfact api\nIt will possibly be active again in 5-10 minutes until then you can use a.cat or a.dog")


@client.event
async def on_ready():
    print("Bot Hazır!")
    await client.change_presence(activity=discord.Game(name=f"👉a.help | a.invite👈 In {len(client.guilds)} Servers With over {str(usercount())} users!"))

   

@client.command(aliases=["cats","catgif","Cat","CatGif","catGif","Catgif","CATS","cATS"])
async def cat(ctx):
  response = requests.get('https://aws.random.cat/meow')
  data = response.json()
  embed = discord.Embed(
      title = 'Cat 😸',
      description = None,
      colour = discord.Colour.purple()
      )
  embed.set_image(url=data['file'])            
  embed.set_footer(text=f"AnimalBot • UTC {ctx.message.created_at.hour}:{ctx.message.created_at.minute}")
  await ctx.send(embed=embed)

@client.command(aliases=["Dog","DOG","DOGGO","doggo","doge","puppy","PUPPY","dogs","DOGS","dogGif","doggif"])
async def dog(ctx):
  response = requests.get('https://dog.ceo/api/breeds/image/random')
  data = response.json()
  embed = discord.Embed(
      title = 'Dog 🐶',
      description = None,
      colour = discord.Colour.purple()
      )
  embed.set_image(url=data['message'])            
  embed.set_footer(text=f"AnimalBot • UTC {ctx.message.created_at.hour}:{ctx.message.created_at.minute}")
  await ctx.send(embed=embed)
  
@client.command(aliases=["Bird","BIRD","BIRB","BirdGif","birdgif","birds","Birds","BIRDS"])
async def bird(ctx):
  response = requests.get('https://some-random-api.ml/img/birb')
  data = response.json()
  embed = discord.Embed(
      title = 'Bird 🐦',
      description = None,
      colour = discord.Colour.purple()
      )
  embed.set_image(url=data['link'])            
  embed.set_footer(text=f"AnimalBot • UTC {ctx.message.created_at.hour}:{ctx.message.created_at.minute}")
  await ctx.send(embed=embed)

@client.command(aliases=["Panda","pandas","pandagif","PANDAS","Pandas"])
async def panda(ctx):
  try:
    response = requests.get('https://some-random-api.ml/img/panda')
    data = response.json()
    embed = discord.Embed(
        title = 'Panda 🐼',
        description = None,
        colour = discord.Colour.purple()
        )
    embed.set_image(url=data['link'])            
    embed.set_footer(text=f"AnimalBot • UTC {ctx.message.created_at.hour}:{ctx.message.created_at.minute}")
    await ctx.send(embed=embed)
  except:
    ctx.send("Random image api is down\nIt will probably be active again in 5-10 minutes")

@client.command(aliases=["Fox","foxes","foxgif","FOXES","Foxes","foxs"])
async def fox(ctx):
  response = requests.get('https://randomfox.ca/floof/?ref=apilist.fun')
  data = response.json()
  embed = discord.Embed(
      title = 'Fox 🦊',
      description = None,
      colour = discord.Colour.purple()
      )
  embed.set_image(url=data['image'])            
  embed.set_footer(text=f"AnimalBot • UTC {ctx.message.created_at.hour}:{ctx.message.created_at.minute}")
  await ctx.send(embed=embed)

@client.command(aliases=["Animal","animal","Search","SEARCH"])
async def search(ctx, animal):
  url = f"https://mlem.tech/api/randommlem?mlemid="
  querystring = {"tag": animal}
  headers = {
      'x-rapidapi-key': "cfda95997emsh1ba42a24b9dd6d9p140a0ajsn0e69ed707876",
      'x-rapidapi-host': "mlemapi.p.rapidapi.com"
      }
  response = requests.request("GET", url, headers=headers, params=querystring)
  response_data = response.json()
  data = response_data['code']
  if data == 200:
    embed = discord.Embed(
        title = 'Searched Animal!',
        description = None,
        colour = discord.Colour.purple()
        )
    embed.set_image(url=response_data['url'])            
    embed.set_footer(text=f"AnimalBot • UTC {ctx.message.created_at.hour}:{ctx.message.created_at.minute}")
    await ctx.send(embed=embed)
  else:
    embed = discord.Embed(
        title = 'No image found.',
        description = None,
        colour = discord.Colour(0xff0000)
        )
    await ctx.send(embed=embed)

@client.command(aliases=["tongue","tongueout","Tongue","Mlem","MLEM"])
async def mlem(ctx):
  response = requests.get('https://mlem.tech/api/randommlem')
  data = response.json()
  f = data['tags']
  embed = discord.Embed(
      title = f'I found a mlemming {" ".join(f)} 👅',
      description = None,
      colour = discord.Colour.purple()
      )
  embed.set_image(url=data['url'])
  embed.set_footer(text=f"AnimalBot • UTC {ctx.message.created_at.hour}:{ctx.message.created_at.minute}")
  await ctx.send(embed=embed)

@client.command(aliases=["Duck","ducks","duckgif","DUCK","Ducks","DUCKS"])
async def duck(ctx):
  response = requests.get('https://random-d.uk/api/random')
  data = response.json()
  embed = discord.Embed(
      title = 'Duck 🦆',
      description = None,
      colour = discord.Colour.purple()
      )
  embed.set_image(url=data['url'])
  embed.set_footer(text=f"AnimalBot • UTC {ctx.message.created_at.hour}:{ctx.message.created_at.minute}")
  await ctx.send(embed=embed)

@client.command(aliases=["Help","HELP","hELP"])
async def help(ctx):
  await ctx.message.add_reaction("📩")
  embed = discord.Embed(
      title = 'Join our support server for further information!',
      url="https://discord.gg/AUZwaXHzNw",
      description = "**   --Commands--**",
      colour = discord.Colour.purple()
      )
  embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/791055420856860705/801135294971510815/catbot.png")
  embed.add_field(name="""😸-Animal Photos-🐶""", value="**a.cat**: Sends a cat photo\n**a.dog**: Sends a dog photo\n**a.bird**: Sends a bird photo\n**a.koala**: Sends a koala photo\n**a.panda**: Sends a panda photo\n**a.fox**: Sends a fox photo\n**a.whale**: Sends a whale photo\n**a.racoon**: Sends a racoon photo\n**a.kangaroo**: Sends a kangaroo photo\n**a.duck**: Sends a duck photo\n**a.mlem**: Sends a mlemming (tongue out) animal\n**a.search [animal]**: Searches the inputted animal photo on the internet!", inline = False)
  embed.add_field(name="""🐼-Animal Facts-🐦""",value="**a.catfact**: Sends a random cat fact\n**a.dogfact**: Sends a random dog fact\n**a.pandafact**: Sends a random pandafact\n**a.birdfact**: Sends a random birdfact\n**a.foxfact**: Sends a random fox fact\n**a.koalafact**: Sends a random koala fact\n**a.elephantfact**: Sends a random elephant fact\n**giraffefact**: Sends a random giraffe fact\n", inline = False)
  embed.add_field(name="""😂-Other-😂""",value="**joke**: Tells a random joke", inline = False)
  embed.add_field(name="""📜-Info-📜""",value="**a.credits**: Sends a list of botmakers\n**a.website**: Sends the official bot website\n**a.invite**: Sends a link that you can use to add me to your own servers\n**a.support**: Sends the link to our support server", inline= True)
  embed.set_author(name="Add AnimalBot to your server!", url="https://discord.com/api/oauth2/authorize?client_id=800873059262660649&permissions=85056&scope=bot", icon_url="https://cdn.discordapp.com/attachments/791055420856860705/801135294971510815/catbot.png")
  embed.set_footer(text=f"AnimalBot • UTC {ctx.message.created_at.hour}:{ctx.message.created_at.minute}")
  await ctx.author.send(embed=embed)

@client.command()
async def joke(ctx):
  try:
    response = requests.get('https://some-random-api.ml/joke')
    data = response.json()
    embed = discord.Embed(
        title = 'Joke 😂',
        description = data['joke'],
        colour = discord.Colour.purple()
        )
    embed.set_footer(text=f"AnimalBot • UTC {ctx.message.created_at.hour}:{ctx.message.created_at.minute}")
    await ctx.send(embed=embed)
  except:
    ctx.send("Random image joke is down\nIt will probably be active again in 5-10 minutes")


@client.command(aliases=["Koala","Koalas","KOALAS","KOALA","Koalagif","koalaGif","koalagif","KoalaGif"])
async def koala(ctx):
  try:
    response = requests.get('https://some-random-api.ml/img/koala')
    data = response.json()
    embed = discord.Embed(
        title = 'Koala 🐨',
        description = None,
        colour = discord.Colour.purple()
        )
    embed.set_image(url=data['link'])
    embed.set_footer(text=f"AnimalBot • UTC {ctx.message.created_at.hour}:{ctx.message.created_at.minute}")
    await ctx.send(embed=embed)
  except:
    ctx.send("Random image api is down\nIt will probably be active again in 5-10 minutes")

@client.command(aliases=["Whale","Whales","whales","WHALE","WHALES"])
async def whale(ctx):
  try:
    response = requests.get('https://some-random-api.ml/img/whale')
    data = response.json()
    embed = discord.Embed(
        title = 'Whale 🐳',
        description = None,
        colour = discord.Colour.purple()
        )
    embed.set_image(url=data['link'])
    embed.set_footer(text=f"AnimalBot • UTC {ctx.message.created_at.hour}:{ctx.message.created_at.minute}")
    await ctx.send(embed=embed)
  except:
    ctx.send("Random image api is down\nIt will probably be active again in 5-10 minutes")

@client.command(aliases=["Racoon","RACOON","Racoons","racoons","RACOONS"])
async def racoon(ctx):
  try:
    response = requests.get('https://some-random-api.ml/img/racoon')
    data = response.json()
    embed = discord.Embed(
        title = 'Racoon 🦝',
        description = None,
        colour = discord.Colour.purple()
        )
    embed.set_image(url=data['link'])
    embed.set_footer(text=f"AnimalBot • UTC {ctx.message.created_at.hour}:{ctx.message.created_at.minute}")
    await ctx.send(embed=embed)
  except:
    ctx.send("Random image api is down\nIt will probably be active again in 5-10 minutes")

@client.command(aliases=["Kangaroo","KANGAROO","Kangaroos","kangaroos","KANGAROOS"])
async def kangaroo(ctx):
  try:
    response = requests.get('https://some-random-api.ml/img/kangaroo')
    data = response.json()
    embed = discord.Embed(
        title = 'Kangaroo 🦘',
        description = None,
        colour = discord.Colour.purple()
        )
    embed.set_image(url=data['link'])
    embed.set_footer(text=f"AnimalBot • UTC {ctx.message.created_at.hour}:{ctx.message.created_at.minute}")
    await ctx.send(embed=embed)
  except:
    ctx.send("Random image api is down\nIt will probably be active again in 5-10 minutes")


@client.command()
@commands.is_owner()
async def servers(ctx):
  sum = 0
  serverlist = []
  for server in client.guilds:
    print(str(server.member_count) +"    "+ server.name)
    serverlist.append(server.name)
    sum += server.member_count
  await ctx.send("**The Servers That AnimalBot is in**\n------------------------------------\n```" + "\n".join(str(item) for item in serverlist) + "```" + f"\n **AnimalBot is in {len(client.guilds)} servers with {usercount()} users!**")
  totalmem = 0
  await client.change_presence(activity=discord.Game(name=f"👉a.help | a.invite👈 In {len(client.guilds)} Servers With over {str(usercount())} users!"))

def usercount():
  sum = 0
  for server in client.guilds:
    sum += server.member_count
  return str(sum)
  

@client.command()
async def support(ctx):
  await ctx.message.add_reaction("📩")
  await ctx.author.send("https://discord.gg/gED6d3JRsa")

@client.command()
@commands.is_owner()
async def durumayarla(ctx, *, durum):
  await client.change_presence(activity=discord.Game(name=durum))

@client.command()
async def website(ctx):
  await ctx.send("http://animalbot.netlify.app/")

@client.command()
async def credits(ctx):
  embed = discord.Embed(
        title = 'Developers',
        description = None,
        colour = discord.Colour.purple()
        )
  embed.add_field(name="Web-Development, Coding, and Design", value="`Eren#2222`")
  embed.add_field(name="Testing", value="`ˇ Expecto#1710`", inline= False)
  await ctx.send(embed=embed)


TOKEN = os.environ.get("BOT_TOKEN")
client.run(TOKEN)