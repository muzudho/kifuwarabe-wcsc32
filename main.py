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
