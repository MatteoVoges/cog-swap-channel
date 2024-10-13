import asyncio

import discord
from discord.utils import get
from redbot.core import commands


class SwapChannel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(manage_channels=True)
    async def swapchannel(self, ctx, talk_id: int = 1):

        PENTHOUSE_NAME = "💎 Penthouse"
        TALK_CHANNEL_NAME = f"💬 Talk #{talk_id}"

        try:
            penthouse = get(ctx.guild.voice_channels, name=PENTHOUSE_NAME)
            talk_channel = get(ctx.guild.voice_channels, name=TALK_CHANNEL_NAME)

            if talk_channel is None:
                await ctx.send(f"Channel ' {TALK_CHANNEL_NAME} ' not found.")
                return

            penthouse_position = penthouse.position
            await penthouse.edit(name=TALK_CHANNEL_NAME, position=talk_channel.position)
            await talk_channel.edit(name=PENTHOUSE_NAME, position=penthouse_position)
            await ctx.send(f"Channels {PENTHOUSE_NAME} and {TALK_CHANNEL_NAME} have been swapped")
        except discord.Forbidden:
            await ctx.send("You don't have permission to manage channels.")
        except discord.HTTPException as e:
            await ctx.send(f"An error occurred: {str(e)}")
            
    @commands.command()   
    async def sendadmin(self, ctx, text: str):
        admin_channel = get(ctx.guild.text_channels, name="admin-channel")
        await admin_channel.send(text)
        if text == "!swapchannel":
            await self.swapchannel(admin_channel)
