from flask import Flask, render_template, request
from takeinput import InputForm,InputFormTour
from simulation import IteratedPD, twoplayergame, tournament
from selfstrategy import SelfImportPD


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/twoplayer', methods=['GET', 'POST'])
def two():
    form = InputForm(request.form)
    mygame = IteratedPD(form.R.data,form.T.data,form.S.data,form.P.data)

    if request.method == 'POST' and form.validate():
        #if form.SA.data == form.rounds.data:
        importgame = SelfImportPD(form.R.data,form.T.data,form.S.data,form.P.data)

        result = twoplayergame(mygame,importgame,form.fixgame.data,form.rounds.data,form.w.data,form.SA.data,form.SB.data,form.mA0.data,form.mB0.data,
                 [form.p1.data, form.p2.data,form.p3.data,form.p4.data],
                 [form.q1.data, form.q2.data,form.q3.data,form.q4.data],
                 )

    else:
        result = None

    return render_template('twoplayer.html', form=form, result=result)

@app.route('/tournament', methods=['GET', 'POST'])

def tour():
    form = InputFormTour(request.form)
    mygame = IteratedPD(form.R.data,form.T.data,form.S.data,form.P.data)
    
    if request.method == 'POST': # and form.validate():
        #string = tournament(mygame, form.n.data, form.rounds.data, form.S_self.data, form.m0.data, form.p_one.data)
            #[form.p_one.data[1],form.p_one.data[2],form.p_one.data[3],form.p_one.data[4] ] )
            #[form.p1.data,form.p2.data,form.p3.data,form.p4.data] )
            #[form.p_one.MemOneP.p1.data,form.p_one.MemOneP.p2.data,form.p_one.MemOneP.p3.data,form.p_one.MemOneP.p4.data ] )
        string = tournament(mygame, form.n.data, form.rounds.data, form.S_self.data, form.m0.data, 
            [form.p1.data,form.p2.data,form.p3.data,form.p4.data ] )
        result = string.split(',')[0]
        score = string.split(',')[1:]
    else:
        result = None
        score = None

    return render_template('tournament.html', form=form, result=result, score=score)


if __name__ == '__main__':
    app.run(debug=True)
    #port = int(os.environ.get("PORT", 5000))
    #app.run(host='0.0.0.0', port=port)
    
    #app.run()
    #app.run(host='216.174.124.203',debug=True)
#import tkinter
#import _tkinter
