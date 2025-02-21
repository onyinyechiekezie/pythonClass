class Entry:
    def __init__(self, entry_id, title, body):
        self.entry_id = entry_id
        self.title = title
        self.body = body

    def get_id(self):
        return self.entry_id

    def set_title(self, title):
        self.title = title

    def set_body(self, body):
        self.body = body

    def __str__(self):
        return f"Entry ID: {self.entry_id}\nTitle: {self.title}\nBody: {self.body}"
