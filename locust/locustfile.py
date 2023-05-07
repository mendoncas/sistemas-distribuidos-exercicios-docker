from locust import HttpUser, TaskSet, task
import base64

# task_set = UserBehavior
credentials = {"username": "fkjsaflsaj", "password": "pennyroyal290898"}
auth_token = base64.b64encode(
    f"{credentials['username']}:{credentials['password']}".encode('ascii'))
auth_header = {"Authorization": f"Basic {auth_token}"}


class WebsiteUser(HttpUser):
    min_wait = 5000
    max_wait = 9000

    @task
    def index(self):
        self.client.get("/")  # Realiza um get na url <HOST_DO_WORDPRESS>/?p=1

    @task(2)
    def login_and_out(l):
        # l.client.post("/login", credentials)
        l.client.post("/login", {"username": "ronaldo", "password": "pennyroyal290898"})

    @task(3)
    def create_post(l):
        l.client.post("/wp-json/wp/v2/posts",
                      data={
                          "title": "título do post!",
                          "content": "esse é o conteúdo do post"
                      },
                      headers=auth_header
                      )

    # @task(3)
    # def logout(l):
    #     l.client.post("/logout", {"username": "ricardo", "password": "pennyroyal290898"})
        # l.client.post("/logout", credentials)

    # @task
    # def profile(l):
    #     l.client.get("/profile")


# class WebsiteUser(HttpUser):
#     task_set = UserTasks
# from locust import HttpUser, TaskSet

# def index(l):
#     l.client.get("/")
