from bottle import get, post, run, request, response
from json import dumps

"""
curl -X POST -H 'Content-Type: application/json' -d '{"name": "alan", "born": 1903}' http://127.0.0.1:8888/customers
curl http://127.0.0.1:8888/customers/alan
"""

customers = {}

@get('/customers')
def all_customers():
    response.content_type = 'application/json'
    return dumps(customers.values())

@get('/customers/<name>')
def get_customer(name=None):
    customer = customers.get(name, None)
    if customer:
        return customer
    else:
        response.status = 404
        return 'Customer {} not found.'.format(name)

@post('/customers')
def create_customer():
    customer = request.json
    name = customer['name']
    customers[name] = customer
    return {'status': 'ok'}

customers['ada'] = {'name': 'ada', 'born': 1815}

run(host='0.0.0.0', port=8888, debug=True)
