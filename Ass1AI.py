class State:
    def __init__(self,x1,y1,x2,y2,oriented,parent):
        self.x1=x1
        self.y1=y1
        self.x2=x2      #x2<0 cot dung
        self.y2=y2
        self.oriented=oriented  #0:Vertical,1:HorizontalX;2:HorizontalY;
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
            if currentState==self.goalState:
                return currentState
            if not self.isVisted(currentState,listVisted):
                stack+=self.successor(currentState)
            listVisted.append(currentState)
        return None
    def isVisted(self,currentState,listVisted):
        return  currentState in listVisted
    def successor(self,currentState:State):
        listSuccessor=[]
        if  currentState.oriented==0:# Column is Vertical
            stateRight=State(currentState.x1+1,currentState.y1,currentState.x1+2,currentState.y1,1,currentState)
            if(self.isValidState(stateRight) and self.isValidState(stateRight)):
                listSuccessor.append(stateRight)

            stateLeft=State(currentState.x1-1,currentState.y1,currentState.x1-2,currentState.y1,1,currentState)
            if(self.isValidState(stateLeft)and self.isValidState(stateLeft)):
                listSuccessor.append(stateLeft)

            stateTop=State(currentState.x1,currentState.y1-1,currentState.x1,currentState.y1-2,2,currentState)#mapMatrix có hàng 1 cột 1=0
            if(self.isValidState(stateTop)and self.isValidState(stateTop)):
                listSuccessor.append(stateTop)

            stateDown=State(currentState.x1,currentState.y1+1,currentState.x1,currentState.y1+2,2,currentState)#mapMatrix có hàng 1 cột 1=0
            if(self.isValidState(stateDown)and self.isValidState(stateDown)):
                listSuccessor.append(stateDown)
        else:
            if currentState.oriented==1: #Column is HorizontalY
                stateRight=State(currentState.x2+1,currentState.y1,-1,-1,0,currentState)
                if(self.isValidState(stateRight)and self.isValidState(stateRight)):
                    listSuccessor.append(stateRight)

                stateLeft=State(currentState.x1-1,currentState.y1,-1,-1,0,currentState)
                if(self.isValidState(stateLeft)and self.isValidState(stateLeft)):
                    listSuccessor.append(stateLeft)

                stateTop=State(currentState.x1,currentState.y1-1,currentState.x2,currentState.y2-1,1,currentState)#mapMatrix có hàng 1 cột 1=0
                if(self.isValidState(stateTop)and self.isValidState(stateTop)):
                    listSuccessor.append(stateTop)

                stateDown=State(currentState.x1,currentState.y1+1,currentState.x2,currentState.y2+1,1,currentState)#mapMatrix có hàng 1 cột 1=0
                if(self.isValidState(stateDown)and self.isValidState(stateDown)):
                    listSuccessor.append(stateDown)
            if currentState.oriented==2: #Column is HorizontalX
                stateRight=State(currentState.x1+1,currentState.y1,currentState.x2+1,currentState.y2,2,currentState)
                if(self.isValidState(stateRight)and self.isValidState(stateRight)):
                    listSuccessor.append(stateRight)

                stateLeft=State(currentState.x1-1,currentState.y1,currentState.x2-1,currentState.y2,2,currentState)
                if(self.isValidState(stateLeft)and self.isValidState(stateLeft)):
                    listSuccessor.append(stateLeft)

                stateTop=State(currentState.x1,currentState.y1-1,-1,-1,0,currentState)#mapMatrix có hàng 1 cột 1=0
                if(self.isValidState(stateTop)and self.isValidState(stateTop)):
                    listSuccessor.append(stateTop)

                stateDown=State(currentState.x1,currentState.y2+1,-1,-1,0,currentState)#mapMatrix có hàng 1 cột 1=0
                if(self.isValidState(stateDown)and self.isValidState(stateDown)):
                    listSuccessor.append(stateDown)


    def isValidState(self,stateCheck:State):
        if(self.mapMatrix[stateCheck.x1][stateCheck.y1]*self.mapMatrix[stateCheck.x1][stateCheck.y1]!=0):
            return True
        else :
            return False
def main():
    print("aa")
if __name__ == "__main__":
    main()
