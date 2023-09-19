class Board:

    def __init__(self, player_1, player_2):

        self.board_status = { 'c1': '', 'c2': '', 'c3': '', 'c4': '', 'c5': '', 'c6': '', 'c7': '', 'c8': '', 'c9': '' }

        self.winning_conditions = ( ('c1', 'c2', 'c3'), ('c4', 'c5', 'c6'), ('c7', 'c8', 'c9'),
                                    ('c1', 'c4', 'c7'), ('c2', 'c5', 'c8'), ('c3', 'c6', 'c9'),
                                    ('c1', 'c5', 'c9'), ('c3', 'c5', 'c7'))

        self.player_1 = player_1 
        self.player_2 = player_2
        self.current_player = player_1


    def reset_board(self):
        # Reiniciar el tablero a su estado inicial (vacío).

        self.board_status = { 'c1': '', 'c2': '', 'c3': '', 'c4': '', 'c5': '', 'c6': '', 'c7': '', 'c8': '', 'c9': '' }


    def render_instructions(self):
        # Mostrar las instrucciones del juego.

        print(' -  TIC TAC TOE  - ')
        print('\n')
        print('  c1  |  c2  |  c3  \n------+------+------\n  c4  |  c5  |  c6  \n------+------+------\n  c7  |  c8  |  c9  ')
        print('\n')
        print(f'Jugador 1: {self.player_1} - Jugador 2: {self.player_2}')
        print('En cada turno el jugador deberá ingresar la celda que va utilizar.')


    def render_board_status(self):
        # Mostrar el tablero con el valor actual de cada celda.

        cell_values =  [' ' if value == '' else value for value in self.board_status.values()]
        print('  {}  |  {}  |  {}  \n-----+-----+-----\n  {}  |  {}  |   {}   \n-----+-----+-----\n  {}  |  {}  |  {}  '.format(*cell_values))

    
    def fill_cell(self, cell):
        # Almacenar dentro de la celda seleccionada el jugador al cual pertenece.

        self.board_status[cell] = self.current_player.id

    
    def check_board(self):
        # Verificar el tablero para determinar si existe un ganador.
        # Retorna: 'G' (si existe un ganador), 'E' (si es empate) o 'C' (si el juego continua)
        
        exists_winner = False;

        for winning_condition in self.winning_conditions:
            a = self.board_status.get(winning_condition[0])
            b = self.board_status.get(winning_condition[1])
            c = self.board_status.get(winning_condition[2])
            
            if a=='' and b=='' and c=='':
                continue

            if a==b and b==c:
                exists_winner = True
                break
        
        if exists_winner:
            return 'G'
        else:
            if '' not in self.board_status.values():
                return 'E'
            else:
                return 'C'


    def change_current_player(self):
        # Intercambiar el jugador actual, alternando entre jugador 1 y 2.

        self.current_player = self.player_2 if self.current_player==self.player_1 else self.player_1

    
    def start(self):
        # Ejecutar el juego.

        self.reset_board()        
        
        while True:
            free_cells = { key:value for (key,value) in self.board_status.items() if value == ''}.keys()

            cell = self.current_player.play_turn(free_cells)            
            self.fill_cell(cell)
            self.render_board_status()

            result = self.check_board()
            if result == 'G':
                print(f'Ganó el jugador {self.current_player}')
                break
            else:
                if result == 'E':
                    print('Empate')
                    break
                else:
                    self.change_current_player()
                    continue