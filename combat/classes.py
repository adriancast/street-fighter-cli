from fighters.classes import Fighter
from typing import List
import time


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
        """
        Simulate a turn based combat. First, the fighters will attack the final boss.
        If the final boss is alive after the fighters attack, the final boss will attack the fighters.
        """
        while self.final_boss.is_alive and self.fighters_still_alive:
            # First, the fighters attack the final boss
            for fighter in self.fighters:
                print('\nFighters are starting their attack!!')
                print('Fighter {} attacked final boss {}'.format(fighter.name, self.final_boss.name))

                fighter.attack(self.final_boss)

                print('Boss health: ', self.final_boss.health)
                time.sleep(0.5)

            # Then, if the final boss is alive he attacks the fighters
            if self.final_boss.is_alive:
                print('\nFinal boss is starting his attack!!')
                for fighter in self.fighters:
                    if fighter.is_alive:
                        print('Boss {} attacked fighter {}'.format(self.final_boss.name, fighter.name))

                        self.final_boss.attack(fighter)

                        print('Fighter health: ', fighter.health)
                        time.sleep(0.5)
