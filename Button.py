# Vk
import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id
from random import randint
# My
from Register import long_poll, authorize

class Button:
    def __init__(self, text, keyboard = VkKeyboard(one_time=False), line=None, color=None):

        # Keyboard, text button, debug message
        self.text = text
        self.keyboard = keyboard

        # '\n' - in button
        if line is True:
            self.keyboard.add_line()

        # Color button vk api
        color_name = ['red', 'green', 'blue', 'white']

        color_vk_api = [VkKeyboardColor.NEGATIVE, VkKeyboardColor.POSITIVE, # [red, green]
                        VkKeyboardColor.PRIMARY, VkKeyboardColor.SECONDARY] # [blue, white]
        # alg
        for i in range(len(color_name)):
            if color_name[i] == color:
                color = color_vk_api[i]

        # create button
        self.keyboard.add_button(self.text, color=color)

    def clear(self, user_id, message):
        authorize.method("messages.send", dict(user_id=user_id,message=message, keyboard=[],random_id=get_random_id()))

    # Create message [ user_id ; message ]
    def create_message(self, user_id, message=None, sticker=None, img=None):

        """  DEBUG MESSAGE """
        debug_message = {'arg1': ['[BOT DEBUG] Аргумент (1)\nНомер стикера должен быть в формате [int]\n',

                                  '[BOT DEBUG] Аргумент (1)\n'
                                  'Укажите первое значение, номер стикера'
                                  ],
                         'arg2': ['[BOT DEBUG] Аргумент (2)\nНомер режима должен быть в формате [int]\n',

                                  '[BOT DEBUG] Аргумент (2)\n'
                                  '1. В режиме [top], отправляется сначала sticker, потом message.\n'
                                  '2. В режиме [down], отправляется сначала message, потом sticker.\n'
                                  '3. Без указаний режимов, отправляется рандомно.\n'
                                  ],
                         'arg3': ['[BOT DEBUG] Аргумент (3)\nНазвание режима должно быть в формате [str]\n',

                                 '[BOT DEBUG] Аргумент (3)\n'
                                 '1. В режиме "vk", при отправке стикера, высвечивается его номер во вконтакте\n'
                                 '2. В режиме "console", при отправке стикера, высвечивается его номер, в консоле\n'
                                 '3. Без указаний режимов, мод отключен.']}
        """  DEBUG CODE """

        # if not message, text message from button
        if message and message == '':
            message = self.text

        if message:
            authorize.method("messages.send", dict(user_id=user_id, message=message,keyboard=self.keyboard.get_keyboard(),random_id=get_random_id()))

        if img:
            authorize.method("messages.send", dict(user_id=user_id, attachment=img, random_id=get_random_id()))

        # Sticker [0]
        if sticker:
            try:
                if type(sticker[0]) != int:
                    print(debug_message['arg1'][0]); return
            except IndexError:
                print(debug_message['arg1'][1]); return

            # Sticker [1]
            try:
                if type(sticker[1]) != str:
                    print(debug_message['arg2'][0]); return
                if sticker[1] != 'top' and sticker[1] != 'down':
                    print(debug_message['arg2'][1]); return
            except IndexError:
                sticker.append(False)

            # Sticker [2]
            try:
                if type(sticker[2]) != str:
                    print(debug_message['arg3'][0]); return
                if sticker[2] != 'vk' and sticker[2] != 'console':
                    print(debug_message['arg3'][1]); return
            except IndexError:
                sticker.append(False)

            """  DEBUG CODE END """

            # id sticker
            message_id_sticker = f'[BOT INFO] Номер стикера: {sticker[0]}'

            try:
                if sticker[0] and message:
                    if sticker[1] == 'top':
                        authorize.method("messages.send", dict(user_id=user_id,message=message,keyboard=self.keyboard.get_keyboard(),random_id=get_random_id()))
                        authorize.method("messages.send", dict(user_id=user_id,sticker_id=sticker[0],random_id=get_random_id()))
                    else:
                        authorize.method("messages.send", dict(user_id=user_id,sticker_id=sticker[0],random_id=get_random_id()))
                        authorize.method("messages.send", dict(user_id=user_id,message=message,keyboard=self.keyboard.get_keyboard(),random_id=get_random_id()))

                elif sticker[0] and not message:
                    authorize.method("messages.send",dict(user_id=user_id,sticker_id=sticker[0],random_id=get_random_id()))
                else:
                    authorize.method("messages.send",dict(user_id=user_id,message=message,keyboard=self.keyboard.get_keyboard(),random_id=get_random_id()))

                # Message id sticker
                if sticker[2] and sticker[2] == 'vk':
                    authorize.method("messages.send",dict(user_id=user_id, message=message_id_sticker, random_id=get_random_id()))
                elif sticker[2]:
                    print(message_id_sticker)

            except vk_api.exceptions.ApiError:
                if sticker[2] == 'console':
                    print(f'[BOT DEBUG] У вас нет этого стикера: {sticker[0]} :(\n'
                          f'Или допущена ошибка в аргументах функции')
                else:
                    authorize.method("messages.send", dict(user_id=user_id,message=f'[BOT DEBUG] У вас нет этого стикера: {sticker[0]} :(\nИли допущена ошибка в аргументах функции',random_id=get_random_id()))