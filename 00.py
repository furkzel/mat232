import random
import math

class Card:

    suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
    values = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':11, 'Q':12, 'K':13}
    symbols = {'Spades': '♠', 'Hearts': '♥', 'Diamonds': '♦', 'Clubs': '♣'}

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        if self.value == 1:
            return "A{}".format(Card.symbols[self.suit])
        elif self.value == 11:
            return "J{}".format(Card.symbols[self.suit])
        elif self.value == 12:
            return "Q{}".format(Card.symbols[self.suit])
        elif self.value == 13:
            return "K{}".format(Card.symbols[self.suit])
        else:
            return "{}{}".format(self.value, Card.symbols[self.suit])
    
    def __repr__(self):
        return "{} of {}".format(self.value, self.suit)
    
    def __lt__(self, other):
        if self.value < other.value:
            return True
        elif self.value == other.value:
            return self.suit < other.suit
        else:
            return False

class Deck:
    def __init__(self):
        self.cards = []
        for suit in Card.suits:
            for value in Card.values:
                card = Card(suit, value)
                self.cards.append(card)
    
    def shuffle(self):
        random.shuffle(self.cards)

    def draw_random_card(self):
        print(self.cards[(random.randint(0, len(self.cards)-1))])
    
    def show_cards(self):
        for card in self.cards:
            print(card)

    def length(self):
        return "Deck of {} cards".format(len(self.cards))

class DHeap:
    def __init__(self, d):
        self.heap = []
        self.d = d

    def insert(self, value):
        self.heap.append(value)
        self.heapify_up(len(self.heap)-1)

    def minimum(self):
        return self.heap[0]
    
    def extract_min(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        min = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return min
    
    def maximum(self):
        return self.heap[0]
    
    def extract_max(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        max = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return max
    
    def delete_min(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        min = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return min
    
    def delete_max(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        max = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return max
    
    def delete(self, value):
        for i in range(len(self.heap)):
            if self.heap[i] == value:
                self.heap[i] = self.heap.pop()
                self.heapify_down(i)
                return True
        return False
    
    def heapify_up(self, index):
        parent = math.floor((index-1)/self.d)
        if parent >= 0 and self.heap[parent] > self.heap[index]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            self.heapify_up(parent)

    def heapify_down(self, index):
        child = self.smallest_child(index)
        if child != None and self.heap[child] < self.heap[index]:
            self.heap[child], self.heap[index] = self.heap[index], self.heap[child]
            self.heapify_down(child)

    def smallest_child(self, index):
        smallest = None
        for i in range(1, self.d+1):
            child = self.d*index + i
            if child < len(self.heap):
                if smallest == None or self.heap[child] < self.heap[smallest]:
                    smallest = child
        return smallest
    
    def largest_child(self, index):
        largest = None
        for i in range(1, self.d+1):
            child = self.d*index + i
            if child < len(self.heap):
                if largest == None or self.heap[child] > self.heap[largest]:
                    largest = child
        return largest
    
    def __str__(self):
        return str(self.heap)
    

# We will test our heap algorithm using the card and deck classes I have defined.

# First, we will create a deck of cards and shuffle it.
deck = Deck()
deck.shuffle()

# Then, we will create a 4-heap and insert all the cards into it.
heap = DHeap(4)
for card in deck.cards:
    heap.insert(card)

# Finally, we will extract all the cards from the heap and print them out.
for i in range(len(heap.heap)):
    print(heap.extract_min())

# We can see that the cards are printed out in order, so our heap algorithm works.

# Now we'll define another application for heaps: a priority queue.
# A priority queue is a data structure that allows us to insert elements with a priority and extract the element with the highest priority.

# We will use a heap to implement a priority queue.

class PriorityQueue:
    def __init__(self, d):
        self.heap = DHeap(d)
    
    def insert(self, value):
        self.heap.insert(value)
    
    def maximum(self):
        return self.heap.maximum()
    
    def extract_max(self):
        return self.heap.extract_max()
    
    def delete_max(self):
        return self.heap.delete_max()
    
    def delete(self, value):
        return self.heap.delete(value)
    
    def __str__(self):
        return str(self.heap)
    
    def __repr__(self):
        return str(self.heap)
    

# We will test our priority queue using the card and deck classes I have defined.

# First, we will create a deck of cards and shuffle it.
deck = Deck()
deck.shuffle()

# Then, we will create a priority queue and insert all the cards into it.a
pq = PriorityQueue(4)
for card in deck.cards:
    pq.insert(card)
    
# Finally, we will extract all the cards from the priority queue and print them out.
for i in range(len(pq.heap.heap)):
    print(pq.extract_max())

# We can see that the cards are printed out in order, so our priority queue works.

# Now we'll define another application for heaps: Application d'Algorithme de 'Sorting ALgortihms as Special Cases of a Prirority Queue Sort'

def parent(i, d):
    return (i - 1) // d

def child(i, j, d):
    return d * i + j + 1

def max_heapify(A, i, n, d):
    largest = i
    for j in range(d):
        c = child(i, j, d)
        if c < n and A[c] > A[largest]:
            largest = c
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest, n, d)

def build_max_dheap(A, d):
    n = len(A)
    for i in range(n // d - 1, -1, -1):
        max_heapify(A, i, n, d)

def d_heapsort(A, d):
    build_max_dheap(A, d)
    n = len(A)
    for i in range(n - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        max_heapify(A, 0, i, d)

# We will test our heap algorithm using the card and deck classes I have defined.

# First, we will create a deck of cards and shuffle it.
deck = Deck()
deck.shuffle()

# Then, we will create a list of cards and insert all the cards into it.
cards = []
for card in deck.cards:
    cards.append(card)

# Finally, we will sort the cards using d-heapsort and print them out.
d_heapsort(cards, 1)
print(cards)
print(deck.cards)