from flask import Flask, jsonify, request
from sqlalchemy import ForeignKey
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_TRACE_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:dragoncross9@localhost:5432/ImobEnforce'
app.debug = True
db = SQLAlchemy(app)

class owner(db.Model):
    __tablename__ = 'proprietario'
    id_owner = db.Column(db.Integer(), primary_key=True, autoincrement=True, unique=True)
    name_owner = db.Column(db.String(255), nullable=False)
    rg_owner = db.Column(db.String(9), nullable=False)
    cpf_owner = db.Column(db.String(11), nullable=False)
    birth_date_owner = db.Column(db.String(10), nullable=False)
    civil_status_owner = db.Column(db.String(20), nullable=False)
    email_owner = db.Column(db.String(100), nullable=False)
    cel_owner = db.Column(db.String(11), nullable=False)
    prof_owner = db.Column(db.String(50), nullable=False)
    tempo_prop = db.Column(db.String(5), nullable= False)

    def __init__(self, id_owner, name_owner, rg_owner, cpf_owner, birth_date_owner, civil_status_owner, email_owner, cel_owner, prof_owner, tempo_prop):
        self.id_owner = id_owner
        self.name_owner = name_owner
        self.rg_owner = rg_owner
        self.cpf_owner = cpf_owner
        self.birth_date_owner = birth_date_owner
        self.civil_status_owner = civil_status_owner
        self.email_owner = email_owner
        self.cel_owner = cel_owner
        self.prof_owner = prof_owner
        self.tempo_prop = tempo_prop

class adress_immobile(db.Model):
    __tablename__ = 'endereco_imovel'
    id_endereco_imov = db.Column(db.Integer(), primary_key=True, autoincrement=True, unique=True)
    rua_imov = db.Column(db.String(255), nullable=False)
    numero_imov = db.Column(db.String(10), nullable=False)
    apto_imov = db.Column(db.String(2), nullable=False)
    bloco_imov = db.Column(db.String(20), nullable=False)
    bairro_imov = db.Column(db.String(50), nullable=False)
    cep_imov = db.Column(db.String(11), nullable=False)
    cidade_imov = db.Column(db.String(50), nullable=False)
    uf_imov = db.Column(db.String(2), nullable=False)

    def __init__(self, id_endereco_imov, rua_imov, numero_imov, apto_imov, bloco_imov, bairro_imov, cep_imov, cidade_imov, uf_imov):
        self.id_endereco_imov = id_endereco_imov
        self.rua_imov = rua_imov
        self.numero_imov = numero_imov
        self.apto_imov = apto_imov
        self.bloco_imov = bloco_imov
        self.bairro_imov = bairro_imov
        self.cep_imov = cep_imov
        self.cidade_imov = cidade_imov
        self.uf_imov = uf_imov

class adress_client(db.Model):
    __tablename__ = 'endereco_cliente'
    id_endereco_cli = db.Column(db.Integer(), primary_key=True, autoincrement=True, unique=True)
    rua_cli = db.Column(db.String(255), nullable=False)
    numero_cli = db.Column(db.String(10), nullable=False)
    apto_cli = db.Column(db.String(2), nullable=False)
    bloco_cli = db.Column(db.String(20), nullable=False)
    bairro_cli = db.Column(db.String(50), nullable=False)
    cep_cli = db.Column(db.String(11), nullable=False)
    cidade_cli = db.Column(db.String(50), nullable=False)
    uf_cli = db.Column(db.String(2), nullable=False)

    def __init__(self, id_endereco_cli, rua_cli, numero_cli, apto_cli, bloco_cli, bairro_cli, cep_cli, cidade_cli, uf_cli):
        self.id_endereco_cli = id_endereco_cli
        self.rua_cli = rua_cli
        self.numero_cli = numero_cli
        self.apto_cli = apto_cli
        self.bloco_cli = bloco_cli
        self.bairro_cli = bairro_cli
        self.cep_cli = cep_cli
        self.cidade_cli = cidade_cli
        self.uf_cli = uf_cli

