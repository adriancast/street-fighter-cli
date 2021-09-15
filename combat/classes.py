from fighters.classes import Fighter
from typing import List


class Combat:

    def __init__(self, final_boss: Fighter, fighters: List[Fighter]):
        self.final_boss = final_boss
        self.fighters = fighters

    @property
    def fighters_still_alive(self):
        return all([
            fighter.is_alive for fighter in self.fighters
        ])

    @staticmethod
    def _print_combat_result(final_boss: Fighter, fighters: List[Fighter], final_boss_won: bool):
        print(
            """
______                _ _         
| ___ \              | | |      _ 
| |_/ /___  ___ _   _| | |_ ___(_)
|    // _ \/ __| | | | | __/ __|  
| |\ \  __/\__ \ |_| | | |_\__ \_ 
\_| \_\___||___/\__,_|_|\__|___(_)                        
            """

        )
        print('Boss stats:',  final_boss)
        print('==========================')
        for fighter in fighters:
            print('Fighter: ', fighter)

        if final_boss_won:
            print('Sorry, bad guys won this time :(')
        else:
            print('Yaaaaay! Good guys won again!')

    def print_results(self):
        self._print_combat_result(
            final_boss=self.final_boss,
            fighters=self.fighters,
            final_boss_won=self.final_boss.is_alive
        )

    def start(self):
        while self.final_boss.is_alive and self.fighters_still_alive:
            # First, the heroes attack the final boss
            for hero in self.fighters:
                hero.attack(self.final_boss)

            # Then, if the final boss is alive he attacks the fighters
            if self.final_boss.is_alive:
                for hero in self.fighters:
                    if hero.is_alive:
                        self.final_boss.attack(hero)
