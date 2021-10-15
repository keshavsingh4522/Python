#include <iostream>
using namespace std;

//computer squares are 1, player squares are -1.

char gridChar(int i)
{
    switch (i)
    {
    case -1:
        return 'X';
    case 0:
        return ' ';
    case 1:
        return 'O';
    }
}

void draw(int b[9])
{
    cout << gridChar(b[0]) << "  | " << gridChar(b[1]) << " | " << gridChar(b[2]) << endl;
    cout << "---+---+---\n";
    cout << gridChar(b[3]) << "  | " << gridChar(b[4]) << " | " << gridChar(b[5]) << endl;
    cout << "---+---+---\n";
    cout << gridChar(b[6]) << "  | " << gridChar(b[7]) << " | " << gridChar(b[8]) << endl;
}

int win(const int board[9])
{
    //determines if a player has won, returns 0 otherwise.
    unsigned wins[8][3] = {{0, 1, 2}, {3, 4, 5}, {6, 7, 8}, {0, 3, 6}, {1, 4, 7}, {2, 5, 8}, {0, 4, 8}, {2, 4, 6}};
    int i;
    for (i = 0; i < 8; ++i)
    {
        if (board[wins[i][0]] != 0 &&
            board[wins[i][0]] == board[wins[i][1]] &&
            board[wins[i][0]] == board[wins[i][2]])
            return board[wins[i][2]];
    }
    return 0;
}

int minimax(int board[9], int player)
{
    /* This function tests if a specific player wins. Possibilities:
       Three rows    [X X X] or [O O O]
       Three cols    [X X X] or [O O O]
       Two diagonals [X X X] or [O O O]*/
    int winner = win(board);
    if (winner != 0)
        return winner * player;

    int move = -1;
    int score = -2;
    int i;
    for (i = 0; i < 9; ++i) //For all moves,
    {
        if (board[i] == 0) //If legal,
        {
            board[i] = player; //Try the move
            int thisScore = -minimax(board, player * -1);
            if (thisScore > score)
            {
                score = thisScore;
                move = i;
            }             //Pick the one that's worst for the opponent
            board[i] = 0; //Reset board after try
        }
    }
    if (move == -1)
        return 0;
    return score;
}

void computerMove(int board[9])
{
    int move = -1;
    int score = -2;
    int i;
    for (i = 0; i < 9; ++i)
    {
        if (board[i] == 0)
        {
            board[i] = 1;
            int tempScore = -minimax(board, -1);
            board[i] = 0;
            if (tempScore > score)
            {
                score = tempScore;
                move = i;
            }
        }
    }
    //returns a score based on minimax tree at a given node.
    board[move] = 1;
}

void playerMove(int board[9])
{
    int move = 0;
    do
    {
        cout << "\nInput move ([0..8]): ";
        cin >> move;
        cout << endl;
    } while (move >= 9 || move < 0 && board[move] == 0);
    board[move] = -1;
}

int main()
{
    int board[9] = {0, 0, 0, 0, 0, 0, 0, 0, 0};
    //computer squares are 1, player squares are -1.
    cout << "Computer: O, You: X\nPlay (1)st or (2)nd? ";
    int player = 0;
    cin >> player;
    cout << endl;
    unsigned turn;
    for (turn = 0; turn < 9 && win(board) == 0; ++turn)
    {
        if ((turn + player) % 2 == 0)
            computerMove(board);
        else
        {
            draw(board);
            playerMove(board);
        }
    }
    switch (win(board))
    {
    case 0:
        draw(board);
        cout << "A draw! " << endl;
        break;
    case 1:
        draw(board);
        cout << "You lose" << endl;
        break;
    case -1:
        draw(board);
        cout << "You win!" << endl;
        break;
    }
}
