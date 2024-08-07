import discord
import groq
from discord.ext import commands

import config


class Error(discord.Cog, name="Errors"):
    def __init__(self, bot: discord.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_application_command_error(self, ctx: discord.ApplicationContext,
                                           err: discord.ApplicationCommandInvokeError):
        if isinstance(err, commands.MissingPermissions):
            perms = "`" + '`, `'.join(err.missing_permissions) + "`"
            return await ctx.respond(f"{config.crossmark} **You are missing {perms} permissions.**", ephemeral=True)

        if isinstance(err, commands.BotMissingPermissions):
            perms = "`" + '`, `'.join(err.missing_permissions) + "`"
            return await ctx.respond(f"{config.crossmark} **I'm missing {perms} permissions**", ephemeral=True)

        if isinstance(err, commands.CommandOnCooldown):
            return await ctx.respond(
                f"{config.crossmark} **This command is on co!!!oldown for {round(err.retry_after)} more seconds.**",
                ephemeral=True)

        if isinstance(err, commands.MemberNotFound):
            return await ctx.respond(f"{config.confused} **Could not find user `{err.argument}`", ephemeral=True)

        if isinstance(err, discord.NotFound):
            return await ctx.respond("I could not find the argument you have provided.", ephemeral=True)

        err = err.original  # Unwrap the exception to catch any non-discord errors

        if isinstance(err, groq.RateLimitError):
            return await ctx.respond(f"You are using this command too much! {err.message.split('.')[1]}s",
                                     ephemeral=True)

        await ctx.respond("An unknown error occured! This will be logged and fixed!", ephemeral=True)
        print(f"{ctx.author.global_name} used /{ctx.command} which caused {err}")


def setup(bot):
    bot.add_cog(Error(bot))
