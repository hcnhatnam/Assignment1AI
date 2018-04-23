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

class specialSquare:
    def __init__(self,xLocate,yLocate,Open:list,attribute):#attribute=2 X;attribute=3 O;attribute=4 Slipt;
        self.xLocate=xLocate
        self.yLocate=yLocate
        self.Open=Open
        self.attribute=attribute


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


            if(currentState.oriented==3):
                a=0
            if self.isGoal(currentState):
                return currentState
            if not self.isVisted(currentState, currentState.listVisited):
                if currentState.oriented != 3:
                    stack += self.successor(currentState,currentState.listVisited,currentState.matrixMap)
                elif currentState.oriented == 3:
                    stack += self.successorSingleBlockStep1(currentState,currentState.listVisited,currentState.matrixMap)
            currentState.listVisited.append(currentState)
        return None


    def successorSingleBlockStep1(self,currentState:State,listVisited,matrixMap):
        listSuccessor=[]

        stateRight=self.checkCombine(State(currentState.x1,currentState.y1+1,currentState.x2,currentState.y2,3,currentState.listVisited,currentState.matrixMap,currentState.parent))
        listSuccessor+=self.addListSuccessor(listVisited,stateRight)
        listVisited+=self.successorSingleBlockStep2(stateRight,listVisited,matrixMap)

        stateLeft=self.checkCombine(State(currentState.x1,currentState.y1-1,currentState.x2,currentState.y2,3,currentState.listVisited,currentState.matrixMap,currentState.parent))
        listSuccessor+=self.addListSuccessor(listVisited,stateLeft)
        listVisited+=self.successorSingleBlockStep2(stateLeft,listVisited,matrixMap)


        stateTop=self.checkCombine(State(currentState.x1-1,currentState.y1,currentState.x2,currentState.y2,3,currentState.listVisited,currentState.matrixMap,currentState.parent))
        listSuccessor+=self.addListSuccessor(listVisited,stateTop)
        listVisited+=self.successorSingleBlockStep2(stateTop,listVisited,matrixMap)


        stateDown=self.checkCombine(State(currentState.x1+1,currentState.y1,currentState.x2,currentState.y2,3,currentState.listVisited,currentState.matrixMap,currentState.parent))
        listSuccessor+=self.addListSuccessor(listVisited,stateDown)
        listVisited+=self.successorSingleBlockStep2(stateDown,listVisited,matrixMap)

        return listSuccessor


    def successorSingleBlockStep2(self,currentState:State,listVisited,matrixMap):
        stack=[currentState]
        allStateVisited=[currentState]
        while stack.__len__()!=0:
            currentState=stack.pop()#pop(0) BFS search


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


    def checkCombine(self,currentState:State):
        if currentState.x1==currentState.x2:
            if currentState.y1-currentState.y2==-1:
                return State(currentState.x1,currentState.y1,currentState.x2,currentState.y2,2,currentState.listVisited,currentState.matrixMap,currentState.parent)
            if currentState.y1-currentState.y2==1:
                return State(currentState.x2,currentState.y2,currentState.x1,currentState.y1,2,currentState.listVisited,currentState.matrixMap,currentState.parent)
        if currentState.y1==currentState.y2:
            if currentState.x1-currentState.x2==-1:
                return State(currentState.x1,currentState.y1,currentState.x2,currentState.y2,1,currentState.listVisited,currentState.matrixMap,currentState.parent)
            if currentState.x1-currentState.x2==1:
                return State(currentState.x2,currentState.y2,currentState.x1,currentState.y1,1,currentState.listVisited,currentState.matrixMap,currentState.parent)
        return currentState

    def SolveBFS(self):
        stack=[self.startState]
        while stack.__len__()!=0:
            currentState=stack.pop(0)

            if(currentState.oriented==3):
                a=0
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
        if(self.isValidState(state) and not self.isVisted(state,listVisited)):
            return [self.enterSpecialSquare(state)]
        else:
            return  []

    def enterSpecialSquare(self,stateCheck:State):
        if (stateCheck.oriented==0 and stateCheck.matrixMap[stateCheck.x1][stateCheck.y1]==2) or (stateCheck.matrixMap[stateCheck.x1][stateCheck.y1]==3 or stateCheck.matrixMap[stateCheck.x2][stateCheck.y2]==3 ):# ô X
            specialSquare=None
            if(stateCheck.oriented!=3):
                for x in self.specialSquareList:
                    if (x.xLocate==stateCheck.x1 and x.yLocate==stateCheck.y1) or (x.xLocate==stateCheck.x2 and x.yLocate==stateCheck.y2):
                        specialSquare=x
                        break
                stateCheck.matrixMap=copy.deepcopy(stateCheck.matrixMap)#Copy matrixMap
            else:# tránh trường hợp 1 khối nằm trên ô X 1 khối nằm trên ô O
                for x in list(filter(lambda x:x.attribute==3,self.specialSquareList)):
                    if  (x.xLocate==stateCheck.x1 and x.yLocate==stateCheck.y1) or (x.xLocate==stateCheck.x2 and x.yLocate==stateCheck.y2):
                        specialSquare=x
                        break
                stateCheck.matrixMap=copy.deepcopy(stateCheck.matrixMap)#Copy matrixMap
            for i in specialSquare.Open:
                stateCheck.matrixMap[i[0]][i[1]] = int(not stateCheck.matrixMap[i[0]][i[1]])#toggle
        elif stateCheck.oriented==0 and stateCheck.matrixMap[stateCheck.x1][stateCheck.y1]==4:
            specialSquare=None
            for x in self.specialSquareList:
                if x.xLocate==stateCheck.x1 and x.yLocate==stateCheck.y1:
                    specialSquare=x
                    break
            stateCheck.x1,stateCheck.y1,stateCheck.x2,stateCheck.y2=specialSquare.Open[0][0],specialSquare.Open[0][1],specialSquare.Open[1][0],specialSquare.Open[1][1]
            stateCheck.oriented=3
        return stateCheck

    def isValidState(self,stateCheck:State):
        if(stateCheck.oriented==0):
            if(stateCheck.matrixMap[stateCheck.x1][stateCheck.y1]!=0):
                return True
        else:
            if(stateCheck.matrixMap[stateCheck.x1][stateCheck.y1]*self.mapMatrix[stateCheck.x2][stateCheck.y2]!=0):
                return True
        return False

