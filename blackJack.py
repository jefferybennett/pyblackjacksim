#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 Jeff Bennett (jeffery.bennett@gmail.com)
#
# Distributed under terms of the MIT license.
###############################################################################

import sys
import itertools
import functools
import random

'''****************************
   *** Game ***
   ****************************'''
class Game:

    def __init__(self, config):
        self.settings = config['settings'];
        self.players = [];
        self.shoe = Shoe(self.settings['decksInShoe']);
        self.pastHands = [];
        self.currentHand = Hand(self);

        for player in config['players']:
            self.players.append(Player(player));

    @property
    def state(self):
        return State(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

    def __str__(self):
        s = "game"
        return s

    def __repr__(self):
        return self.state

    def reset(self):
        self.shoe = Shoe(self.settings['decksInShoe']);

    def step(self, action):
        
        # Play next Card
        if action == 1 or action == 2:
            self.players[0].MakeMove(action);

        self.state == self.GetCurrentState();

        return self.state

    def GetCurrentState():
        returnSelf.dealerCard1 = 
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

class Hand:

    def __init__(self, game):
        self.numberCardsDealt = 0
        self.game = game;

    def Deal(self):

        # if no cards have been dealt
            # deal to players
        for player in self.game.players:
            game._dealer.DealCardToPlayer(player, 2);
        

        
'''****************************
   *** Player ***
   ****************************'''
class Player:

    def __init__(self, playerConfig):
        self.settings = playerConfig;
        self.cardsInHand = [];


'''****************************
   *** Dealer ***
   ****************************'''
class Dealer:

    def __init__(self, game):
        self.game = game;

    def DealCardToPlayer(self, player, numberCardsToDeal):

        card = game.shoe.GetCardToDeal();

'''****************************
   *** Shoe ***
   ****************************'''
class Shoe:

    def __init__(self, decksInShoe):
        self.totalDecksInShoe = decksInShoe;
        self.totalCardsInShoe = decksInShoe * 52;
        self.totalCardsDealt = 0;
        self.cardsPlayed = [];
        self.depth_threshold = 50;

        self.Shuffle();

    ''' Shoe.Shuffle '''
    def Shuffle(self):
        ranks = ['A'] + [str(n) for n in range(2, 11)] + ['J', 'Q', 'K']
        suits = Card.SUITS
        decks = [itertools.product(ranks, suits)
                 for ideck in range(self.totalDecksInShoe)]
        cards = functools.reduce(lambda x, y: x + y,
                                 [list(deck) for deck in decks])

        self._cards = [Card(rank, suit) for (rank, suit) in cards]
        random.shuffle(self._cards)

    ''' Shoe.GetCardToDeal '''
    def GetCardToDeal(self):
        if len(self.cards) == 0:
                self.check_reshuffle();
        return self.cards.pop();

    def check_reshuffle(self):
        if self.totalCardsDealt / self.totalCardsInShoe >= self.depth_threshold:
            self.Shuffle()

    def __repr__(self):
        #shoe_repr = 'decks=%d, reshuffle at %.2f.' % (self._ndecks,
        #                                              self._depth_threshold)
        shoe_repr = 'Total Decks In Shoe: %d | ' % (self.totalDecksInShoe);
        shoe_repr += 'x: %d/%d' % (len(self._cards), self.totalCardsInShoe)
        return shoe_repr

'''****************************
   *** Card ***
   ****************************'''
class Card:

    val_map = {'A': [1, 11], 'J': [10], 'Q': [10], 'K': [10]}
    val_map.update({str(n): [n] for n in range(2, 11)})
    SUITS = [SPADE, HEART, DIAMOND, CLUB] = ['\u2660', '\u2665',
                                             '\u2666', '\u2663']

    def __init__(self, rank, suit):
        if suit not in Card.SUITS:
            raise ValueError('suit: %s not one of %s', (suit, Card.SUITS));
        if rank not in Card.val_map:
            raise ValueError('rank: %s not one of %s', (rank, Card.val_map));
        self.rank = rank;
        self.suit = suit;
        # Even though only Ace can have more than one value, all Cards will
        # return lists so that invokers don't need to treat the return values
        # differently.
        self._values = Card.val_map[rank];

    @property
    def values(self): return self._values

    @property
    def card_rep(self): return self.rank + self.suit

    def __repr__(self):
        values = ','.join([str(s) for s in self.values])
        return '%s%s (%s)' % (self.rank, self.suit, values)

    def __str__(self):
        '''Color-coded string representation.  Red if heart or diamond.'''
        (clr0, clr1) = ('', '')
        if self.suit in [Card.HEART, Card.DIAMOND]:     # heart or diamond
            (clr0, clr1) = ('\x1b[31m', '\x1b[0m')  # red markup decorators
        return clr0 + self.card_rep + clr1