class client(db.Model):
    __tablename__ = 'cliente'
    id_cli = db.Column(db.Integer(), primary_key=True, autoincrement=True, unique=True)
    name_cli = db.Column(db.String(255), nullable=False)
    rg_cli = db.Column(db.String(9), nullable=False)
    cpf_cli = db.Column(db.String(11), nullable=False)
    birth_date_cli = db.Column(db.String(10), nullable=False)
    civil_status_cli = db.Column(db.String(20), nullable=False)
    email_cli = db.Column(db.String(100), nullable=False)
    cel_cli = db.Column(db.String(11), nullable=False)
    id_endereco_cli = db.Column(db.Integer(), ForeignKey('endereco_cliente.id_endereco_cli'), unique=True)
    prof_cli = db.Column(db.String(50), nullable=False)
    
    def __init__(self, id_cli, name_cli, rg_cli, cpf_cli, birth_date_cli, civil_status_cli, email_cli, cel_cli, prof_cli, tempo_prop):
        self.id_cli = id_cli
        self.name_cli = name_cli
        self.rg_cli = rg_cli
        self.cpf_cli = cpf_cli
        self.birth_date_cli = birth_date_cli
        self.civil_status_cli = civil_status_cli
        self.email_cli = email_cli
        self.cel_cli = cel_cli
        self.prof_cli = prof_cli

class seller(db.Model):
    __tablename__ = 'vendedor'
    id_vendedor = db.Column(db.Integer(), primary_key=True, autoincrement=True, unique=True)
    name_vendedor = db.Column(db.String(255), nullable=False)
    matricula_vendedor = db.Column(db.String(9), nullable=False)
    email_vendedor = db.Column(db.String(11), nullable=False)
    telefone_vendedor = db.Column(db.String(10), nullable=False)
        
    def __init__(self, id_vendedor, name_vendedor, matricula_vendedor, email_vendedor, telefone_vendedor):
        self.id_vendedor = id_vendedor
        self.name_vendedor = name_vendedor
        self.matricula_vendedor = matricula_vendedor
        self.email_vendedor = email_vendedor
        self.telefone_vendedor = telefone_vendedor

class banks(db.Model):
    __tablename__ = 'bancos'
    id_banco = db.Column(db.Integer(), primary_key=True, autoincrement=True, unique=True)
    name_banco = db.Column(db.String(20), nullable=False)
            
    def __init__(self, id_bancos, name_banco):
        self.id_banco = id_banco
        self.name_banco = name_banco        

class finance(db.Model):
    __tablename__ = 'financiamento'
    id_financiamento = db.Column(db.Integer(), primary_key=True, autoincrement=True, unique=True)
    id_cli = db.Column(db.Integer(), ForeignKey('cliente.id_cli'), unique=True)
    id_banco = db.Column(db.Integer(), ForeignKey('bancos.id_banco'), unique=True)
    entrada = db.Column(db.Numeric(), nullable= False)
    num_parcela = db.Column(db.Integer(), nullable=False)

            
    def __init__(self, id_financiamento, id_cli, id_banco, entrada, num_parcela):
        self.id_financiamento = id_financiamento
        self.id_cli = id_cli 
        self.id_banco = id_banco
        self.entrada = entrada
        self.num_parcela = num_parcela

class payment_type(db.Model):
    __tablename__ = 'tipo_compra'
    id_tipo_compra = db.Column(db.Integer(), primary_key=True, autoincrement=True, unique=True)
    vista = db.Column(db.Boolean(), nullable=False)
    id_financiamento = db.Column(db.Integer(), ForeignKey('financiamento.id_financiamento'), unique=True)
            
    def __init__(self, id_tipo_compra, vista, id_financiamento):
        self.id_tipo_compra = id_tipo_compra
        self.vista = vista 
        self.id_financiamento = id_financiamento

