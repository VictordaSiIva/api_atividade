from models import Pessoas

def insere_pessoas():
    pessoa = Pessoas(nome='Victor', idade=21)
    print(pessoa)
    pessoa.save()

def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)
    pessoa = Pessoas.query.filter_by(nome='Victor').first()
    print(pessoa.idade)
def altera_pessoa():
    pessoa =   pessoa = Pessoas.query.filter_by(nome='Silva').first()
    pessoa.nome = 'Felipe'
    pessoa.save()

def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Felipe').first()
    pessoa.delete()

if __name__ == '__main__':
    exclui_pessoa()
    consulta_pessoas()