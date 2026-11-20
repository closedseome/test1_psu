class Entity:
    def __init__(self, name: str, max_hp: int):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.block = 0

    def take_damage(self, amount: int):
        # Сначала урон поглощается броней (блоком)
        blocked = min(self.block, amount)
        self.block -= blocked
        remaining_damage = amount - blocked
        self.hp = max(0, self.hp - remaining_damage)
        print(f"  [{self.name}] получает {remaining_damage} урона (заблокировано: {blocked}). Осталось HP: {self.hp}/{self.max_hp}")

    def heal(self, amount: int):
        self.hp = min(self.max_hp, self.hp + amount)
        print(f"  [{self.name}] восстанавливает {amount} HP. Текущее HP: {self.hp}/{self.max_hp}")

    def add_block(self, amount: int):
        self.block += amount
        print(f"  [{self.name}] получает {amount} брони. Текущая броня: {self.block}")

    def is_alive(self) -> bool:
        return self.hp > 0

    def reset_block(self):
        self.block = 0


class Player(Entity):
    def __init__(self, name: str = "Герой", max_hp: int = 50):
        super().__init__(name, max_hp)
        self.deck = []  # Колода карт игрока


class Enemy(Entity):
    def __init__(self, name: str, max_hp: int, base_damage: int):
        super().__init__(name, max_hp)
        self.base_damage = base_damage

    def take_turn(self, player: Player):
        """Базовая логика хода врага. Переопределяется в подклассах (например, для Боссов)."""
        print(f"\nХод врага {self.name}!")
        player.take_damage(self.base_damage)

# =====================================================================
# МЕСТО ДЛЯ ВТОРОГО РАЗРАБОТЧИКА: Создание новых врагов и Боссов
# =====================================================================
# Пример:
# class GoblinBoss(Enemy):
#     def take_turn(self, player: Player):
#         # Уникальная логика босса (например, бьет дважды или накладывает дебафф)
#         pass