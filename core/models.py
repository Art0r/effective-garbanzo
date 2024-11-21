from django.db import models
import uuid


class TaskStatus(models.IntegerChoices):

    ON_HOLD = 1, 'On Hold'
    IN_PROGRESS = 2, 'In Progress'
    STOPPED = 3, 'Stopped'
    FINISHED = 4, 'Finished'


class Base(models.Model):
    """
    This is the class that will be extended from all other models
    """

    id = models.UUIDField(name='id',
                          primary_key=True,
                          default=uuid.uuid4,
                          editable=False)

    created = models.DateTimeField(name='created',
                                   verbose_name='Created',
                                   auto_now_add=True,
                                   editable=False)

    updated = models.DateTimeField(name='updated',
                                   verbose_name='Updated',
                                   auto_now=True)

    class Meta:
        abstract = True


class Task(Base):

    title = models.CharField(name='title',
                             verbose_name='Title',
                             editable=True,
                             null=False,
                             max_length=64)

    description = models.TextField(name='description',
                                   verbose_name='Description',
                                   editable=True,
                                   null=False)

    department = models.CharField(name='department',
                                  verbose_name='Department',
                                  editable=True,
                                  null=False,
                                  max_length=32)

    status = models.IntegerField(name='status',
                                 verbose_name='Status',
                                 editable=True,
                                 choices=TaskStatus.choices,
                                 default=TaskStatus.ON_HOLD)
