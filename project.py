import simple_blogger.CommonBlogger
from datetime import timedelta

class Project():
    def __get_category_folder(self, task):
        return task['group']
                    
    def __get_topic_folder(self, task):
        return task['name']

    def __system_prompt(self, task):
        return "Ты - блогер с 1000000 подписчиков"

    def __task_converter(self, idea):
        TOPIC_WORD_LIMIT = 100
        return { 
            "name": idea['name'],
            "theory_prompt": f"Расскажи интересный факт про теорию '{idea['name']}' из категории '{idea['category']}' из области '{idea['domain']}', используй не более {TOPIC_WORD_LIMIT} слов, используй смайлики",
            "theory_image": f"Нарисуй рисунок, вдохновлённый теорией '{idea['name']}' из категории '{idea['category']}' из области '{idea['domain']}'",
            "group": f"{idea['domain']}/{idea['category']}",
        }

    def __init__(self):
        self.blogger = simple_blogger.CommonBlogger(
            review_chat_id=-1002374309134,
            production_chat_id='@theory_the',
            blogger_bot_token_name='ATHE_BOT_TOKEN',
            catagory_folder_getter=self.__get_category_folder,
            topic_folder_getter=self.__get_topic_folder,
            project_name='theory_the',
            system_prompt=self.__system_prompt,
            task_converter=self.__task_converter,
            days_between_posts=timedelta(days=1),
            text_ai_token_name='OPENAI_API_KEY',
            ai_text_model='chatgpt-4o-latest',
            text_base_url='https://api.openai.com/v1'   
        )

    def init_project(self):
        self.blogger.init_project()

    def push(self):
        self.blogger.push()

    def revert(self):
        self.blogger.revert()

    def gen_image(self, task, type):
        self.blogger.gen_image(task, type)

    def gen_text(self, task, type):
        self.blogger.gen_text(task, type)

    def review(self, type):
        self.blogger.review(type)

    def send(self, type):
        self.blogger.send(type)