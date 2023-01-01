import hikari
import lightbulb
import yfinance as yf
from currency_converter import CurrencyConverter

# BOT

# Discord bot token
bot = lightbulb.BotApp(
    token='token', # Enter your generated token here
    default_enabled_guilds=('') # Enter Server ID here
)

# Displays if the bot has started
@bot.listen(hikari.StartedEvent)
async def on_started(event):
    print("The bot has started!")

# Stock Price Command
@bot.command
@lightbulb.option('stock', 'Enetered stock') # Enter field for stock
@lightbulb.command('stockprice', 'Search the price of a chosen stock!')
@lightbulb.implements(lightbulb.SlashCommand) # Uses the slash command feature
async def stockPrice(ctx):
    inputtedStock = ctx.options.stock # Takes user input of stock
    findStock = yf.Ticker(inputtedStock) # Uses library to find stock
    endStockPrice = round(findStock.info['regularMarketPrice'], 2) # Takes stock price, roudnds to 2 D.P
    endStockName = findStock.info['longName'] # Takes stock name
    output = "The price of " + str(endStockName) + " is $" + str(endStockPrice) + "."
    await ctx.respond(output) # Ouputs stock price and name to user

# Stock Info Command
@bot.command
@lightbulb.option('stock', 'Entered stock') # Enter field for stock
@lightbulb.command('stockinfo', 'Recieve information about a chosen stock!')
@lightbulb.implements(lightbulb.SlashCommand) # Uses the slash command feature
async def stockInfo(ctx):
    inputtedStock = ctx.options.stock # Takes user input of stock
    findStock = yf.Ticker(inputtedStock) # Uses library to find stock
    stockName = findStock.info['longName'] # Takes stock name
    stockPrice = round(findStock.info['regularMarketPrice'], 2) # Takes stock price, roudnds to 2 D.P
    stockSummary = findStock.info['longBusinessSummary'] # # Takes stock summary 
    stockCity = findStock.info['city'] # Takes stock city 
    stockState = findStock.info['state'] # Takes stock state
    stockCountry = findStock.info['country'] # Takes stock country
    stockPhone = findStock.info['phone'] # Takes stock phone number
    stockWebsite = findStock.info['website'] # Takes stock website URL
    output = "Stock Name: " + str(stockName) + "\nStock Price: $" + str(stockPrice) + "\nStock Website: " + str(stockWebsite) + "\nStock Phone: " + str(stockPhone) + "\nStock City: " + str(stockCity) + "\nStock State: " + str(stockState) + "\nStock Country: " + str(stockCountry)
    await ctx.respond(output) # Responds with output variable
    await ctx.respond(stockSummary) # Responds with summary variable, since output is limited to 2000 characters

# Currency Converter USD to EUR
@bot.command
@lightbulb.option('amount', 'Enter USD', str)
@lightbulb.command('usd-eur', 'Convert from USD to EUR')
@lightbulb.implements(lightbulb.SlashCommand)
async def convertCurrencyUSDEUR(ctx):
    convert = CurrencyConverter()
    inputtedAmount = ctx.options.amount
    converted = round(convert.convert(inputtedAmount, 'USD', 'EUR'), 2)
    output = str(inputtedAmount) + " USD is " + str(converted) + " EUR "
    await ctx.respond(output)

# Currency Converter EUR to USD
@bot.command
@lightbulb.option('amount', 'Enter EUR', str)
@lightbulb.command('eur-usd', 'Convert from EUR to USD')
@lightbulb.implements(lightbulb.SlashCommand)
async def convertCurrencyEURUSD(ctx):
    convert = CurrencyConverter()
    inputtedAmount = ctx.options.amount
    converted = round(convert.convert(inputtedAmount, 'EUR', 'USD'), 2)
    output = str(inputtedAmount) + " EUR is " + str(converted) + " USD "
    await ctx.respond(output)

# Currency Converter USD to GBP
@bot.command
@lightbulb.option('amount', 'Enter USD', str)
@lightbulb.command('usd-gbp', 'Convert from USD to GBP')
@lightbulb.implements(lightbulb.SlashCommand)
async def convertCurrencyUSDGBP(ctx):
    convert = CurrencyConverter()
    inputtedAmount = ctx.options.amount
    converted = round(convert.convert(inputtedAmount, 'USD', 'GBP'), 2)
    output = str(inputtedAmount) + " USD is " + str(converted) + " GBP "
    await ctx.respond(output)

# Currency Converter GBP to USD
@bot.command
@lightbulb.option('amount', 'Enter GBP', str)
@lightbulb.command('gbp-usd', 'Convert from GBP to USD')
@lightbulb.implements(lightbulb.SlashCommand)
async def convertCurrencyGBPUSD(ctx):
    convert = CurrencyConverter()
    inputtedAmount = ctx.options.amount
    converted = round(convert.convert(inputtedAmount, 'GBP', 'USD'), 2)
    output = str(inputtedAmount) + " GBP is " + str(converted) + " USD "
    await ctx.respond(output)

# Currency Converter GBP to JPY
@bot.command
@lightbulb.option('amount', 'Enter GBP', str)
@lightbulb.command('gbp-jpy', 'Convert from GBP to JPY')
@lightbulb.implements(lightbulb.SlashCommand)
async def convertCurrencyGBPJPY(ctx):
    convert = CurrencyConverter()
    inputtedAmount = ctx.options.amount
    converted = round(convert.convert(inputtedAmount, 'GBP', 'JPY'), 2)
    output = str(inputtedAmount) + " GBP is " + str(converted) + " JPY "
    await ctx.respond(output)

# Currency Converter JPY to GBP
@bot.command
@lightbulb.option('amount', 'Enter JPY', str)
@lightbulb.command('jpy-gbp', 'Convert from JPY to GBP')
@lightbulb.implements(lightbulb.SlashCommand)
async def convertCurrencyJPYGBP(ctx):
    convert = CurrencyConverter()
    inputtedAmount = ctx.options.amount
    converted = round(convert.convert(inputtedAmount, 'JPY', 'GBP'), 2)
    output = str(inputtedAmount) + " JPY is " + str(converted) + " GBP "
    await ctx.respond(output)

bot.run() # Runs bot
