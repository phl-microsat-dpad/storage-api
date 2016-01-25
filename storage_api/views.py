import json
from flask import request
from sqlalchemy.exc import IntegrityError
from storage_api import app, db, models


@app.route('/')
def index():
    return "hi!"


@app.route('/scenes', methods=['GET'])
def get_scenes():
    scenes = models.Scene.query.all()

    json_scenes = [scene.serialize for scene in scenes]
    return json.dumps(json_scenes)


@app.route('/scenes/<scene_id>', methods=['GET'])
def get_scene(scene_id):
    scene = models.Scene.query.get(scene_id)

    if scene is None:
        return "Scene not found", 404
    else:
        return json.dumps(scene.serialize)


@app.route('/scenes', methods=['POST'])
def create_scene():
    try:
        scene = models.Scene(
            scene_id=request.form['scene_id'],
            bundle_size=request.form['bundle_size'],
            bundle_url=request.form.get('bundle_url'),
            bundle_hash=request.form.get('bundle_hash'))
    except KeyError:
        return 'A required parameter is missing!', 422

    try:
        db.session.add(scene)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return "Scene already exists!", 409

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
