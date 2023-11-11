class Card:
    """
    Superclass for cards.

    
    """

    Clubs = u"\N{BLACK CLUB SUIT}"
    Diamonds = u"\N{WHITE DIAMOND SUIT}"
    Hearts = u"\N{WHITE HEART SUIT}"
    Spades = u"\N{BLACK SPADE SUIT}"
    Jack = 11
    Queen = 12 
    King = 13
    Ace = 1

    def __init__(self, rank: int, suit: str) -> None:
        assert suit in (Card.Clubs, Card.Diamonds, Card.Hearts, Card.Spades)
        assert 1 <= rank < 14
        self.rank = rank
        self.suit = suit
        self. order = rank

    @property
    def hardValue(self) -> int:
        return self.rank
    
    @property
    def softValue(self) -> int:
        return self.rank
    