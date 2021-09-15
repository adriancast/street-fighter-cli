from fighters.classes import Fighter
from combat.classes import Combat

final_boss_kwargs = {
    'name': 'Mr.Chacho',
    'health': 100,
    'damage': 15,
}

fighters_kwargs = [
    {
        'name': 'Ken',
        'health': 40,
        'damage': 6,
    },
    {
        'name': 'Ryu',
        'health': 35,
        'damage': 6,
    },
]

final_boss = Fighter(**final_boss_kwargs)
fighters = [
    Fighter(**fighters_kwarg) for fighters_kwarg in fighters_kwargs
]

combat = Combat(
    final_boss=final_boss,
    fighters=fighters
)

combat.start()
combat.print_results()
