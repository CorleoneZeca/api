import datetime

from flask import Flask, jsonify

from models.store.store_sales_team_apply_model import StoreSalesTeamApplyModel

import server_conector

__author__ = 'Jose Alvaro Sacramento <corleone_zeca@hotmail.com> \
              & Sidnei José Corrêa Junior'
app = Flask(__name__)


class StoreSalesTeamApplyView(StoreSalesTeamApplyModel):

    def __init__(self, **kwargs):
        self.el = server_conector.ServerConector()

    def retrieve(self, request, **kwargs):
        resp_list = []
        resp_dict = {}

        data = request.get_json()
        if not data:
            resp_dict['status'] = 'Error'
            resp_dict['status_desc'] = 'Nenhum json encontrado.'
            return jsonify(resp_dict), 400

        field = data.pop('field', None)
        if not field:
            resp_dict['status'] = 'Error'
            resp_dict['status_desc'] = 'Campo field não ' + \
                'especificado.'
            return jsonify(resp_dict), 400

        value = data.pop('value', None)
        if not value:
            resp_dict['status'] = 'Error'
            resp_dict['status_desc'] = 'Campo value não ' + \
                'especificado.'
            return jsonify(resp_dict), 400

        resp_list = self.el.retrieve_el(
            index='shop_store_sales_team_apply',
            unique_hash_field=field,
            unique_hash_value=value,
            model=self.get_index_fields())

        return jsonify(resp_list['resp_list']), resp_list['status_code']

    def retrieve_id(self, request, **kwargs):
        resp_dict = {}

        data = request.get_json()
        if not data:
            resp_dict = {}
            resp_dict['status'] = 'Error'
            resp_dict['status_desc'] = 'Nenhum json encontrado.'
            return jsonify(resp_dict), 400

        _id = data.pop('doc_id', None)
        if not _id:
            resp_dict['status'] = 'Error'
            resp_dict['status_desc'] = 'Campo doc_id não especificado.'
            return jsonify(resp_dict), 400

        res = self.el.retrieve_id_el(
            index='shop_store_sales_team_apply',
            _id=_id,
            model=self.get_index_fields())

        return jsonify(res), res['status_code']

    def update(self, request):
        # app.logger.error('LOGIN_TEXT2')
        resp_dict = {}

        data = request.get_json()
        if not data:
            resp_dict = {}
            resp_dict['status'] = 'Error'
            resp_dict['status_desc'] = 'Nenhum json encontrado.'
            return jsonify(resp_dict), 400

        _id = data.pop('doc_id', None)
        if not _id:
            resp_dict['status'] = 'Error'
            resp_dict['status_desc'] = 'Campo doc_id não especificado.'
            return jsonify(resp_dict), 400

        if not data.get('last_update_user', ''):
            resp_dict['status'] = 'Error'
            resp_dict['status_desc'] = 'Campo last_update_user não ' + \
                'especificado.'
            return jsonify(resp_dict), 400

        for key in data:
            resp_dict[key] = data[key]

        resp_dict['last_update'] = datetime.datetime.now()

        res = self.el.update_el(
            index='shop_store_sales_team_apply',
            _id=_id,
            data=resp_dict)

        resp_dict['status'] = res['status']
        if res['status'] == 'Error':
            resp_dict['status_desc'] = 'Erro ao editar documento.'
        else:
            resp_dict['status_desc'] = 'Documento editado com sucesso.'

        return jsonify(resp_dict), res['status_code']

    def insert(self, request):
        # app.logger.error('LOGIN_TEXT2')
        resp_dict = {}

        data = request.get_json()
        if not data:
            resp_dict = {}
            resp_dict['status'] = 'Error'
            resp_dict['status_desc'] = 'Nenhum json encontrado.'
            return jsonify(resp_dict), 400

        unique_store_hash = data.get('unique_store_hash', '')
        if not unique_store_hash:
            resp_dict['status'] = 'Error'
            resp_dict['status_desc'] = 'Campo unique_store_hash não ' + \
                'especificado.'
            return jsonify(resp_dict), 400

        unique_salesman_hash = data.get('unique_salesman_hash', '')
        if not unique_salesman_hash:
            resp_dict['status'] = 'Error'
            resp_dict['status_desc'] = 'Campo unique_salesman_hash não ' + \
                'especificado.'
            return jsonify(resp_dict), 400

        if not data.get('last_update_user', ''):
            resp_dict['status'] = 'Error'
            resp_dict['status_desc'] = 'Campo last_update_user não ' + \
                'especificado.'
            return jsonify(resp_dict), 400

        for key in data:
            resp_dict[key] = data[key]

        resp_dict['record_status'] = 'Active'
        resp_dict['creation_date'] = datetime.datetime.now()
        resp_dict['last_update'] = resp_dict['creation_date']

        res = self.el.insert_el(
            index='shop_store_sales_team_apply', data=resp_dict)

        resp_dict['status'] = res['status']
        resp_dict['doc_id'] = res['doc_id']

        if res['status'] == 'Error':
            resp_dict['status_desc'] = 'Erro ao inserir documento.'
        else:
            resp_dict['status_desc'] = 'Documento inserido com sucesso.'

        return jsonify(resp_dict), res['status_code']

    def deactivate(self, request):
        # app.logger.error('LOGIN_TEXT2')
        resp_dict = {}

        data = request.get_json()
        if not data:
            resp_dict = {}
            resp_dict['status'] = 'Error'
            resp_dict['status_desc'] = 'Nenhum json encontrado.'
            return jsonify(resp_dict), 400

        _id = data.pop('doc_id', None)
        if not _id:
            resp_dict['status'] = 'Error'
            resp_dict['status_desc'] = 'Campo doc_id não especificado.'
            return jsonify(resp_dict), 400

        if not data.get('last_update_user', ''):
            resp_dict['status'] = 'Error'
            resp_dict['status_desc'] = 'Campo last_update_user não ' + \
                'especificado.'
            return jsonify(resp_dict), 400

        resp_dict['record_status'] = 'Inactive'
        resp_dict['last_update'] = datetime.datetime.now()
        resp_dict['last_update_user'] = data.get('last_update_user', '')

        res = self.el.update_el(
            index='shop_store_sales_team_apply',
            _id=_id,
            data=resp_dict)

        resp_dict['status'] = res['status']
        if res['status'] == 'Error':
            resp_dict['status_desc'] = 'Erro ao desativar documento.'
        else:
            resp_dict['status_desc'] = 'Documento desativado com sucesso.'

        return jsonify(resp_dict), res['status_code']

    def activate(self, request):
        # app.logger.error('LOGIN_TEXT2')
        resp_dict = {}

        data = request.get_json()
        if not data:
            resp_dict = {}
            resp_dict['status'] = 'Error'
            resp_dict['status_desc'] = 'Nenhum json encontrado.'
            return jsonify(resp_dict), 400

        _id = data.pop('doc_id', None)
        if not _id:
            resp_dict['status'] = 'Error'
            resp_dict['status_desc'] = 'Campo doc_id não especificado.'
            return jsonify(resp_dict), 400

        if not data.get('last_update_user', ''):
            resp_dict['status'] = 'Error'
            resp_dict['status_desc'] = 'Campo last_update_user não ' + \
                'especificado.'
            return jsonify(resp_dict), 400

        resp_dict['record_status'] = 'Active'
        resp_dict['last_update'] = datetime.datetime.now()
        resp_dict['last_update_user'] = data.get('last_update_user', '')

        res = self.el.update_el(
            index='shop_store_sales_team_apply',
            _id=_id,
            data=resp_dict)

        resp_dict['status'] = res['status']
        if res['status'] == 'Error':
            resp_dict['status_desc'] = 'Erro ao ativar documento.'
        else:
            resp_dict['status_desc'] = 'Documento ativado com sucesso.'

        return jsonify(resp_dict), res['status_code']

    def delete(self, request):
        # app.logger.error('LOGIN_TEXT2')
        resp_dict = {}

        data = request.get_json()
        if not data:
            resp_dict = {}
            resp_dict['status'] = 'Error'
            resp_dict['status_desc'] = 'Nenhum json encontrado.'
            return jsonify(resp_dict), 400

        _id = data.pop('doc_id', None)
        if not _id:
            resp_dict['status'] = 'Error'
            resp_dict['status_desc'] = 'Campo doc_id não especificado.'
            return jsonify(resp_dict), 400

        if not data.get('last_update_user', ''):
            resp_dict['status'] = 'Error'
            resp_dict['status_desc'] = 'Campo last_update_user não ' + \
                'especificado.'
            return jsonify(resp_dict), 400

        resp_dict['record_status'] = 'Deleted'
        resp_dict['last_update'] = datetime.datetime.now()
        resp_dict['last_update_user'] = data.get('last_update_user', '')

        res = self.el.update_el(
            index='shop_store_sales_team_apply',
            _id=_id,
            data=resp_dict)

        resp_dict['status'] = res['status']
        if res['status'] == 'Error':
            resp_dict['status_desc'] = 'Erro ao deletar documento.'
        else:
            resp_dict['status_desc'] = 'Documento deletado com sucesso.'

        return jsonify(resp_dict), res['status_code']
