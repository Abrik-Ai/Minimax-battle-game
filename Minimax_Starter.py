import time

state = { #hold the starting numbers
    'player_hp':  100,
    'enemy_hp':  100,
    'player_block': 0,
    'enemy_block': 0
}

def evaluate(state):
    """AI's eyes. Decide winning or losing """

    score = state['enemy_hp'] - state['player_hp']
        #Base Strategy
        #HP diiference
    
    return score
    

def is_terminal(state):
    """Game is over when either AI's or Player's health less or equal to zero"""
    return state['player_hp'] <= 0 or state['enemy_hp'] <= 0

def get_moves(state):
    """"AI will create 3 futures using 3 items choosing the best one"""
    return ["attack", "heal", "block"] 

def apply_move(state, move, actor):
    """The game process"""
    # Students implement effects
    new_state = state.copy()
    if move == "attack":
        if actor == 'enemy': 
            if state['player_block'] > 0:
                new_state['player_hp'] -=5
                new_state['player_block'] -=1
            else: 
                new_state['player_hp']-=10
        elif actor == 'player' :
            if state['enemy_block'] > 0:
               new_state['enemy_hp'] -=5
               new_state['enemy_block'] -=1
            else:
                new_state['enemy_hp']-=10
          
    elif move == "heal":
        if actor == 'enemy':
            new_state['enemy_hp'] = min(100, new_state['enemy_hp'] + 7)
        else:
            new_state['player_hp']= min(100, new_state['player_hp'] + 7)

    elif move == "block":
        if actor == 'enemy':
            new_state['enemy_block'] +=1
        else:
            new_state['player_block'] +=1
    
    return new_state

def minimax(state, depth, maximizing):
    """Minimax algorithm, """
    if depth == 0 or is_terminal(state): # If AI reach the depth == 0 point game is stopped
        return evaluate(state)
    if maximizing:
        best = float('-inf') #Starts with worst possible score, even a little can damage 
        for move in get_moves(state):#AI trying every move to maximize its chances/damage
            new_state = apply_move(state, move, 'enemy') #Create for each move new state copying the orginal one in order to not change the orginal values
            best = max(best, minimax(new_state, depth-1, False)) #False means now Player's turn in depth-1 and AI see what the Player whould gdo
            #Max shows the best move and value of best changes
                                                                  
        return best
    else:
        best = float('inf')  #Find the lowest number worst for the player
        for move in get_moves(state):
            new_state = apply_move(state, move, 'player')
            best = min(best, minimax(new_state, depth-1, True)) #AI assumes the player is smart and choose the move that gives the AI - lowest score 
        return best
    


#Test all 3 moves to see which gives the highest score
def get_best_ai_move(state): #Uses state for know the starting point and predict scenarios see 
    print("AI is thinking...")
    time.sleep(1)
    best_score = float('-inf') # Any will be better than -inf
    best_move = None #Hasn't diceded what to do yet

    for move in get_moves(state): #Check all options
      simulated_state = apply_move(state, move, 'enemy') #create simulations for checking
      score = minimax(simulated_state, 3, False) #Executing minimax algo
      print(f"AI considers {move}: Score = {score}")

      if score > best_score:
         best_score = score
         best_move = move
         #comparing all outcomes
    return best_move #return the nest action

print("--- BATTLE START ---")

while not is_terminal(state):
   print(f"\nPlayer HP: {state['player_hp']} | Block: {state['player_block']}")
   print(f"Enemy HP: {state['enemy_hp']}| Block: {state['enemy_block']}")
#displays status bar
   move = input("Your move (attack, heal, block): ").lower().strip()
   if move == "stop":
       print("Game stopped.")
       break

   if move in get_moves(state):
        state = apply_move(state, move, 'player')
        print(f"You used {move}!")
   else:
        print("Invalid move! Try again.")
        continue

   
   if is_terminal(state): break

   best_move = get_best_ai_move(state)
   state = apply_move(state, best_move, 'enemy')
   print(f"Enemy used {best_move}!")

   # End Game
if state['player_hp'] > 0:
    print("\nVICTORY!")
else:
    print("\nDEFEAT!") 
