import asyncio
import time

import discord
from discord.ext import commands

from utils import botchecker, unverified, AutoVerify, Colors


class Members(commands.Cog, name="Members"):
    def __init__(self, bot):
        self.bot = bot
        self.inactives_checker = AutoVerify(self.bot)

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        if member.guild.id == 715969701771083817:
            await asyncio.sleep(20)
            if member in member.guild.members:  # If member isn't a bot (95% accurate)
                if await botchecker(member):
                    return
                channel = member.guild.get_channel(1066357407443333190)
                embed = discord.Embed(color=Colors.purple)
                embed.set_thumbnail(url=member.display_avatar)
                embed.description = f"""
Welcome to the server, {member.mention}!\nFeel free to visit <id:customize> for roles & channels and <id:guide> for some useful info!
__**IMPORTANT**__: To gain access to the rest of the server, you need to first gain a level by chatting in this channel.
Thank you for reading and have fun!"""
                await channel.send(content=f"<@&822886791312703518>, welcome {member.mention}", embed=embed)
                await self.inactives_checker.add_member((member.id, time.time()))

    @commands.Cog.listener()
    async def on_member_update(self, member, member_new: discord.Member):
        if member_new.guild.id == 715969701771083817:
            await unverified(member_new.guild)

    inactives = discord.SlashCommandGroup(name="inactives",
                                          default_member_permissions=discord.Permissions(manage_guild=True,
                                                                                         kick_members=True))

    @inactives.command()
    async def get(self, ctx):
        """ Get all inactive members """
        await ctx.defer()
        members = await self.inactives_checker.get_members()
        await ctx.respond(members)


def setup(bot):
    bot.add_cog(Members(bot))
