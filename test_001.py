from tkinter import *
import random
import copy
class Game2048():
    result = [[0,0,0,0] for i in range(4)]
    color = {None: "#CCC0B3",2: "#EEE4DA",4: "#EDE0C8",8: "#F2B179",
        16: "#F59563",32: "#F67C5F",64: "#F65E3B",128: "#EDCF72",
        256: "#EDCF72",512: "#EDCF72",1024: "#EDCF72",2048: "#EDCF72",
        4096: "#EDCF72",8192: "#EDCF72",16384: "#EDCF72",32768: "#EDCF72"}
    def __init__(self):
        self.root = Tk()
        self.root.title('2048')
        self.root.geometry('600x700+350+50')
        self.result = [[0,0,0,0] for i in range(4)]
        self.arg()
        self.btn = Button(self.root,text='开始',font=('黑体',20),command=lambda:self.action('开始')).place(x=0,y=600,width=100,height=100)
        self.btn0 = Button(self.root,text='退出',font=('黑体',20),command=lambda:self.action('退出')).place(x=500,y=600,width=100,height=100)
        self.btn1 = Button(self.root,text='上',font=('黑体',20),command=lambda:self.action('上')).place(x=100,y=600,width=100,height=100)
        self.btn2 = Button(self.root,text='下',font=('黑体',20),command=lambda:self.action('下')).place(x=200,y=600,width=100,height=100)
        self.btn3 = Button(self.root,text='左',font=('黑体',20),command=lambda:self.action('左')).place(x=300,y=600,width=100,height=100)
        self.btn4 = Button(self.root,text='右',font=('黑体',20),command=lambda:self.action('右')).place(x=400,y=600,width=100,height=100)
    def arg(self,data=result):
        for i in range(16):
            if i<4:
                self.text = data[0][i] if data[0][i] !=0 else None
                self.label1 = Label(self.root,text=self.text,font=('黑体',20),bg=self.color[self.text],relief = RAISED).place(x=i*150,y=0,width=150,height=150)
            elif i<8:
                self.text = data[1][i-4] if data[1][i-4] !=0 else None
                self.label1 = Label(self.root,text=self.text,font=('黑体',20),bg=self.color[self.text],relief = RAISED).place(x=(i-4)*150,y=150,width=150,height=150)
            elif i<12:
                self.text = data[2][i-8] if data[2][i-8] !=0 else None
                self.label1 = Label(self.root,text=self.text,font=('黑体',20),bg=self.color[self.text],relief = RAISED).place(x=(i-8)*150,y=300,width=150,height=150)
            else :
                self.text = data[3][i-12] if data[3][i-12] !=0 else None
                self.label1 = Label(self.root,text=self.text,font=('黑体',20),bg=self.color[self.text],relief = RAISED).place(x=(i-12)*150,y=450,width=150,height=150)
    def action(self,command):
        self.list = copy.deepcopy(self.result)
        self.sum = 0
        for i in range(4):
            self.sum += sum(self.list[i])
        if command == '开始':
            for i in range(len(self.list)):
                for j in range(len(self.list[i])):
                    self.list[i][j] = 0
            i,j = random.sample(range(0,4),2)
            self.list[i][j] = 2
            self.result = self.list
            self.arg(self.result)
        elif command == '退出':
            self.root.destroy()
        elif command == '左' and self.sum!=0:
            self.co = [[] for i in range(4)]
            for i in range(4):
                for j in range(4):
                    if self.list[i][j] != 0:
                        self.co[i].append(self.list[i][j])
            for i in range(len(self.co)):
                if len(self.co[i]) == 1:
                    self.co[i] = [self.co[i][0],0,0,0]
                elif len(self.co[i]) == 0:
                    self.co[i] = [0,0,0,0]
                else:        
                    for j in range(len(self.co[i])-1):
                        if self.co[i][j+1] == self.co[i][j]:
                            self.co[i][j] *=2
                            self.co[i][j+1] = 0
                    while 0 in self.co[i]:
                        self.co[i].remove(0)
                    while len(self.co[i]) < 4:
                        self.co[i].append(0)
            self.list = self.co
            if self.result != self.list:
                rowcol = list()
                for i in range(4):
                    for j in range(4):
                        if self.list[i][j] == 0:
                            rowcol.append([i,j])                    
                zuobiao = random.choice(rowcol)
                i,j = zuobiao[0],zuobiao[1]
                self.list[i][j] = 2
                self.result = self.list
            self.arg(self.result)
        elif command == '右' and self.sum!=0:
            self.co = [[] for i in range(4)]
            for i in range(4):
                for j in range(4):
                    if self.list[i][j] != 0:
                        self.co[i].append(self.list[i][j])
            for i in range(len(self.co)):
                if len(self.co[i]) == 1:
                    self.co[i] = [0,0,0,self.co[i][0]]
                elif len(self.co[i]) == 0:
                    self.co[i] = [0,0,0,0]
                else:        
                    for j in range(len(self.co[i])-1):
                        if self.co[i][-(j+1)] == self.co[i][-(j+2)]:
                            self.co[i][-(j+1)] *= 2
                            self.co[i][-(j+2)] = 0
                    while 0 in self.co[i]:
                        self.co[i].remove(0)
                    while len(self.co[i]) < 4:
                        self.co[i].insert(0,0)
            self.list = self.co
            if self.result != self.list:
                rowcol = list()
                for i in range(4):
                    for j in range(4):
                        if self.list[i][j] == 0:
                            rowcol.append([i,j])                    
                zuobiao = random.choice(rowcol)
                i,j = zuobiao[0],zuobiao[1]
                self.list[i][j] = 2
                self.result = self.list
            self.arg(self.result)
        elif command == '上' and self.sum!=0:
            self.co = [[] for i in range(4)]
            for i in range(4):
                for j in range(4):
                    if self.list[j][i] != 0:
                        self.co[i].append(self.list[j][i])    
            for i in range(len(self.co)):
                if len(self.co[i]) == 1:
                    self.co[i] = [self.co[i][0],0,0,0]
                elif len(self.co[i]) == 0:
                    self.co[i] = [0,0,0,0]
                else:        
                    for j in range(len(self.co[i])-1):
                        if self.co[i][j+1] == self.co[i][j]:
                            self.co[i][j] *= 2
                            self.co[i][j+1] = 0
                    while 0 in self.co[i]:
                        self.co[i].remove(0)
                    while len(self.co[i]) < 4:
                        self.co[i].append(0)
            for i in range(4):
                for j in range(4):
                    self.list[j][i] = self.co[i][j]
            if self.result != self.list:
                rowcol = list()
                for i in range(4):
                    for j in range(4):
                        if self.list[i][j] == 0:
                            rowcol.append([i,j])                    
                zuobiao = random.choice(rowcol)
                i,j = zuobiao[0],zuobiao[1]
                self.list[i][j] = 2
                self.result = self.list
            self.arg(self.result)
        elif command == '下' and self.sum!=0:
            self.co = [[] for i in range(4)]
            for i in range(4):
                for j in range(4):
                    if self.list[-(j+1)][i] != 0:
                        self.co[i].append(self.list[-(j+1)][i])   
            for i in range(len(self.co)):
                if len(self.co[i]) == 1:
                    self.co[i] = [self.co[i][0],0,0,0]
                elif len(self.co[i]) == 0:
                    self.co[i] = [0,0,0,0]
                else:        
                    for j in range(len(self.co[i])-1):
                        if self.co[i][j+1] == self.co[i][j]:
                            self.co[i][j] *= 2
                            self.co[i][j+1] = 0
                    while 0 in self.co[i]:
                        self.co[i].remove(0)
                    while len(self.co[i]) < 4:
                        self.co[i].append(0)
            for i in range(4):
                for j in range(4):
                    self.list[-(j+1)][i] = self.co[i][j]
            if self.result != self.list:
                rowcol = list()
                for i in range(4):
                    for j in range(4):
                        if self.list[i][j] == 0:
                            rowcol.append([i,j])                    
                zuobiao = random.choice(rowcol)
                i,j = zuobiao[0],zuobiao[1]
                self.list[i][j] = 2
                self.result = self.list
            self.arg(self.result)
if __name__ == '__main__':
    game = Game2048()
    game.root.mainloop()