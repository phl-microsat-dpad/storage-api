import json
from storage_api import app, db, models

@app.route('/')
def index():
    return "hi!"


@app.route('/scenes', methods=['GET'])
def get_scenes():
    users = models.Scene.query.all()
    return json.dumps(users)


@app.route('/scenes/<scene_id>', methods=['GET'])
def get_scene(scene_id):
    user = models.Scene.query.get(scene_id)
    return json.dumps({'success': True})


@app.route('/scenes', methods=['POST'])
def create_scene():
    return json.dumps({'success': True})


@app.route('/scenes/<scene_id>', methods=['PATCH'])
def update_scene(scene_id):
    return json.dumps({'success': True})


@app.route('/scenes/<scene_id>', methods=['DELETE'])
def delete_scene(scene_id):
    return json.dumps({'success': True})


@app.route('/products', methods=['GET'])
def get_products():
    return json.dumps([])

