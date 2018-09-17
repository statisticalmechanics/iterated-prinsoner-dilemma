import numpy as np
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt

import os, glob, time
import pandas as pd
from pandas.tools.plotting import table


class IteratedPD():
    def __init__(self, R, T, S, P):
        self.R = R
        self.T = T
        self.S = S
        self.P = P
        self.payoffs = ( ( (R,R), (S,T) ) ,  ( (T,S), (P,P) ) )
        
    def onegame(self, mA, mB):
        if mA == 'C' and mB == 'C':
            return self.payoffs[0][0]
        elif mA == 'C' and mB == 'D':
            return self.payoffs[0][1]
        elif mA == 'D' and mB == 'C':
            return self.payoffs[1][0]
        elif mA == 'D' and mB == 'D':
            return self.payoffs[1][1]        
        else:
            sys.exit('unexpected input %s %s' % (mA, mB) )

    def alld(self):
        return 'D'
    
    def allc(self):
        return 'C'

    def tft(self, mB):
        '''
        tit for tat
        '''
        if  mB:
            if mB[-1] == 'C':
                return 'C'
            elif mB[-1] == 'D':
                return 'D'
        else:
            return 'C'

    def ranc(self):
        '''
        '''
        prob = 0.5
        if np.random.rand() < prob:
            return 'C'
        else:
            return 'D'

    def memone(self, mB, mA, m0, p): 
        '''
        memory-one 
        '''
        if mB and mA:
            if mB[-1] == 'C' and mA[-1] == 'C':
                prob = p[0] 
            elif mB[-1] == 'D' and mA[-1] == 'C':
                prob = p[1] 
            elif mB[-1] == 'C' and mA[-1] == 'D':
                prob = p[2] 
            #elif mB[-1] == 'D' and mA[-1] == 'D':
            else:
                prob = p[3] 

            if np.random.rand() < prob:
                return 'C'
            else:
                return 'D'
        else:
            return m0

    def zerodet(self, mB, mA, m0, p):
        '''
         A sets the expected score of B
        '''
        try:
            p1 = p[0]
            p4 = p[3]
            p2 = (p1*(self.T-self.P) - (1+p4)*(self.T-self.R)) / (self.R-self.P)   
            p3 = ((1-p1)*(self.P-self.S) + p4*(self.R-self.S)) / (self.R-self.P)   
       
            return self.memone(mB, mA, m0,[p1,p2,p3,p4])
        except:
            pass
   
    def sB_zerodet(self, p):
        '''
         P <= sB <= R
        '''
        try:
            p1 = p[0]
            p4 = p[3]
            return ( (1-p1)*self.P + p4*self.R) / (1-p1+p4)
        except:
            return None
   
    def player(self, playerid, m_opponent, m_self, m0='C', p=[1,1,1,1]):
        if playerid == 0:
            return self.alld()
        elif playerid == 1:
            return self.allc()
        elif playerid == 2:
            return self.tft(m_opponent)
        elif playerid == 3:
            return self.ranc()
        elif playerid == 4:
            return self.memone(m_opponent, m_self, m0, p)
        elif playerid == 5:
            return self.zerodet(m_opponent, m_self, m0, p)
   

