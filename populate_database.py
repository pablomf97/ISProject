import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'IS_Project.settings')

django.setup()
from myapp.models import Song, User, CollaborativeList

python_songs = [
    {
        "name": "Brianstorm",
        "author": "Arctic Monkeys",
        "album": "Favourite Worst Nightmare",
        "duration": "2:53"
    },
    {
        "name": "505",
        "author": "Arctic Monkeys",
        "album": "Favourite Worst Nightmare",
        "duration": "4:14"
    },
    {
        "name": "Old Yellow Bricks",
        "author": "Arctic Monkeys",
        "album": "Favourite Worst Nightmare",
        "duration": "3:13"
    },
    {
        "name": "The Bad Thing",
        "author": "Arctic Monkeys",
        "album": "Favourite Worst Nightmare",
        "duration": "2:25"
    },
    {
        "name": "Square One",
        "author": "Coldplay",
        "album": "X&Y",
        "duration": "4:34"
    },
    {
        "name": "What If",
        "author": "Coldplay",
        "album": "X&Y",
        "duration": "4:59"
    },

]

python_users = [
    {
        "username": "Miguel",
        "email": "miguel@email.com"
    },
    {
        "username": "Miguel.A",
        "email": "miguel.a@email.com"
    },
    {
        "username": "Raúl",
        "email": "raul@email.com"
    },
    {
        "username": "Pablo",
        "email": "pablo@email.com"
    },
    {
        "username": "Eduardo",
        "email": "edu@email.com"
    },
]


def populateDatabase():
    playlist1 = CollaborativeList(name="My First List")
    playlist2 = CollaborativeList(name="My Second List")

    playlist1.save()
    playlist2.save()

    for idx, song in enumerate(python_songs):
        s = addSong(song["name"], song["author"], song["album"], song["duration"])
        if idx % 2 == 0:
            playlist1.songs.add(s)
        else:
            playlist2.songs.add(s)

    for idx, user in enumerate(python_users):
        u = addUser(user["username"], user["email"])
        if idx % 2 == 0:
            playlist1.users.add(u)
        else:
            playlist2.users.add(u)


def addUser(name, email):
    user = User.objects.get_or_create(userName=name, email=email)[0]
    user.save()
    return user


def addSong(name, author, album, duration):
    song = Song.objects.get_or_create(name=name, author=author, album=album, duration=duration)[0]
    song.save()
    return song

if __name__ == '__main__':
    print("Populating database...")
    populateDatabase()
