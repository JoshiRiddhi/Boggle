from typing import List, Tuple, Set

class TrieNode:
    def __init__(self, letter=None) -> None:
        self.letter = letter
        self.end_word = False
        self.word = ""
        self.pointers = dict()

        # add attributes for whether it is the end of a word and a collection of pointers to
        # next letters

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def generate_tree_from_file(self)->None:
        words = self._load_words()
         #add code here to set up the TrieNode tree structure for the words
        
        for w in words:
            node = self.root
            for l in reversed(w):
                root_dict = node.pointers
                if not l in root_dict:
                    root_dict[l] = TrieNode(l)
                    node = root_dict[l]
                else:
                    node = root_dict[l]
            node.end_word = True                  

    # helper to load words. No modifications needed
    def _load_words(self):
        words = []
        with open("words.txt", "r", encoding="utf-8") as file:
            for line in file:
                word = line.strip()
                words.append(word)
        return words

# Implement the Boggled Solver. This Boggle has the following special properties:
# 1) All words returned should end in a specified suffix (i.e. encode the trie in reverse)
# 2) Board tiles may have more than    letter (e.g. "qu" or "an")
# 3) The number of times you can use the same tile in a word is variable
# Your implementation should account for all these properties.
directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
class Boggled:

    

    # setup test initializes the game with the game board and the max number of times we can use each 
    # tile per word
    def setup_board(self, max_uses_per_tile: int, board:List[List[str]])->None:
        self.max_uses = max_uses_per_tile
        self.board = board
        self.uses_board = [[0]*len(board) for i in range(len(board))]
        side = len(self.board)
        # for i in range(side):
        #     num_list = list()
        #     for k in range(side):
        #         num_list.append(0)
        #     self.uses_board.append(num_list)
        self.trie = Trie()
        self.trie.generate_tree_from_file()
        self.words = set()



    
    # Returns a set of all words on the Boggle board that end in the suffix parameter string. Words can be found
    # in all 8 directions from a position on the board
    def get_all_words(self, suffix:str)->Set:
        
        words_set = set()
        
        self.suffix=suffix
        for r in range(len(self.board)):
            for c in  range(len(self.board[r])):
                last_letter = suffix[len(suffix)-1] # optimization to only recurse for letters that start
                board_letter = self.board[r][c]
                if board_letter[len(board_letter)-1] is last_letter:
               # if self.board[r][c] == suffix[len(suffix)-1]:
                    word = self.get_all_words_recursive((r,c), len(suffix)-1, self.trie.root,"")
                    words_set.update(self.words)
        
        return words_set


    # recursive helper for get_all_words. Customize parameters as needed; you will likely need params for 
    # at least a board position and tile
    def get_all_words_recursive(self,curr_pos:Tuple[int,int], suff_index:int, node:TrieNode = None, word:str=""):
        # first find all letters in suffix 
        if self.uses_board[curr_pos[0]][curr_pos[1]]+1 > self.max_uses:
            return
        
        cell=self.board[curr_pos[0]][curr_pos[1]]
        
        for letters in reversed(cell):
            #node=node.pointers[letters]
            if self.get_all_words_helper(letters,node)==False:
            #if node is None:
                return
            else:
                node=node.pointers[letters]
                if suff_index > -1 :
                    if self.suffix[suff_index] is not letters:
                        return
                    suff_index=suff_index-1
                word=letters+word
        
        if suff_index==-1 and len(word)>len(self.suffix) and node.end_word== True:
            self.words.add(word)

        self.uses_board[curr_pos[0]][curr_pos[1]]+=1 

        for direction in directions:
            new_row = curr_pos[0]+direction[0]
            new_col = curr_pos[1]+direction[1]

            if self.is_valid_move(new_row, new_col):
                self.get_all_words_recursive((new_row, new_col),suff_index , node, word) 
        self.uses_board[curr_pos[0]][curr_pos[1]] -= 1 #unchoose  
    
    def is_valid_move(self, row, col):
        return row >= 0 and row < len(self.board) and col >=0  and col < len(self.board)

        
    def get_all_words_helper(self, letter, node:TrieNode):
            if letter in node.pointers:
                return True
            else:
                return False
            


