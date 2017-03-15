# from django.contrib.auth.models import User
from django.db import models


class StateData(models.Model):
    """
    The Prisoner model maintains the different information associated with a prisoner

    Author: Dani Adkins
    """
    YEARS = (
        (2014, '2014'),
        (2015, '2015'),
        (2016, '2016'),
    )

    STATES = (
        (Alabama, 'Alabama')
        # (Alabama, 'Alabama')
        # (Alabama, 'Alabama')
        # (Alabama, 'Alabama')
        # (Alabama, 'Alabama')
        # (Alabama, 'Alabama')
        # (Alabama, 'Alabama')
        # (Alabama, 'Alabama')
        # (Alabama, 'Alabama')
        # (Alabama, 'Alabama')
        # (Alabama, 'Alabama')
        # (Alabama, 'Alabama')
        # (Alabama, 'Alabama')
        # (Alabama, 'Alabama')
        # (Alabama, 'Alabama')
        # (Alabama, 'Alabama')
        # (Alabama, 'Alabama')
        # (Alabama, 'Alabama')
        # (Alabama, 'Alabama')


    )

    total_male = models.PositiveIntegerField(default=0)
    total_female = models.PositiveIntegerField(default=0)
    total_private = models.PositiveIntegerField(default=0)
    total_local_jails = models.PositiveIntegerField(default=0)
    total_other_prison = models.PositiveIntegerField(default=0)
    total_non_citizen = models.PositiveIntegerField(default=0)
    total_minor = models.PositiveIntegerField(default=0)

    # Do I want to do race totals?

    year = models.IntegerField(max_length=2, choices=YEARS)
    state = models.CharField(choices=STATES, unique=True)

    class Meta:
        verbose_name_plural = 'State Data'

    def __str__(self):
        return '{} {}'.format(self.state, self.year)









