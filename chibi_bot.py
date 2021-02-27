import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id

# Vk API
token = '6c9fda8bb0392af480cb06eac528f830cd4e876521957fd9ad08e11d2e2b45a7caecc68f71982788a00a5'
autorize = vk_api.VkApi(token=token)
longpoll = VkLongPoll(autorize)

keyboard = VkKeyboard(one_time=False)
keyboard_1 = VkKeyboard(one_time=False)
keyboard_2 = VkKeyboard(one_time=False)
keyboard_3 = VkKeyboard(one_time=False)
keyboard_4 = VkKeyboard(one_time=False)
keyboard_5 = VkKeyboard(one_time=False)


# Create Button
class Button:
    global keyboard_1, keyboard_2, keyboard_3, keyboard_4, keyboard_5

    def __init__(self, text, color=None, lines=None, count=None):
        self.text = text
        self.color = color
        self.lines = lines
        self.count = count

        if lines == 1:
            keyboard.add_line()

        if color == 'red':
            color = VkKeyboardColor.NEGATIVE
        elif color == 'green':
            color = VkKeyboardColor.POSITIVE
        elif color == 'blue':
            color = VkKeyboardColor.PRIMARY
        else:
            color = VkKeyboardColor.PRIMARY

        if count == 1:
            keyboard_1.add_button(text, color, lines)
        elif count == 2:
            keyboard_2.add_button(text, color, lines)
        elif count == 3:
            keyboard_3.add_button(text, color, lines)
        elif count == 4:
            keyboard_4.add_button(text, color, lines)
        elif count == 5:
            keyboard_5.add_button(text, color, lines)
        else:
            keyboard.add_button(text, color, lines)


# Create Message
def bot_main():
    global keyboard_1, keyboard_2, keyboard_3, keyboard_4, keyboard_5

    def menu():

        # ════════════════════════════════════
        #           @  Gl.Menu  @
        # ════════════════════════════════════
        Button('Посмотреть на чиби &#128064;', color='blue')
        Button('Магазин &#127978;', lines=1)
        Button('Работа &#127981;')
        Button('Обмен &#128200;', lines=1)
        Button('Бонус &#127873;')
        Button('Профиль &#128100;', lines=1)
        Button('Топ &#127942;')
        Button('Донат &#128176;', lines=1)

        # ════════════════════════════════════
        #           @  Menu Shop  @
        # ════════════════════════════════════
        Button('Выход &#128281;', count=1)

        # ════════════════════════════════════
        #           @  Menu Work  @
        # ════════════════════════════════════

        Button('Устроиться на работу', count=2)
        Button('Выход &#128281;', count=2)

        # ════════════════════════════════════
        #           @  Menu Trade  @
        # ════════════════════════════════════
        Button('Выход &#128281;', count=3)

        # ════════════════════════════════════
        #           @  Menu Profile  @
        # ════════════════════════════════════
        Button('Выход &#128281;', count=4)

        # ════════════════════════════════════
        #           @  Menu Donate  @
        # ════════════════════════════════════
        Button('Выход &#128281;', count=5)

    menu()

    def write_message(sender, message):
        if my_var == 1:
            autorize.method("messages.send",
                            dict(user_id=sender, message=message, keyboard=btn, random_id=get_random_id()))
        elif my_var == 2:
            autorize.method("messages.send",
                            dict(user_id=sender, message=message, keyboard=btn, random_id=get_random_id()))
        elif my_var == 3:
            autorize.method("messages.send",
                            dict(user_id=sender, message=message, keyboard=btn, random_id=get_random_id()))
        elif my_var == 4:
            autorize.method("messages.send",
                            dict(user_id=sender, message=message, keyboard=btn, random_id=get_random_id()))
        elif my_var == 5:
            autorize.method("messages.send",
                            dict(user_id=sender, message=message, keyboard=btn, random_id=get_random_id()))
        else:
            autorize.method("messages.send",
                            dict(user_id=sender, message=message, keyboard=keyboard.get_keyboard(),
                                 random_id=get_random_id()))

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
            received_message = event.text
            sender = event.user_id

            if received_message == 'Начать' or 'Чиби':
                text = fun.register(sender)
                write_message(sender, text)
                my_bool = True

            # Message Gl.Menu
            for i in range(0, 1):
                if i == 0:
                    my_var = 0
                    if received_message == 'Бонус 🎁':
                        write_message(sender, "Вашь бонус")
                    elif received_message == 'Топ 🏆':
                        write_message(sender, "Топ лист")
                    elif received_message == 'Посмотреть на чиби 👀':
                        write_message(sender, "Вашь чиби персонаж")

            if received_message == 'Магазин 🏪':
                my_var = 1
                btn = keyboard_1.get_keyboard()
            elif received_message == 'Работа 🏭':
                my_var = 2
                btn = keyboard_2.get_keyboard()
            elif received_message == 'Обмен 📈':
                my_var = 3
                btn = keyboard_3.get_keyboard()
            elif received_message == 'Профиль 👤':
                my_var = 4
                btn = keyboard_4.get_keyboard()
            elif received_message == 'Донат 💰':
                my_var = 5
                btn = keyboard_5.get_keyboard()
            write_message(sender, "text")


bot_main()
