import flask
from flask import Flask, jsonify, request
from sqlalchemy import ForeignKey
from flask_sqlalchemy import SQLAlchemy
from flask_restplus import Api, Resource

flask_app = flask.Flask(__name__)
app = Api(app = flask_app)
flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:dragoncross9@localhost:5432/ImobEnforce'
flask_app.debug = True
name_space = app.namespace('main', description='Main APIs')

db = SQLAlchemy(flask_app)

@name_space.route("/")
class MainClass(Resource):
	def get(self):
		return {
			"status": "Got new data"
		}
	def post(self):
		return {
			"status": "Posted new data"
		}

from Owner import owner
from AdressImmobile import adress_immobile
from AdressCliente import adress_client
from Client import client
from Seller import seller 
from Banks import banks
from Finance import finance    
from PaymentType import payment_type
from Payment import payment
from ImmobileType import immobile_type
from Immobile import immobile    

# @app.route('/test', methods=['GET'])
# def test():
#     return {
#         'test': 'test1'
#     }

owners = [
{"id_owner": "2",
    "name_owner": "test",
    "rg_owner": "123456789",
    "cpf_owner": "12345678912",
    "birth_date_owner": "1234567890",
    "civil_status_owner": "12345678901234567890",
    "email_owner": "test5",
    "cel_owner": "test6",
    "prof_owner": "test7",
    "tempo_prop": "test8"}
] 

@app.route('/owners')
class gpOwners(Resource):
    def get(self):
        allOwners = owner.query.all()
        output = []
        for owners in allOwners:
            currOwner = {}
            currOwner['id_owner'] = owners.id_owner
            currOwner['name_owner'] = owners.name_owner
            currOwner['rg_owner'] = owners.rg_owner
            currOwner['cpf_owner'] = owners.cpf_owner
            currOwner['birth_date_owner'] = owners.birth_date_owner
            currOwner['civil_status_owner'] = owners.civil_status_owner
            currOwner['email_owner'] = owners.email_owner
            currOwner['cel_owner'] = owners.cel_owner
            currOwner['prof_owner'] = owners.prof_owner
            currOwner['tempo_prop'] = owners.tempo_prop
            output.append(currOwner)
            # output = request.get_json()
        return jsonify(output)

    def post(self):
        # ownersData = request.get_json()
        # owners = owner(id_owner=ownersData['id_owner'], 
        #             name_owner=ownersData['name_owner'], 
        #             rg_owner=ownersData['rg_owner'], 
        #             cpf_owner=ownersData['cpf_owner'], 
        #             birth_date_owner=ownersData['birth_date_owner'], 
        #             civil_status_owner=ownersData['civil_status_owner'], 
        #             email_owner=ownersData['email_owner'], 
        #             cel_owner=ownersData['cel_owner'], 
        #             prof_owner=ownersData['prof_owner'], 
        #             tempo_prop=ownersData['tempo_prop'])
        # db.session.add(owners)
        # db.session.commit()
        return jsonify(owners)

# @app.route('/immobile_adress', methods=['GET'])
# def gImmobileAdress():
#     allImmobileAdress = adress_immobile.query.all()
#     output = []
#     for adress in allImmobileAdress:
#         currImmobileAdress = {}
#         currImmobileAdress['id_endereco_imov'] = adress.id_endereco_imov
#         currImmobileAdress['rua_imov'] = adress.rua_imov
#         currImmobileAdress['numero_imov'] = adress.numero_imov
#         currImmobileAdress['apto_imov'] = adress.apto_imov
#         currImmobileAdress['bloco_imov'] = adress.bloco_imov
#         currImmobileAdress['bairro_imov'] = adress.bairro_imov
#         currImmobileAdress['cep_imov'] = adress.cep_imov
#         currImmobileAdress['cidade_imov'] = adress.cidade_imov
#         currImmobileAdress['uf_imov'] = adress.uf_imov
#         output.append(currImmobileAdress)
#         # output = request.get_json()
#     return jsonify(output)

# @app.route('/immobile_adress', methods=['POST'])
# def pImmobileAdress():
#     immobileAdressData = request.get_json()
#     immobileAdress = adress_immobile(id_endereco_imov=immobileAdressData['id_endereco_imov'], 
#                                      rua_imov=immobileAdressData['rua_imov'], 
#                                      numero_imov=immobileAdressData['numero_imov'], 
#                                      apto_imov=immobileAdressData['apto_imov'], 
#                                      bloco_imov=immobileAdressData['bloco_imov'], 
#                                      bairro_imov=immobileAdressData['bairro_imov'], 
#                                      cep_imov=immobileAdressData['cep_imov'], 
#                                      cidade_imov=immobileAdressData['cidade_imov'], 
#                                      uf_imov=immobileAdressData['uf_imov'])
#     db.session.add(immobileAdress)
#     db.session.commit()
#     return jsonify(immobileAdressData)