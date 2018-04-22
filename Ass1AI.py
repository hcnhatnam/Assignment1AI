import bloxorz as blo
import time
import copy
start_time = time.time()
class State:
    def __init__(self,x1,y1,x2,y2,oriented,listVisted,matrixMap,parent):
        self.x1=x1
        self.y1=y1
        self.x2=x2      #x2<0 cot dung
        self.y2=y2
        self.oriented=oriented  #0:Vertical,1:song song truc x(|); 2:song song Y(--);3:chia lam 2
        self.listVisted=listVisted
        self.matrixMap=matrixMap
        self.parent=parent

class specialSquare:
    def __init__(self,xLocate,yLocate,Open:list,attribute):#attribute=2 X;attribute=3 O;
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
            if self.isGoal(currentState):
                return currentState
            if not self.isVisted(currentState,currentState.listVisted):
                stack+=self.successor(currentState,currentState.listVisted,currentState.matrixMap)
            currentState.listVisted.append(currentState)
        return None

    def SolveBFS(self):
        stack=[self.startState]
        while stack.__len__()!=0:
            currentState=stack.pop(0)
            if self.isGoal(currentState):
                return currentState
            if not self.isVisted(currentState,currentState.listVisted):
                stack+=self.successor(currentState,currentState.listVisted,currentState.matrixMap)
            currentState.listVisted.append(currentState)
        return None


    def isGoal(self,currentState):
        return self.goalState.x1==currentState.x1 and self.goalState.y1==currentState.y1 and currentState.oriented==0


    def isVisted(self,currentState:State,listVisted:list):
        for i in listVisted:
            if i.x1==currentState.x1 and i.y1==currentState.y1 and  i.x2==currentState.x2 and i.y2==currentState.y2 and i.oriented==currentState.oriented and i.matrixMap==currentState.matrixMap:
                return True
        return False


    def successor(self,currentState:State,listVisted,matrixMap):
        listSuccessor=[]
        if  currentState.oriented==0:# Column is Vertical
            self.addListSuccessor(listSuccessor,listVisted,State(currentState.x1,currentState.y1+1,currentState.x1,currentState.y1+2,2,listVisted,matrixMap,currentState))#stateRight
            self.addListSuccessor(listSuccessor,listVisted,State(currentState.x1,currentState.y1-2,currentState.x1,currentState.y1-1,2,listVisted,matrixMap,currentState))#stateLeft
            self.addListSuccessor(listSuccessor,listVisted,State(currentState.x1-2,currentState.y1,currentState.x1-1,currentState.y1,1,listVisted,matrixMap,currentState))#stateTop
            self.addListSuccessor(listSuccessor,listVisted,State(currentState.x1+1,currentState.y1,currentState.x1+2,currentState.y1,1,listVisted,matrixMap,currentState))#stateDown

        else:
            if currentState.oriented==2: #2:song song Y(--);
                self.addListSuccessor(listSuccessor,listVisted,State(currentState.x2,currentState.y1+2,-1,-1,0,listVisted,matrixMap,currentState))#stateRight
                self.addListSuccessor(listSuccessor,listVisted,State(currentState.x1,currentState.y1-1,-1,-1,0,listVisted,matrixMap,currentState))#stateLeft
                self.addListSuccessor(listSuccessor,listVisted,State(currentState.x1-1,currentState.y1,currentState.x2-1,currentState.y2,2,listVisted,matrixMap,currentState))#stateTop
                self.addListSuccessor(listSuccessor,listVisted,State(currentState.x1+1,currentState.y1,currentState.x2+1,currentState.y2,2,listVisted,matrixMap,currentState))#stateDown

            if currentState.oriented==1: #1:song song truc x(|)
                self.addListSuccessor(listSuccessor,listVisted,State(currentState.x1,currentState.y1+1,currentState.x2,currentState.y2+1,1,listVisted,matrixMap,currentState))#stateRight
                self.addListSuccessor(listSuccessor,listVisted,State(currentState.x1,currentState.y1-1,currentState.x2,currentState.y2-1,1,listVisted,matrixMap,currentState))#stateLeft
                self.addListSuccessor(listSuccessor,listVisted,State(currentState.x1-1,currentState.y1,-1,-1,0,listVisted,matrixMap,currentState))#stateTop
                self.addListSuccessor(listSuccessor,listSuccessor,State(currentState.x2+1,currentState.y2,-1,-1,0,listVisted,matrixMap,currentState))#stateDown
        return listSuccessor

    def addListSuccessor(self,listSuccessor,listVisted,state):

        if(self.isValidState(state)and not self.isVisted(state,listVisted)):
            if(state.matrixMap[state.x1][state.y1]!=1):
                listSuccessor.append(self.enterSpecialSquare(state))
            else:
                listSuccessor.append(state)


    def enterSpecialSquare(self,stateCheck:State):
        if (stateCheck.oriented==0 and stateCheck.matrixMap[stateCheck.x1][stateCheck.y1]==2) or (stateCheck.matrixMap[stateCheck.x1][stateCheck.y1]==3 or stateCheck.matrixMap[stateCheck.x2][stateCheck.y2]==3):# ô X
            specialSquare=next(x for x in self.specialSquareList if (x.xLocate==stateCheck.x1 and x.yLocate==stateCheck.y1))
            stateCheck.matrixMap=copy.deepcopy(stateCheck.matrixMap)#Copy matrixMap
            for i in specialSquare.Open:
                stateCheck.matrixMap[i[0]][i[1]] = int(not stateCheck.matrixMap[i[0]][i[1]])#toggle
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
        time.sleep(0.4)
        top=listResult.pop()
        #print("("+str(top.x1)+","+str(top.y1)+")"+"|"+"("+str(top.x2)+","+str(top.y2)+")"+"|"+str(top.oriented))
        blo.level_array=top.matrixMap
        blo.drawBlo(top.x1,top.y1,top.oriented)




def main():
    '''
    mapMatrix=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,1,1,1,0,0,0,0,0,0,0,0,0],
               [0,0,1,1,1,1,1,1,0,0,0,0,0,0],
               [0,0,1,1,1,1,1,1,1,1,1,0,0,0],
               [0,0,0,1,1,1,1,1,1,1,1,1,0,0],
               [0,0,0,0,0,0,0,1,1,-1,1,1,0,0],
               [0,0,0,0,0,0,0,0,1,1,1,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
    '''
    mapMatrix = []
    with open('Stage2.txt') as f:
        mapMatrix = [[int(x) for x in line.split(',')] for line in f]
    print(mapMatrix)
    #bloxorz=Bloxorz(mapMatrix,[],State(3,3,-1,-1,0,[],mapMatrix,None),State(6,9,-1,-1,0,[],mapMatrix,None))#Stage1
    bloxorz=Bloxorz(mapMatrix,[specialSquare(4,4,[(6,6),(6,7)],3),specialSquare(3,10,[(6,12),(6,13)],2)],State(6,3,-1,-1,0,[],mapMatrix,None),State(3,15,-1,-1,0,[],mapMatrix,None))#Stage2
    blo.level_array=mapMatrix
    blo.drawBlo(6,3,0)
    result=(bloxorz.SolveBFS())
    print("Thời gian chạy %s giây" % (time.time() - start_time))
    printResult(result)
if __name__ == "__main__":
    main()














