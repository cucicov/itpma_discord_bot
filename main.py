import discord
import os
import time
import logging
from discord.ext import tasks

# for webscraping
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# for generating random color
import random
import randomcolor
from PIL import Image
import colorsys

logging.basicConfig(filename='bot.log', level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')

TOKEN='MTA4NzI5MjY4MTk5MjAyODE5MQ.GM1WLv.wT5iHY0otuInOxc8R7peJJXo7kDhBrl0pNFV0A'

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
client = discord.Client(intents=intents)


oblique = ["A very small object         ",
"Abandon desire",
"Abandon normal instructions",
"Abandon normal instruments",
"Accept advice",
"Accretion",
"Allow an easement (an easement is the abandonment of a stricture)",
"Always first steps",
"Always give yourself credit for having more than personality (given by Arto Lindsay)",
"Always the first steps",
"Are there sections?  Consider transitions",
"Ask people to work against their better judgement",
"Ask your body",
"Assemble some of the elements in a group and treat the group",
"Balance the consistency principle with the inconsistency principle",
"Be dirty",
"Be extravagant",
"Be less critical",
"Breathe more deeply",
"Bridges   -build   -burn",
"Bridges -build -burn",
"Cascades",
"Change ambiguities to specifics",
"Change instrument roles",
"Change nothing and continue consistently",
"Change nothing and continue with immaculate consistency",
"Change specifics to ambiguities",
"Children   -speaking     -singing",
"Cluster analysis",
"Consider different fading systems",
"Consider transitions",
"Consult other sources   -promising   -unpromising",
"Convert a melodic element into a rhythmic element",
"Courage!",
"Cut a vital conenction",
"Cut a vital connection",
"Decorate, decorate",
"Define an area as `safe' and use it as an anchor",
"Destroy  -nothing   -the most important thing",
"Destroy nothing; Destroy the most important thing",
"Discard an axiom",
"Disciplined self-indulgence",
"Disconnect from desire",
"Discover the recipes you are using and abandon them",
"Discover your formulas and abandon them",
"Display your talent",
"Distort time",
"Distorting time",
"Do nothing for as long as possible",
"Do something boring",
"Do something sudden, destructive and unpredictable",
"Do the last thing first",
"Do the washing up",
"Do the words need changing?",
"Do we need holes?",
"Don't avoid what is easy",
"Don't be frightened of cliches",
"Don't break the silence",
"Don't stress on thing more than another [sic]",
"Don't stress one thing more than another",
"Dont be afraid of things because they're easy to do",
"Dont be frightened to display your talents",
"Emphasize differences",
"Emphasize repetitions",
"Emphasize the flaws",
"Faced with a choice, do both (from Dieter Rot)",
"Faced with a choice, do both (given by Dieter Rot)",
"Feed the recording back out of the medium",
"Fill every beat with something",
"Find a safe part and use it as an anchor",
"Get your neck massaged",
"Ghost echoes",
"Give the game away",
"Give the name away",
"Give way to your worst impulse",
"Go outside.  Shut the door.",
"Go outside. Shut the door.",
"Go slowly all the way round the outside",
"Go to an extreme, come part way back",
"Honor thy error as a hidden intention",
"Honor thy mistake as a hidden intention",
"How would someone else do it?",
"How would you have done it?",
"Humanize something free of error",
"Idiot glee (?)",
"Imagine the piece as a set of disconnected events",
"In total darkness, or in a very large room, very quietly",
"Infinitesimal gradations",
"Intentions   -nobility of  -humility of   -credibility of",
"Into the impossible",
"Is it finished?",
"Is something missing?",
"Is the information correct?",
"Is the style right?",
"Is there something missing",
"It is quite possible (after all)",
"It is simply a matter or work",
"Just carry on",
"Left channel, right channel, center channel",
"Listen to the quiet voice",
"Look at the order in which you do things",
"Look closely at the most embarrassing details & amplify them",
"Lost in useless territory",
"Lowest common denominator",
"Magnify the most difficult details",
"Make a blank valuable by putting it in an exquisite frame",
"Make a sudden, destructive unpredictable action; incorporate",
"Make an exhaustive list of everything you might do & do the last thing on the list",
"Make it more sensual",
"Make what's perfect more human",
"Mechanicalize something idiosyncratic",
"Move towards the unimportant",
"Mute and continue",
"Not building a wall but making a brick",
"Not building a wall; making a brick",
"Once the search has begun, something will be found",
"Only a part, not the whole",
"Only one element of each kind",
"Openly resist change",
"Overtly resist change",
"Pae White's non-blank graphic metacard",
"Put in earplugs",
"Question the heroic",
"Question the heroic approach",
"Reevaluation (a warm feeling)",
"Remember quiet evenings",
"Remember those quiet evenings",
"Remove a restriction",
"Remove ambiguities and convert to specifics",
"Remove specifics and convert to ambiguities",
"Repetition is a form of change",
"Retrace your steps",
"Reverse",
"Short circuit (example; a man eating peas with the idea that they will improve  his virility shovels them straight into his lap)",
"Simple Subtraction",
"Simple subtraction",
"Simply a matter of work",
"Slow preparation, fast execution",
"Spectrum analysis",
"State the problem as clearly as possible",
"State the problem in words as clearly as possible",
"Take a break",
"Take away the elements in order of apparent non-importance",
"Take away the important parts",
"Tape your mouth (given by Ritva Saarikko)",
"The inconsistency principle",
"The most easily forgotten thing is the most important",
"The most important thing is the thing most easily forgotten",
"The tape is now the music",
"Think - inside the work -outside the work",
"Think of the radio",
"Tidy up",
"Towards the insignificant",
"Trust in the you of now",
"Try faking it (from Stewart Brand)",
"Turn it upside down",
"Twist the spine",
"Use 'unqualified' people",
"Use `unqualified' people",
"Use an old idea",
"Use an unacceptable color",
"Use cliches",
"Use fewer notes",
"Use filters",
"Use something nearby as a model",
"Use your own ideas",
"Voice your suspicions",
"Water",
"What are the sections sections of?    Imagine a caterpillar moving",
"What are you really thinking about just now?",
"What context would look right?",
"What is the reality of the situation?",
"What is the simplest solution?",
"What mistakes did you make last time?",
"What to increase? What to reduce? What to maintain?",
"What were you really thinking about just now?",
"What would your closest friend do?",
"What wouldn't you do?",
"When is it for?",
"Where is the edge?",
"Which parts can be grouped?",
"Work at a different speed",
"Would anyone want it?",
"You are an engineer",
"You can only make one dot at a time",
"You don't have to be ashamed of using your own ideas",
"[blank white card]"]


# set the path and the name for the temporary PNG image of the color
filepath = "/Users/denisflueraru/Documents/dibot/itpma_discord_bot"
tempname = "temp_img.png"
filepath = filepath + tempname

# set catchphrases for loading time
loading_text = ["Mhmmm, let's see...","I bet you've never heard of this one before.", "Do you know this one?", 
                "Let me think, what new colors are there?", "I have updates for you...",
                "Allow me to find a color made especially just for you"]

def generate_color():

    global color_hex
    # generate a random color and get its hex number. the output is a list, and we need a string  
    color_hex = randomcolor.RandomColor().generate()

    # create an empty string and convert the list to string
    color_string= ''

    for x in color_hex:
        color_string +=''+ x
        color_hex = color_string # this is just a string for e.g #ab2f42

    return color_hex


def get_color_info(color_hex):

    global color_name
    global r, g ,b

    web = 'https://chir.ag/projects/name-that-color/'

    # to create the complete website url joing the web link with the color_hex 
    url = web + color_hex # it should be something like https://chir.ag/projects/name-that-color/#ab2f42
    
    # Use a headless browser to simulate a web browser without opening a window
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(options=options)

    driver.get(url)

    # Wait for the color name element to appear before getting its text
    color_name_element = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.ID, 'colorname'))
    )
            
    color_name = color_name_element.text
            
    # Get the RGB values
    color_rgb_element = WebDriverWait(driver, 0.01).until(
        EC.presence_of_element_located((By.ID, 'colorrgb')) #for eg color_rgb_element = RGB: 125, 239, 110
    )
        
    color_rgb = color_rgb_element.text[4:] #parse only the tuple of RGB values; for eg: "125, 239, 110"
            
    # split and convert the string into list and then convert each item of the list in int numbers for R,G,B values
    color_rgb = color_rgb.split(',')
    r = int(color_rgb[0])
    g = int(color_rgb[1])
    b = int(color_rgb[2])
        
    # create image with RGB values
    img = Image.new('RGB', (300, 200), (r,g,b))
            
    # temporarily save the image to the path
    img.save(filepath)

    # Remove the approx. or solid. substring from the color name text
    color_name = color_name.replace("approx.","").replace("solid.","")

    # Close the browser
    driver.quit()