def printResult(lastState:State):
    listResult=[]
    path=lastState
    while path!=None:
        listResult.append(path)
        path=path.parent

    while listResult.__len__()!=0:
        time.sleep(0.5)
        top=listResult.pop()
        print("("+str(top.x1)+","+str(top.y1)+")"+"|"+"("+str(top.x2)+","+str(top.y2)+")"+"|"+str(top.oriented))
        blo.level_array=top.matrixMap
        blo.drawBlo(top.x1,top.y1,top.oriented,top.x2,top.y2)

def main():
    mapMatrix = []
    stage='Stage8.txt'
    with open(stage) as f:
        mapMatrix = [[int(x) for x in line.split(',')] for line in f]
    print(mapMatrix)
    bloxorz=0
    if stage=='Stage1.txt':
        bloxorz=Bloxorz(mapMatrix,[],State(3,3,-1,-1,0,[],mapMatrix,None),State(6,9,-1,-1,0,[],mapMatrix,None))#Stage1
    elif stage=='Stage2.txt':
        bloxorz=Bloxorz(mapMatrix,[specialSquare(4,4,[(6,6),(6,7)],3),specialSquare(3,10,[(6,12),(6,13)],2)],State(6,3,-1,-1,0,[],mapMatrix,None),State(3,15,-1,-1,0,[],mapMatrix,None))#Stage2
    elif stage=='Stage8.txt':
        bloxorz=Bloxorz(mapMatrix,[specialSquare(6,6,[(3,11),(9,11)],4)],State(6,3,-1,-1,0,[],mapMatrix,None),State(6,14,-1,-1,0,[],mapMatrix,None))#Stage8
    blo.level_array=mapMatrix
    blo.drawBlo(6,3,0)
    result=(bloxorz.SolveDFS())
    print("Thời gian chạy %s giây" % (time.time() - start_time))
    #printResult(result)
if __name__ == "__main__":
    main()














