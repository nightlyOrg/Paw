import time

import discord

import utils
from utils.data import Colors


async def send_welcome_message(member: discord.Member):
    channel = member.guild.get_channel(1066357407443333190)
    embed = discord.Embed(color=Colors.purple)
    embed.set_thumbnail(url=member.display_avatar)
    embed.description = f"""
Welcome to the server, {member.mention}!\nFeel free to visit <id:customize> for roles & channels and <id:guide> for some useful info!
__**IMPORTANT**__: To gain access to the rest of the server, you need to first gain a level by chatting in this channel.
Thank you for reading and have fun!"""
    await channel.send(content=f"<@&822886791312703518>, welcome {member.mention}", embed=embed)


async def unverified_role_handler(member_old: discord.Member, member: discord.Member):
    verified_roles = utils.inactive_roles

    unverified_role = member.guild.get_role(1165755854730035301)

    if any(role.id in verified_roles for role in member.roles):  # If member has a verified role
        if unverified_role in member.roles:  # If member has the unverified role
            await member.remove_roles(unverified_role)
    elif any(role.id in verified_roles for role in member_old.roles):  # If member had a verified role before
        if unverified_role in member.roles:  # If member has the unverified role
            await member.remove_roles(unverified_role)
    else:  # If member didn't have a verified role before or after
        if unverified_role not in member.roles:
            await member.add_roles(unverified_role)


async def userbot_kicker(member: discord.Member):
    member = member.guild.get_member(member.id)  # Get updated member object for up-to-date roles
    botroles_list = [891021633505071174, 731233454716354710]  # Red, Bear
    botroles_list2 = [891021633505071174, 731233454716354710, 731245341495787541,
                      731241481284616282, 731241703100383242, 738350937659408484,
                      738356235841175594]  # Red, Bear Hetero, Male, Single, Europe, Chat Revival
    ignored_roles = [1165755854730035301,  # Unverified role
                     715969701771083817,  # Everyone
                     778893728701087744]  # Townsfolk
    member_roles = [role.id for role in member.roles if role.id not in ignored_roles]
    member_roles_match = set(member_roles) == set(botroles_list) or set(member_roles) == set(
        botroles_list2)  # boolean for both role checks on the member
    if member_roles_match or len(member.roles) >= 75:  # 78 is the number of selfroles + the "mandatory" roles
        try:
            await member.send(
                "You've been kicked from The Paw Kingdom for botlike behaviour. If you are a human, rejoin and select different selfroles")
        except discord.Forbidden:
            pass
        except discord.HTTPException as e:
            return print(f"Kicking member {member.display_name} failed {e}")
        try:
            await member.kick(reason="Bot")
        except Exception as e:
            print(f"Unable to kick bot {member.display_name} ({member.id}). Error:\n{e}")
            return False  # Failsafe
        embed = discord.Embed(color=Colors.orange)
        embed.set_author(name=f"Bot Kick | {member.display_name}", icon_url=member.display_avatar.url)
        embed.set_footer(text=member.id)
        embed.description = f"**User**: {member.mention}\n**User ID**: {member.id}"
        logchannel = member.guild.get_channel(760181839033139260)
        await logchannel.send(embed=embed)
        return True  # Member / Bot has been kicked
    return False  # Member has not been kicked


async def get_inactives(guild: discord.Guild) -> dict[str, list[discord.Member]]:
    unverified = []
    kickworthy = []
    current_time = time.time()
    for member in guild.members:
        if any(role.id in utils.inactive_roles for role in member.roles) or member.bot:
            continue
        if member.joined_at.timestamp() + 604800 < current_time:  # If 7 days passed since join
            kickworthy.append(member)
        else:
            unverified.append(member)

    return {"unverified": unverified, "kickworthy": kickworthy}


def get_gender(member: discord.Member) -> str:
    if isinstance(member, discord.User):
        return "undetermined"

    if member.guild.id != 715969701771083817:
        return "undetermined"
    male_role = member.guild.get_role(731241481284616282)
    female_role = member.guild.get_role(731241521558323227)

    if male_role in member.roles:
        if female_role not in member.roles:
            return "Male"
        else:
            return "undetermined"
    elif female_role in member.roles:
        return "Female"
    else:
        return "undetermined"