def generate_random_blue():
    # Set the hue to a random value in the blue range (200-260)
    h = random.randint(200, 260)
    # Set the saturation to a random value (50-100)
    s = random.randint(50, 100)
    # Set the value to a random value (50-100)
    v = random.randint(50, 100)
    # Convert the HSV color to RGB color | Hue: 0-360 degree -> 0.0-1.0; Saturation: 0-100% -> 0.0-1.0; Value: 0-100% -> 0.0-1.0
    r, g, b = tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h/360, s/100, v/100))
     # Convert RGB color to hex code
    blue_hex = "#{:02x}{:02x}{:02x}".format(r, g, b)
    return blue_hex

def generate_random_red():
    # Set hue to a random value in the range of red colors
    h = random.uniform(0, 10)/360 + random.uniform(0, 3)/360
    # Set saturation to a random value between 50% and 100%
    s = random.uniform(50, 100) / 100
    # Set value to a random value between 50% and 100%
    v = random.uniform(50, 100) / 100
    # Convert HSV color to RGB color
    r, g, b = tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))
    # Convert RGB color to hex code
    red_hex = "#{:02x}{:02x}{:02x}".format(r, g, b)
    return red_hex

def generate_random_orange():
    # Set hue to a random value in the range of orange colors
    h = random.uniform(10, 40)/360 + random.uniform(0, 10)/360
    # Set saturation to a random value between 50% and 100%
    s = random.uniform(50, 100) / 100
    # Set value to a random value between 50% and 100%
    v = random.uniform(50, 100) / 100
    # Convert HSV color to RGB color
    r, g, b = tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))
    # Convert RGB color to hex code
    orange_hex = "#{:02x}{:02x}{:02x}".format(r, g, b)
    return orange_hex

