
class Fighter:

    def __init__(self, name: str, health: int, damage: int):
        self.name = name
        self.health = health
        self.damage = damage

    def __str__(self):
        return (
            'Name: {name}, Health: {health}, Damage: {damage}'
        ).format(
            name=self.name,
            health=self.health,
            damage=self.damage,
        )

    @property
    def is_alive(self) -> bool:
        """
        Check if the fighter is alive

        :return: True if the fighter is alive
        """
        return bool(self.health > 0)

    def attack(self, fighter: 'Fighter') -> bool:
        """
        Attack a given fighter

        :param fighter: fighter instance that is going to receive the damage
        :return: True if the attacked fighter died after retrieving the damage
        """
        return fighter.retrieve_damage(self.damage)

    def retrieve_damage(self, damage: int) -> bool:
        """
        Decrease the health of the fighter subtracting the damage
        to the current health.

        :param damage: inflicted damage
        :return: True if the fighter died after retrieving the damage
        """
        self.health = self.health - damage
        if self.health <= 0:
            self.health = 0  # Prevent negative health
            return True
        else:
            return False
