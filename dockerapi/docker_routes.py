"""
docker_routes.py contains routes related to Docker engine API.
Reference: https://docs.docker.com/engine/api/v1.41/
"""

try:
    import sys
    import logging
    import random
    from dockerapi.utils import Utils
    from dockerapi.docker_consts import *
    from flask import Flask, request, jsonify
except ImportError as ierr:
    print("[!] Import error %s" % ierr)
    sys.exit(1)

util = Utils()
customLog = util.setup_logger("app_log")

app = Flask(__name__)


@app.route('/<version>/version', methods=["GET", "POST"])
@app.route('/<version>/info', methods=["GET", "POST"])
def api_version_info(version):
    """
    Return Docker API version https://docs.docker.com/engine/api/v1.41/#section/Versioning
    :param version: Docker API Engine
    :return: constant value of API engine
    """

    logging.info("api_version_info - %s, %s, %s, %s, %s" % (
        version, request.remote_addr, request.user_agent, request.data, request.url))
    req_objs = util.save_request_obj(request)
    customLog.info(req_objs)
    return API_VERSION


@app.route('/info', methods=["GET", "POST"])
@app.route('/version', methods=["GET", "POST"])
def api_info():
    """
    Return Docker API version https://docs.docker.com/engine/api/v1.41/#section/Versioning
    :return:  constant value of API_VERSION
    """
    logging.info("info -  %s, %s, %s, %s" % (request.remote_addr, request.user_agent, request.data, request.url))
    req_objs = util.save_request_obj(request)
    customLog.info(req_objs)
    return API_VERSION


@app.route('/<version>/images/json', methods=["GET"])
def api_images_list_json(version):
    """
    Return Docker Image listing https://docs.docker.com/engine/api/v1.41/#tag/Image
    :param version: Docker API version
    :return: string of fake images associated with honeypot.
    """

    logging.info("images-list - %s, %s, %s, %s, %s" % (
        version, request.remote_addr, request.user_agent, request.data, request.url))
    req_objs = util.save_request_obj(request)
    customLog.info(req_objs)
    return API_RESP_IMAGES_JSON_LIST


@app.route('/<version>/containers/json', methods=["GET"])
def api_containers_list(version):
    """
    Return Docker containers https://docs.docker.com/engine/api/v1.41/#operation/ContainerList
    :return: string of fake containers
    """

    logging.info("container-list - %s, %s, %s, %s, %s" % (
        version, request.remote_addr, request.user_agent, request.data, request.url))
    req_objs = util.save_request_obj(request)
    customLog.info(req_objs)
    return API_RESP_CONTAINERS_JSON_LIST


@app.route('/<version>/containers/json', methods=["GET"])
def api_containers_list_v124(version):
    """
    Return Docker containers https://docs.docker.com/engine/api/v1.41/#operation/ContainerList
    :return: string of fake containers
    """
    logging.info("container-list - %s, %s, %s, %s, %s" % (
        version, request.remote_addr, request.user_agent, request.data, request.url))
    req_objs = util.save_request_obj(request)
    customLog.info(req_objs)
    return API_RESP_CONTAINERS_JSON_LIST


@app.route('/_ping', methods=["GET", "HEAD"])
def api_ping():
    """
    Return dummy endpoint https://docs.docker.com/engine/api/v1.41/#operation/SystemPingHead
    :return:  200
    """
    logging.info(
        "docker-ping -list - %s, %s, %s, %s" % (request.remote_addr, request.user_agent, request.data, request.url))
    req_objs = util.save_request_obj(request)
    customLog.info(req_objs)
    return "200"


@app.route('/<version>/containers/create', methods=["POST"])
def api_containers_create(version):
    """
    Create Docker container endpoint https://docs.docker.com/engine/api/v1.41/#operation/ContainerCreate
    :param version: Docker engine API version
    :return: JSON string of "API containers created"
    """

    logging.info("container-create - %s, %s, %s, %s, %s" % (
        version, request.remote_addr, request.user_agent, request.data, request.url))
    req_objs = util.save_request_obj(request)
    customLog.info(req_objs)
    # Add a chance for a failure condition during creation to be returned to the attacker
    if random.randint(1, 100) % 2 == 0:
        return API_RESP_CONTAINERS_JSON_CREATE
    else:
        return API_RESP_CONTAINERS_JSON_CREATE_NO_SUCH_CONTAINER


@app.route('/images/create', methods=["POST"])
def api_images_create():
    """
    https://docs.docker.com/engine/api/v1.41/#operation/ImageCreate
    Mocking create an image, note at the time of this development the APIs don't have a actual response.
    :return: status 200
    """
    req_objs = util.save_request_obj(request)
    customLog.info(req_objs)
    return "200"


@app.route('/containers/<id>/json', methods=["GET"])
def api_containers_json_list(id):
    """
    :param id: Container ID to access
    :return: string value indicating success or failure based on modulus calculation
    """
    logging.info(
        "container-create - %s, %s, %s, %s" % (request.remote_addr, request.user_agent, request.data, request.url))
    req_objs = util.save_request_obj(request)
    customLog.info(req_objs)
    if random.randint(1, 100) % 2 == 0:
        return API_RESP_CONTAINERS_JSON_CREATE
    else:
        return API_RESP_CONTAINERS_JSON_CREATE_NO_SUCH_CONTAINER


