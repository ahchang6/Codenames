import random
import string


class Game:

    @staticmethod
    def words_select():
        result = []
        lines = open("./wordlist.txt").readlines()

        words = lines

        while len(result)<25:
            word_inter = random.choice(words)
            result.append(word_inter[:-1])
            words.remove(word_inter)

        return result

    def return_list_of_coordinate(self, words):
        result = []
        for n in self.process_list:
            if self.process_list[n] in words:
                result.append(n)
        return result

    def __init__(self):
        # a list of words
        self.word_list = Game.words_select()
        # process list is the coordinate coupled with the words
        self.process_list = {}
        # a chart that keeps track of what has been revealed
        self.reveal_chart = {}
        x = 0
        y = 0
        for n in self.word_list:
            self.process_list[(x, y)] = n
            x += 1
            if x % 5 == 0:
                y += 1
                x = 0
        for n in self.word_list.keys():
            self.reveal_chart[n] = False

        chosen_words = random.choice(self.word_list, 18)
        self.assassin = self.return_list_of_coordinate(chosen_words[0])
        blue_index = random.choice([8,9])
        self.starter = 'RED'
        self.blue_words = self.return_list_of_coordinate(chosen_words[1:blue_index])
        self.red_words = self.return_list_of_coordinate(chosen_words[blue_index:])
        if blue_index == 8:
            self.starter = 'BLUE'

        self.room = str(''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(32)]))
        self.turn = ''
        self.redPoint = 0
        self.bluePoint = 0

    def print_room(self):
        print self.word_list
        return self.room