class payment(db.Model):
    __tablename__ = 'compra'
    id_compra = db.Column(db.Integer(), primary_key=True, autoincrement=True, unique=True)
    id_vendedor = db.Column(db.Integer(), ForeignKey('vendedor.id_vendedor'), unique=True)
    id_cli = db.Column(db.Integer(), ForeignKey('cliente.id_cli'), unique=True)
    valor_compra = db.Column(db.Numeric(), nullable=False)
    id_tipo_compra = db.Column(db.Integer(), ForeignKey('tipo_compra.id_tipo_compra'), unique=True)
            
    def __init__(self, id_compra, id_vendedor, id_cli, valor_compra, id_tipo_compra):
        self.id_compra = id_compra
        self.id_vendedor = id_vendedor 
        self.id_cli = id_cli
        self.valor_compra = valor_compra
        self.id_tipo_compra = id_tipo_compra

class immobile_type(db.Model):
    __tablename__ = 'tipo_imovel'
    id_tipo_imovel = db.Column(db.Integer(), primary_key=True, autoincrement=True, unique=True)
    tipo_imovel = db.Column(db.String(20), nullable=False)
            
    def __init__(self, id_tipo_imovel, tipo_imovel):
        self.id_tipo_imovel = id_tipo_imovel
        self.tipo_imovel = tipo_imovel  

class payment(db.Model):
    __tablename__ = 'imovel'
    id_imovel = db.Column(db.Integer(), primary_key=True, autoincrement=True, unique=True)
    id_endereco_imov = db.Column(db.Integer(), ForeignKey('endereco_imovel.id_endereco_imov'), unique=True)
    id_owner = db.Column(db.Integer(), ForeignKey('proprietario.id_owner'), unique=True) 
    id_vendedor = db.Column(db.Integer(), ForeignKey('vendedor.id_vendedor'), unique=True)
    id_tipo_imovel = db.Column(db.Integer(), ForeignKey('tipo_imovel.id_tipo_imovel'), unique=True)
    id_compra = db.Column(db.Integer(), ForeignKey('compra.id_compra'), unique=True)
            
    def __init__(self, id_imovel, id_endereco_imov, id_owner, id_vendedor, id_tipo_imovel, id_compra):
        self.id_imovel = id_imovel
        self.self.id_endereco_imov = id_endereco_imov
        self.id_owner = id_owner
        self.id_vendedor = id_vendedor
        self.id_tipo_imovel = id_tipo_imovel
        self.id_compra = id_compra

@app.route('/test', methods=['GET'])
def test():
    return {
        'test': 'test1'
    }

@app.route('/owners', methods=['GET'])
def gOwners():
    allOwners = owner.query.all()
    output = []
    for owners in allOwners:
        currOwner = {}
        currOwner['id_owner'] = owner.id_owner
        currOwner['name_owner'] = owner.name_owner
        currOwner['rg_owner'] = owner.rg_owner
        currOwner['cpf_owner'] = owner.cpf_owner
        currOwner['birth_date_owner'] = owner.birth_date_owner
        currOwner['civil_status_owner'] = owner.civil_status_owner
        currOwner['email_owner'] = owner.email_owner
        currOwner['cel_owner'] = owner.cel_owner
        currOwner['prof_owner'] = owner.prof_owner
        currOwner['tempo_prop'] = owner.tempo_prop
        output.append(currOwner)
    return jsonify(output)

@app.route('/owners', methods=['POST'])
def pOwners():
    ownersData = request.get_json()
    owners = owner(id_owner=ownersData['id_owner'], 
                   name_owner=ownersData['name_owner'], 
                   rg_owner=ownersData['rg_owner'], 
                   cpf_owner=ownersData['cpf_owner'], 
                   birth_date_owner=ownersData['birth_date_owner'], 
                   civil_status_owner=ownersData['civil_status_owner'], 
                   email_owner=ownersData['email_owner'], 
                   cel_owner=ownersData['cel_owner'], 
                   prof_owner=ownersData['prof_owner'], 
                   tempo_prop=ownersData['tempo_prop'])
    db.session.add(owners)
    db.session.commit()
    return jsonify(ownersData)
    
    

