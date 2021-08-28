from common import create_app

app = create_app({
    'ejemplo_config': 'algun_valor'
})


"""
    para ejecutar la app

    export FLASK_APP=`pwd`/devapp.py
    export FLASK_DEBUG=1
    flask run
"""