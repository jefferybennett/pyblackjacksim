inkling "2.0"

type GameState {
    dealerCard1: number<0..260>,
    dealerCard2: number<0..260>,
    dealerCard3: number<0..260>,
    dealerCard4: number<0..260>,
    dealerCard5: number<0..260>,
    dealerCard6: number<0..260>,
    dealerCard7: number<0..260>,
    dealerCard8: number<0..260>,
    dealerCard9: number<0..260>,
    player1Card1: number<0..260>,
    player1Card2: number<0..260>,
    player1Card3: number<0..260>,
    player1Card4: number<0..260>,
    player1Card5: number<0..260>,
    player1Card6: number<0..260>,
    player1Card7: number<0..260>,
    player1Card8: number<0..260>,
    player1Card9: number<0..260>
}

type Action {
    command: number<stay=1, hit=2>
}

simulator BlackJackSimulator(action: Action): GameState {

}

graph (input: GameState): Action {

    concept balance(input): Action {
        curriculum  {
            source BlackJackSimulator
        }
    }
    output balance
}