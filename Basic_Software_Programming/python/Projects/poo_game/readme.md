# Battle Game

This is a simple text-based battle game implemented in Python. The game features characters, including heroes and enemies, each with their own attributes and abilities. Players can engage in turn-based battles between a hero and an enemy.

## Classes

### `Personagem`
The base class for all characters in the game.

- **Attributes:**
  - `nome` (Name)
  - `vida` (Health)
  - `nivel` (Level)

- **Methods:**
  - `get_nome()`: Returns the name of the character.
  - `get_vida()`: Returns the health of the character.
  - `get_nivel()`: Returns the level of the character.
  - `exibir_detalhes()`: Displays the details of the character.
  - `receber_ataque(dano)`: Reduces health by the damage received.
  - `atacar(alvo)`: Attacks another character, causing a random amount of damage.

### `Heroi` (Inherits from `Personagem`)
Represents the hero controlled by the player.

- **Additional Attributes:**
  - `habilidade` (Ability)

- **Methods:**
  - `get_habilidade()`: Returns the hero's ability.
  - `exibir_detalhes()`: Displays the details of the hero, including their ability.
  - `ataque_especial(alvo)`: Performs a special attack causing increased damage.

### `Inimigo` (Inherits from `Personagem`)
Represents an enemy in the game.

- **Additional Attributes:**
  - `tipo` (Type)

- **Methods:**
  - `get_tipo()`: Returns the enemy's type.
  - `exibir_detalhes()`: Displays the details of the enemy, including their type.

### `Jogo`
Orchestrates the game and manages the battle between the hero and the enemy.

- **Methods:**
  - `iniciar_batalha()`: Manages the battle in turns, allowing the player to choose between a normal attack and a special attack.

## How to Run

1. Clone the repository:
   ```bash
   git clone 

2. Run the game:
```
python game.py

```
## Contributing
Feel free to contribute to this project by opening issues or submitting pull requests.

## License
This project is licensed under the MIT License - see the LICENSE file for details.