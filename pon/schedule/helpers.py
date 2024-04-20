import logging
from db_app.models import User, Tasks
import requests
import datetime


class TasksHelper:

    def get_schedule(self, group_id):
        schedule = requests.get(f'https://digital.etu.ru/api/mobile/schedule?groupNumber={group_id}').json()

        tasks = []

        try:
            days = schedule.get(str(group_id)).get('days')
            lessons_days = []
            for key, value in days.items():
                lessons_days.append(value.get('lessons'))

            for lessons, date in zip(lessons_days, self.get_current_week_dates()):
                for lesson in lessons:
                    task = dict()
                    task['name'] = lesson.get('name')
                    task['description'] = f'{lesson.get("subjectType")} по предмету {lesson.get("name")} ведёт {lesson.get("teacher")}'
                    task['start_time'] = self.time_to_dtm(date, lesson.get('start_time'))
                    task['end_time'] = self.time_to_dtm(date, lesson.get('end_time'))
                    tasks.append(task)
        except Exception as e:
            logging.error(e)

        return tasks

    def schedule_to_tasks(self, group_id):
        tasks = self.get_schedule(group_id)
        user = User.objects.get(id=1)
        for task in tasks:
            db_task = Tasks(
                user=user,
                name=task.get('name'),
                description=task.get('description'),
                start_time=task.get('start_time'),
                end_time=task.get('end_time')
            )
            db_task.save()

    @staticmethod
    def get_current_week_dates():
        today = datetime.date.today()
        weekday = today.weekday()

        start_of_week = today - datetime.timedelta(days=weekday)

        week_dates = [start_of_week + datetime.timedelta(days=i) for i in range(7)]

        return [date.strftime('%Y-%m-%d') for date in week_dates]

    @staticmethod
    def time_to_dtm(date, time):
        time_obj = datetime.datetime.strptime(time, '%H:%M').time()
        date_obj = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        return datetime.datetime.combine(date_obj, time_obj)


test = TasksHelper()
test.get_schedule(9370)
print(test.get_current_week_dates())