from typing import List, Tuple, Set

class TrieNode:
    def __init__(self, letter=None) -> None:
        self.letter = letter
        self.end_word = False
        self.word = ""
        self.pointers = dict()

        # add attributes for whether it is the end of a word and a collection of pointers to
        # next letters

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def generate_tree_from_file(self)->None:
        words = self._load_words()
         #add code here to set up the TrieNode tree structure for the words
        
        for w in words:
            node = self.root
            for l in reversed(w):
                root_dict = node.pointers
                if not l in root_dict:
                    root_dict[l] = TrieNode(l)
                    node = root_dict[l]
                else:
                    node = root_dict[l]
            node.end_word = True                  

    # helper to load words. No modifications needed
    def _load_words(self):
        words = []
        with open("words.txt", "r", encoding="utf-8") as file:
            for line in file:
                word = line.strip()
                words.append(word)
        return words

# Implement the Boggled Solver. This Boggle has the following special properties:
# 1) All words returned should end in a specified suffix (i.e. encode the trie in reverse)
# 2) Board tiles may have more than    letter (e.g. "qu" or "an")
# 3) The number of times you can use the same tile in a word is variable
# Your implementation should account for all these properties.
directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
class Boggled:

    

    # setup test initializes the game with the game board and the max number of times we can use each 
    # tile per word
    def setup_board(self, max_uses_per_tile: int, board:List[List[str]])->None:
        self.max_uses = max_uses_per_tile
        self.board = board
        self.uses_board = [[0]*len(board) for i in range(len(board))]
        side = len(self.board)
        # for i in range(side):
        #     num_list = list()
        #     for k in range(side):
        #         num_list.append(0)
        #     self.uses_board.append(num_list)
        self.trie = Trie()
        self.trie.generate_tree_from_file()
        self.words = set()



    
    # Returns a set of all words on the Boggle board that end in the suffix parameter string. Words can be found
    # in all 8 directions from a position on the board
    def get_all_words(self, suffix:str)->Set:
        
        words_set = set()
        
        self.suffix=suffix
        for r in range(len(self.board)):
            for c in  range(len(self.board[r])):
                last_letter = suffix[len(suffix)-1] # optimization to only recurse for letters that start
                board_letter = self.board[r][c]
                if board_letter[len(board_letter)-1] is last_letter:
               # if self.board[r][c] == suffix[len(suffix)-1]:
                    word = self.get_all_words_recursive((r,c), len(suffix)-1, self.trie.root,"")
                    words_set.update(self.words)
        
        return words_set


    # recursive helper for get_all_words. Customize parameters as needed; you will likely need params for 
    # at least a board position and tile
    def get_all_words_recursive(self,curr_pos:Tuple[int,int], suff_index:int, node:TrieNode = None, word:str=""):
        # first find all letters in suffix 
        if self.uses_board[curr_pos[0]][curr_pos[1]]+1 > self.max_uses:
            return
        
        cell=self.board[curr_pos[0]][curr_pos[1]]
        
        for letters in reversed(cell):
            #node=node.pointers[letters]
            if self.get_all_words_helper(letters,node)==False:
            #if node is None:
                return
            else:
                node=node.pointers[letters]
                if suff_index > -1 :
                    if self.suffix[suff_index] is not letters:
                        return
                    suff_index=suff_index-1
                word=letters+word
        
        if suff_index==-1 and len(word)>len(self.suffix) and node.end_word== True:
            self.words.add(word)

        self.uses_board[curr_pos[0]][curr_pos[1]]+=1 

        for direction in directions:
            new_row = curr_pos[0]+direction[0]
            new_col = curr_pos[1]+direction[1]

            if self.is_valid_move(new_row, new_col):
                self.get_all_words_recursive((new_row, new_col),suff_index , node, word) 
        self.uses_board[curr_pos[0]][curr_pos[1]] -= 1 #unchoose  
    
    def is_valid_move(self, row, col):
        return row >= 0 and row < len(self.board) and col >=0  and col < len(self.board)

        
    def get_all_words_helper(self, letter, node:TrieNode):
            if letter in node.pointers:
                return True
            else:
                return False
            