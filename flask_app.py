from flask import Flask, render_template,request
import relativity as r

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/relativity')
def relativity():
    return render_template('relativity.html')

@app.route('/relativity/e_mc2',methods = ['GET','POST'])
def e_mc2():
    if request.method == 'POST':
        m = float(request.form.get('one'))
        emc = r.e_mc2(m)
        return '<br><br><br><br><br><br><br><br><center><h1>Energy is: '+str(emc)+' Joule'+'</h1></center>'
        
    return render_template('relativity_emc2.html')

@app.route('/relativity/length_contraction',methods = ['GET','POST'])
def length_contraction():
    if request.method == 'POST':
        l = float(request.form.get('one'))
        v = float(request.form.get('two'))
        lc = r.length_contraction(l,v)
        return '<br><br><br><br><br><br><br><br><center><h1>Length Contraction is: '+str(lc)+' metre'+'</h1></center>'
        
    return render_template('relativity_lc.html')

@app.route('/relativity/relativistic_kinetic_energy',methods = ['GET','POST'])
def relativistic_kinetic_energy():
    if request.method == 'POST':
        m = float(request.form.get('one'))
        v = float(request.form.get('two'))
        rke = r.relativistic_kinetic_energy(m,v)
        return '<br><br><br><br><br><br><br><br><center><h1>Relativistic Kinetic Energy is: '+str(rke)+' Joule'+'</h1></center>'
        
    return render_template('relativity_rke.html')

@app.route('/relativity/time_dilation',methods = ['GET','POST'])
def time_dilation():
    if request.method == 'POST':
        t = float(request.form.get('one'))
        v = float(request.form.get('two'))
        td = r.time_dilation(t,v)
        return '<br><br><br><br><br><br><br><br><center><h1>Time Dilation is: '+str(td)+' sec'+'</h1></center>'
        
    return render_template('relativity_td.html')

@app.route('/relativity/velocity_addition',methods = ['GET','POST'])
def velocity_addition():
    if request.method == 'POST':
        v = float(request.form.get('one'))
        w = float(request.form.get('two'))
        va = r.velocity_addition(v,w)
        return '<br><br><br><br><br><br><br><br><center><h1>Velocity Addition is: '+str(va)+' metre sec^2'+'</h1></center>'
        
    return render_template('relativity_va.html')

@app.route('/relativity/mass_variation',methods = ['GET','POST'])
def mass_variation():
    if request.method == 'POST':
        m = float(request.form.get('one'))
        v = float(request.form.get('two'))
        mv = r.mass_variation(m,v)
        return '<br><br><br><br><br><br><br><br><center><h1>Mass Variation is: '+str(mv)+' Kg'+'</h1></center>'
        
    return render_template('relativity_mv.html')

if __name__ == '__main__':
    app.run(debug = True)