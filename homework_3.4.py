
import requests

TOKEN = "AQAAAAAV1JvUAAT_F6mcvPCuJkWFh0gTdRf-ReI"
COUNTER_ID = "48844661"


class Counter:
    def __init__(self, token, counter_id):
        self.token = token
        self.counter_id = counter_id

    @property
    def visits_metrics(self):
        response = requests.get(
            "https://api-metrika.yandex.ru/stat/v1/data",
            params=dict(
            ids=COUNTER_ID,
            oauth_token=TOKEN,
            metrics="ym:s:visits"
            ))
        return "Визиты: {}".format([c['metrics'] for c in response.json()["data"]][0][0])

    @property
    def pageviews_metrics(self):
        response = requests.get(
            "https://api-metrika.yandex.ru/stat/v1/data",
            params=dict(
            ids=COUNTER_ID,
            oauth_token=TOKEN,
            metrics="ym:s:pageviews"
            ))
        return "Количество просмотров: {}".format([c['metrics'] for c in response.json()["data"]][0][0])

    @property
    def users_metrics(self):
        response = requests.get(
            "https://api-metrika.yandex.ru/stat/v1/data",
            params=dict(
            ids=COUNTER_ID,
            oauth_token=TOKEN,
            metrics="ym:s:users"
            ))
        return "Количество посетителей: {}".format([c['metrics'] for c in response.json()["data"]][0][0])

ya_user1 = Counter(TOKEN, COUNTER_ID)

print(ya_user1.visits_metrics)
print(ya_user1.pageviews_metrics)
print(ya_user1.users_metrics)