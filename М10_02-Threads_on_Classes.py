import time
from threading import Thread


class Knight(Thread):

    def __init__(self, name, skill, *args, **kwargs):
        super(Knight, self).__init__(*args, **kwargs)
        self.name = name
        self.skill = skill

    def run(self):
        enemy_people = 100
        e_p = enemy_people - self.skill
        days_battle = 1
        print(f'{self.name}, на нас напали!')
        for i in range(e_p):
            time.sleep(1)
            if e_p > 0:
                print(f'{self.name}, сражается {days_battle} день(дня)..., осталось {e_p} воинов ')
                e_p -= self.skill
                days_battle += 1
            elif e_p == 0:
                print(f'{self.name}, сражается {days_battle} день(дня)..., осталось {e_p} воинов ')
                print(f'{self.name} - ОДЕРЖАЛ ПОБЕДУ спустя {days_battle} дней!')
                return


knight_1 = Knight("Sir Lancelot", 10)
knight_2 = Knight("Sir Galahad", 20)

knight_1.start()
knight_2.start()

knight_1.join()
knight_2.join()

print('Все битвы закончились!')
