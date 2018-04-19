import bloxorz as blo
import time
class State:
    def __init__(self,x1,y1,x2,y2,oriented,parent):
        self.x1=x1
        self.y1=y1
        self.x2=x2      #x2<0 cot dung
        self.y2=y2
        self.oriented=oriented  #0:Vertical,1:song song truc x(|); 2:song song Y(--);
        self.parent=parent

class Bloxorz:
    def __init__(self,mapMatrix:list,startState:State,goalState:State):#Matrix sinh tu(1,1)
        self.mapMatrix=mapMatrix
        self.startState=startState
        self.goalState=goalState

    def SolveDFS(self):
        stack=[self.startState]
        listVisted=[]
        while stack.__len__()!=0:
            currentState=stack.pop()
            #print("("+str(currentState.x1)+","+str(currentState.y1)+")"+"|"+"("+str(currentState.x2)+","+str(currentState.y2)+")")
            if self.isGoal(currentState):
                return currentState
            if not self.isVisted(currentState,listVisted):
                stack+=self.successor(currentState,listVisted)
            listVisted.append(currentState)
        return None


    def isGoal(self,currentState):
        return self.goalState.x1==currentState.x1 and self.goalState.y1==currentState.y1 and currentState.oriented==0


    def isVisted(self,currentState,listVisted):
        for i in listVisted:
            if i.x1==currentState.x1 and i.y1==currentState.y1 and  i.x2==currentState.x2 and i.y2==currentState.y2 and i.oriented==currentState.oriented:
                return True
        return False


    def successor(self,currentState:State,listVisted):
        listSuccessor=[]
        if  currentState.oriented==0:# Column is Vertical
            stateRight=State(currentState.x1,currentState.y1+1,currentState.x1,currentState.y1+2,2,currentState)
            if(self.isValidState(stateRight) and not self.isVisted(stateRight,listVisted)):
                listSuccessor.append(stateRight)

            stateLeft=State(currentState.x1,currentState.y1-2,currentState.x1,currentState.y1-1,2,currentState)
            if(self.isValidState(stateLeft)and not self.isVisted(stateLeft,listVisted)):
                listSuccessor.append(stateLeft)

            stateTop=State(currentState.x1-2,currentState.y1,currentState.x1-1,currentState.y1,1,currentState)#mapMatrix có hàng 1 cột 1=0
            if(self.isValidState(stateTop)and not self.isVisted(stateTop,listVisted)):
                listSuccessor.append(stateTop)

            stateDown=State(currentState.x1+1,currentState.y1,currentState.x1+2,currentState.y1,1,currentState)#mapMatrix có hàng 1 cột 1=0
            if(self.isValidState(stateDown)and not self.isVisted(stateDown,listVisted)):
                listSuccessor.append(stateDown)
        else:
            if currentState.oriented==2: #2:song song Y(--);
                stateRight=State(currentState.x2,currentState.y1+1,-1,-1,0,currentState)
                if(self.isValidState(stateRight)and not self.isVisted(stateRight,listVisted)):
                    listSuccessor.append(stateRight)

                stateLeft=State(currentState.x1,currentState.y1-1,-1,-1,0,currentState)
                if(self.isValidState(stateLeft)and not self.isVisted(stateLeft,listVisted)):
                    listSuccessor.append(stateLeft)

                stateTop=State(currentState.x1-1,currentState.y1,currentState.x2-1,currentState.y2,2,currentState)#mapMatrix có hàng 1 cột 1=0
                if(self.isValidState(stateTop)and not self.isVisted(stateTop,listVisted)):
                    listSuccessor.append(stateTop)

                stateDown=State(currentState.x1+1,currentState.y1,currentState.x2+1,currentState.y2,2,currentState)#mapMatrix có hàng 1 cột 1=0
                if(self.isValidState(stateDown)and not self.isVisted(stateDown,listVisted)):
                    listSuccessor.append(stateDown)


            if currentState.oriented==1: #1:song song truc x(|)
                stateRight=State(currentState.x1,currentState.y1+1,currentState.x2,currentState.y2+1,1,currentState)
                if(self.isValidState(stateRight)and not self.isVisted(stateRight,listVisted)):
                    listSuccessor.append(stateRight)

                stateLeft=State(currentState.x1,currentState.y1-1,currentState.x2,currentState.y2-1,1,currentState)
                if(self.isValidState(stateLeft)and not self.isVisted(stateLeft,listVisted)):
                    listSuccessor.append(stateLeft)

                stateTop=State(currentState.x1-1,currentState.y1,-1,-1,0,currentState)#mapMatrix có hàng 1 cột 1=0
                if(self.isValidState(stateTop)and not self.isVisted(stateTop,listVisted)):
                    listSuccessor.append(stateTop)

                stateDown=State(currentState.x2+1,currentState.y2,-1,-1,0,currentState)#mapMatrix có hàng 1 cột 1=0
                if(self.isValidState(stateDown)and not self.isVisted(stateDown,listVisted)):
                    listSuccessor.append(stateDown)
        return listSuccessor

    def isValidState(self,stateCheck:State):

        if(stateCheck.oriented==0):
            if(self.mapMatrix[stateCheck.x1][stateCheck.y1]!=0):
                return True
        else:
            if(self.mapMatrix[stateCheck.x1][stateCheck.y1]*self.mapMatrix[stateCheck.x2][stateCheck.y2]!=0):
                return True
        return False

def printResult(lastState:State):
    listResult=[]
    path=lastState
    while path!=None:
        listResult.append(path)
        path=path.parent

    while listResult.__len__()!=0:
        time.sleep(0.3)
        top=listResult.pop()
        print("("+str(top.x1)+","+str(top.y1)+")"+"|"+"("+str(top.x2)+","+str(top.y2)+")"+"|"+str(top.oriented))
        blo.drawBlo(top.x1,top.y1,top.oriented)




def main():
    matrixMap=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,1,1,1,0,0,0,0,0,0,0,0,0],
               [0,0,1,1,1,1,1,1,0,0,0,0,0,0],
               [0,0,1,1,1,1,1,1,1,1,1,0,0,0],
               [0,0,0,1,1,1,1,1,1,1,1,1,0,0],
               [0,0,0,0,0,0,0,1,1,-1,1,1,0,0],
               [0,0,0,0,0,0,0,0,1,1,1,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
    bloxorz=Bloxorz(matrixMap,State(3,3,-1,-1,0,None),State(6,9,-1,-1,0,None))
    printResult(bloxorz.SolveDFS())

if __name__ == "__main__":
    main()













