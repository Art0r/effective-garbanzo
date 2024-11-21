import factory
from core.models import Task


class TaskFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Task

    title = factory.Faker('sentence', nb_words=4)
    description = factory.Faker('sentence', nb_words=6)
    department = factory.Faker('name')

    @factory.post_generation
    def save_to_db(obj, create, extracted, **kwargs):
        if create:
            obj.save(using="default")