@app.route('/containers/<id>/logs', methods=["GET"])
def api_containers_log(id):
    """
    :param id: string value indicating container ID to attach to
    :return: Generic API Docker error
    """
    logging.info(
        "container-log - %s, %s, %s, %s" % (request.remote_addr, request.user_agent, request.data, request.url))
    customLog.info("container-log, %s, %s, %s, %s, %s" % (
        "N/A", request.remote_addr, request.user_agent, request.data, request.url))
    req_objs = util.save_request_obj(request)
    customLog.info(req_objs)
    return API_SOMETHING_WENT_WRONG


@app.route('/containers/<id>/export', methods=["GET"])
def api_containers_export(id):
    """
    :param id: container ID to export
    :return: Generic API Docker error
    """
    logging.info("container-export, %s, %s, %s, %s, %s" % (
        "N/A", request.remote_addr, request.user_agent, request.data, request.url))
    req_objs = util.save_request_obj(request)
    customLog.info(req_objs)
    return API_SOMETHING_WENT_WRONG


@app.route('/containers/<id>/attach', methods=["POST"])
def api_containers_attach(id):
    """
    :param id: string value of Container ID
    :return:  Generic API Docker error
    """

    logging.info("container-attach, %s, %s, %s, %s, %s" % (
        "N/A", request.remote_addr, request.user_agent, request.data, request.url))
    req_objs = util.save_request_obj(request)
    customLog.info(req_objs)

    return API_SOMETHING_WENT_WRONG


@app.route('/build', methods=["POST"])
def api_build():
    """
    Docker API for building an image https://docs.docker.com/engine/api/v1.41/#operation/ImageBuild
    :return: Generic API Docker error
    """
    logging.info("container-build, %s, %s, %s, %s, %s" % (
        "N/A", request.remote_addr, request.user_agent, request.data, request.url))
    req_objs = util.save_request_obj(request)
    customLog.info(req_objs)
    return API_SOMETHING_WENT_WRONG


@app.route('/build/prune', methods=["POST"])
def api_build_prune():
    """
    Docker API for deleting builder cache https://docs.docker.com/engine/api/v1.41/#operation/BuildPrune
    :return: JSON string claiming data was pruned.
    """
    logging.info(
        "prune,  %s, %s, %s, %s, %s" % ("N/A", request.remote_addr, request.user_agent, request.data, request.url))
    req_objs = util.save_request_obj(request)
    customLog.info(req_objs)
    return API_RESP_BUILD_PRUNE


@app.route('/images/<name>/json', methods=["GET"])
def api_images_inspect_json(name):
    """
    Docker Engine API reference: https://docs.docker.com/engine/api/v1.41/#operation/ImageInspect
    :param name: name of image to inspect
    :return: JSON string of fake image data.
    """
    logging.info("images-inspect,  %s, %s, %s, %s, %s" % (
        "N/A", request.remote_addr, request.user_agent, request.data, request.url))
    req_objs = util.save_request_obj(request)
    customLog.info(req_objs)
    return API_RESP_IMAGES_JSON_INSPECT


@app.route('/images/<name>/push', methods=["POST"])
def api_images_push(name):
    """
    Docker Engine API reference: https://docs.docker.com/engine/api/v1.41/#operation/ImagePush
    :param name: Name of image to push
    :return:
    """
    logging.info("container-push, %s, %s, %s, %s, %s" % (
        "N/A", request.remote_addr, request.user_agent, request.data, request.url))
    req_objs = util.save_request_obj(request)
    customLog.info(req_objs)
    return API_SOMETHING_WENT_WRONG


@app.route('/images/<name>', methods=["DELETE"])
def api_images_delete(name):
    """
    Docker engine API reference: https://docs.docker.com/engine/api/v1.41/#operation/ImageDelete
    :param name: Name of image to delete
    :return: string indicating an image was deleted
    """
    logging.info("container-delete, %s, %s, %s, %s, %s" % (
        "N/A", request.remote_addr, request.user_agent, request.data, request.url))
    req_objs = util.save_request_obj(request)
    customLog.info(req_objs)
    return '[\n{\n\t"Untagged": "32f21a892" } ]'


@app.route('/commit', methods=["POST"])
def api_images_commit(name):
    """
    Docker engine API reference: https://docs.docker.com/engine/api/v1.41/#operation/ImageCommit
    :param name: Name of image to commit
    :return: JSON string data indicating image was commited.
    """
    logging.info("container-commit,  %s, %s, %s, %s, %s" % (
        "N/A", request.remote_addr, request.user_agent, request.data, request.url))
    req_objs = util.save_request_obj(request)
    customLog.info(req_objs)
    return API_RESP_COMMIT


@app.route('/exec/<id>/start', methods=["POST"])
def api_container_exec(id):
    """
    Docker reference: https://docs.docker.com/engine/api/v1.41/#operation/ContainerExec
    :param id: container ID to start
    :return: Return generic API engine error
    """
    logging.info("container-exec, %s, %s, %s, %s, %s" % (
        "N/A", request.remote_addr, request.user_agent, request.data, request.url))
    req_objs = util.save_request_obj(request)
    customLog.info(req_objs)
    return API_SOMETHING_WENT_WRONG


@app.errorhandler(Exception)
def all_exception_handler(error):
    """
    Catch all for all API errors. This log lets us know what APIs we're not emulating appropriately or odd requests sent
    our way.
    :param error: handle the error
    :return: default Docker API error that exists for all API requests.
    """
    logging.error(
        "api-error,  %s, %s, %s, %s, %s" % ("N/A", request.remote_addr, request.user_agent, request.data, request.url))
    req_objs = util.save_request_obj(request)
    customLog.info(req_objs)
    return API_SOMETHING_WENT_WRONG