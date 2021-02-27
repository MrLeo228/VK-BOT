import vk_api
from vk_api.longpoll import VkLongPoll

token = '6c9fda8bb0392af480cb06eac528f830cd4e876521957fd9ad08e11d2e2b45a7caecc68f71982788a00a5'
authorize = vk_api.VkApi(token=token)
long_poll = VkLongPoll(authorize)