def generate_random_purple():
    # Generate a random hue value in the range 280 to 320 degrees
    h = random.uniform(255, 280) / 360
    # Set saturation and value to 100%
    s = random.uniform(0.5, 1.0)
    v = random.uniform(0.7, 1.0)
    # Convert HSV to RGB
    r, g, b = tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))
    # Convert RGB to hex code
    purple_hex = "#{:02x}{:02x}{:02x}".format(r, g, b)
    return purple_hex

def generate_random_pink():
    # Generate a random hue value in the range 280 to 320 degrees
    h = random.uniform(290, 340) / 360
    # Set saturation and value to 100%
    s = random.uniform(0.5, 1.0)
    v = random.uniform(0.7, 1.0)
    # Convert HSV to RGB
    r, g, b = tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))
    # Convert RGB to hex code
    pink_hex = "#{:02x}{:02x}{:02x}".format(r, g, b)
    return pink_hex

def generate_random_yellow():
    # Generate a random hue value in the range 50 to 60 degrees
    h = random.uniform(50, 60) / 360
    # Set saturation and value to 100%
    s = random.uniform(0.5, 1.0)
    v = random.uniform(0.7, 1.0)
    # Convert HSV to RGB
    r, g, b = tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))
    # Convert RGB to hex code
    yellow_hex = "#{:02x}{:02x}{:02x}".format(r, g, b)
    return yellow_hex

def generate_random_green():
    # Hue values for green range from approximately 90 to 180 degrees
    h = random.uniform(90, 180)/360 + random.uniform(-5, 5)/360
    s = random.uniform(50, 100) / 100
    v = random.uniform(50, 100) / 100
    r, g, b = tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))
    green_hex = '#{:02x}{:02x}{:02x}'.format(r, g, b)
    return green_hex

