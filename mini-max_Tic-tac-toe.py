board =[' ' for i in range(0,11)]

def make_move(pos,value):
    board[pos]=value

def valid_move(pos):
    return board[pos]==' '

def print_board():
    print("   |    |")
    print(' '+board[1] + ' | '+board[2] + '  | ' + board[3])
    print("   |    |")
    print('-------------')
    print("   |    |")
    print(' '+board[4] + ' | '+board[5] + '  |  ' + board[6])
    print("   |    |")
    print('-------------')
    print("   |    |")
    print(' '+board[7] + ' | '+board[8] + '  | ' + board[9])
    print("   |    |")

def is_winner(b,pl):
    return (
    (b[1]==pl and b[2]==pl and b[3]==pl) or
    (b[4]==pl and b[5]==pl and b[6]==pl) or 
    (b[7]==pl and b[8]==pl and b[9]==pl) or
    (b[1]==pl and b[5]==pl and b[9]==pl) or 
    (b[3]==pl and b[5]==pl and b[7]==pl) or
    (b[1]==pl and b[4]==pl and b[7]==pl) or
    (b[2]==pl and b[5]==pl and b[8]==pl) or 
    (b[3]==pl and b[6]==pl and b[9]==pl) )

def is_empty():
    for i in range(1,10):
        if (board[i] == ' '):
            return False
    return True

def mini_max(b,maximizing):
    if(is_winner(b,'X')):
        return 1
        
    elif(is_winner(b,'O')):
        return -1
        
    if(is_empty()):
        return 0
        
    if maximizing:
        best_score=-1000
        for i in range(1,10):
            if(board[i]==' '):
                board[i]='X' 
                score =mini_max(b,False)
                board[i]=' '
                if(score>best_score):
                    best_score=score
        return best_score
    else:
        best_score=1000
        for i in range(1,10):
            if(board[i]==' '):
                board[i]='O' 
                score =mini_max(b,True)
                board[i]=' '
                if(score<best_score):
                    best_score=score
        return best_score
    

def ai_decision():
    best_score=-1000
    best_move=0
    for i in range(1,10):
        if(board[i]==' '):
            board[i]='X' 
            score=mini_max(board,False)
            board[i]=' '
            if(score>best_score):
                best_score=score
                best_move=i
    
    make_move(best_move,'X')



def main_call():
    print("Let's play tic tac toe !")
    print_board()
    flag=0
    while (not is_empty()):
        print("Enter a valid move from (1-9)")
        pos=int(input())
        if(valid_move(pos)):
            make_move(pos,'O')
            print_board()
        else:
            print("invalid move try another move")
            continue
        
        if(is_winner(board,'O')):
            flag=1
            print("you won!")
            break
        
        print("\n\n ---------------------------\n\n")
        
        ai_decision()
        print_board()

        if(is_winner(board,'O')):
            flag=1
            print("you loose !")
            break


    if(is_empty() and flag==0):
        print('Tie')

main_call()
