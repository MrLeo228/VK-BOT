import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from Button import Button as VkButton

# My
from Register import long_poll, authorize

# Data Base
import DataBase




"""
btn1 = VkButton(text='Магазин &#127978;', line=True,color='blue')
btn2 = VkButton(text='Работа &#127981;',color='blue')
btn3 = VkButton(text='Обмен &#128200;', line=True,color='blue')
btn4 = VkButton(text='Бонус &#127873;',color='blue')
btn5 = VkButton(text='Профиль &#128100;', line=True,color='blue')
btn6 = VkButton(text='Топ &#127942;',color='blue')
btn7 = VkButton(text='Донат &#128176;', line=True,color='blue')

btn1.create_message(user_id=sender, message='1')
btn2.create_message(user_id=sender, message='2')
btn3.create_message(user_id=sender, message='3')
btn4.create_message(user_id=sender, message='4')
btn5.create_message(user_id=sender, message='5')
btn6.create_message(user_id=sender, message='6')
btn7.create_message(user_id=sender, message='7')
"""

btn = VkButton(text='Начать', keyboard=VkKeyboard(one_time=True))
btn1 = VkButton(text='Shop', color='green')

for event in long_poll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:

        received_message = event.text
        sender = event.user_id
        register = DataBase.check_register_user(sender)

        if not register:
            btn.create_message(user_id=sender, message='Привет чибик :)')
            if received_message == 'Начать':
                register_user = DataBase.register_user(user_id=sender)



            #register_user = DataBase.register_user(user_id=sender)
        #else:
            #btn1.create_message(user_id=sender, message='-')

        #if not register:
        #    btn.create_message(user_id=sender, message='Регистрация прошла успешно')

        #if received_message == 'Начать':
        #    if not register:
        #        register_user = DataBase.register_user(user_id=sender)
        #        btn.create_message(user_id=sender, message='Регистрация прошла успешно')
        #        btn.clear(user_id=sender, message='Вы уже зарегестрированы :)')
        #    else:
        #        btn1.create_message(user_id=sender, message='-')

        #if received_message == 'Чиби':
            #btn.create_message(user_id=sender, message='-')


            #if

            #register_user = DataBase.register_user(user_id=sender)



        #if received_message == 'del':
        #    btn.clear(user_id=sender,message='')
        #else:
        #    btn.create_message(user_id=sender, message='1')

        """if received_message == 'Чиби' and my_bool == False:
            btn.create_message(user_id=sender, message='1')
            register_user = DataBase.register_user(user_id=sender)
            my_bool = True
        else:
            btn.clear()
            btn1.create_message(user_id=sender, message='asdas')
        """







""""


        
       # if received_message == 'kek':
       #     a1.create_message(user_id=sender)
       # else:
        #    a2.create_message(user_id=sender)
"""
"""import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id

# Vk API
token = '6c9fda8bb0392af480cb06eac528f830cd4e876521957fd9ad08e11d2e2b45a7caecc68f71982788a00a5'
authorize = vk_api.VkApi(token=token)
long_poll = VkLongPoll(authorize)
keyboard = VkKeyboard(one_time=False)
class Button:
    def __init__(self, text, color=None, line=None):
        # list of colors to use in the class
        color_name = ['red', 'green', 'blue', 'white']

        # list of colors to use in the vk api
        color_vk_api = [VkKeyboardColor.NEGATIVE, VkKeyboardColor.POSITIVE, # [red, green]
                        VkKeyboardColor.PRIMARY, VkKeyboardColor.SECONDARY] # [blue, white]

        if line == 1:
            keyboard.add_line()

        # alg
        for i in range(len(color_name)):
            if color_name[i] == color:
                color = color_vk_api[i]
                #return self.color
            elif i == len(color_name) - 1:
                color = color_vk_api[len(color_vk_api) - 1]
                #return self.color

        VkKeyboard(one_time=False).add_button(text, color, line)

def write_message(sender, message, my_var=0):
    if my_var == 1:
        autorize.method("messages.send",
                        dict(user_id=sender, message=message, keyboard=btn, random_id=get_random_id()))

for event in long_poll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        received_message = event.text
        sender = event.user_id
        Button('1', 'red', 1)

        if received_message == 'Начать' or 'Чиби':
            text = '1'  # fun.register(sender)
            btn = keyboard.get_keyboard()
            write_message(sender, "text")
"""