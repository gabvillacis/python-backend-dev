import player
from board import Board

player_x = player.Player('X')
player_y = player.Player('Y')

board = Board(player_x, player_y)

while True:
    print('=' * 50)
    iniciar_partida = input('Desea iniciar una partida? (S/N): ')    
    if iniciar_partida.upper() == 'S':
        board.render_instructions()
        board.start()
    else:
        break