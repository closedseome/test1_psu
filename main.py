from entities import Player, Enemy
from cards import StrikeCard, ShieldCard, HeavyBlowCard
from engine import BattleEngine
from ui import GameUI

def generate_enemies(count: int) -> list[Enemy]:
    enemies = []
    for i in range(1, count + 1):
        enemies.append(Enemy(name=f"Скелет #{i}", max_hp=15 + i * 5, base_damage=4 + i))
    return enemies

def main():
    ui = GameUI()
    ui.clear()
    ui.show_message("Добро пожаловать в GRIM ROLL!")
    
    player = Player(name="Искатель", max_hp=50)
    player.deck = [StrikeCard(), ShieldCard(), HeavyBlowCard()]

    enemies_to_defeat = 3
    enemies = generate_enemies(enemies_to_defeat)

    for idx, enemy in enumerate(enemies, 1):
        ui.show_message(f"Этап {idx} из {enemies_to_defeat}")
        battle = BattleEngine(player, enemy, ui)
        if not battle.start_battle():
            ui.show_message("ВЫ ПОГИБЛИ. Игра окончена.", pause=2.5)
            return

    ui.show_message("ПОБЕДА! Все враги повержены!", pause=3.0)

if __name__ == "__main__":
    main()
