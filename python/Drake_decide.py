from Drake_client import GameState
players = {
    10:2,
    9:3,
    8:4,
    7:5 
}


from collections import Counter

def find_missing(list1, list2):
    count1 = Counter(list1)
    count2 = Counter(list2)
    
    missing = []
    for item, count in count1.items():
        diff = count - count2[item]
        if diff > 0:
            missing.extend([item] * diff)
    
    return missing

# Example
list1 = ["a", "b", "b", "c", "d"]
list2 = ["a", "b", "d"]



def decide(hand: list[str], state: GameState) -> int:
    if state.hands is None:
        state.player_count = players[len(hand)]
        state.hands = [hand.copy()]
        
    if len(state.hands) < state.hand_num:
        state.hands.append(hand)
    else:
        missing = find_missing(state.hands[state.hand_num], hand)
        for item in missing:
            state.enemy_cards_played.append(item)
        state.hands[state.hand_num] = hand.copy()
    
    
    
    state.hand_num = (state.hand_num + 1) % state.player_count
    return 0