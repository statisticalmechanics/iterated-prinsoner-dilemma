from simulation import IteratedPD
import numpy as np

class SelfImportPD(IteratedPD):
    def ownstrategy(self, m_opponent, m_self, m0, p):
        '''
        '''
        pc = 0.5
        if np.random.rand() < pc:
            return 'C'
        else:
            return 'D'

