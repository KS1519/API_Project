from flask import Flask
from calendar import CalendarAPI

app = Flask(__name__)
calendar_api = CalendarAPI()

@app.route('/api/v1/calendar/event', methods=['POST'])
def create_event():
    return calendar_api.create_event()

@app.route('/api/v1/calendar/events', methods=['GET'])
def get_events():
    return calendar_api.get_events()

@app.route('/api/v1/calendar/event/<event_id>', methods=['GET'])
def get_event(event_id):
    return calendar_api.get_event(event_id)

@app.route('/api/v1/calendar/event/<event_id>', methods=['PUT'])
def update_event(event_id):
    return calendar_api.update_event(event_id)

@app.route('/api/v1/calendar/event/<event_id>', methods=['DELETE'])
def delete_event(event_id):
    return calendar_api.delete_event(event_id)

if __name__ == '__main__':
    app.run(debug=True)