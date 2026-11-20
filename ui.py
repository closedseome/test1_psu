import os
import time
from entities import Player, Enemy

class GameUI:
    @staticmethod
    def clear():
        """Очищает консоль для создания эффекта 'экрана' игры."""
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def draw_dice(dice_pool: list[int]) -> str:
        """Отрисовывает кубики. 3-й разработчик может заменить цифры на ASCII-кубики."""
        return "  ".join([f"[ {d} ]" for d in dice_pool])

    def show_battle_screen(self, player: Player, enemy: Enemy, dice_pool: list[int], log_message: str = ""):
        """Главный минималистичный экран боя."""
        self.clear()
        print("╔════════════════════════════════════════════════════════╗")
        print(f"║  GRIM ROLL                       Враг: {enemy.name:<15} ║")
        print("╠════════════════════════════════════════════════════════╣")
        print(f"║  ГЕРОЙ: HP {player.hp}/{player.max_hp} | Броня: {player.block:<27} ║")
        print(f"║  ВРАГ:  HP {enemy.hp}/{enemy.max_hp} | Броня: {enemy.block:<27} ║")
        print("╚════════════════════════════════════════════════════════╝")

        # Вывод последнего события (урон, лечение, ошибка)
        if log_message:
            print(f"\n> {log_message}")

        print(f"\nКубики в запасе: {self.draw_dice(dice_pool)}")
        print("\nДоступные карты:")
        for idx, card in enumerate(player.deck, 1):
            print(f"  [{idx}] {card.name:<16} | Условие: {card.condition_desc:<18} | {card.description}")
        print("  [0] Закончить ход")

    def get_player_action(self, deck_size: int, dice_pool: list[int]) -> tuple[int, int] | None:
        """Запрашивает выбор карты и кубика. Возвращает (индекс_карты, значение_кубика) или None (конец хода)."""
        choice = input("\nВыберите номер карты (0 - конец хода): ").strip()
        if choice == "0":
            return None

        if not choice.isdigit() or not (1 <= int(choice) <= deck_size):
            return (-1, -1) # Код ошибки ввода

        dice_input = input(f"Какой кубик потратить {self.draw_dice(dice_pool)}? ").strip()
        if not dice_input.isdigit():
            return (-1, -1)

        return (int(choice) - 1, int(dice_input))

    @staticmethod
    def show_message(text: str, pause: float = 1.5):
        """Показывает важное сообщение (победа, ход врага, конец игры)."""
        print(f"\n*** {text} ***")
        time.sleep(pause)

# =====================================================================
# МЕСТО ДЛЯ 3-ГО РАЗРАБОТЧИКА:
# 1. Добавить ASCII-портреты для боссов и врагов (dict по enemy.name)
# 2. Сделать красивые псевдографические кубики вместо [ 6 ]
# 3. Подключить библиотеку 'rich' или 'colorama' для цветного текста
# =====================================================================
