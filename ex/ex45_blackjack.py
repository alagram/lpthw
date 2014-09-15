from random import shuffle
from sys import exit
from os import system

class Card(object):
    def __init__(self, suit, face_value):
        self.suit = suit
        self.face_value = face_value

    def pretty_output(self):
        return "The %s of %s." % (self.face_value, self.find_suit())

    def __str__(self):
        return self.pretty_output()

    def find_suit(self):
        if self.suit == 'H':
            return 'Hearts'
        elif self.suit == 'D':
            return 'Diamonds'
        elif self.suit == 'S':
            return 'Spades'
        elif self.suit == 'C':
            return 'Clubs'


class Deck(object):
    def __init__(self):
        self.cards = []
        # self.build_cards()


    def build_cards(self):
        for suit in ['H', 'D', 'S', 'C']:
            for face_value in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']:
                self.cards.append(Card(suit, face_value))
        return self.scramble()

    def scramble(self):
        shuffle(self.cards)
        return self.cards

    def deal_one(self):
        return self.cards.pop()


class Hand(object):
    def show_hand(self):
        print "=== %s's Hand ===" % self.name
        for card in self.cards:
            print "==> %s " % card

        print "Total: %s " % self.total()
        print ""


    def total(self):
        face_values = [card.face_value for card in self.cards]

        total = 0
        for value in face_values:
            if value == "A":
                total += 11
            elif value == "J" or value == "Q" or value == "K":
                total += 10
            else:
                total += int(value)


        count = len([value for value in face_values if value == "A"])

        for x in range(count):
            if total <= 21:
                break
            total -= 10

        return total


    def add_card(self, new_card):
        self.cards.append(new_card)

    def is_busted(self):
        return self.total() > 21


class Player(Hand):
    def __init__(self, name):
        self.name = name
        self.cards = []

    def show_flop(self):
        return super(Player, self).show_hand()
        # return self.show_hand()


class Dealer(Hand):

    def __init__(self):
        self.name = "Dealer"
        self.cards = []


    def show_flop(self):
        print "=== %s's Hand ===" % self.name
        print "==> First card is hidden"
        print "==> Second card is %s " % self.cards[1]


class BlackJack(object):

    def __init__(self):
        self.deck = Deck()
        self.deal = self.deck.build_cards()
        self.player = Player("Albert")
        self.dealer = Dealer()

    def set_player_name(self):
        system("clear")
        self.player.name =  raw_input("What's your name? ")

    def deal_cards(self):
        self.player.add_card(self.deck.deal_one())
        self.dealer.add_card(self.deck.deal_one())
        self.player.add_card(self.deck.deal_one())
        self.dealer.add_card(self.deck.deal_one())

    def show_flop(self):
        self.player.show_flop()
        self.dealer.show_flop()

    def blackjack_or_bust(self, player_or_dealer):
        if player_or_dealer.total() == 21:
            if isinstance(player_or_dealer, Dealer):
                print "Sorry, dealer hit BlackJack. %s loses." % self.player.name
            else:
                print "Congratulations, you hit BlackJack! %s wins!" % self.player.name
            self.play_again()
        elif player_or_dealer.total() > 21:
            if isinstance(player_or_dealer, Dealer):
                print "Congratulations, dealer busted. %s wins!" % self.player.name
            else:
                print "Sorry, %s busted. %s loses." % (self.player.name, self.player.name)
            self.play_again()


    def player_turn(self):
        print "%s's turn" % self.player.name

        self.blackjack_or_bust(self.player)

        while not self.player.total() > 21:
            response = raw_input("What would %s like to do? 1) hit 2) stay " % self.player.name)

            # Fix this!
            # if '1' not in response or '2' not in response:
            #     print "Error: you must enter 1 or 2"
            #     continue

            if response == "2":
                print  self.player.name, "chose to stay"
                break

            new_card = self.deck.deal_one()
            print "Dealing new card to %s : %s" % (self.player.name, new_card)
            self.player.add_card(new_card)
            print "%s's total is now: %s" % (self.player.name, self.player.total())

            self.blackjack_or_bust(self.player)

        print "%s stay's at %s" % (self.player.name, self.player.total())
        print ""

    def dealer_turn(self):
        print "Dealer's turn"

        self.blackjack_or_bust(self.dealer)

        while self.dealer.total() < 17:
            new_card = self.deck.deal_one()
            print "Dealing new card to dealer: %s" % new_card
            self.dealer.add_card(new_card)
            print "Dealer's total is now: %s" % self.dealer.total()

            self.blackjack_or_bust(self.dealer)

        print "Dealer stays at %s" % self.dealer.total()


    def who_won(self):
        if self.player.total() > self.dealer.total():
            print "Congratulations, %s wins!" % self.player.name
        elif self.player.total() < self.dealer.total():
            print "Sorry, %s wins" % self.dealer.name
        else:
            print "It's a tie."
            self.play_again()


    def play_again(self):
        print ""
        response = raw_input("Would you like to play again? 1) yes 2) no, exit ")
        if response == "1":
            system("clear")
            print "Starting new game..."
            print ""
            self.deck = Deck()
            self.deal = self.deck.build_cards()
            self.player.cards = []
            self.dealer.cards = []
            self.start()
        else:
            print "Goodbye"
            exit(1)

    def start(self):
        self.set_player_name()
        self.deal_cards()
        self.show_flop()
        self.player_turn()
        self.dealer_turn()
        self.who_won()


game = BlackJack()
game.start()
