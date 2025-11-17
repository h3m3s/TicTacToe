from game import Game

if __name__ == "__main__":
    while True:
        print("Wybierz tryb gry:")
        print("1 - Gracz vs Gracz")
        print("2 - Gracz vs Bot")
        print("3 - Wyjście")

        choice = input("Twój wybór: ")
        if choice == "3":
            break

        vs_bot = choice == "2"

        game = Game(vs_bot=vs_bot)
        game.play()

        input("Naciśnij ENTER, aby zagrać ponownie...")
