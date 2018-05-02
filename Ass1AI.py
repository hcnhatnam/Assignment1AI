import bloxorz as blo
import time
import copy
import sys
start_time = time.time()

class State:
    def __init__(self,x1,y1,x2,y2,oriented,listVisited,matrixMap,parent):
        self.x1=x1
        self.y1=y1
        self.x2=x2      #x2<0 cot dung
        self.y2=y2
        self.oriented=oriented  #0:Vertical,1:song song truc x(|); 2:song song Y(--);3:chia lam 2
        self.listVisited=listVisited
        self.matrixMap=matrixMap
        self.parent=parent
#Đích -1,
class specialSquare:
    def __init__(self,xLocate,yLocate,Open:list,attribute,constance=0):#attribute=2 X;attribute=3 O;attribute=4 Slipt;constance: (0 normal,1 Alway Open, 2 Close)
        self.xLocate=xLocate
        self.yLocate=yLocate
        self.Open=Open
        self.attribute=attribute
        self.constance=constance


class Bloxorz:
    def __init__(self,mapMatrix:list,specialSquareList:list,startState:State,goalState:State):#Matrix sinh tu(1,1)
        self.mapMatrix=mapMatrix
        self.startState=startState
        self.goalState=goalState
        self.specialSquareList=specialSquareList


    def SolveDFS(self):
        stack=[self.startState]
        while stack.__len__()!=0:
            currentState=stack.pop()
            #time.sleep(1)
            #blo.level_array=currentState.matrixMap
            #blo.drawBlo(currentState.x1,currentState.y1,currentState.oriented,currentState.x2,currentState.y2)
            if self.isGoal(currentState):
                printResult(currentState)
                sys.exit()
            if currentState.oriented==3:
                stack += self.successorSingleBlockStep1(currentState,currentState.listVisited,currentState.matrixMap)
            elif not self.isVisted(currentState, currentState.listVisited):
                stack += self.successor(currentState,currentState.listVisited,currentState.matrixMap)
            currentState.listVisited.append(currentState)
        return None


    def successorSingleBlockStep1(self,currentState:State,listVisited,matrixMap):
        listSuccessor=[]
        lenght=0
        stateRight=self.checkCombine(State(currentState.x1,currentState.y1+1,currentState.x2,currentState.y2,3,currentState.listVisited,currentState.matrixMap,currentState))
        listSuccessor+=self.addListSuccessor(listVisited,stateRight)
        if(listSuccessor.__len__()>lenght):
            lenght+=1
            listVisited+=self.successorSingleBlockStep2(stateRight,listVisited,matrixMap)

        stateLeft=self.checkCombine(State(currentState.x1,currentState.y1-1,currentState.x2,currentState.y2,3,currentState.listVisited,currentState.matrixMap,currentState))
        listSuccessor+=self.addListSuccessor(listVisited,stateLeft)
        if(listSuccessor.__len__())>lenght):
            lenght+=1
            listVisited+=self.successorSingleBlockStep2(stateLeft,listVisited,matrixMap)


        stateTop=self.checkCombine(State(currentState.x1-1,currentState.y1,currentState.x2,currentState.y2,3,currentState.listVisited,currentState.matrixMap,currentState))
        listSuccessor+=self.addListSuccessor(listVisited,stateTop)
        if(listSuccessor.__len__()>lenght):
            lenght+=1
            listVisited+=self.successorSingleBlockStep2(stateTop,listVisited,matrixMap)


        stateDown=self.checkCombine(State(currentState.x1+1,currentState.y1,currentState.x2,currentState.y2,3,currentState.listVisited,currentState.matrixMap,currentState))
        listSuccessor+=self.addListSuccessor(listVisited,stateDown)
        if(listSuccessor.__len__()>lenght):
            lenght+=1
            listVisited+=self.successorSingleBlockStep2(stateDown,listVisited,matrixMap)
        return listSuccessor


    def successorSingleBlockStep2(self,currentState:State,listVisited,matrixMap):
        stack=[currentState]
        allStateVisited=[currentState]
        while stack.__len__()!=0:
            currentState=stack.pop()#pop(0) BFS search
            #time.sleep(1)
            #blo.level_array=currentState.matrixMap
            #blo.drawBlo(currentState.x1,currentState.y1,currentState.oriented,currentState.x2,currentState.y2)
            if (currentState.x1,currentState.y1)==(3,1) or (currentState.x2,currentState.y2)==(3,1) and currentState.oriented == 3:
                print("ok")
            print("("+str(currentState.x1)+","+str(currentState.y1)+")"+"|"+"("+str(currentState.x2)+","+str(currentState.y2)+")"+"|"+str(currentState.oriented))
            if currentState.x1==3 and currentState.y1==13 and currentState.x2==3 and currentState.y2==14:
                a=0
            if self.isGoal(currentState):
                printResult(currentState)
                sys.exit()
            if not self.isVisted(currentState,currentState.listVisited):
                if currentState.oriented!=3:
                    successor= self.successor(currentState,currentState.listVisited,currentState.matrixMap)
                    stack+=successor
                    allStateVisited+=successor
                elif currentState.oriented==3:
                    successor=self.successorSingleBlockX2Y2(currentState,currentState.listVisited,currentState.matrixMap)
                    stack+=successor
                    allStateVisited+=successor
            currentState.listVisited.append(currentState)
        return allStateVisited
    def successorSingleBlockX2Y2(self,currentState:State,listVisited,matrixMap):
        listSuccessor=[]
        stateRight=self.checkCombine(State(currentState.x1,currentState.y1,currentState.x2,currentState.y2+1,currentState.oriented,listVisited,matrixMap,currentState))
        listSuccessor+=self.addListSuccessor(listVisited,stateRight)

        stateLeft=self.checkCombine(State(currentState.x1,currentState.y1,currentState.x2,currentState.y2-1,currentState.oriented,listVisited,matrixMap,currentState))
        listSuccessor+=self.addListSuccessor(listVisited,stateLeft)

        stateTop=self.checkCombine(State(currentState.x1,currentState.y1,currentState.x2-1,currentState.y2,currentState.oriented,listVisited,matrixMap,currentState))
        listSuccessor+=self.addListSuccessor(listVisited,stateTop)

        stateDown=self.checkCombine(State(currentState.x1,currentState.y1,currentState.x2+1,currentState.y2,currentState.oriented,listVisited,matrixMap,currentState))
        listSuccessor+=self.addListSuccessor(listVisited,stateDown)

        return listSuccessor

    def checkCombine(self,newState:State):
        if newState.x1==newState.x2:
            if newState.y1-newState.y2==-1:
                return State(newState.x1,newState.y1,newState.x2,newState.y2,2,newState.listVisited,newState.matrixMap,newState.parent)
            if newState.y1-newState.y2==1:
                return State(newState.x2,newState.y2,newState.x1,newState.y1,2,newState.listVisited,newState.matrixMap,newState.parent)
        if newState.y1==newState.y2:
            if newState.x1-newState.x2==-1:
                return State(newState.x1,newState.y1,newState.x2,newState.y2,1,newState.listVisited,newState.matrixMap,newState.parent)
            if newState.x1-newState.x2==1:
                return State(newState.x2,newState.y2,newState.x1,newState.y1,1,newState.listVisited,newState.matrixMap,newState.parent)
        return newState



    def SolveBFS(self):
        stack=[self.startState]
        while stack.__len__()!=0:
            currentState=stack.pop(0)
            if self.isGoal(currentState):
                return currentState
            if not self.isVisted(currentState, currentState.listVisited):
                if currentState.oriented != 3:
                    stack += self.successor(currentState,currentState.listVisited,currentState.matrixMap)
                elif currentState.oriented == 3:
                    stack += self.successorSingleBlockStep1(currentState,currentState.listVisited,currentState.matrixMap)
            currentState.listVisited.append(currentState)
        return None

    def isGoal(self,currentState):
        return self.goalState.x1==currentState.x1 and self.goalState.y1==currentState.y1 and currentState.oriented==0

    def isVisted(self,currentState:State,listVisited:list):
        for i in listVisited:
            if i.x1==currentState.x1 and i.y1==currentState.y1 and  i.x2==currentState.x2 and i.y2==currentState.y2 and i.oriented==currentState.oriented and i.matrixMap==currentState.matrixMap:
                return True
            if  currentState.oriented==3 and i.x1==currentState.x2 and i.y1==currentState.y2 and i.x2==currentState.x1 and i.y2==currentState.y1  and i.matrixMap==currentState.matrixMap:
                return True
        return False

    def successor(self,currentState:State,listVisited,matrixMap):
        listSuccessor=[]
        if  currentState.oriented==0:# Column is Vertical
            listSuccessor+=self.addListSuccessor(listVisited,State(currentState.x1,currentState.y1+1,currentState.x1,currentState.y1+2,2,listVisited,matrixMap,currentState))#stateRight
            listSuccessor+=self.addListSuccessor(listVisited,State(currentState.x1,currentState.y1-2,currentState.x1,currentState.y1-1,2,listVisited,matrixMap,currentState))#stateLeft
            listSuccessor+=self.addListSuccessor(listVisited,State(currentState.x1-2,currentState.y1,currentState.x1-1,currentState.y1,1,listVisited,matrixMap,currentState))#stateTop
            listSuccessor+=self.addListSuccessor(listVisited,State(currentState.x1+1,currentState.y1,currentState.x1+2,currentState.y1,1,listVisited,matrixMap,currentState))#stateDown

        else:
            if currentState.oriented==2: #2:song song Y(--);
                listSuccessor+=self.addListSuccessor(listVisited,State(currentState.x2,currentState.y1+2,-1,-1,0,listVisited,matrixMap,currentState))#stateRight
                listSuccessor+=self.addListSuccessor(listVisited,State(currentState.x1,currentState.y1-1,-1,-1,0,listVisited,matrixMap,currentState))#stateLeft
                listSuccessor+=self.addListSuccessor(listVisited,State(currentState.x1-1,currentState.y1,currentState.x2-1,currentState.y2,2,listVisited,matrixMap,currentState))#stateTop
                listSuccessor+=self.addListSuccessor(listVisited,State(currentState.x1+1,currentState.y1,currentState.x2+1,currentState.y2,2,listVisited,matrixMap,currentState))#stateDown

            if currentState.oriented==1: #1:song song truc x(|)
                listSuccessor+=self.addListSuccessor(listVisited,State(currentState.x1,currentState.y1+1,currentState.x2,currentState.y2+1,1,listVisited,matrixMap,currentState))#stateRight
                listSuccessor+=self.addListSuccessor(listVisited,State(currentState.x1,currentState.y1-1,currentState.x2,currentState.y2-1,1,listVisited,matrixMap,currentState))#stateLeft
                listSuccessor+=self.addListSuccessor(listVisited,State(currentState.x1-1,currentState.y1,-1,-1,0,listVisited,matrixMap,currentState))#stateTop
                listSuccessor+=self.addListSuccessor(listVisited,State(currentState.x2+1,currentState.y2,-1,-1,0,listVisited,matrixMap,currentState))#stateDown
        return listSuccessor

    def addListSuccessor(self,listVisited,state):
        if (state.x1,state.y1)==(3,3) and (state.x2,state.y2)==(4,3):
            print("ok")
        if self.isValidState(state) and not self.isVisted(state,listVisited):
            return[self.enterSpecialSquare(state)]
        else:
            return  []

    def enterSpecialSquare(self,stateCheck:State):
        specialSquare=[]
        stateCheck.matrixMap=copy.deepcopy(stateCheck.matrixMap)#Copy matrixMap
        if stateCheck.oriented==0:
            if stateCheck.matrixMap[stateCheck.x1][stateCheck.y1]==2 or stateCheck.matrixMap[stateCheck.x1][stateCheck.y1]==3:#Đứng ở ô dấu X
                for x in self.specialSquareList:
                    if  x.xLocate==stateCheck.x1 and x.yLocate==stateCheck.y1 :
                        specialSquare.append(x)
            elif stateCheck.matrixMap[stateCheck.x1][stateCheck.y1]==4:#Đứng ở ô chi đôi
                for x in self.specialSquareList:
                    if x.xLocate==stateCheck.x1 and x.yLocate==stateCheck.y1:
                        stateCheck.x1,stateCheck.y1,stateCheck.x2,stateCheck.y2=x.Open[0][0],x.Open[0][1],x.Open[1][0],x.Open[1][1]
                        stateCheck.oriented=3
                        return stateCheck
        elif stateCheck.oriented==1 or stateCheck.oriented==2:#Dang nằm ở ô đặc biệt(ô O rỗng)
            if stateCheck.matrixMap[stateCheck.x1][stateCheck.y1]==3 and ((stateCheck.x1,stateCheck.y1) not in [(stateCheck.parent.x1,stateCheck.parent.y1),(stateCheck.parent.x2,stateCheck.parent.y2)]):
                for x in self.specialSquareList:
                    if (x.xLocate==stateCheck.x1 and x.yLocate==stateCheck.y1 ):
                        specialSquare.append(x)
            if stateCheck.matrixMap[stateCheck.x2][stateCheck.y2]==3 and((stateCheck.x2,stateCheck.y2) not in [(stateCheck.parent.x1,stateCheck.parent.y1),(stateCheck.parent.x2,stateCheck.parent.y2)]):
                for x in self.specialSquareList:
                    if (x.xLocate==stateCheck.x2 and x.yLocate==stateCheck.y2 ):
                        specialSquare.append(x)
        elif stateCheck.oriented==3:#2 khối tách đôi        #Chú ý: tránh trường hợp 1 khối nằm trên ô X 1 khối nằm trên ô O mà nó lại bật ô X lên
            for x in list(filter(lambda x:x.attribute==3,self.specialSquareList)):#Lọc những ô O rỗnng
                if  (x.xLocate==stateCheck.x1 and x.yLocate==stateCheck.y1) and (stateCheck.x1!=stateCheck.parent.x1 or stateCheck.y1!=stateCheck.parent.y1) :#Tránh trường hợp 1 khối nhở nằm ở 1 vị trí cố định và khối 2 di chuyền mà vẫn bật tắt=>Sai
                    specialSquare.append(x)
                elif (x.xLocate==stateCheck.x2 and x.yLocate==stateCheck.y2) and (stateCheck.x2!=stateCheck.parent.x2 or stateCheck.y2!=stateCheck.parent.y2):
                    specialSquare.append(x)
        #Xử lý luôn bật hoặc luôn tắt
        for special in specialSquare:
            if special.constance==0:
                for i in special.Open:
                    stateCheck.matrixMap[i[0]][i[1]] = int(not stateCheck.matrixMap[i[0]][i[1]])#toggle
            elif special.constance==1:#Luon Bat
                if  stateCheck.matrixMap[special.Open[0][0]][special.Open[0][1]] == 0:
                    for i in special.Open:
                        stateCheck.matrixMap[i[0]][i[1]] = 1
            elif special.constance==2:#Luon Tat
                if  stateCheck.matrixMap[special.Open[0][0]][special.Open[0][1]] == 1:
                    for i in special.Open:
                        stateCheck.matrixMap[i[0]][i[1]] = 0
        return stateCheck
        '''
        if (stateCheck.oriented==0 and stateCheck.matrixMap[stateCheck.x1][stateCheck.y1]==2) or (stateCheck.matrixMap[stateCheck.x1][stateCheck.y1]==3 or stateCheck.matrixMap[stateCheck.x2][stateCheck.y2]==3 ):# ô X
            specialSquare=[]
            if(stateCheck.oriented!=3):#đang dính nhau (Đang đứng ở ô X hoặc O) hoặc đang nằm ở ô O
                stateCheck.matrixMap=copy.deepcopy(stateCheck.matrixMap)#Copy matrixMap
                if(stateCheck.matrixMap[stateCheck.x1][stateCheck.y1]==2 or stateCheck.matrixMap[stateCheck.x1][stateCheck.y1]==3):#(x1,y1) la ô đặc biệt
                    for x in self.specialSquareList:
                        if (x.xLocate==stateCheck.x1 and x.yLocate==stateCheck.y1 and stateCheck.parent.x1!=stateCheck.x1 ):
                            specialSquare.append(x)
                if(stateCheck.matrixMap[stateCheck.x2][stateCheck.y2]==2 or stateCheck.matrixMap[stateCheck.x2][stateCheck.y2]==3):#(x2,y2) la ô đặc biệt
                    for x in self.specialSquareList:
                        if (x.xLocate==stateCheck.x2 and x.yLocate==stateCheck.y2):
                            specialSquare.append(x)
            else:# tránh trường hợp 1 khối nằm trên ô X 1 khối nằm trên ô O mà nó lại bật ô X lên
                for x in list(filter(lambda x:x.attribute==3,self.specialSquareList)):
                    if  (x.xLocate==stateCheck.x1 and x.yLocate==stateCheck.y1) and (x.xLocate==stateCheck.parent.x1 and x.yLocate==stateCheck.parent.y1) :#Tránh trường hợp 1 khối nhở nằm ở 1 vị trí cố định và khối 2 di chuyền mà vẫn bật tắt=>Sai
                        specialSquare.append(x)
                    elif (x.xLocate==stateCheck.x2 and x.yLocate==stateCheck.y2) and (x.xLocate==stateCheck.parent.x2 and x.yLocate==stateCheck.parent.y2):
                        specialSquare.append(x)
                stateCheck.matrixMap=copy.deepcopy(stateCheck.matrixMap)#Copy matrixMap
            for special in specialSquare:
                if special.constance==0:
                    for i in special.Open:
                        stateCheck.matrixMap[i[0]][i[1]] = int(not stateCheck.matrixMap[i[0]][i[1]])#toggle
                elif special.constance==1:#Luon Bat
                    if  stateCheck.matrixMap[special.Open[0][0]][special.Open[0][1]] == 0:
                        for i in special.Open:
                            stateCheck.matrixMap[i[0]][i[1]] = 1
                elif special.constance==2:#Luon Tat
                    if  stateCheck.matrixMap[special.Open[0][0]][special.Open[0][1]] == 1:
                        for i in special.Open:
                            stateCheck.matrixMap[i[0]][i[1]] = 0
        elif stateCheck.oriented==0 and stateCheck.matrixMap[stateCheck.x1][stateCheck.y1]==4:
            specialSquare=None
            for x in self.specialSquareList:
                if x.xLocate==stateCheck.x1 and x.yLocate==stateCheck.y1:
                    specialSquare=x
                    break
            stateCheck.x1,stateCheck.y1,stateCheck.x2,stateCheck.y2=specialSquare.Open[0][0],specialSquare.Open[0][1],specialSquare.Open[1][0],specialSquare.Open[1][1]
            stateCheck.oriented=3
        return stateCheck
        '''
    def isValidState(self,stateCheck:State):
        if(stateCheck.oriented==0):
            if(stateCheck.matrixMap[stateCheck.x1][stateCheck.y1]==0 or stateCheck.matrixMap[stateCheck.x1][stateCheck.y1]==5):#Đang đứng 0 va go
                return False
            else:
                return True
        else:#Đang nằm và (x1,y1) hoặc (x2,y2) đều là ô có gạch
            if(stateCheck.matrixMap[stateCheck.x1][stateCheck.y1]*stateCheck.matrixMap[stateCheck.x2][stateCheck.y2]!=0):
                return True
            else:
                return False