def twoplayergame(mygame, importgame, fixgame, rounds, w, SA, SB, mA0='C', mB0='C', p=[1,1,1,1], q=[1,1,1,1]):
    '''
    mygame: an object of class IteratedPD
    importgame: an object of class SelfImportPD
    '''
    scoresA = []
    scoresB = []
    movesA = []
    movesB = []

    if fixgame == 1:
        for i in range(rounds):
            if SA == 6:
                moveA = importgame.ownstrategy(movesB, movesA, mA0, p)
            else:   
                moveA = mygame.player(SA,movesB, movesA, mA0, p)
            moveB = mygame.player(SB,movesA, movesB, mB0, q)
            
            scoreA, scoreB = mygame.onegame(moveA,moveB)
            movesA.append(moveA)
            movesB.append(moveB)
            scoresA.append(scoreA)
            scoresB.append(scoreB)
    else:
        while np.random.rand()<w:
            moveA = mygame.player(SA,movesB, movesA, mA0, p)
            moveB = mygame.player(SB,movesA, movesB, mB0, q)
        
            scoreA, scoreB = mygame.onegame(moveA,moveB)
            movesA.append(moveA)
            movesB.append(moveB)
            scoresA.append(scoreA)
            scoresB.append(scoreB)

    if SA == 5:
        sB_expect = mygame.sB_zerodet(p)

    moves = range(1,len(movesA)+1)
    plt.figure(figsize=(15,6))
    #plt.figure()
    plt.subplot(131)
    plt.plot(moves, scoresA, 'r-')
    plt.plot(moves, scoresB, 'b-')
    plt.xlabel("round")
    plt.ylabel("instant score")
    plt.subplot(132)
    scoresA_cum = np.cumsum(scoresA)
    scoresB_cum  = np.cumsum(scoresB)
    plt.plot(moves, scoresA_cum, 'r-', label = 'A')
    plt.plot(moves, scoresB_cum, 'b-', label = 'B')
    plt.xlabel("round")
    plt.ylabel("cumulative score")
    plt.legend()
    plt.subplot(133)
    plt.plot(moves, scoresA_cum/moves, 'r-', label = 'A')
    plt.plot(moves, scoresB_cum/moves, 'b-', label = 'B')
    if SA == 5 and sB_expect != None:
        plt.plot([1, moves[-1]], [sB_expect,sB_expect], 'k--', label = 'B expected: %.2f' %sB_expect)

    plt.ylim(-1,6)
    plt.xlabel("round")
    plt.ylabel("cumulative average score")
    plt.legend()

    
    if not os.path.isdir('static'):
        os.mkdir('static')
    else:
        for filename in glob.glob(os.path.join('static','*.png')):
            os.remove(filename)

    plotfile = os.path.join('static', str(time.time()) + '.png')

    plt.savefig(plotfile)

    return plotfile

def tournament(mygame, nplayers, rounds, S_self, m0, p_one):
 
    scores_pair = np.zeros((nplayers+1, nplayers+1))
    for i in range(nplayers):
        for j in range(i+1, nplayers+1):
            scoresA = []
            scoresB = []
            movesA = []
            movesB = []
            for k in range(rounds):
                moveA = mygame.player(i,movesB, movesA, m0, p_one)

                if j < nplayers:
                    moveB = mygame.player(j,movesA, movesB, m0, p_one)
                else:
                    moveB = mygame.player(S_self,movesA, movesB, m0, p_one)
                scoreA, scoreB = mygame.onegame(moveA,moveB)
                movesA.append(moveA)
                movesB.append(moveB)
                scoresA.append(scoreA)
                scoresB.append(scoreB)

            scoresA_cum = np.cumsum(scoresA)
            scoresB_cum = np.cumsum(scoresB)
            scores_pair[i][j] = scoresA_cum[-1]
            scores_pair[j][i] = scoresB_cum[-1]
    
    #plt.figure(figsize=(4,4))
    #plt.imshow(scores_pair)
    #plt.colorbar()


    plt.figure(figsize=(6,2))
    df=pd.DataFrame(scores_pair)
    df['average'] = df.sum(axis=1)
    df.loc[:, 'average'] *= 1.0/nplayers

    #df.round(1)
    ax = plt.subplot(111, frame_on=False) # no visible frame
    #ax = plt.plot(frame_on=False) # no visible frame
    ax.xaxis.set_visible(False)  # hide the x axis
    ax.yaxis.set_visible(False)  # hide the y axis
    #table(ax, df, loc='center')  #
    table(ax, np.round(df, 1), loc='center')  #

    if not os.path.isdir('static'):
        os.mkdir('static')
    else:
        for filename in glob.glob(os.path.join('static','*.png')):
            os.remove(filename)
    plotfile = os.path.join('static', str(time.time()) + '.png')
    plt.savefig(plotfile)

    final_score = [scores_pair[nplayers][i] for i in range(nplayers) ]
    #final_score = [scores_pair[2][i] for i in range(nplayers+1) ]
    #return plotfile+"  "+ str(final_score)
    #return plotfile+"  "+ ' '.join(str(x) for x in final_score)
    return plotfile+","+ ' '.join(map(str, final_score))


#if __name__ = '__main__':
#    print ()
