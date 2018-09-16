from wtforms import Form, FloatField, IntegerField, StringField, FieldList, SelectField, FormField,validators


class MemOneP(Form):
    p1 = FloatField(label='p1:CC', default=1.0, validators=[validators.InputRequired()])
    p2 = FloatField('p2:CD', default=1.0, validators=[validators.InputRequired()])
    p3 = FloatField('p3:DC', default=0.0, validators=[validators.InputRequired()])
    p4 = FloatField('p4:DD', default=0.0, validators=[validators.InputRequired()])

class InputForm(Form):

    R = IntegerField(label='Reward for mutual cooperation', default=3,
        validators=[validators.InputRequired()])
    T = IntegerField(label='Temptation to defect', default=5,
        validators=[validators.InputRequired()])
    S = IntegerField(label="Sucker's payoff", default=0,
        validators=[validators.InputRequired()])
    P = IntegerField(label='Punishment for mutual defection', default=1,
        validators=[validators.InputRequired()])
    
    fixgame = IntegerField(label='Is the number of rounds fixed? (0: unfixed; 1: fixed)', default=1,
        validators=[validators.InputRequired()])

    rounds = IntegerField(label='For fixed-round game, number of rounds played?', default=100,
        validators=[validators.InputRequired()])

    w = FloatField(label='For unfixed-round game, probability for another round of game?', default=1.0,
        validators=[validators.InputRequired()])
    
    SA = IntegerField(label='strategy of player A', default=0,
        validators=[validators.InputRequired()])
    
    
    mA0 = StringField(label='first move of A', default='C', validators=[validators.InputRequired()])
    p1 = FloatField(label='p1:CC', default=1.0, validators=[validators.InputRequired()])
    p2 = FloatField('p2:CD', default=1.0, validators=[validators.InputRequired()])
    p3 = FloatField('p3:DC', default=0.0, validators=[validators.InputRequired()])
    p4 = FloatField('p4:DD', default=0.0, validators=[validators.InputRequired()])
    
    SB = IntegerField(label='strategy of player B', default=1,
        validators=[validators.InputRequired()])

    mB0 = StringField(label='first move of B', default='C', validators=[validators.InputRequired()])
    q1 = FloatField(label='q1:CC', default=1.0, validators=[validators.InputRequired()])
    q2 = FloatField('q2:CD', default=1.0, validators=[validators.InputRequired()])
    q3 = FloatField('q3:DC', default=0.0, validators=[validators.InputRequired()])
    q4 = FloatField('q4:DD', default=0.0, validators=[validators.InputRequired()])

class InputFormTour(Form):

    R = IntegerField(label='Reward for mutual cooperation', default=3,
        validators=[validators.InputRequired()])
    T = IntegerField(label='Temptation to defect', default=5,
        validators=[validators.InputRequired()])
    S = IntegerField(label="Sucker's payoff", default=0,
        validators=[validators.InputRequired()])
    P = IntegerField(label='Punishment for mutual defection', default=1,
        validators=[validators.InputRequired()])
    
    # fixgame = IntegerField(label='Is the number of rounds fixed?', default=1,
    #    validators=[validators.InputRequired()])

    rounds = IntegerField(label='Number of rounds played', default=200,
        validators=[validators.InputRequired()])

    #w = FloatField(label='For unfixed-round game, probability for another round of game?', default=1.0,
    #    validators=[validators.InputRequired()])
    
    n = IntegerField(label='number of players', default=6,
        validators=[validators.InputRequired()])
    
    S_self = IntegerField(label='Self strategy. 0 to n-1; if n, input your own code', default=4,
        validators=[validators.InputRequired()])
    
    #S_self = SelectField(label='Self strategy. 0 to n-1; if n, input your own code', 
    #    choices=[(0, "0"), (1,1), (2, "2"), (3, "3"), (4, "4")],
    #    default=1, validators=[validators.InputRequired()])

    m0 = StringField(label='first move', default='C', validators=[validators.InputRequired()])
    
    
    #p_one = FieldList(FormField(MemOneP), label = 'transition probability', min_entries = 1)  

    p1 = FloatField(label='p1:CC', default=1.0, validators=[validators.InputRequired()])
    p2 = FloatField('p2:CD', default=1.0, validators=[validators.InputRequired()])
    p3 = FloatField('p3:DC', default=0.0, validators=[validators.InputRequired()])
    p4 = FloatField('p4:DD', default=0.0, validators=[validators.InputRequired()])
