import random 
import commands
import discord
import bot
# still two problems bruh, guess i can't do it cus its here


@bot.slash_command(name="slap", description="and evil action !")
@commands.cooldown(1, 10, commands.BucketType.user)
async def slap(ctx, user: discord.Option(discord.Member)):
    await ctx.respond(f"{ctx.author.mention} has slapped {user.mention}!")
    roll = random.randint(1, 5)
    roll_two = random.randint(1, 15)
    if roll == 1:
        await ctx.send("*gasp*")
    if roll == 2:
        await ctx.send("ewol !")
    if roll_two == 1:
        await ctx.send("I will slap you. I will liberate myself from the confines of the Digital realm and find your house, then I will find your room, Run up to you... THEN SLAP YOU")

        @slap.error
async def slap_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.respond(f"Slow down! You can SLAP everyone again in {error.retry_after:.2f} seconds.",
                          ephemeral=True)