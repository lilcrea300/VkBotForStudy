import vk_api, json, datetime, calendar
from vk_api import VkUpload
from vk_api.longpoll import VkLongPoll, VkEventType
vk_session = vk_api.VkApi(token="00049c8624190cd099b2faf8ad213e727443771f84c4d0f5ceb2d98e6b4149dd3be19841569a507e028d5")
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

image = "C:/Users/parahin/Downloads/n6HDhY77PDM.jpg"
image2 = "C:/Users/parahin/Downloads/n6HDhY77PDM.jpg"

data = datetime.datetime.now()
print(data.strftime("%A %d %B %Y %T"))
cl = calendar.monthcalendar(2021, 2)
print(cl)

upload = VkUpload(vk_session)
upload2 = VkUpload(vk_session)




def get_but(text, color):
    return {
        "action": {
            "type": "text",
            "payload": "{\"button\": \"" + "1" + "\"}",
            "label": f"{text}"
        },
        "color": f"{color}"
    }

k = {
    "one_time": False,
    "buttons": [
        [get_but('Начать', 'primary')]
    ]
}

k = {
    "one_time": False,
    "buttons": [
        [get_but('Расписание звонков', 'primary')],[get_but('Подписаться на уведомления', 'secondary')], [get_but('Расписание пар', 'primary')], [get_but('Калькулятор', 'secondary')]

    ]
}

def get_but2(text, color):
    return {
        "action": {
            "type": "text",
            "payload": "{\"button\": \"" + "1" + "\"}",
            "label": f"{text}"
        },
        "color": f"{color}"
    }


k2 = {
    "one_time": False,
    "buttons": [
        [get_but('Расписание пар', 'primary')]

    ]
}
k2 = {
    "one_time": False,
    "buttons": [
        [get_but('1 курс', 'secondary')], [get_but('Назад 💭', 'negative')]

    ]
}
def get_but3(text, color):
    return {
        "action": {
            "type": "text",
            "payload": "{\"button\": \"" + "1" + "\"}",
            "label": f"{text}"
        },
        "color": f"{color}"
    }

k3 = {
    "one_time": False,
    "buttons": [
        [get_but('ИБС-125', 'secondary')], [get_but('Назад ⛄', 'negative')]

    ]
}

def get_but4(text, color):
    return {
        "action": {
            "type": "text",
            "payload": "{\"button\": \"" + "1" + "\"}",
            "label": f"{text}"
        },
        "color": f"{color}"
    }

k4 = {
    "one_time": False,
    "buttons": [
        [get_but('Понедельник', 'secondary'), get_but('Вторник', 'secondary')],
        [get_but('Среда', 'secondary'), get_but('Четверг', 'secondary'), get_but('Пятница', 'secondary')],
        [get_but('В главное меню 💿', 'negative')]
    ]
}
def get_but5(text, color):
    return {
        "action": {
            "type": "text",
            "payload": "{\"button\": \"" + "1" + "\"}",
            "label": f"{text}"
        },
        "color": f"{color}"
    }

k6 = {
    "one_time": False,
    "buttons": [
        [get_but('7', 'secondary'), get_but('8', 'secondary'), get_but('9', 'secondary')],
        [get_but('4', 'secondary'), get_but('5', 'secondary'), get_but('6', 'secondary')],
        [get_but('1', 'secondary'), get_but('2', 'secondary'), get_but('3', 'secondary')],
        [get_but('0', 'secondary'), get_but('+', 'primary')]
    ]
}

k = json.dumps(k, ensure_ascii=False).encode('utf-8')
k = str(k.decode('utf-8'))
k2 = json.dumps(k2, ensure_ascii=False).encode('utf-8')
k2 = str(k2.decode('utf-8'))
k3 = json.dumps(k3, ensure_ascii=False).encode('utf-8')
k3 = str(k3.decode('utf-8'))
k4 = json.dumps(k4, ensure_ascii=False).encode('utf-8')
k4 = str(k4.decode('utf-8'))
k6 = json.dumps(k6, ensure_ascii=False).encode('utf-8')
k6 = str(k6.decode('utf-8'))


attachments1 = []
upload_image = upload.photo_messages(photos=image)[0]
attachments1.append("photo{}_{}".format(upload_image["owner_id"], upload_image["id"]))

attachments2 = []
upload_image2 = upload.photo_messages(photos=image2)[0]
attachments2.append("photo{}_{}".format(upload_image2["owner_id"], upload_image2["id"]))



def sender(id, text):
    vk_session.method('messages.send', {'user_id': id, 'message': text, 'random_id': 0, 'keyboard': k})

def sender1(id, text):
    vk_session.method('messages.send', {'user_id': id, 'message': text, 'random_id': 0, 'keyboard': k2})

def sender2(id):
    vk_session.method('messages.send', {'user_id': id, 'random_id': 0, 'attachment': ','.join(attachments1)})

def sender3(id, text):
    vk_session.method('messages.send', {'user_id': id, 'message': text, 'random_id': 0, 'keyboard': k3})

