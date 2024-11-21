from django.core.management.base import BaseCommand
from core.models import Task
from core.factories import TaskFactory
from django.core.management import call_command
from faker import Faker


class Command(BaseCommand):

    def handle(self, *args, **optionsd):
        call_command("flush")

        for i in range(30):
            TaskFactory()
