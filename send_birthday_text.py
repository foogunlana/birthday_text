import csv

class User:

    def __init__(self, first_name, email, number):
        self.first_name = first_name
        self.email = email
        self.number = number

    def fb_friends(self):
        return []


def get_users():
    with open('users.csv') as handle:
        user_csv = csv.reader(handle, delimiter=',', quotechar='|')
        return [User(*data) for data in user_csv]


if __name__ == '__main__':
    users = get_users()
    for user in users:
        friends = user.fb_friends()
        for friend in friends:
            if friend.birthday_is_today():
                send_birthday_message(user, friend)