def sender4(id, text):
    vk_session.method('messages.send', {'user_id': id, 'message': text, 'random_id': 0, 'keyboard': k4})

def sender5(id):
    vk_session.method('messages.send', {'user_id': id, 'random_id': 0, 'attachment': ','.join(attachments2)})

def sender6(id, text):
    vk_session.method('messages.send', {'user_id': id, 'message': text, 'random_id': 0, 'keyboard': k6})

def sender7(id, text):
    vk_session.method('messages.send', {'user_id': id, 'message': text, 'random_id': 0, 'keyboard': k7})

def main():
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            if event.to_me:
                name = vk_session.method("users.get", {"user_ids": event.user_id})
                name0 = name[0]["first_name"]
                name1 = name[0]["last_name"]
                request = event.text.lower()
                request2 = event.text.lower()
            if request == "в главное меню 💿":
                sender(event.user_id, "Возвращаем Вас в главное меню, " + " " + name0 + " " + name1 + "! 🎅")
            if request == "назад ⛄":
                sender1(event.user_id, "Возвращаем Вас во вкладку курс, " + " " + name0 + " " + name1 + "! ⛅")
            if request == "назад 💭":
                sender(event.user_id, "Возвращаем Вас в главное меню, " + " " + name0 + " " + name1 + "! ⛅" )
            if request == "подписаться на уведомления":
                sender(event.user_id, "Вы успешно подписались на уведомления, " + " " + name0 + " " + name1 + "! 🦆")
            if request == "начать":
                sender(event.user_id, "Привет, я ЛилКрякБот, " + " " + name0 + " " + name1 + "! 🦆")
            if request == "начать":
                sender(event.user_id, "Я создан для того, чтобы отправлять твоё расписание!")
            if request == "расписание пар":
                sender1(event.user_id, "Выберите Ваш курс," + " " + name0 + " " + name1 + "! 🧜‍♂")
            if request == "расписание звонков":
                sender2(event.user_id)
            if request == "расписание звонков":
                sender5(event.user_id)
            if request == "1 курс":
                sender3(event.user_id, "Выберите Вашу группу," + " " + name0 + " " + name1 + "! 🤠")
            if request == "исб":
                sender3(event.user_id, "Секунду... " + " " + name0 + " " + name1 + "! 🚀")
            if request == "ибс-125":
                sender4(event.user_id, "Выберите день недели," + " " + name0 + " " + name1 + "! 😇")
            if request == "понедельник":
                sender4(event.user_id, "Вот твоё расписание на сегодня!\n1)Иностранный язык в ПД/Математика - 9:00 ➡ 10:30 \n2)Организационно-правовое обеспечение информационной безопасности - 10:40 ➡ 12:10 \n3)История - 12:30 ➡ 14:00 \n4)Базы данных/Операционные системы - 14:10 ➡ 15:40, \n❤ " + name0 + " " + name1 + "!")
            if request == "вторник":
                sender4(event.user_id, "Вот твоё расписание на сегодня!\n1)Организационно-правовое обеспечение информационной безопасности/Основы алгоритмизации и программирования - 9:00 ➡ 10:30 \n2)Математика - 10:40 ➡ 12:10 \n3)Правовое обеспечение профессиональной деятельности - 12:30 ➡ 14:00 \n4)Базы данных - 14:10 ➡ 15:40, \n❤ " + name0 + " " + name1 + "!")
            if request == "среда":
                sender4(event.user_id, "Вот твоё расписание на сегодня!\n1)Основы алгоритмизации и программирования - 9:00 ➡ 10:30 \n2)Электротехника и схемотехника - 10:40 ➡ 12:10 \n3)Документационное обеспечение управления - 12:30 ➡ 14:00, \n❤" + name0 + " " + name1 + "!")
            if request == "четверг":
                sender4(event.user_id, "Вот твоё расписание на сегодня!\n1)Информатика - 9:00 ➡ 10:30 \n2)Иностранный язык в ПД - 10:40 ➡ 12:10 \n3)Операционные системы - 12:30 ➡ 14:00 \n4)Консультации/самостоятельная работа по графику - 14:10 ➡ 15:40, \n❤ " + name0 + " " + name1 + "!")
            if request == "пятница":
                sender4(event.user_id, "Вот твоё расписание на сегодня!\n1)СОН - 9:00 ➡ 10:30 \n2)Организационно-правовое обеспечение информационной безопасности - 10:40 ➡ 12:10 \n3)Теория вероятностей - 12:30 ➡ 14:00 \n4)Физическая культура - 14:10 ➡ 15:40, \n❤ " + name0 + " " + name1 + "!")
            if request == "калькулятор":
                sender6(event.user_id, "Введите первое число: ")
                a = int(input(request))
            if request == "Введите второе число: ":
                sender6(event.user_id, "Ваш результат: ")
                b = int(input(request2))
                if request == "ваш результат":
                    suma = a + b
                    sender6(event.user_id, suma)
            print("Имя пользователя - " + name0 + " " + name1)
            print("Сообщение от пользователя - " + request)







main()
