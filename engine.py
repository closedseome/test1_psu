import random
from entities import Player, Enemy

class BattleEngine:
    def __init__(self, player: Player, enemy: Enemy):
        self.player = player
        self.enemy = enemy
        self.dice_pool = []

    def roll_dice(self, count: int = 3):
        self.dice_pool = [random.randint(1, 6) for _ in range(count)]

    def start_battle(self) -> bool:
        """Запускает бой. Возвращает True, если игрок победил, и False, если проиграл."""
        print(f"\n{'='*40}")
        print(f"ВСТРЕЧА С ВРАГОМ: {self.enemy.name} (HP: {self.enemy.hp})")
        print(f"{'='*40}")

        while self.player.is_alive() and self.enemy.is_alive():
            self.player.reset_block()
            self.roll_dice(3)
            self._player_turn()

            if not self.enemy.is_alive():
                print(f"\n[Победа!] Враг {self.enemy.name} повержен!")
                return True

            self.enemy.reset_block()
            self.enemy.take_turn(self.player)

        return False

    def _player_turn(self):
        while self.dice_pool and self.enemy.is_alive():
            print(f"\n--- ВАШ ХОД ---")
            print(f"Ваше HP: {self.player.hp}/{self.player.max_hp} | Броня: {self.player.block}")
            print(f"Враг {self.enemy.name} HP: {self.enemy.hp}/{self.enemy.max_hp} | Броня: {self.enemy.block}")
            print(f"Доступные кубики: {self.dice_pool}")
            print("\nВаши карты:")
            
            for idx, card in enumerate(self.player.deck):
                print(f"  {idx + 1}. {card.name} [{card.condition_desc}] — {card.description}")
            print("  0. Закончить ход")

            choice = input("\nВыберите номер карты: ").strip()
            if choice == "0":
                break

            if not choice.isdigit() or not (1 <= int(choice) <= len(self.player.deck)):
                print("Неверный выбор карты. Попробуйте снова.")
                continue

            selected_card = self.player.deck[int(choice) - 1]
            
            dice_input = input(f"Какое значение кубика потратить из {self.dice_pool}? ").strip()
            if not dice_input.isdigit() or int(dice_input) not in self.dice_pool:
                print("Такого кубика нет в пуле!")
                continue

            dice_val = int(dice_input)
            if selected_card.can_use(dice_val):
                self.dice_pool.remove(dice_val)
                selected_card.play(self.player, self.enemy, dice_val)
            else:
                print(f"Ошибка: Кубик [{dice_val}] не подходит под условие '{selected_card.condition_desc}'!")
