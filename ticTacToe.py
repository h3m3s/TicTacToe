from game import Game

if __name__ == "__main__":
    while True:
        print("Wybierz tryb gry:")
        print("1 - Gracz vs Gracz")
        print("2 - Gracz vs Bot (łatwy)")
        print("3 - Gracz vs Bot (trudny)")
        print("4 - Wyjście")

        choice = input("Twój wybór: ")
        if choice == "4":
            break

        vs_bot = choice in ["2", "3"]
        difficult = choice == "3"

        game = Game(vs_bot=vs_bot, difficult=difficult)
        game.play()

        input("Naciśnij ENTER, aby zagrać ponownie...")
