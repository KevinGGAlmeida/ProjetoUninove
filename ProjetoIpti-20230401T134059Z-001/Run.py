from flask import Flask,request,render_template,session,redirect,flash
from flask_session import Session
from functions import ValidaUser,write_Json,AdicionaCurso
import unicodedata

app = Flask(__name__,template_folder='templates',static_folder='static')
app.secret_key = "secret key"

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)



#HomePage
@app.route("/",methods=['GET','POST'])

#Home Page
def index():
    
    #Valida se o usuário ja esta logado, estando redireciona o mesmo para a homepage
    if not session.get('Name'):
        
        if request.method == 'GET':
            
            return render_template("index.html")
    
    #Do contrário, envia o mesmo para a HomePage para realizar o login
    else:
        
        return render_template("index.html",User=session['Name'])
            

#Autenticação
@app.route('/Auth',methods=['POST'])
def Auth():
    #Valida o metodo da requisição
    if request.method == 'POST':
        
        #Valida se o login e senha estão corretos, estando, realiza o login e redireciona para a homepage
        if ValidaUser(request.form.get("Login"),request.form.get("Senha")) == True:
            session['Name'] = request.form.get("Login")
            return redirect('/')
        
        #Caso o login esteja incorreto, é gerado um alerta
        else:
            flash('Senha incorreta, tente novamente!')
            return render_template('index.html',message='Senha incorreta, tente novamente')            



#Criação de Usuário
@app.route("/Create",methods=['POST','GET'])
def Create():
        
        #Valida o metodo da requisição
        if request.method == 'POST':

            #Valida se já existe um usuário igual, não existindo, cria o usuário e o redireciona para a HomePage
            if write_Json(request.form.get('Login'),request.form.get("Senha"),request.form.get("Email")) == True:
                return redirect('/')

            #Do contrário, é gerado um alerta de que já existe um usuário cadastrado
            else:
                return render_template('index.html',Erro="Email ou Usuário ja cadastrado")


#Realiza Logout
@app.route("/logout")
def logout():
    if request.method == 'GET':
        session['Name'] = ''
        return render_template('index.html')


#Inscrever-se no Curso
@app.route("/CadastraCurso",methods=['POST','GET'])
def CadastroCurso():
    
    #Valida se o usuário está logado, estando, poderá ocorrer 2 condições
    if session['Name'] != '':
        if request.method == 'POST':

            Retorno = AdicionaCurso(session['Name'],unicodedata.normalize("NFKD",request.form.get("curso")))
            
            #Se o usuário não estiver no curso, o mesmo será cadastrado no curso, como também, será gerado um alerta para confirmação visual
            if 'Parabéns' in Retorno:
                flash(Retorno)
                return redirect('/')
        
            #Do contrário, será gerado um alerta informando que o usuário ou já está cadastrado no curso, ou não realizou Login
            else:
                flash(Retorno)
                return redirect('/')

        else:
            return redirect('/')

    #Do contrário é informado para o usuário realizar o Login e é redirecionado para  HomePage
    else:
        flash('Para prosseguir, realize o login!')
        return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)