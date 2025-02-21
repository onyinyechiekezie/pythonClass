from DiaryApp.my_diary import MyDiary


class Diaries:
    def __init__(self):
        self.diaries = []

    def create_diary(self, username, password):
        # Placeholder for creating a diary if needed
        pass

    def add(self, username, password):
        diary = MyDiary(username, password)
        self.diaries.append(diary)

    def find_by_username(self, username):
        for diary in self.diaries:
            if diary.get_user_name() == username:
                return diary
        return None

    def delete_diary(self, username):
        for diary in self.diaries:
            if diary.get_user_name() == username:
                self.diaries.remove(diary)
                break
