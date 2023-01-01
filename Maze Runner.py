import tkinter as tk
from tkinter import messagebox  
from tkinter import ttk
from tkinter.font import families

import time
from typing import Counter
bc = tk.Tk()
bc.geometry('560x610+300+0')
bc.title("Maze Runner")
bc.resizable(width=False, height=False)

class Maze :
    start = False
    block = list()
    for i in range(9) :
        block.append([])
        for j in range(9) :
            block[i].append({
                'u' : True ,
                'r' : True ,
                'l' : True ,
                'd' : True ,
                'v' : -1 ,
                'seen' : False ,
                's_id' : -1 , 
                'can_check' : -1 
            })
    Horizental_wall = dict()
    for i in range(10):
        for j in range(9) :
            if i == 0 or i == 9 :
                Horizental_wall[f'wall{i}{j}'] = tk.Button(bc , background = "gray" , bd = 0)
            else :
                Horizental_wall[f'wall{i}{j}'] = tk.Button(bc , background = "#a6d0de" , bd= 0)
            
            Horizental_wall[f'wall{i}{j}'].place(height = 10 , width = 50 , x = j * 50 +(j+1)*10 + 5, y = i*50 + i * 10 +5)
    Vertical_wall = dict()
    for i in range(9) :
        for j in range(10) :
            if j == 0 or j == 9 :
                Vertical_wall[f'wall{i}{j}'] = tk.Button(bc , background = "gray" , bd = 0)
            else :
                Vertical_wall[f'wall{i}{j}'] = tk.Button(bc , background = "#a6d0de" , bd =0)
            
            
            Vertical_wall[f'wall{i}{j}'].place(height = 50 , width = 10 , x = j * 50 + (j)*10 + 5, y = i*50+(i+1)*10 + 5)
    for i in range(10) :
        for j in range(9) :
            Horizental_wall[f'wall{i}{j}'].config(command = lambda arg = Horizental_wall[f'wall{i}{j}'] , x = j , y = i , typew = 'h' : Maze.creat_wall(arg,x,y,typew))   
    for i in range(9) :
        for j in range(10) :
            Vertical_wall[f'wall{i}{j}'].config(command = lambda arg = Vertical_wall[f'wall{i}{j}'] , x = j , y = i , typew = 'v': Maze.creat_wall(arg,x,y,typew))
    Square = dict()
    for i in range(9) :
        for j in range(9) :
            Square[f'sq{i}{j}'] = tk.Label(bc , bg = "white" , bd = 0)
            Square[f'sq{i}{j}'].place(height = 50 , width = 50 , y = (i+1)*10 + 50*i + 5 , x = (j+1) * 10 + j*50 + 5)
            
    def creat_wall(arg,x,y,typew) :
        if Maze.start == False :
            if arg['bg'] == "#a6d0de" :
                arg['bg'] = "#59696e" #gray
            elif arg['bg'] == "#59696e" :
                arg['bg'] = "#a6d0de"
    def mapping_wall() :
        for i in range(9) :
            for j in range(9) :
                if Maze.Horizental_wall[f'wall{i}{j}']['bg'] != '#a6d0de'  : #light blue 
                    Maze.block[i][j]['u'] = True 
                else :
                    Maze.block[i][j]['u'] = False
                if Maze.Horizental_wall[f'wall{i+1}{j}']['bg'] != '#a6d0de' :
                    Maze.block[i][j]['d'] = True
                else :
                    Maze.block[i][j]['d'] = False
                if Maze.Vertical_wall[f'wall{i}{j}']['bg'] != '#a6d0de' :
                    Maze.block[i][j]['l'] = True
                else :
                    Maze.block[i][j]['l'] = False
                if Maze.Vertical_wall[f'wall{i}{j+1}']['bg'] != '#a6d0de' :
                    Maze.block[i][j]['r'] = True
                else :
                    Maze.block[i][j]['r'] = False
    def initializing() :
        #Robot.go_up()
        Maze.start = True
        
        Maze.mapping_wall()
        start.place_forget()
        go.place(height=40 , width=80 , x = 240 , y = 560)
        Maze.block[Robot.y][Robot.x]['seen'] = True
        Maze.Square[f'sq{Robot.y}{Robot.x}']['bg'] = "#FEFFE4"
        
        
