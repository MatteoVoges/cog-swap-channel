from .swap_channel import SwapChannel


async def setup(bot):
    await bot.add_cog(SwapChannel(bot))
