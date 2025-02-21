from DiaryApp.entry import Entry


class MyDiary:
    def __init__(self, user_name, password):
        self.is_diary_exist = True
        self.is_empty_diary = True
        self.user_name = user_name
        self.password = password
        self.is_diary_locked = True
        self.entry_id = 1
        self.entries = []

    def get_user_name(self):
        return self.user_name

    def is_exist(self):
        return self.is_diary_exist

    def is_locked(self):
        return self.is_diary_locked

    def is_empty(self):
        return self.is_empty_diary

    def unlock_diary(self, password):
        if self.password == password:
            self.is_diary_locked = False
        else:
            raise ValueError("Incorrect username or password. Try Again!")

    def lock_diary(self):
        return self.is_diary_locked

    def create_entry(self, title, body):
        entry = Entry(self.entry_id, title, body)
        self.entries.append(entry)
        self.entry_id += 1

    def delete_entry(self, entry_id):
        entry_to_delete = self.find_entry_by_id(entry_id)
        if entry_to_delete:
            self.entries.remove(entry_to_delete)

    def find_entry_by_id(self, entry_id):
        for entry in self.entries:
            if entry.get_id() == entry_id:
                return entry
        return None

    def update_entry(self, entry_id, title, body):
        entry_to_update = self.find_entry_by_id(entry_id)
        if entry_to_update:
            entry_to_update.set_title(title)
            entry_to_update.set_body(body)

    def view_entry(self, entry_id):
        entry = self.find_entry_by_id(entry_id)
        if entry:
            return str(entry)
        return None