
class Fighter:

    def __init__(self, name: str, health: int, damage: int):
        self.name = name
        self.health = health
        self.damage = damage

    def __str__(self):
        return (
            'Name: {name}, '
            'Health: {health}, '
            'Damage: {damage}'
        ).format(
            name=self.name,
            health=self.health,
            damage=self.damage,
        )

    @property
    def is_alive(self) -> bool:
        return bool(self.health > 0)

    def retrieve_damage(self, damage: int) -> bool:
        """

        :param damage:
        :return:
        """
        self.health = self.health - damage
        if self.health <= 0:
            self.health = 0  # Prevent negative health
            return True
        else:
            return False


class Hero(Fighter):
    pass

class Villain(Fighter):
    pass
