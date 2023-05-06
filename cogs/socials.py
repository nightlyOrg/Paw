import data
from discord.ext import commands, bridge
from discord import slash_command, option
from utils import *
import json


class socials(commands.Cog, name="social"):
    def __init__(self, bot):
        self.bot = bot
        self.help_icon = "♥️"

    @bridge.bridge_command(brief="Snuggle someone")
    @option("members", str, description="Mention users to snuggle")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def snuggle(self, ctx, *, members):
        """ Snuggle the specified people """
        memberlist = await mentionconverter(self, ctx, members)
        embed = await interactions(ctx, memberlist, "snuggled", data.snuggle)
        view = interactionsView(ctx, memberlist, "snuggled",  "Snuggle", data.snuggle)
        await ctx.respond(embed=embed, view=view)

    @bridge.bridge_command(brief="Hug someone")
    @option("members", str, description="Mention users to hug")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def hug(self, ctx, *, members):
        memberlist = await mentionconverter(self, ctx, members)
        embed = await interactions(ctx, memberlist, "hugged", data.hug)
        view = interactionsView(ctx, memberlist, "hugged",  "Hug", data.hug)
        await ctx.respond(embed=embed, view=view)

    @bridge.bridge_command(brief="Boop someone")
    @option("members", str, description="Mention users to boop")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def boop(self, ctx, *, members):
        """ Boop the specified people """
        memberlist = await mentionconverter(self, ctx, members)
        embed = await interactions(ctx, memberlist, "booped", data.boop)
        view = interactionsView(ctx, memberlist, "booped", "Boop", data.boop)
        await ctx.respond(embed=embed, view=view)

    @bridge.bridge_command(brief="Kiss someone")
    @option("members", str, description="Mention users to kiss")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def kiss(self, ctx, *, members):
        """ Kiss the specified people """
        memberlist = await mentionconverter(self, ctx, members)
        embed = await interactions(ctx, memberlist, "kissed", data.kiss)
        view = interactionsView(ctx, memberlist, "kissed", "Kiss", data.kiss)
        await ctx.respond(embed=embed, view=view)

    @bridge.bridge_command(brief="Lick someone")
    @option("members", str, description="Mention users to lick")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def lick(self, ctx, *, members):
        """ Lick the specified people """
        memberlist = await mentionconverter(self, ctx, members)
        embed = await interactions(ctx, memberlist, "licked", data.lick)
        view = interactionsView(ctx, memberlist, "licked", "Lick", data.lick)
        await ctx.respond(embed=embed, view=view)

    @bridge.bridge_command(brief="Give someone bellyrubs")
    @option("members", str, description="Mention users to bellrub")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def bellyrub(self, ctx, *, members):
        """ Give bellyrubs to the specified people """
        memberlist = await mentionconverter(self, ctx, members)
        embed = await interactions(ctx, memberlist, "rubbed the belly of", data.bellyrub)
        view = interactionsView(ctx, memberlist, "rubed the belly off", "Rub", data.bellyrub, "given bellyrubs")
        await ctx.respond(embed=embed, view=view)

    @bridge.bridge_command(brief="Nuzzle someone")
    @option("members", str, description="Mention users to nuzzle")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def nuzzle(self, ctx, *, members):
        """ Nuzzle the specified people """
        memberlist = await mentionconverter(self, ctx, members)
        embed = await interactions(ctx, memberlist, "nuzzled", data.nuzzle)
        view = interactionsView(ctx, memberlist, "nuzzled", "Nuzzle", data.nuzzle)
        await ctx.respond(embed=embed, view=view)

    @bridge.bridge_command(brief="Cuddle someone")
    @option("members", str, description="Mention users to cuddle")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def cuddle(self, ctx, *, members):
        """ Cuddle the specified people """
        memberlist = await mentionconverter(self, ctx, members)
        embed = await interactions(ctx, memberlist, "cuddled", data.cuddle)
        view = interactionsView(ctx, memberlist, "cuddled", "Cuddle", data.cuddle)
        await ctx.respond(embed=embed, view=view)

    @bridge.bridge_command(brief="Feed someone")
    @option("members", str, description="Mention users to feed")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def feed(self, ctx, *, members):
        """ Feed the specified people """
        memberlist = await mentionconverter(self, ctx, members)
        embed = await interactions(ctx, memberlist, "fed", data.feed)
        view = interactionsView(ctx, memberlist, "fed", "Feed", data.feed)
        await ctx.respond(embed=embed, view=view)

    @bridge.bridge_command(brief="Glomp someone")
    @option("members", str, description="Mention users to glomp")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def glomp(self, ctx, *, members):
        """ Glomp on the specified people """
        memberlist = await mentionconverter(self, ctx, members)
        embed = await interactions(ctx, memberlist, "glomped", data.glomp)
        view = interactionsView(ctx, memberlist, "glomped", "Glomp", data.glomp)
        await ctx.respond(embed=embed, view=view)

    @bridge.bridge_command(brief="Highfive someone")
    @option("members", str, description="Mention users to highfive")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def highfive(self, ctx, *, members):
        """ Highfive the specified people """
        memberlist = await mentionconverter(self, ctx, members)
        embed = await interactions(ctx, memberlist, "highfived", data.highfive)
        view = interactionsView(ctx, memberlist, "highfived", "Highfive", data.highfive)
        await ctx.respond(embed=embed, view=view)

    @bridge.bridge_command(brief="Rawr")
    @option("members", str, description="Mention users to rawr at")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def rawr(self, ctx, *, members):
        """ Rawr at the specified people """
        memberlist = await mentionconverter(self, ctx, members)
        embed = await interactions(ctx, memberlist, "rawred at", data.rawr)
        view = interactionsView(ctx, memberlist, "rawred at", "Rawr", data.rawr)
        await ctx.respond(embed=embed, view=view)

    @bridge.bridge_command(brief="Howl to the moon, or someone")
    @option("members", str, description="Mention users to howl at")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def howl(self, ctx, *, members):
        """ Howl at the specified people """
        memberlist = await mentionconverter(self, ctx, members)
        embed = await interactions(ctx, memberlist, "howled at", data.howl)
        view = interactionsView(ctx, memberlist, "howled at", "Howl", data.howl)
        await ctx.respond(embed=embed, view=view)

    @bridge.bridge_command(brief="Pat someone")
    @option("members", str, description="Mention users to pat")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def pat(self, ctx, *, members):
        """ Pat the specified people """
        memberlist = await mentionconverter(self, ctx, members)
        embed = await interactions(ctx, memberlist, "pats", data.pet)
        view = interactionsView(ctx, memberlist, "pats", "Pat", data.pet, "Pat")
        await ctx.respond(embed=embed, view=view)

    @bridge.bridge_command(brief="Give a cookie to someone")
    @option("members", str, description="Mention users to give a cookie to")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def cookie(self, ctx, *, members):
        """ Give cookies to the specified people """
        memberlist = await mentionconverter(self, ctx, members)
        embed = await interactions(ctx, memberlist, "gave a cookie to", data.cookie)
        view = interactionsView(ctx, memberlist, "gave a cookie to", "Give a cookie", data.cookie, "given a cookie")
        await ctx.respond(embed=embed, view=view)

    @bridge.bridge_command(brief="Dance with someone")
    @option("members", str, description="Mention users to dance with", required=False)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def dance(self, ctx, *, members=False):
        """ Dance with someone """
        if not members:
            memberlist = None
            return await feelings(ctx, memberlist, "dances", data.dance)
        memberlist = await mentionconverter(self, ctx, members)
        embed = await interactions(ctx, memberlist, "danced with", data.dance)
        view = interactionsView(ctx, memberlist, "danced with", "Dance", data.dance)
        await ctx.respond(embed=embed, view=view)

    @bridge.bridge_command(brief="Blush")
    @option("members", str, description="Mention users that made you blush", required=False)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def blush(self, ctx, *, members):
        """ Blush (optionally because of specified people) """
        if not members:
            memberlist = None
        else:
            memberlist = await mentionconverter(self, ctx, members)
        await feelings(ctx, memberlist, "blushes", data.blush)

    @bridge.bridge_command(brief="Be happy")
    @option("members", str, description="Mention users that made you happy", required=False)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def happy(self, ctx, *, members):
        """ Be happy (optionally because of specified people) """
        if not members:
            memberlist = None
        else:
            memberlist = await mentionconverter(self, ctx, members)
        await feelings(ctx, memberlist, "smiles", data.happy)

    @bridge.bridge_command(brief="Wag your tail ")
    @option("members", str, description="Mention users that made you wag", required=False)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def wag(self, ctx, *, members):
        """ Wag your tail (Optionally because of specified people) """
        if not members:
            memberlist = None
        else:
            memberlist = await mentionconverter(self, ctx, members)
        await feelings(ctx, memberlist, "wags their tail", data.wag)

    @bridge.bridge_command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def fact(self, ctx):
        """ Get a random animal fact """
        facts = random.choice(["https://some-random-api.com/facts/dog", "https://some-random-api.com/facts/cat", "https://some-random-api.com/facts/panda",
                               "https://some-random-api.com/facts/fox", "https://some-random-api.com/facts/bird", "https://some-random-api.com/facts/koala"])

        fact = await apireq(facts)
        await ctx.respond(fact['fact'])

    @bridge.bridge_command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def fox(self, ctx):
        """ Get a random fox image"""
        json = await apireq("https://randomfox.ca/floof/")
        embed = discord.Embed(title="Floofy fox!", color=discord.Color.orange())
        embed.set_image(url=json['image'])
        await ctx.respond(embed=embed)

    @bridge.bridge_command(brief="Give someone's avatar a rainbow overlay")
    @option("user", discord.Member, description="Select a user", required=False)
    @option("border", bool, description="Make it a border?", required=False, default=False)
    @option("server-avatar", bool, description="Use their server avatar?", required=False, default=False)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def gay(self, ctx, user=None, border=False, server_avatar=False):
        """ Gay overlay on avatar """
        link = ""
        if not user:
            if ctx.message:  # additional check to make slash commands not break at .message.reference
                if ctx.message.reference:
                    reference = await ctx.fetch_message(ctx.message.reference.message_id)
                    user = reference.author
            else:
                user = ctx.author
        if not server_avatar:
            url = user.avatar.url
        else:
            url = user.display_avatar.url
        if not border:
            link = f"https://some-random-api.com/canvas/gay/?avatar={url}"
        else:
            link = f"https://some-random-api.com/canvas/misc/lgbt/?avatar={url}"
        e = discord.Embed(color=discord.Color.random())
        e.set_image(url=link)
        e.set_footer(text=f"Gay avatar: {user}")
        await ctx.respond(embed=e)

    @slash_command()
    @option("text", str, description="What do you want to tell Paw?")
    async def gpt(self, ctx, text):
        """ Talk to Paw! """
        await ctx.defer()
        url = "https://free.churchless.tech/v1/chat/completions"
        adata = {
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "system", "content": f"""{data.gaslight} The user's name is {ctx.author.display_name}. Do not use the user's full name, use their call name derived from their full name."""},
                         {"role": "user", "content": text}],
            "max_tokens": 500
        }
        headers = {
            "Content-Type": "application/json"
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=headers, data=json.dumps(data)) as response:
                if response.status_code == 200:
                    response_json = json.loads(response.content)
                    content = response_json["choices"][0]["message"]["content"]
                    await ctx.respond(f"""**Prompt:** {text}\n**Paw**: {content}""")
                elif response.status_code == 500:
                    await ctx.respond("Something went wrong with the API, try again")
                else:
                    await ctx.respond("Error: API call failed with status code", response.status_code)


def setup(bot):
    bot.add_cog(socials(bot))
