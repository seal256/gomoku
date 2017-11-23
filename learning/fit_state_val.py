from __future__ import print_function
import pickle
import numpy as np
from sklearn.linear_model import LogisticRegression, LinearRegression, Ridge

class FeatExtr:
    def __init__(self, board_size=3):
        self.board_size = board_size

        self.all_pos = []
        for x in range(self.board_size):
            for y in range(self.board_size):
                self.all_pos.append((x, y))

    def get_token(self, state_hash, pos):
        return state_hash[pos[1] * self.board_size + pos[0]]
    
    def get_val1(self, token):
        val = [0.] * 2
        if token == 'x':
            val[0] = 1
        elif token == 'o':
            val[1] = 1.
        return val

    def get_val2(self, token1, token2):
        val = [0.] * 3
        if token1 == 'x' and token2 == 'x':
            val[0] = 1.
        elif token1 == 'x' and token2 == 'o':
            val[1] = 1.
        elif token1 == 'o' and token2 == 'x':
            val[2] = 1.

        return val


    def get_feat(self, state_hash):
        """Get features from game state hash"""

        feat = []
        for pos in self.all_pos:
            token = self.get_token(state_hash, pos)
            val = self.get_val1(token)
            feat.extend(val)

        for pos1 in self.all_pos:
            token1 = self.get_token(state_hash, pos1)
            for pos2 in self.all_pos:
                token2 = self.get_token(state_hash, pos2)
                val = self.get_val2(token1, token2)
                feat.extend(val)

        return feat


def fit_state_val_3x3(fname='./data/state_val_3x3.pkl'):

    state_val = pickle.load(open(fname, 'rb'))
    featExtr = FeatExtr()

    X = []
    Y = []

    for state_hash, val in state_val.iteritems():
        X.append(featExtr.get_feat(state_hash))
        Y.append(val)

    model = Ridge(alpha=0.1)
    model.fit(X, Y)
    #print(model.classes_)
    print(model.coef_, model.intercept_)
    print(model.score(X, Y))


if __name__ == '__main__':
    fit_state_val_3x3()


