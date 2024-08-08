import random

def roll_die():
    return random.randint(1, 6)

def player_turn(player):
    score = 0
    turn_active = True
    print(f"Turno del Jugador {player}")
    while turn_active:
        roll = roll_die()
        print(f"El dado muestra: {roll}")
        if roll == 1:
            print("¡Perdiste tu turno!")
            score = 0
            turn_active = False
        else:
            score += roll
            print(f"Tu puntuación actual es: {score}")
            response = input("¿Quieres tirar de nuevo? (s/n): ")
            if response.lower() != 's':
                turn_active = False
    return score

def main():
    player1_score = 0
    player2_score = 0
    winning_score = 100

    while player1_score < winning_score and player2_score < winning_score:
        player1_score += player_turn(1)
        print(f"Puntuación total del Jugador 1: {player1_score}")
        if player1_score >= winning_score:
            break

        player2_score += player_turn(2)
        print(f"Puntuación total del Jugador 2: {player2_score}")

    if player1_score >= winning_score:
        print("¡El Jugador 1 gana!")
    else:
        print("¡El Jugador 2 gana!")

if __name__ == "__main__":
    main()

