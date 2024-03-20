from calendar import CalendarAPI

class CalendarAPI:
    def __init__(self):
        self.events = []

    def create_event(self, event_data):
        date, title, text = event_data.split('|')

        if len(title) > 30 or len(text) > 200:
            return "Ошибка: Превышена максимальная длина"

        for event in self.events:
            if event['date'] == date:
                return "Ошибка: Нельзя добавить более одного события в день"

        new_event = {
            'id': len(self.events) + 1,
            'date': date,
            'title': title,
            'text': text
        }
        self.events.append(new_event)
        return "Событие создано"

    def get_events(self):
        return self.events

    def get_event(self, event_id):
        for event in self.events:
            if event['id'] == int(event_id):
                return event
        return "Событие не найдено"

    def update_event(self, event_id, event_data):
        for event in self.events:
            if event['id'] == int(event_id):
                date, title, text = event_data.split('|')
                event['date'] = date
                event['title'] = title
                event['text'] = text
                return "Событие обновлено"
        return "Событие не найдено"

    def delete_event(self, event_id):
        for event in self.events:
            if event['id'] == int(event_id):
                self.events.remove(event)
                return "Событие удалено"
        return "Событие не найдено"