def printResult(lastState:State):
    listResult=[]
    path=lastState
    while path!=None:
        listResult.append(path)
        path=path.parent
    while listResult.__len__()!=0:
        top=listResult.pop()
        print("("+str(top.x1)+","+str(top.y1)+")"+"|"+"("+str(top.x2)+","+str(top.y2)+")"+"|"+str(top.oriented))
        blo.level_array=top.matrixMap
        blo.drawBlo(top.x1,top.y1,top.oriented,top.x2,top.y2)
        time.sleep(1)


#Gỗ 5
def main():
    mapMatrix = []
    stage='Stage/Stage16.txt'
    with open(stage) as f:
        mapMatrix = [[int(x) for x in line.split(',')] for line in f]
    print(mapMatrix)
    bloxorz=0
    if stage=='Stage/Stage1.txt':
        bloxorz=Bloxorz(mapMatrix,[],State(3,3,-1,-1,0,[],mapMatrix,None),State(6,9,-1,-1,0,[],mapMatrix,None))#Stage1
    elif stage=='Stage/Stage2.txt':
        bloxorz=Bloxorz(mapMatrix,[specialSquare(4,4,[(6,6),(6,7)],3),specialSquare(3,10,[(6,12),(6,13)],2)],State(6,3,-1,-1,0,[],mapMatrix,None),State(3,15,-1,-1,0,[],mapMatrix,None))#Stage2
    elif stage=='Stage/Stage3.txt':
        bloxorz=Bloxorz(mapMatrix,[],State(5,3,-1,-1,0,[],mapMatrix,None),State(5,15,-1,-1,0,[],mapMatrix,None))
    elif stage=='Stage/Stage4.txt':
        bloxorz=Bloxorz(mapMatrix,[],State(7,3,-1,-1,0,[],mapMatrix,None),State(9,8,-1,-1,0,[],mapMatrix,None))
    elif stage=='Stage/Stage5.txt':
        bloxorz=Bloxorz(mapMatrix,[specialSquare(3,10,[(3,7),(3,8)],3),specialSquare(5,5,[(10,7),(10,8)],3,1),specialSquare(7,8,[(10,7),(10,8)],3,2),specialSquare(8,16,[(10,7),(10,8)],3)],State(3,15,-1,-1,0,[],mapMatrix,None),State(10,3,-1,-1,0,[],mapMatrix,None))
    elif stage=='Stage/Stage6.txt':
        bloxorz=Bloxorz(mapMatrix,[],State(5,2,-1,-1,0,[],mapMatrix,None),State(6,15,-1,-1,0,[],mapMatrix,None))
    elif stage=='Stage/Stage7.txt':
        bloxorz=Bloxorz(mapMatrix,[specialSquare(6,11,[(8,5)],2)],State(5,3,-1,-1,0,[],mapMatrix,None),State(5,15,-1,-1,0,[],mapMatrix,None))
    elif stage=='Stage/Stage8.txt':
        bloxorz=Bloxorz(mapMatrix,[specialSquare(6,6,[(3,11),(9,11)],4)],State(6,3,-1,-1,0,[],mapMatrix,None),State(6,15,-1,-1,0,[],mapMatrix,None))
    elif stage=='Stage/Stage9.txt':
        bloxorz=Bloxorz(mapMatrix,[specialSquare(3,15,[(3,4),(3,14)],4)],State(3,3,-1,-1,0,[],mapMatrix,None),State(5,9,-1,-1,0,[],mapMatrix,None))
    elif stage=='Stage/Stage10.txt':
        bloxorz=Bloxorz(mapMatrix,[specialSquare(3,14,[(3,11),(3,14)],4),specialSquare(11,7,[(3,5),(3,6)],3),specialSquare(11,13,[(3,8),(3,9),(4,14),(5,14)],2)],State(3,11,-1,-1,0,[],mapMatrix,None),State(3,3,-1,-1,0,[],mapMatrix,None))#Stage8
    elif stage=='Stage/Stage11.txt':
        bloxorz=Bloxorz(mapMatrix,[specialSquare(8,8,[(2,6),(3,6)],3,2)],State(7,2,-1,-1,0,[],mapMatrix,None),State(3,4,-1,-1,0,[],mapMatrix,None))
    elif stage=='Stage/Stage12.txt':
        bloxorz=Bloxorz(mapMatrix,[specialSquare(4,8,[(4,14)],2),specialSquare(2,14,[(6,8)],2)],State(8,4,-1,-1,0,[],mapMatrix,None),State(6,6,-1,-1,0,[],mapMatrix,None))
    elif stage=='Stage/Stage13.txt':
        bloxorz=Bloxorz(mapMatrix,[],State(5,14,-1,-1,0,[],mapMatrix,None),State(6,9,-1,-1,0,[],mapMatrix,None))
    elif stage=='Stage/Stage14.txt':
        bloxorz=Bloxorz(mapMatrix,[specialSquare(5,14,[(4,3),(4,4)],2),specialSquare(11,15,[(5,3),(5,4)],2)],State(4,6,-1,-1,0,[],mapMatrix,None),State(10,5,-1,-1,0,[],mapMatrix,None))
    elif stage=='Stage/Stage15.txt':
        bloxorz=Bloxorz(mapMatrix,[specialSquare(9,13,[(10,11),(10,12)],3,2),specialSquare(11,13,[(10,11),(10,12)],3,2),specialSquare(7,9,[(10,3),(3,15)],4),specialSquare(5,10,[(3,7),(3,8)],3),specialSquare(5,10,[(3,12),(3,13)],3),specialSquare(3,14,[(4,4),(4,5)],2),specialSquare(3,14,[(3,7),(3,8)],2)],State(10,3,-1,-1,0,[],mapMatrix,None),State(10,14,-1,-1,0,[],mapMatrix,None))
    elif stage=='Stage/Stage16.txt':
        bloxorz=Bloxorz(mapMatrix,[specialSquare(7,11,[(3,2),(2,3)],4),specialSquare(3,4,[(3,2),(3,4)],4),specialSquare(3,2,[(2,3),(3,4)],4),specialSquare(4,3,[(3,2),(4,3)],4),specialSquare(2,3,[(3,7),(3,9)],4),specialSquare(3,7,[(3,5),(3,6)],2,1),specialSquare(3,8,[(3,10),(3,11)],2,1)],State(7,5,-1,-1,0,[],mapMatrix,None),State(3,13,-1,-1,0,[],mapMatrix,None))
    elif stage=='Stage/Stage17.txt':
        bloxorz=Bloxorz(mapMatrix,[specialSquare(10,3,[(9,10)],3),specialSquare(8,14,[(4,9)],2,1),specialSquare(11,14,[(3,11)],2,1),specialSquare(11,14,[(9,10)],2,2),specialSquare(5,14,[(8,8)],2,2),specialSquare(5,15,[(8,8)],2,1)],State(3,3,-1,-1,0,[],mapMatrix,None),State(4,15,-1,-1,0,[],mapMatrix,None))
    elif stage=='Stage/Stage18.txt':
        bloxorz=Bloxorz(mapMatrix,[specialSquare(5,3,[(5,10),(5,11)],3,2),specialSquare(3,4,[(10,3),(10,4)],3,2),specialSquare(3,4,[(5,14),(5,15)],3,2),specialSquare(7,4,[(10,3),(10,4)],3,2),specialSquare(7,4,[(5,14),(5,15)],3,2),specialSquare(2,9,[(5,10),(5,11)],3,1),specialSquare(8,10,[(10,3),(10,4)],3,1),specialSquare(8,10,[(5,14),(5,15)],3,1),specialSquare(10,5,[(6,7)],2)],State(5,4,-1,-1,0,[],mapMatrix,None),State(9,14,-1,-1,0,[],mapMatrix,None))
    elif stage=='Stage/Stage19.txt':
        bloxorz=Bloxorz(mapMatrix,[specialSquare(2,12,[(7,9),(7,10)],3),specialSquare(7,12,[(11,4),(11,5)],3,2),specialSquare(11,12,[(11,4),(11,5)],3,1)],State(2,3,-1,-1,0,[],mapMatrix,None),State(8,3,-1,-1,0,[],mapMatrix,None))
    elif stage=='Stage/Stage20.txt':
        bloxorz=Bloxorz(mapMatrix,[specialSquare(9,3,[(3,12),(3,13)],3),specialSquare(6,5,[(3,7),(3,8)],3,2),specialSquare(4,9,[(3,7),(3,8)],3,2),specialSquare(6,11,[(3,7),(3,8)],3,2),specialSquare(6,9,[(3,15),(9,15)],4),specialSquare(8,14,[(8,12),(8,13)],3)],State(4,10,-1,-1,0,[],mapMatrix,None),State(10,15,-1,-1,0,[],mapMatrix,None))

    blo.level_array=mapMatrix
    blo.drawBlo(bloxorz.startState.x1,bloxorz.startState.y1,bloxorz.startState.oriented)
    result=(bloxorz.SolveDFS())
    print("Thời gian chạy %s giây" % (time.time() - start_time))
    #printResult(result)
if __name__ == "__main__":
    main()