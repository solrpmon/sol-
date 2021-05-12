import discord, datetime, asyncio, random

from discord import channel #모듈 불러오기
token = "ODQxNTUwNjIzMjc5NTQ2Mzg5.YJoZFw.JwX_kjNtNaAWAxbdP1Rro2UALUI" #봇 토큰 설정하기

client = discord.Client() #client 설정하기

@client.event
async def on_ready(): #봇이 준비되엇을 때
    print("봇 준비 완료!")
    print(client.user)
    print("==================================")

@client.event
async def on_message(message): #메세지 입력햇을때
    if message.content == "솔로몬":
        await message.channel.send("네! 주인님")
    if message.content == "솔로몬 제작자":
        await message.channel.send("SOL로몬님")
    if message.content == "ㅅ제작자":
        await message.channel.send("SOL로몬님")
    if message.content == "솔로몬 꺼져":
        await message.channel.send("니나 꺼져")
    if message.content == "ㅅ꺼져":
        await message.channel.send("니나 꺼져")
#===============================================================================================================================
    if message.content == "솔로몬 소개":
        embed = discord.Embed(colour=discord.Colour.red(), title="솔로몬 봇", description="저는 아주 똑똑한 주인인 SOL로몬님이 만드신 봇입니다" )
        embed.set_thumbnail(url = "http://2yahp.com/wp-content/uploads/2017/10/1-51.png")
        embed.set_image(url = "http://image.kmib.co.kr/online_image/2018/0911/201809111620_23110923993172_1.jpg")
        embed.set_footer(text=message.author, icon_url = message.author.avatar_url)
        await message.channel.send(embed=embed)
    if message.content == "ㅅ소개":
        embed = discord.Embed(colour=discord.Colour.red(), title="솔로몬 봇", description="저는 아주 똑똑한 주인인 SOL로몬님이 만드신 봇입니다" )
        embed.set_thumbnail(url = "http://2yahp.com/wp-content/uploads/2017/10/1-51.png")
        embed.set_image(url = "http://image.kmib.co.kr/online_image/2018/0911/201809111620_23110923993172_1.jpg")
        embed.set_footer(text=message.author, icon_url = message.author.avatar_url)
        await message.channel.send(embed=embed)
#==============================================================================================================================
    if message.content == "솔로몬 도움말":
        embed = discord.Embed(colour=discord.Colour.blue(), title="도움말", description= "")
        embed.add_field(name="ㅅ", value="솔로몬을 ㅅ으로 줄여서 쓸수있다", inline=False)
        embed.add_field(name="솔로몬", value="네! 주인님", inline=False)
        embed.add_field(name="솔로몬 꺼져", value="^^", inline=False)
        embed.add_field(name="솔로몬 사랑해", value="주인님도 사랑 받을 준비하세욧!", inline=False)
        embed.add_field(name="솔로몬 소개", value="자기 소개를 한다", inline=False)
        embed.add_field(name="솔로몬 내정보", value="명령어를 친 사람의 정보를 알려준다", inline=False)
        embed.add_field(name="솔로몬 제작자", value="솔로몬 봇의 제작자를 알려준다", inline=False)
        embed.add_field(name="솔로몬 도배", value="도배를 한다^^", inline=False)
        embed.add_field(name="솔로몬 타이머 <시간(10, 30, 60)>", value="각 시간의 타이머를 실행한다", inline=False)
        await message.channel.send(embed=embed)
    if message.content == "ㅅ도움말":
        embed = discord.Embed(colour=discord.Colour.blue(), title="도움말", description= "")
        embed.add_field(name="ㅅ", value="솔로몬을 ㅅ으로 줄여서 쓸수있다", inline=False)
        embed.add_field(name="솔로몬", value="네! 주인님", inline=False)
        embed.add_field(name="솔로몬 꺼져", value="^^", inline=False)
        embed.add_field(name="솔로몬 사랑해", value="주인님도 사랑 받을 준비하세욧!", inline=False)
        embed.add_field(name="솔로몬 소개", value="자기 소개를 한다", inline=False)
        embed.add_field(name="솔로몬 내정보", value="명령어를 친 사람의 정보를 알려준다", inline=False)
        embed.add_field(name="솔로몬 제작자", value="솔로몬 봇의 제작자를 알려준다", inline=False)
        embed.add_field(name="솔로몬 도배", value="도배를 한다^^", inline=False)
        embed.add_field(name="솔로몬 타이머 <시간(10, 30, 60)>", value="각 시간의 타이머를 실행한다", inline=False)
        await message.channel.send(embed=embed)
