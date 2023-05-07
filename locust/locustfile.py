from locust import HttpUser, TaskSet, task
from pathlib import Path
import base64

cred = ("admin", "e3Lq e75g ln8S AYIj lEsB xa1r")


def base_post(l, content):
    l.client.post("/wp-json/wp/v2/posts", data=content, auth=cred)


class WebsiteUser(HttpUser):
    min_wait = 5000
    max_wait = 9000

    def send_image(l, url):
        return

    @task
    def index(self):
        self.client.get("/")  # Realiza um get na url <HOST_DO_WORDPRESS>/?p=1

    @task
    def small_post(l):
        base_post(l, {
            "title": "título do post!",
            "content": Path('resources/400kb.txt').read_text()
        })

    @task
    def big_post(l):
        base_post(l, {
            "title": "título do post!",
            "content": Path('resources/1mb.txt').read_text()
        })