from entities import Player, Enemy

class Card:
    def __init__(self, name: str, description: str, condition_desc: str):
        self.name = name
        self.description = description
        self.condition_desc = condition_desc # Текстовое описание требования к кубику

    def can_use(self, dice_value: int) -> bool:
        """Проверяет, подходит ли значение кубика для активации карты. По умолчанию подходит любой."""
        return True

    def play(self, player: Player, enemy: Enemy, dice_value: int):
        """Эффект карты при розыгрыше. Переопределяется для каждой карты."""
        raise NotImplementedError("Метод play() должен быть реализован в конкретной карте!")


# =====================================================================
# МЕСТО ДЛЯ ВТОРОГО РАЗРАБОТЧИКА: Добавление новых карт
# =====================================================================

class StrikeCard(Card):
    def __init__(self):
        super().__init__(
            name="Удар мечом",
            description="Наносит урон, равный значению кубика.",
            condition_desc="Любой кубик"
        )

    def play(self, player: Player, enemy: Enemy, dice_value: int):
        print(f"Вы используете '{self.name}' со значением {dice_value}!")
        enemy.take_damage(dice_value)


class ShieldCard(Card):
    def __init__(self):
        super().__init__(
            name="Глухая оборона",
            description="Дает броню, равную значению кубика + 2.",
            condition_desc="Только четные (2, 4, 6)"
        )

    def can_use(self, dice_value: int) -> bool:
        return dice_value % 2 == 0

    def play(self, player: Player, enemy: Enemy, dice_value: int):
        print(f"Вы используете '{self.name}' со значением {dice_value}!")
        player.add_block(dice_value + 2)


class HeavyBlowCard(Card):
    def __init__(self):
        super().__init__(
            name="Сокрушение",
            description="Наносит 12 ед. урона.",
            condition_desc="Кубик >= 5"
        )

    def can_use(self, dice_value: int) -> bool:
        return dice_value >= 5

    def play(self, player: Player, enemy: Enemy, dice_value: int):
        print(f"Вы используете '{self.name}'!")
        enemy.take_damage(12)
