import discord


async def error_fatal_edit(ctx, status_msg, text, *, mention=True):
    embed = discord.Embed(
        color=0xFF0000, description=f':x: {text}')
    embed.set_footer(icon_url=ctx.author.avatar_url,
                     text=f'{ctx.author.name}#{ctx.author.discriminator}')

    if mention is True:
        return await status_msg.edit(content=ctx.author.mention, embed=embed)

    return await status_msg.edit(embed=embed)


async def error_warning_edit(ctx, status_msg, text, *, mention=True):
    embed = discord.Embed(
        color=0xF1C40F,
        description=f':exclamation: {text}')
    embed.set_footer(icon_url=ctx.author.avatar_url,
                     text=f'{ctx.author.name}#{ctx.author.discriminator}')

    if mention is True:
        return await status_msg.edit(content=ctx.author.mention, embed=embed)

    return await status_msg.edit(embed=embed)


async def error_fatal_send(ctx, text, *, mention=True):
    embed = discord.Embed(
        color=0xFF0000, description=f':x: {text}')
    embed.set_footer(icon_url=ctx.author.avatar_url,
                     text=f'{ctx.author.name}#{ctx.author.discriminator}')

    if mention is True:
        return await ctx.send(content=ctx.author.mention, embed=embed)

    return await ctx.send(embed=embed)


async def error_warning_send(ctx, text, *, mention=True):
    embed = discord.Embed(
        color=0xF1C40F,
        description=f':exclamation: {text}')
    embed.set_footer(icon_url=ctx.author.avatar_url,
                     text=f'{ctx.author.name}#{ctx.author.discriminator}')

    if mention is True:
        return await ctx.send(content=ctx.author.mention, embed=embed)

    return await ctx.send(embed=embed)


async def set_footer(ctx, embed):
    return embed.set_footer(
        icon_url=ctx.author.avatar_url,
        text=f'{ctx.author.name}#{ctx.author.discriminator}')
