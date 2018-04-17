from flask import Flask, request, render_template, jsonify

from songkick_api.sk_api_mgr import log
from songkick_api.sk_event import Event
from songkick_api import sk_api_mgr as api_mgr

app = Flask(__name__)


@app.route('/events')
def build_response():
    request_ip = request.remote_addr
    print('Request IP: ' + str(request_ip))
    response_data = build_events(request)
    return jsonify(response_data), 200


@app.route('/')
def hello_world():
    return render_template("hello.html")


@app.route('/goodbye')
def goodbye_world():
    return render_template("goodbye.html")


def build_events(req: request) -> [Event]:

    # client_ip = req.remote_addr
    #  TODO When running this non-locally: uncomment this line AND comment out the line below
    client_ip = '75.73.22.98'

    log('Events requested from: ' + str(client_ip))

    api_data = api_mgr.search_local_events_for_ip(client_ip)

    events_objects_list = api_mgr.instantiate_events_from_list(api_data)

    serialized_events_list = api_mgr.serialize_event_list(events_objects_list)

    return serialized_events_list



