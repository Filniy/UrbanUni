import hashlib
from time import sleep

def hash_password(password: str) -> int: 
    sha256 = hashlib.sha256()
    sha256.update(password.encode('utf-8'))
    hashed_password = sha256.hexdigest()
    return int(hashed_password, 16)


class User:

    def __init__(self, nickname: str, password: str, age: int):
        self.nickname = nickname
        self.password = hash_password(password)
        self.age = age

    def __str__(self):
        return f"{self.nickname}"

class Video:
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

class UrTube:

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None



    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == password:
                self.current_user = user
                return True
        return False

    def register(self, nickname, password, age):
        if len(self.users) == 0:
            new_user = User(nickname, password, age)
            self.users.append(new_user)
            if self.log_in(new_user.nickname, new_user.password):
                self.current_user = new_user
        else:
            for user in self.users:
                if user.nickname == nickname:
                    print(f"Пользователь {nickname} уже существует")
                    return
                else:
                    new_user = User(nickname, password, age)
                    self.users.append(new_user)
                    if self.log_in(new_user.nickname, new_user.password):
                        self.current_user = new_user
                    return

    def log_out(self):
        self.current_user = None

    def add(self, *videos: Video):
        for video in videos:
            if not any(v.title == video.title for v in self.videos):
                self.videos.append(video)

    def get_videos(self, search_word: str):
        search_word = search_word.lower()
        matching_videos = [video.title for video in self.videos if search_word in video.title.lower()]
        return matching_videos

    def watch_video(self, name_video: str):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return
        for video in self.videos:
            if name_video.lower() in video.title.lower():
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                else:
                    for i in range(1, 11):
                        print(i, end='')
                        sleep(1)
                    print(" Конец видео")
                return
        return
    
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')