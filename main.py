import discord
from discord.ext import commands
from discord import app_commands

TOKEN = "MTM5ODIwNTYwNTQ4MjcyNTQ0Ng.GWoR6L.AIBpwSi3f9zQMH2guYwiJW5ksiAftoMfFD7aVQ"
GUILD_ID = 1398017348199518272

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

class RoleButtonView(discord.ui.View):
    def __init__(self, role: discord.Role):
        super().__init__(timeout=None)
        self.role = role

    @discord.ui.button(label="Vfy    ", style=discord.ButtonStyle.primary, custom_id="verify_role_button")
    async def verify_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        member = interaction.user
        if self.role in member.roles:
            await member.remove_roles(self.role)
            await interaction.response.send_message("เอาออกหาพ่อมึงแงะ?", ephemeral=True)
        else:
            await member.add_roles(self.role)
            await interaction.response.send_message("เอายศไปไอควยย", ephemeral=True)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    try:
        synced = await bot.tree.sync(guild=discord.Object(id=GUILD_ID))
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(f"Sync error: {e}")

@bot.tree.command(name="kuyrole", description="ส่งปุ่มยืนยันตัวตนไปยังช่องที่เลือก", guild=discord.Object(id=GUILD_ID))
@app_commands.describe(channel="ช่องที่จะส่งข้อความ", role="ยศที่จะให้เมื่อกดปุ่ม")
async def kuyrole(interaction: discord.Interaction, channel: discord.TextChannel, role: discord.Role):
    embed = discord.Embed(
        title="🟣 Vfy server",
        description="กดปุ่มด้านล่างเพื่อ **ยืนยันตัวตน** และรับยศเข้าเซิร์ฟเวอร์",
        color=0x9b59b6

    )
    embed.set_image(url="https://gifdb.com/images/high/purple-anime-498-x-278-gif-qfxrlc4b9yjkwm9h.gif")
    embed.set_footer(text="Kuyrai Kairuy")

    await channel.send(embed=embed, view=RoleButtonView(role))
    await interaction.response.send_message(f"ส่งปุ่มยืนยันไปยัง {channel.mention} แล้ว!", ephemeral=True)

bot.run(TOKEN)