class Robot :
    x = 0
    y = 2
    step = 1
    x_home = 0
    y_home = 2
    x_goal = int()
    y_goal = int()
    lbl_robot = tk.Label(bc , bg = "#e84343")
    lbl_robot.place(height=40 , width=40 , x = 20 , y = 140)
    wall = {
        'u' : False ,
        'r' : False ,
        'l' : False ,
        'd' : False
    }
    should_back = False
    def detect_wall() :
        Robot.wall['u'] = False
        Robot.wall['r'] = False
        Robot.wall['l'] = False
        Robot.wall['d'] = False
        if Maze.Horizental_wall[f'wall{Robot.y}{Robot.x}']['bg'] != "#a6d0de" : #up
            Robot.wall['u'] = True
        if Maze.Horizental_wall[f'wall{Robot.y+1}{Robot.x}']['bg'] != "#a6d0de" : #down
            Robot.wall['d'] = True
        if Maze.Vertical_wall[f'wall{Robot.y}{Robot.x}']['bg'] != "#a6d0de" : #left
            Robot.wall['l'] = True
        if Maze.Vertical_wall[f'wall{Robot.y}{Robot.x+1}']['bg'] != "#a6d0de" : #right
            Robot.wall['r'] = True
    
    
    
    def go_up():
        Robot.y -= 1
        Robot.step += 1
        Maze.block[Robot.y][Robot.x]['seen'] = True
        if Maze.Square[f'sq{Robot.y}{Robot.x}']['bg'] == "white" :
            Maze.Square[f'sq{Robot.y}{Robot.x}']['bg'] = "#F8E4E0"
        Robot.lbl_robot.place(x= (Robot.x+1)*10 + Robot.x*50 + 10 , y=(Robot.y+1)*10 + Robot.y*50 + 10)
    def go_down():
        Robot.y += 1
        Robot.step += 1
        Maze.block[Robot.y][Robot.x]['seen'] = True
        if Maze.Square[f'sq{Robot.y}{Robot.x}']['bg'] == "white" :
            Maze.Square[f'sq{Robot.y}{Robot.x}']['bg'] = "#F8E4E0"
        Robot.lbl_robot.place(x= (Robot.x+1)*10 + Robot.x*50 + 10 , y=(Robot.y+1)*10 + Robot.y*50 + 10)
    def go_right() :
        Robot.x += 1
        Robot.step += 1
        Maze.block[Robot.y][Robot.x]['seen'] = True
        if Maze.Square[f'sq{Robot.y}{Robot.x}']['bg'] == "white" :
            Maze.Square[f'sq{Robot.y}{Robot.x}']['bg'] = "#F8E4E0"
        Robot.lbl_robot.place(x= (Robot.x+1)*10 + Robot.x*50 + 10 , y=(Robot.y+1)*10 + Robot.y*50 + 10)
    def go_left() :
        Robot.x -= 1
        Robot.step += 1
        Maze.block[Robot.y][Robot.x]['seen'] = True
        if Maze.Square[f'sq{Robot.y}{Robot.x}']['bg'] == "white" :
            Maze.Square[f'sq{Robot.y}{Robot.x}']['bg'] = "#F8E4E0"
        Robot.lbl_robot.place(x= (Robot.x+1)*10 + Robot.x*50 + 10 , y=(Robot.y+1)*10 + Robot.y*50 + 10)
    
    
    def is_several_nod(next) :
        Robot.detect_wall()
        counter = 0
        if next == 'u' :
            if Robot.wall['r'] == False :
                if Maze.block[Robot.y][Robot.x+1]['seen'] == False :
                    counter += 1
            if Robot.wall['l'] == False :
                if Maze.block[Robot.y][Robot.x-1]['seen'] == False :
                    counter += 1
            if Robot.wall['d'] == False :
                if Maze.block[Robot.y+1][Robot.x]['seen'] == False :
                    counter += 1
            if counter > 0 :
                return True
        elif next == 'r' :
            if Robot.wall['u'] == False :
                if Maze.block[Robot.y-1][Robot.x]['seen'] == False :
                    counter += 1
            if Robot.wall['l'] == False :
                if Maze.block[Robot.y][Robot.x-1]['seen'] == False :
                    counter += 1
            if Robot.wall['d'] == False :
                if Maze.block[Robot.y+1][Robot.x]['seen'] == False :
                    counter += 1
            if counter > 0 : 
                return True
        elif next == 'l' :
            if Robot.wall['u'] == False :
                if Maze.block[Robot.y-1][Robot.x]['seen'] == False :
                    counter += 1
            if Robot.wall['r'] == False :
                if Maze.block[Robot.y][Robot.x+1]['seen'] == False :
                    counter += 1
            if Robot.wall['d'] == False :
                if Maze.block[Robot.y+1][Robot.x]['seen'] == False :
                    counter += 1
            if counter > 0 :
                return True
        elif next == 'd' :
            if Robot.wall['u'] == False :
                if Maze.block[Robot.y-1][Robot.x]['seen'] == False :
                    counter += 1
            if Robot.wall['r'] == False :
                if Maze.block[Robot.y][Robot.x+1]['seen'] == False :
                    counter += 1
            if Robot.wall['l'] == False :
                if Maze.block[Robot.y][Robot.x-1]['seen'] == False :
                    counter += 1
            if counter > 0 :
                return True

        return False
    def reset_vblock() :
        for i in range(9) :
            for j in range(9) :
                Maze.block[i][j]['v'] = -1
            
    
    def clear_several() :
        #messagebox.showinfo("p" , "clear several")
        for i in range(9) :
            for j in range(9) :
                counter = 0
                wall = 0
                if Maze.block[i][j]['s_id'] != -1 :
                    if Maze.block[i][j]['u'] == False :
                        wall += 1
                        if Maze.block[i-1][j]['seen'] == True :
                            counter += 1
                    if Maze.block[i][j]['r'] == False :
                        wall += 1
                        if Maze.block[i][j+1]['seen'] == True :
                            counter += 1
                    if Maze.block[i][j]['l'] == False :
                        wall += 1
                        if Maze.block[i][j-1]['seen'] == True :
                            counter += 1
                    if Maze.block[i][j]['d'] == False :
                        wall += 1
                        if Maze.block[i+1][j]['seen'] == True :
                            counter += 1
                #if Maze.block[i][j]['s_id'] != -1 :
                    #messagebox.showinfo("info sev" , f'{i}{j} : wall :{wall} , counter :{counter}')
                if wall == counter :
                    Maze.block[i][j]['s_id'] = -1
    def reset_can_check() :
        for i in range(9) :
            for j in range(9) :
                Maze.block[i][j]['can_check'] = -1
    def find_goal() :
        #messagebox.showinfo("find Goal")
        back = True
        Robot.reset_can_check()
        for i in range(9):
            for j in range(9) :
                if Maze.block[i][j]['seen'] == False :
                    Maze.block[i][j]['can_check'] = 0
                    step = 0
                    while True :
                        f = False
                        for ii in range(9) :
                            for jj in range(9) :
                                
                                if Maze.block[ii][jj]['can_check'] == step :
                                        #messagebox.showinfo("v" , f'{i} {j} : {step}')
                                        if Maze.block[ii][jj]['u'] == False:
                                            if Maze.block[ii-1][jj]['can_check'] == -1 :
                                                #messagebox.showinfo("v" , f'u {i-1} {j} : {step + 1}')
                                                Maze.block[ii-1][jj]['can_check'] = step + 1
                                                f = True
                                        if Maze.block[ii][jj]['r'] == False  :
                                            if Maze.block[ii][jj+1]['can_check'] == -1 :
                                                #messagebox.showinfo("v" , f'r {i} {j+1} : {step + 1}')
                                                Maze.block[ii][jj+1]['can_check'] = step + 1
                                                f = True
                                        if Maze.block[ii][jj]['l'] == False :
                                            if Maze.block[ii][jj-1]['can_check'] == -1 :
                                                #messagebox.showinfo("v" , f'l {i} {j-1} : {step + 1}')
                                                Maze.block[ii][jj-1]['can_check'] = step + 1
                                                f = True
                                        if Maze.block[ii][jj]['d'] == False :
                                            if Maze.block[ii+1][jj]['can_check'] == -1 :
                                                #messagebox.showinfo("v" , f' d {i+1} {j} : {step + 1}')
                                                Maze.block[ii+1][jj]['can_check'] = step + 1
                                                f = True
                        step += 1
                        if f == False :
                            break
                    if Maze.block[Robot.y][Robot.x]['can_check'] != -1 :
                        back = False
        if back == True :
            if Robot.should_back == False :
                messagebox.showinfo("" , "^_^ Back To Home.")
            Robot.x_goal = Robot.x_home
            Robot.y_goal = Robot.y_home
            Robot.should_back = True
        else :
            Robot.clear_several()
            c = 0
            for i in range(9) :
                for j in range(9) :
                    if Maze.block[i][j]['s_id'] > c :
                        Robot.x_goal = j
                        Robot.y_goal = i
                        c = Maze.block[i][j]['s_id']
                        #messagebox.showinfo("s_id" , f'{i} {j} : {c}')
        #messagebox.showinfo("end find Goal" , f'{Robot.y_goal} {Robot.x_goal}')
    def up_search() :
        Robot.detect_wall()
        if Robot.wall['u'] == False :
            if Maze.block[Robot.y-1][Robot.x]['seen'] == False :
                if Robot.is_several_nod('u') :
                    #messagebox.showinfo(f'{Robot.y} {Robot.x} : {Robot.step}',"several nod u")
                    Maze.block[Robot.y][Robot.x]['s_id'] = Robot.step
                Robot.go_up()
            else :
                Robot.right_search()
        else :
            Robot.right_search()
    def right_search() :
        Robot.detect_wall()
        if Robot.wall['r'] == False :
            if Maze.block[Robot.y][Robot.x+1]['seen'] == False :
                if Robot.is_several_nod('r') :
                    #messagebox.showinfo(f'{Robot.y} {Robot.x} : {Robot.step}',"several nod r")
                    Maze.block[Robot.y][Robot.x]['s_id'] = Robot.step
                Robot.go_right()
            else :
                Robot.left_search()
        else :
            Robot.left_search()
    def left_search() :
        Robot.detect_wall()
        if Robot.wall['l'] == False :
            if Maze.block[Robot.y][Robot.x-1]['seen'] == False :
                if Robot.is_several_nod('l') :
                    #messagebox.showinfo(f'{Robot.y} {Robot.x} : {Robot.step}',"several nod l")
                    Maze.block[Robot.y][Robot.x]['s_id'] = Robot.step
                Robot.go_left()
            else :
                Robot.down_search()
        else :
            Robot.down_search()
    def down_search() :
        Robot.detect_wall()
        if Robot.wall['d'] == False :
            if Maze.block[Robot.y+1][Robot.x]['seen'] == False :
                if Robot.is_several_nod('d') :
                    #messagebox.showinfo(f'{Robot.y} {Robot.x} : {Robot.step}' , "several nod d")
                    Maze.block[Robot.y][Robot.x]['s_id'] = Robot.step
                Robot.go_down()
            else :
                Robot.find_goal()
                Robot.go_to_goal()
        else :
            Robot.find_goal()
            Robot.go_to_goal()
            #u = Robot.wall['u']
            #r = Robot.wall['r']
            #l = Robot.wall['l']
            #d = Robot.wall['d']
            #messagebox.showinfo("wall",f'u:{u} r:{r} l:{l} d:{d}')
            #messagebox.showinfo("error" , "saerch field")
    def go_to_goal() :
        #messagebox.showinfo("go goal")
        
        if Robot.x == Robot.x_home and Robot.y == Robot.y_home and Robot.x_goal == Robot.x_home and Robot.y_goal == Robot.y_home and Robot.should_back == True:
            messagebox.showinfo("End Searching", "I'm Home :)")
        else :
            if Robot.x == Robot.x_goal and Robot.y == Robot.y_goal :
                messagebox.showinfo("pass :/")
                pass
            else :
                #messagebox.showinfo("go goal" , "if main")
                step = 0
                Robot.reset_vblock()
                Maze.block[Robot.y][Robot.x]['v'] = 0
                Maze.mapping_wall()
                while True :
                    f = False
                    for i in range(9) :
                        for j in range(9) :
                            if Maze.block[i][j]['v'] == step :
                                #messagebox.showinfo("v val" , f'{i}{j} : {step}')
                                #u = Maze.block[i][j]['u']
                                #r = Maze.block[i][j]['r']
                                #l = Maze.block[i][j]['l']
                                #d = Maze.block[i][j]['d']
                                #messagebox.showinfo("wall" , f'{i}{j} [] u:{u} r:{r} l:{l} d:{d}')
                                if Maze.block[i][j]['u'] == False :
                                    if Maze.block[i-1][j]['v'] == -1 :
                                        Maze.block[i-1][j]['v'] = step + 1
                                        #messagebox.showinfo("v val" , f'{i-1}{j} : {step+1}')
                                        f = True
                                if Maze.block[i][j]['r'] == False :
                                    if Maze.block[i][j+1]['v'] == -1 :
                                        Maze.block[i][j+1]['v'] = step + 1
                                        #messagebox.showinfo("v val" , f'{i}{j+1} : {step+1}')
                                        f = True
                                if Maze.block[i][j]['l'] == False :
                                    if Maze.block[i][j-1]['v'] == -1 :
                                        Maze.block[i][j-1]['v'] = step + 1
                                        #messagebox.showinfo("v val" , f'{i}{j-1} : {step+1}')
                                        f = True
                                if Maze.block[i][j]['d'] == False :
                                    if Maze.block[i+1][j]['v'] == -1 :
                                        Maze.block[i+1][j]['v'] = step + 1
                                        #messagebox.showinfo("v val" , f'{i+1}{j} : {step+1}')
                                        
                                        f = True
                    step += 1
                    if Maze.block[Robot.y_goal][Robot.x_goal]['v'] != -1 :
                        break
                x_next = Robot.x_goal
                y_next = Robot.y_goal
                c = Maze.block[y_next][x_next]['v']
                #messagebox.showinfo("first c value" , c)

                
                
                
                while True :
                #messagebox.showinfo("wall" , f'{y_next}{x_next} [] u:{u} r:{r} l:{l} d:{d}')
                    if c == 1 :
                        break
                    if Maze.block[y_next][x_next]['u'] == False :
                        if Maze.block[y_next-1][x_next]['v'] == c - 1 :
                            y_next -= 1
                            
                            #messagebox.showinfo("c - 1" ,f'U:{y_next}{x_next}:{c-1}' )
                            c -= 1
                        else :
                            if Maze.block[y_next][x_next]['r'] == False :
                                if Maze.block[y_next][x_next+1]['v'] == c - 1 :
                                    x_next += 1
                                    
                                    #messagebox.showinfo("c - 1" ,f'R:{y_next}{x_next}:{c-1}' )
                                    c -= 1
                                else :
                                    if Maze.block[y_next][x_next]['l'] == False :
                                        if Maze.block[y_next][x_next-1]['v'] == c - 1 :
                                            x_next -= 1
                                            
                                            #messagebox.showinfo("c - 1" ,f'L:{y_next}{x_next}:{c-1}' )
                                            c -= 1
                                        else :
                                            if Maze.block[y_next][x_next]['d'] == False :
                                                if Maze.block[y_next+1][x_next]['v'] == c - 1 :
                                                    y_next += 1
                                                    #messagebox.showinfo("c - 1" ,f'D:{y_next}{x_next}:{c-1}' )  
                                                    c -= 1
                                            
                                                        
                                    elif Maze.block[y_next][x_next]['d'] == False :
                                        if Maze.block[y_next+1][x_next]['v'] == c - 1 :
                                            y_next += 1
                                            #messagebox.showinfo("c - 1" ,f'D:{y_next}{x_next}:{c-1}' )  
                                            c -= 1
                                    
                                        
                            elif Maze.block[y_next][x_next]['l'] == False :
                                if Maze.block[y_next][x_next-1]['v'] == c - 1 :
                                    x_next -= 1
                                    
                                    #messagebox.showinfo("c - 1" ,f'L:{y_next}{x_next}:{c-1}' )
                                    c -= 1
                                else :
                                    if Maze.block[y_next][x_next]['d'] == False :
                                        if Maze.block[y_next+1][x_next]['v'] == c - 1 :
                                            y_next += 1
                                            #messagebox.showinfo("c - 1" ,f'D:{y_next}{x_next}:{c-1}' )  
                                            c -= 1
                                    
                                                
                            elif Maze.block[y_next][x_next]['d'] == False :
                                if Maze.block[y_next+1][x_next]['v'] == c - 1 :
                                    y_next += 1
                                    #messagebox.showinfo("c - 1" ,f'D:{y_next}{x_next}:{c-1}' )  
                                    c -= 1 
                            
                    elif Maze.block[y_next][x_next]['r'] == False :
                        if Maze.block[y_next][x_next+1]['v'] == c - 1 :
                            x_next += 1
                            
                            #messagebox.showinfo("c - 1" ,f'R:{y_next}{x_next}:{c-1}' )
                            c -= 1
                        else :
                            if Maze.block[y_next][x_next]['l'] == False :
                                if Maze.block[y_next][x_next-1]['v'] == c - 1 :
                                    x_next -= 1
                                    
                                    #messagebox.showinfo("c - 1" ,f'L:{y_next}{x_next}:{c-1}' )
                                    c -= 1
                                else :
                                    if Maze.block[y_next][x_next]['d'] == False :
                                        if Maze.block[y_next+1][x_next]['v'] == c - 1 :
                                            y_next += 1
                                            #messagebox.showinfo("c - 1" ,f'D:{y_next}{x_next}:{c-1}' )  
                                            c -= 1
                                    
                                                
                            elif Maze.block[y_next][x_next]['d'] == False :
                                if Maze.block[y_next+1][x_next]['v'] == c - 1 :
                                    y_next += 1
                                    #messagebox.showinfo("c - 1" ,f'D:{y_next}{x_next}:{c-1}' )  
                                    c -= 1
                            
                                
                    elif Maze.block[y_next][x_next]['l'] == False :
                        if Maze.block[y_next][x_next-1]['v'] == c - 1 :
                            x_next -= 1
                            
                            #messagebox.showinfo("c - 1" ,f'L:{y_next}{x_next}:{c-1}' )
                            c -= 1
                        else :
                            if Maze.block[y_next][x_next]['d'] == False :
                                if Maze.block[y_next+1][x_next]['v'] == c - 1 :
                                    y_next += 1
                                    #messagebox.showinfo("c - 1" ,f'D:{y_next}{x_next}:{c-1}' )  
                                    c -= 1
                            
                                        
                    elif Maze.block[y_next][x_next]['d'] == False :
                        if Maze.block[y_next+1][x_next]['v'] == c - 1 :
                            y_next += 1
                            #messagebox.showinfo("c - 1" ,f'D:{y_next}{x_next}:{c-1}' )  
                            c -= 1  
                        
               
                #messagebox.showinfo("next" , f'{y_next} {x_next}')
                if y_next - Robot.y > 0 :
                    Robot.go_down()
                elif y_next - Robot.y < 0 :
                    Robot.go_up()
                
                if x_next - Robot.x > 0 :
                    Robot.go_right()
                elif x_next - Robot.x < 0 :
                    Robot.go_left()
    
    def algorithm() :
        Robot.up_search()
        
        
#########################################    main


start = tk.Button(bc , text="Start" , background="#0099ff" , command=lambda : Maze.initializing())
start.place(height=40 , width=80 , x = 240 , y = 560)

go = tk.Button(bc , text="Go!" , background="#9ff792" , command= lambda : Robot.algorithm())



bc.mainloop()