@client.event
async def on_message(message):

    # don't respond to ourselves
    if message.author == client.user:
        return

    logging.info(f'{message.author}: {message.content}')
    
    # if somebody types /color, the bot responds
    if message.content == '/color':

        await message.channel.send(loading_text[random.randint(0,5)])   # have the bot reply with one of the loading catchphrases   
        
        generate_color()
        get_color_info(color_hex)

        # send message and image on Discord server
        await message.channel.send(f"{color_name} or {color_hex}")
        await message.channel.send(file=discord.File(filepath))  #send image
        
        # delete the image after x seconds
        time.sleep(1)
        os.remove(filepath)   

    if message.content == '/blue':
        
        await message.channel.send("Let me think of a blue color for you...")

        blue_shade = generate_random_blue()
        get_color_info(blue_shade)

        # send message and image on Discord server
        await message.channel.send(f"There are many shades of blue color, for example {color_name} or {blue_shade}")
        await message.channel.send(file=discord.File(filepath))  #send image
        
        # delete the image after x seconds
        time.sleep(1)
        os.remove(filepath)

    if message.content == '/green':
        
        await message.channel.send("Let me think of a green color for you...")

        green_shade = generate_random_green()
        get_color_info(green_shade)

        # send message and image on Discord server
        await message.channel.send(f"There are many shades of green color, for example {color_name} or {green_shade}")
        await message.channel.send(file=discord.File(filepath))  #send image
        
        # delete the image after x seconds
        time.sleep(1)
        os.remove(filepath)

    if message.content == '/red':
        
        await message.channel.send("Let me think of a red color for you...")

        red_shade = generate_random_red()
        get_color_info(red_shade)

        # send message and image on Discord server
        await message.channel.send(f"There are many shades of red color, for example {color_name} or {red_shade}")
        await message.channel.send(file=discord.File(filepath))  #send image
        
        # delete the image after x seconds
        time.sleep(1)
        os.remove(filepath)

    if message.content == '/yellow':
        
        await message.channel.send("Let me think of a yellow color for you...")

        yellow_shade = generate_random_yellow()
        get_color_info(yellow_shade)

        # send message and image on Discord server
        await message.channel.send(f"There are many shades of yellow color, for example {color_name} or {yellow_shade}")
        await message.channel.send(file=discord.File(filepath))  #send image
        
        # delete the image after x seconds
        time.sleep(1)
        os.remove(filepath)

    if message.content == '/purple':
        
        await message.channel.send("Let me think of a purple color for you...")

        purple_shade = generate_random_purple()
        get_color_info(purple_shade)

        # send message and image on Discord server
        await message.channel.send(f"There are many shades of purple color, for example {color_name} or {purple_shade}")
        await message.channel.send(file=discord.File(filepath))  #send image
        
        # delete the image after x seconds
        time.sleep(1)
        os.remove(filepath)

    if message.content == '/orange':
        
        await message.channel.send("Let me think of a orange color for you...")

        orange_shade = generate_random_orange()
        get_color_info(orange_shade)

        # send message and image on Discord server
        await message.channel.send(f"There are many shades of orange color, for example {color_name} or {orange_shade}")
        await message.channel.send(file=discord.File(filepath))  #send image
        
        # delete the image after x seconds
        time.sleep(1)
        os.remove(filepath)

    if message.content == '/pink':
        
        await message.channel.send("Let me think of a pink color for you...")

        pink_shade = generate_random_pink()
        get_color_info(pink_shade)

        # send message and image on Discord server
        await message.channel.send(f"There are many shades of pink color, for example {color_name} or {pink_shade}")
        await message.channel.send(file=discord.File(filepath))  #send image
        
        # delete the image after x seconds
        time.sleep(1)
        os.remove(filepath)

    if message.content == "/help":
        with open("help.txt", "r") as f:
            help_text = f.read()
        await message.author.send(help_text) # private text sent by bot
        await message.author.send("Pssst, you can also chat with me in private :shushing_face: :spy: :wink:")
        await message.channel.send(help_text) # text send on the channel
            
    if message.content == "/shuffle":
        await message.channel.send(oblique[random.randint(0,187)])

      if message.content.startswith('/play'):
        channelVoice = client.get_guild(1087291719898382427).get_channel(1087291720531705939)
        voice_client = await channelVoice.connect()
        voice_client.play(discord.FFmpegPCMAudio("Sound\\The Weeknd - Starboy (Live From The AMAs) (192 kbps).mp3"))      

@client.event
async def on_guild_join(guild):
    logging.info(f'Joined server: {guild.id}')

    channels = guild.text_channels
    voice_channels = guild.voice_channels

    channel = client.get_guild(guild.id).get_channel(channels[0].id)
    await channel.send("hey, guys!")

    channel = client.get_guild(guild.id).get_channel(channels[0].id)
    await channel.send("Are you ready to become the world's finest color connoisseur?")
    await myLoop.start(guild.id,channel.id)

    #channel_voice = client.get_guild(guild.id).get_channel(voice_channels[0].id)
    #voice = await channel_voice.connect()
    #voice.play(discord.FFmpegPCMAudio("C:/Users/dorin/Downloads/sample.mp3"))


@client.event
async def on_ready():
    logging.info(f'{client.user} has connected to Discord!')
    print("Bot connected to the server!")
     

@tasks.loop(seconds = 3600) # repeat every hour
async def myLoop(guild_id, channel_id):
    await client.wait_until_ready()
  

    channel = client.get_guild(guild_id).get_channel(channel_id)

    generate_color()
    get_color_info(color_hex)

    # send message and image on Discord server
    await channel.send(f"The new color of the moment is {color_name} or {color_hex}")
    await channel.send(file=discord.File(filepath))  #send image
            
    # delete the image after x seconds
    time.sleep(1)
    os.remove(filepath)





client.run(TOKEN)
