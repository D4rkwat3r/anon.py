import anonym

client = anonym.Client()

client.auth("your login", "your password")

users = client.getOnlineUsers()

for login in users.login:
  client.startChat(login, "Hey!")
