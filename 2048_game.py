import random
import keyboard
import msvcrt as m


board_size = 4
first_num = 2
second_num = 4
#empty_place = 0

class Game_2048:
    def __init__(self):
        self.m_board = [ [0, 0, 0, 0], 
                    [0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0] ]
        self.first_x  = random.randint(0, board_size-1)
        self.first_y = random.randint(0, board_size-1)
        self.second_x, self.second_y = 0, 0
        #self.directions = { "right": [0, 1], "down": [1, 0], "left": [0, -1], "up": [-1, 0] }
        self.directions = { "right": (0, 1), "down": (1, 0), "left": (0, -1), "up": (-1, 0) }

        while (self.second_x == self.first_x):
            self.second_x = random.randint(0,board_size-1)

        while (self.second_y == self.first_y):
            self.second_y = random.randint(0,board_size-1)

        self.m_board[self.first_x][self.first_y] = first_num
        self.m_board[self.second_x][self.second_y] = second_num
        print(self.m_board)
        

    def move(self):
        #n = len(self.m_board)
        #m = len(self.m_board[0])

        
        while True:
            if keyboard.is_pressed("left arrow"):
                print("left")
                self.move_left() 
            elif keyboard.is_pressed("right arrow"):
                print("right")
                self.move_right()
            elif keyboard.is_pressed("up arrow"):
                if(flag == True):
                    #print("up")
                    self.move_up()  
                    #self.set_num()
                    flag = False   
                else:
                    m.getch()
                    print("up->elif->else")
                #    self.set_num()
                #    continue       
            elif keyboard.is_pressed("down arrow"):
                print("down")
                self.move_down()


    def set_num(self):
        num_coords = []
        all_coords = [[self.first_x, self.first_y], [self.second_x, self.second_y]]
        new_num_x = 0
        new_num_y = 0
        random_num = 2

        while True:
            random_num = random.randint(2,4)
            if((random_num == 2) or (random_num == 4)):
                break
        print("random_num", random_num)

        for coord in all_coords:
            while((new_num_x == coord[0]) or (new_num_y == coord[1])):
                new_num_x = random.randint(0,board_size-1)
                #print("new_num_x", new_num_x)
                new_num_y = random.randint(0,board_size-1)
                #print("new_num_y", new_num_y)
            break
        num_coords.append(new_num_x)
        num_coords.append(new_num_y)
        all_coords.append(num_coords)
        print(all_coords)

        self.m_board[new_num_x][new_num_y] = random_num


    def move_up(self):
        i_first = self.first_x
        i_second = self.second_x
        n = len(self.m_board)
        #print("n = ", n)

        prev_first_x = self.first_x
        prev_second_x = self.second_x
        dir_key = "up"
        i = n - 1
        j = n - 1


        while(i_first >= 0):
            self.first_x = i_first 
            i_first += self.directions[dir_key][0] 


        while(i_second >= 0):
            self.second_x = i_second
            i_second += self.directions[dir_key][0] 

        
        for i in range(n-1, -1, -1): 
            for j in range(n-1, -1, -1):
                if(self.m_board[i][j] == 0):
                    self.m_board[i-1][j] = self.m_board[i][j]
                    self.m_board[i][j] = 0
                    if(prev_first_x != 0):
                        #print("prev_first_x = ", prev_first_x, "j = ", j, "self.m_board[prev_first_x][j]", self.m_board[prev_first_x][j])
                        self.m_board[prev_first_x][j] = 0
                    elif(prev_second_x != 0):
                        #print("prev_second_x = ", prev_second_x, "j = ", j, "self.m_board[prev_second_x][j]", self.m_board[prev_second_x][j])
                        self.m_board[prev_second_x][j] = 0
                else:
                    pass


        self.set_num()
        #self.m_board[prev_first_x][self.first_y] = 0
        #self.m_board[prev_second_x][self.second_y] = 0


        self.m_board[self.first_x][self.first_y] = first_num
        self.m_board[self.second_x][self.second_y] = second_num
        print(self.m_board)  



    def move_left(self):   
        pass


    def move_right(self):
        pass


    def move_down(self):
        pass




ob = Game_2048()
#ob.move_up()
ob.move()
