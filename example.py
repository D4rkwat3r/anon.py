import anonym
import asyncio

client = anonym.Client()

async def main():
  await client.auth("your login", "your password")
  users = await client.getOnlineUsers()
  for login in users.login:
    await client.startChat(login, "Hey!")


if __name__ == "__main__":
  asyncio.get_event_loop().run_until_complete(main())
