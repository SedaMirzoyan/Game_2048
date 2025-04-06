import random
import msvcrt as m


board_size = 4
first_num = 2
second_num = 4
#empty_place = 0

class Game_2048:
    def __init__(self):
        self.m_board = [[0 for j in range(board_size)] for i in range(board_size)]

        self.first_x = random.randint(0, board_size-1)
        self.first_y = random.randint(0, board_size-1)
        self.second_x, self.second_y = 0, 0
        self.directions = { "right": (0, 1), "down": (1, 0), "left": (0, -1), "up": (-1, 0) }

        while (self.second_x == self.first_x):
            self.second_x = random.randint(0,board_size-1)

        while (self.second_y == self.first_y):
            self.second_y = random.randint(0,board_size-1)

        self.m_board[self.first_x][self.first_y] = first_num
        self.m_board[self.second_x][self.second_y] = second_num

        self.all_coords = [[self.first_x, self.first_y], [self.second_x, self.second_y]]
        self.all_nums = [first_num, second_num]
        #print(self.m_board)


    def print_board(self):
        for i in self.m_board:
            print(i)

        
    def move(self):
        while True:
            try:
                if(m.kbhit()):
                    input_dir = m.getch()

                    if(input_dir == b'q'):
                        print("Quit the game")
                        break
                    
                    if((input_dir == b'\xe0')):
                        input_dir = m.getch()
                        if (input_dir == b'K'):             #left arrow
                            print("left")
                        elif (input_dir == b'M'):           #right arrow
                            print("right")
                        elif (input_dir == b'H'):           #up arrow"
                            print("up")
                            self.move_up()
                            self.find_coords()
                            self.set_num()
                            self.print_board()
                        elif (input_dir == b'P'):           #down arrow
                            print("down")
                    else:
                        print("Incorrect input, please enter one of the arrow keys")
                    
            except Exception as e:
                print("Error occured, wrong key")
            #except KeyBoardInterrupt:
            #    print("For quitting the game please press 'q'")


    def generate_random_num(self):
        random_num = random.choice([2, 4])
        print("random_num", random_num)

        self.all_nums.append(random_num)

        return random_num
    

    def find_coords(self):
        num_coords = []
        new_num_x, new_num_y = 0, 0

        for coord in self.all_coords:
            while((new_num_x == coord[0]) or (new_num_y == coord[1])):
                new_num_x = random.randint(0,board_size-1)
                new_num_y = random.randint(0,board_size-1)
            break
        num_coords.append(new_num_x)
        num_coords.append(new_num_y)
        self.all_coords.append(num_coords)
        print(self.all_coords)

        #random_num = self.generate_random_num()
        #self.m_board[new_num_x][new_num_y] = random_num
        
        #print(self.m_board)
        #return (new_num_x, new_num_y)
    

    def set_num(self):
        #coords_tuple = self.find_coords()
        self.generate_random_num()
        print("self.all_nums = ", self.all_nums)
        count = 2   #0th and 1st nums are self.first_num and self.second_num

        #self.m_board[coords_tuple[0]][coords_tuple[1]] = random_num


        for coord in self.all_coords:
            if(((coord[0] != self.first_x) and (coord[0] != self.second_x)) and ((coord[1] != self.first_y) and (coord[1] != self.second_y))): 
                self.m_board[coord[0]][coord[1]] = self.all_nums[count]
                count += 1
                print("count = ", count)

        print("all_coords = ", self.all_coords)
        return self.m_board
    


    def move_up(self):
        print("calling move up")
        i_first = self.first_x
        i_second = self.second_x
        n = len(self.m_board)
        #print("n = ", n)

        prev_first_x = self.first_x
        prev_second_x = self.second_x
        dir_key = "up"
        i = n - 1
        j = n - 1
        sum = 0

        #shift first element to the 1st row
        while(i_first >= 0):
            self.first_x = i_first 
            i_first += self.directions[dir_key][0] 

        #shift second element to the 1st row
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
                    if(self.m_board[i-1][j] == self.m_board[i][j]):
                        print("hiiiiiiiiiiiii")
                        sum = self.m_board[i-1][j] + self.m_board[i][j]
                        self.m_board[i-1][j] = sum
                        self.m_board[i][j] = 0


        #self.set_num()         

        #self.m_board[prev_first_x][self.first_y] = 0
        #self.m_board[prev_second_x][self.second_y] = 0

        self.m_board[self.first_x][self.first_y] = first_num
        self.m_board[self.second_x][self.second_y] = second_num
        #print(self.m_board)  
        #return self.board



    def move_left(self):   
        pass


    def move_right(self):
        pass


    def move_down(self):
        pass



def main():
 
    ob = Game_2048()
    ob.print_board()
    print("Enter arrow keys for moving the elements and 'q' for quitting the game")
    ob.move()
    


if __name__=="__main__":
    main()