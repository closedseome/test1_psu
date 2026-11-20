from entities import Player, Enemy
from cards import StrikeCard, ShieldCard, HeavyBlowCard
from engine import BattleEngine

def generate_enemies(count: int) -> list[Enemy]:
    """Генерирует список из N врагов. Сюда можно легко встроить босса на последний этап."""
    enemies = []
    for i in range(1, count + 1):
        # С каждым шагом враги становятся немного сильнее
        enemies.append(Enemy(name=f"Скелет-воин #{i}", max_hp=15 + i * 5, base_damage=4 + i))
    
    # МЕСТО ДЛЯ ВТОРОГО РАЗРАБОТЧИКА: Можно заменить последнего врага на Босса
    # enemies[-1] = GoblinBoss("Король Гоблинов", max_hp=50, base_damage=10)
    return enemies

def main():
    print("Добро пожаловать в Dice & Cards!")
    player = Player(name="Искатель приключений", max_hp=50)
    
    # Стартовая колода
    player.deck = [
        StrikeCard(),
        ShieldCard(),
        HeavyBlowCard()
    ]

    enemies_to_defeat = 3  # Цель: победить N врагов
    enemies = generate_enemies(enemies_to_defeat)

    for idx, enemy in enumerate(enemies, 1):
        print(f"\n>>> Этап {idx} из {enemies_to_defeat} <<<")
        battle = BattleEngine(player, enemy)
        won = battle.start_battle()

        if not won:
            print("\nВЫ ПОГИБЛИ. Игра окончена.")
            return

    print("\nПОЗДРАВЛЯЕМ! Вы победили всех врагов и прошли игру!")

if __name__ == "__main__":
    main()
