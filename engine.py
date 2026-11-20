import random
from entities import Player, Enemy
from ui import GameUI

class BattleEngine:
    def __init__(self, player: Player, enemy: Enemy, ui: GameUI):
        self.player = player
        self.enemy = enemy
        self.ui = ui
        self.dice_pool = []

    def roll_dice(self, count: int = 3):
        self.dice_pool = [random.randint(1, 6) for _ in range(count)]

    def start_battle(self) -> bool:
        self.ui.show_message(f"Начинается бой! Противник: {self.enemy.name}")

        while self.player.is_alive() and self.enemy.is_alive():
            self.player.reset_block()
            self.roll_dice(3)
            self._player_turn()

            if not self.enemy.is_alive():
                self.ui.show_message(f"Победа! {self.enemy.name} повержен!")
                return True

            self.enemy.reset_block()
            self.ui.show_message(f"Ходит {self.enemy.name}...", pause=1.0)
            self.enemy.take_turn(self.player)
            time_pause = 1.5 # Даем игроку прочитать, сколько урона он получил
            import time; time.sleep(time_pause)

        return False

    def _player_turn(self):
        last_log = "Ваш ход! Выберите карту и кубик."

        while self.dice_pool and self.enemy.is_alive():
            self.ui.show_battle_screen(self.player, self.enemy, self.dice_pool, last_log)
            action = self.ui.get_player_action(len(self.player.deck), self.dice_pool)

            if action is None:
                break

            card_idx, dice_val = action
            if card_idx == -1 or dice_val not in self.dice_pool:
                last_log = "Ошибка: Неверный номер карты или такого кубика нет!"
                continue

            selected_card = self.player.deck[card_idx]
            if selected_card.can_use(dice_val):
                self.dice_pool.remove(dice_val)
                selected_card.play(self.player, self.enemy, dice_val)
                last_log = f"Сыграна карта '{selected_card.name}' с кубиком [{dice_val}]!"
            else:
                last_log = f"Кубик [{dice_val}] не подходит! Нужно: {selected_card.condition_desc}"
