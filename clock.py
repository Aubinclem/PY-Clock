import time
import os

def get_terminal_width():
    # Retourne la largeur de la fenêtre de la console
    return os.get_terminal_size().columns

def print_ascii_clock():
    terminal_width = get_terminal_width()
    
    # Créer une horloge ASCII avec un cadre
    clock_frame = """
  +-------------------+
  |                   |
  |    {time}       |
  |    {date}     |
  |      15°C         |
  +-------------------+
    """
    
    # Calculer les espaces nécessaires pour centrer l'horloge
    spaces = (terminal_width - len(clock_frame.splitlines()[0])) // 2

    while True:
        # Obtenir l'heure et la date actuelle
        current_time = time.strftime("%H:%M:%S", time.localtime())
        current_date = time.strftime("%d/%m/%Y", time.localtime())  # Format JJ/MM/YYYY
        
        # Formater l'horloge ASCII avec l'heure et la date actuelles
        formatted_clock = clock_frame.format(time=current_time, date=current_date)
        
        # Effacer la ligne précédente pour réécrire l'horloge
        print("\033[H", end="")  # Retourne au début de la console
        
        # Afficher l'horloge ASCII centrée
        print(" " * spaces + formatted_clock, end="")
        time.sleep(1)

# Lancer l'horloge ASCII
print_ascii_clock()
