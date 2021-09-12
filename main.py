from fighters.classes import Villain, Hero
from typing import List


def build_villain() -> Villain:
    villain_data = {
            'name': 'Mr.Chacho',
            'health': 100,
            'damage': 6,
        }

    return Villain(**villain_data)


def build_heroes() -> List[Hero]:
    heroes_data = [
        {
            'name': 'Mr.Bison',
            'health': 100,
            'damage': 6,
        },
        {
            'name': 'Mr.Chacho',
            'health': 100,
            'damage': 6,
        },
    ]

    return [
        Hero(**heroe_data) for heroe_data in heroes_data
    ]


def print_combat_result(villain: Villain, heroes: List[Hero]):
    print('Villain stats: ')
    print(villain)

    print('Heroes stats: ')
    for hero in heroes:
        print(hero)

    print('=====================')

def heroes_remaining(heroes: List[Hero]) -> bool:
    return any([
        hero.is_alive for hero in heroes
    ])

heroes = build_heroes()
villain = build_villain()

while villain.is_alive and heroes_remaining(heroes):
    # First, the heroes attack the villain
    for hero in heroes:
        villain.retrieve_damage(
            damage=hero.damage
        )
    if villain.is_alive:
        for hero in heroes:
            if hero.is_alive:
                hero.retrieve_damage(damage=villain.damage)


    print_combat_result(heroes=heroes, villain=villain)


if villain.is_alive:
    print('Sorry, bad guys won :(')