#==============================================================================================================================   
    if message.content == '솔로몬 내정보':
        user = message.author
        date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
        await message.channel.send(f"{message.author.mention}의 가입일 : {date.year}/{date.month}/{date.day}")
        await message.channel.send(f"{message.author.mention}의 이름 / 아이디 / 닉네임 : {user.name}/{user.id}/{user.display_name}")
        await message.channel.send(message.author.avatar_url)
    if message.content == 'ㅅ내정보':
        user = message.author
        date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
        await message.channel.send(f"{message.author.mention}의 가입일 : {date.year}/{date.month}/{date.day}")
        await message.channel.send(f"{message.author.mention}의 이름 / 아이디 / 닉네임 : {user.name}/{user.id}/{user.display_name}")
        await message.channel.send(message.author.avatar_url)
#============================================================================================================================== 
    if message.content.startswith('$greet'):
        channel = message.channel
        await channel.send('say hello!')

        def check(m):
            return m.content == 'hello' and m.channel == channel

        msg = await client.wait_for('message', check=check)
        await channel.send('hello {.author}'.format(msg))
#============================================================================================================================== 
    if message.content == "솔로몬 랜덤":
        await message.channel.send(random.choice(["꽝!", "당첨!", "꽝!", "꽝!", "꽝!", "꽝!", "꽝!"]))
    if message.content == "ㅅ랜덤":
        await message.channel.send(random.choice(["꽝!", "당첨!", "꽝!", "꽝!", "꽝!", "꽝!", "꽝!"]))
    
    if message.content == "솔로몬 사랑해":
        await message.channel.send(random.choice(["저도 사랑해요 주인님", "?", "웃기고 자빠졌네", "항항ㅎㅎ"]))
    if message.content == "ㅅ사랑해":
        await message.channel.send(random.choice(["저도 사랑해요 주인님", "?", "웃기고 자빠졌네", "항항ㅎㅎ"]))
    
    if message.content == "솔로몬 도배":
        await message.channel.send(random.choice(["도배" * 500, "홀롤로롤" * 250, "SOL로몬님 천재!" * 150]))
    if message.content == "ㅅ도배":
        await message.channel.send(random.choice(["도배" * 500, "홀롤로롤" * 250, "SOL로몬님 천재!" * 150]))
#============================================================================================================================== 
    if message.content == "솔로몬 타이머 10":
        await asyncio.sleep(10)
        await message.channel.send(f"{message.author.mention}, 10초가 지났어요")
    if message.content == "ㅅ타이머 10":
        await asyncio.sleep(10)
        await message.channel.send(f"{message.author.mention}, 10초가 지났어요")
    
    if message.content == "솔로몬 타이머 30":
        await asyncio.sleep(30)
        await message.channel.send(f"{message.author.mention}, 30초가 지났어요")
    if message.content == "ㅅ타이머 30":
        await asyncio.sleep(30)
        await message.channel.send(f"{message.author.mention}, 30초가 지났어요")
    
    if message.content == "솔로몬 타이머 60":
        await asyncio.sleep(60)
        await message.channel.send(f"{message.author.mention}, 60초가 지났어요")
    if message.content == "ㅅ타이머 60":
        await asyncio.sleep(60)
        await message.channel.send(f"{message.author.mention}, 60초가 지났어요")
#==============================================================================================================================
    if message.content.startswith("!청소"):
        number = int(message.content.split(" ")[1])
        await message.delete()
        await message.channel.purge(limit=number)
        await message.channel.send(f"{number}개의 메세지를 삭제했습니다")
#==============================================================================================================================
    
client.run(token)