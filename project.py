from simple_blogger import CommonBlogger
from simple_blogger.generators.OpenAIGenerator import OpenAITextGenerator
from datetime import timedelta

class Project(CommonBlogger):
    def _get_category_folder(self, task):
        return task['group']
                    
    def _get_topic_folder(self, task):
        return task['name']

    def _system_prompt(self, task):
        return "Ты - блогер с 1000000 подписчиков"

    def _task_converter(self, idea):
        TOPIC_WORD_LIMIT = 100
        return { 
            "name": idea['name'],
            "theory_prompt": f"Расскажи интересный факт про теорию '{idea['name']}' из категории '{idea['category']}' из области '{idea['domain']}', используй не более {TOPIC_WORD_LIMIT} слов, используй смайлики",
            "theory_image": f"Нарисуй рисунок, вдохновлённый теорией '{idea['name']}' из категории '{idea['category']}' из области '{idea['domain']}'",
            "group": f"{idea['domain']}/{idea['category']}",
        }

    def __init__(self):
        super().__init__(
            review_chat_id=-1002374309134,
            production_chat_id='@theory_the',
            blogger_bot_token_name='ATHE_BOT_TOKEN',
            project_name='theory_the',
            days_between_posts=timedelta(days=1),
            text_generator=OpenAITextGenerator()
        )