class Player:    
    def __init__(self, id):
        self.id = id        
    
    def play_turn(self, allowed_cells):
        # Capturar la celda que ingresa el jugador durante su turno, verificando que la celda ingresada sea una celda permitida. Retorna: la celda ingresada.

        while True:
            cell = input(f'\nJugador {self.id} >>: ').lower()

            if cell in allowed_cells:
                return cell
            else:
                print('¡Mala jugada! Intente de nuevo.')
                continue       
    
    def __str__(self):
        return self.id