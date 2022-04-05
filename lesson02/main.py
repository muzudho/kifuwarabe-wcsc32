from view import print_board_header, print_board_body

while True:
    tokens = input().split()

    if 1<=len(tokens):
        if tokens[0] == 'usi':
            print('id name Kifuwaranoki')
            print('id author Satoshi TAKAHASHI')
            print('usiok')
        elif tokens[0] == 'isready':
            print('readyok')
        elif tokens[0] == 'usinewgame':
            pass
        elif tokens[0] == 'position':
            pass
        elif tokens[0] == 'go':
            print('bestmove resign')
        elif tokens[0] == 'quit':
            break
        elif tokens[0] == 'pos':
            # 局面表示
            print_board_header()
            print_board_body()
            pass

