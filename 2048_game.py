import random
import keyboard

#dir_i = 0       #change later? or not
#dir_j = 0

first_num = 2
second_num = 4
#empty_place = 0

class Game_2048:
    def __init__(self):
        self.m_board = [ [0, 0, 0, 0], 
                    [0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0] ]
        self.first_x = random.randint(0, 3)
        self.first_y = random.randint(0, 3)
        self.second_x = random.randint(0, 3)
        self.second_y = random.randint(0, 3)
        #self.directions = { "right": [dir_i, dir_j+1], "down": [dir_i+1, dir_j], "left": [dir_i, dir_j-1], "up": [dir_i-1, dir_j] }
        self.directions = { "right": [0, 1], "down": [1, 0], "left": [0, -1], "up": [-1, 0] }

        while (self.second_x == self.first_x):
            self.second_x = random.randint(0,3)

        while (self.second_y == self.first_y):
            self.second_y = random.randint(0,3)

        self.m_board[self.first_x][self.first_y] = first_num
        self.m_board[self.second_x][self.second_y] = second_num
        print(self.m_board)
        

    def move(self):
        #n = len(self.m_board)
        #m = len(self.m_board[0])
        #j = 0
        #i = 0
        #directions = { "right": [i, j+1], "down": [i+1, j], "left": [i, j-1], "up": [i-1, j] }
        dir_key = keyboard.is_pressed("left arrow")

        while True:
            if keyboard.is_pressed("left arrow"):
                print("left")
                dir_key = "left"
                #call function move_left() ##############
            elif keyboard.is_pressed("right arrow"):
                print("right")
                dir_key = "right" 
            elif keyboard.is_pressed("up arrow"):
                print("up")
                dir_key = "up"       
                print(i, j)   
                self.move_up()          
            elif keyboard.is_pressed("down arrow"):
                print("down")
                dir_key = "down" 
        #else:
        #    print("l or r or d or up")     
       # i += self.directions[dir_key][0]  
       # j += self.directions[dir_key][1] 


    def move_up(self):
        i_first = self.first_x
        i_second = self.second_x
        n = len(self.m_board)

        prev_first_x = self.first_x
        prev_second_x = self.second_x
        dir_key = "up"
        i = 3
        j = 0


        while(i_first >= 0):
            self.first_x = i_first 
            print("self.first_x = ", i_first) 
            i_first += self.directions[dir_key][0] 

        while(i_second >= 0):
            self.second_x = i_second
            print("self.second_x = ", i_second) 
            i_second += self.directions[dir_key][0] 
        
        while((i > i_first) and (j < n)): #0
            print("yoho")
            self.m_board[i-1][j] = self.m_board[i][j]
            self.m_board[i][j] = 0
            if(prev_first_x != 0):
                self.m_board[prev_first_x][j] = 0
            elif(prev_second_x != 0):
                self.m_board[prev_second_x][j] = 0
            i -= 1
            j += 1
            print(self.m_board)  


        print("self.first_x", self.first_x, "self.first_y", self.first_y) 
        print("self.second_x", self.second_x, "self.second_y", self.second_y)   

        #self.m_board[prev_first_x][self.first_y] = 0
        #self.m_board[prev_second_x][self.second_y] = 0


        self.m_board[self.first_x][self.first_y] = first_num
        self.m_board[self.second_x][self.second_y] = second_num
        print(self.m_board)  



    def move_left(self):   
        pass


    def move_right(self):
        pass


    def move_top(self):
        pass




ob = Game_2048()
ob.move_up()
ob.move()
