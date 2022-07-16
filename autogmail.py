import requests
import random, string
import datetime
from time import sleep

V2B_REG_REL_URL = '/api/v1/passport/auth/register'
# V2B_SUB_REL_URL = '/api/v1/user/getSubscribe'
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0'

home_urls = (
   # 'https://cooc.cloud',
    #'https://baipiao.buzz',
    'https://circlecloud123.com',
    'https://hmkj3.com',
    'https://sub.chbjpw.mobi',
    'https://acec.icu',
)
times = 1
proxies = {
    'http': 'http://127.0.0.1:7890',
    'https': 'http://127.0.0.1:7890'
}

subsgmail = []
for current_url in home_urls:
    i = 0
    while i < times:
        form_data = {'email': ''.join(random.choice(string.ascii_letters+string.digits) for _ in range(12)),
                    'password': 'nichacha123',
                    'invite_code': '',
                'email_code': ''}
        
        form_data2 = {'email': ''.join(random.choice(string.ascii_letters+string.digits) for _ in range(12))+'@gmail.com',
                    'password': 'nichacha123',
                    'invite_code': '',
                'email_code': ''}
        try:
            response = requests.post(current_url+V2B_REG_REL_URL, json=form_data2)
        except:
            continue
        # print(response.text)
        try:
            subscription_url = f'{current_url}/api/v1/client/subscribe?token={response.json()["data"]["token"]}'
            subsgmail.append(subscription_url)
        except:
            print(f'Invalid response: {response.text.encode("utf-8")}')
            sleep(3)
        else:
            i += 1
            print(f'Number succeeded: {i}\t{subscription_url}')

print(f'{times} accounts created for each site. Subscription URLs:\n----------')
print(*subsgmail, sep='\n')

with open('subsgmail.txt', 'w') as fil:
    print(f'{datetime.datetime.now().isoformat()}\n{times} accounts created for each site. Subscription URLs:\n----------', file=fil)
    print(*subsgmail, sep='\n', file=fil)
