import json
import unicodedata

#Escreve no Arquivo Json
def write_Json(Nome,Senha,Email,filename="Person.json"):
    with open(filename,'r+') as file:
        Readfile = json.load(file)
        
        for valores in Readfile['Usuarios']:
            if Email in valores['Email']:
                return False
            
        Readfile['Usuarios'].append({"Nome":Nome,'Email':Email,"Senha":Senha,"Curso":[]})
        file.seek(0)
        json.dump(Readfile,file,indent= 4)
        return True


#Valida se o O login e senha informado estão corretos
def ValidaUser(Nome,Senha,filename='Person.json'):
    with open(filename,'r+') as file:
        ReadFile = json.load(file)
        for valores in ReadFile["Usuarios"]:
            if Nome.lower() == valores['Nome'].lower() and Senha == valores['Senha']:
                return True


#Adiciona o Usuário no curso
def AdicionaCurso(Usuario,NomeCurso,filename="Person.json"):
    with open(filename,'r+',encoding='utf-8') as file:
        Readfile = json.load(file)
        contador = 0

        for valores in Readfile['Usuarios']:
            if Usuario == valores['Nome'] and Usuario != '' and NomeCurso not in valores['Curso'] :
                Readfile['Usuarios'][contador]['Curso'].append(unicodedata.normalize("NFKD",NomeCurso))
                file.seek(0)
                json.dump(Readfile,file,indent=4)
                file.truncate()
                return f"Parabéns, {Usuario}, você se cadastrou ao curso {NomeCurso}"

            elif Usuario == '':
                return f'Você deve realizar login!' 
            
            elif NomeCurso in valores['Curso']:
                return f"Você já esta cadastrado no curso {NomeCurso}"

            contador+=1
