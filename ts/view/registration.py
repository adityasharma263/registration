from ts.model.registration import Application
from ts import app
from sqlalchemy import or_
from flask import jsonify, request
from ts.schema.registration import ApplicationSchema


@app.route('/api/v1/application', methods=['GET', 'POST'])
def patner_api():
    if request.method == 'GET':
        args = request.args.to_dict()
        args.pop('page', None)
        args.pop('per_page', None)
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))
        data = Application.query.filter_by(**args).offset((int(page) - 1) * int(per_page)).limit(int(per_page)).all()
        result = ApplicationSchema(many=True).dump(data)
        return jsonify({'result': {'applications': result.data}, 'message': "Success", 'error': False})
    else:
        post = Application(**request.json)
        post.save()
        result = ApplicationSchema().dump(post)
        return jsonify({'result': {'application': result.data}, 'message': "Success", 'error': False})


@app.route('/api/v1/partner/<int:id>', methods=['PUT', 'DELETE'])
def partner_id(id):
    if request.method == 'PUT':
        put = Application.query.filter_by(id=id).update(request.json)
        if put:
            Application.update_db()
            s = Application.query.filter_by(id=id).first()
            result = ApplicationSchema(many=False).dump(s)
            return jsonify({'result': result.data, "status": "Success", 'error': False})
    else:
        partners = Application.query.filter_by(id=id).first()
        if not partners:
            return jsonify({'result': {}, 'message': "No Found", 'error': True})
        Application.delete_db(partners)
        return jsonify({'result': {}, 'message': "Success", 'error': False})