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

    Alabama = 'Alabama'
    Alaska = 'Alaska'
    Arizona = 'Arizona'
    Arkansas = 'Arkansas'
    California = 'California'
    Colorado = 'Colorado'
    Conneticut = 'Conneticut'
    Delaware = 'Delaware'
    DistrictOfColombia = 'District of Colombia'
    Florida = 'Florida'
    Georgia = 'Georgia'
    Hawaii = 'Hawaii'
    Idaho = 'Idaho'
    Illinois = 'Illinois'
    Indiana = 'Indiana'
    Iowa = 'Iowa'
    Kansas = 'Kansas'
    Kentucky = 'Kentucky'
    Louisiana = 'Louisiana'
    Maine = 'Maine'
    Maryland = 'Maryland'
    Massachusetts = 'Massachusetts'
    Michigan = 'Michigan'
    Minnesota = 'Minnesota'
    Mississippi = 'Mississippi'
    Missouri = 'Missouri'
    Montana = 'Montana'
    Nebraska = 'Nebraska'
    Nevada = 'Nevada'
    New_Hampshire = 'New Hampshire'
    New_Jersey = 'New Jersey'
    New_Mexico = 'New Mexico'
    New_York = 'New York'
    North_Carolina = 'North Carolina'
    North_Dakota = 'North Dakota'
    Ohio = 'Ohio'
    Oklahoma = 'Oklahoma'
    Oregon = 'Oregon'
    Pennsylvania = 'Pennsylvania'
    Rhode_Island = 'Rhode Island'
    South_Carolina = 'South_Carolina'
    South_Dakota = 'South_Dakota'
    Tennessee = 'Tennessee'
    Texas = 'Texas'
    Utah = 'Utah'
    Vermont = 'Vermont'
    Virginia = 'Virginia'
    Washington = 'Washington'
    West_Virginia = 'West Virginia'
    Wisconsin = 'Wisconsin'
    Wyoming = 'Wyoming'

    STATES = (
        (Alabama, 'Alabama'),
        (Alaska, 'Alaska'),
        (Arizona, 'Arizona'),
        (Arkansas, 'Arkansas'),
        (California, 'California'),
        (Colorado, 'Colorado'),
        (Conneticut, 'Conneticut'),
        (Delaware, 'Delaware'),
        (DistrictOfColombia, 'District of Columbia'),
        (Florida, 'Florida'),
        (Georgia, 'Georgia'),
        (Hawaii, 'Hawaii'),
        (Idaho, 'Idaho'),
        (Illinois, 'Illinois'),
        (Indiana, 'Indiana'),
        (Iowa, 'Iowa'),
        (Kansas, 'Kansas'),
        (Kentucky, 'Kentucky'),
        (Louisiana, 'Louisiana'),
        (Maine, 'Maine'),
        (Maryland, 'Maryland'),
        (Massachusetts, 'Massachusetts'),
        (Michigan, 'Michigan'),
        (Minnesota, 'Minnesota'),
        (Mississippi, 'Mississippi'),
        (Missouri, 'Missouri'),
        (Montana, 'Montana'),
        (Nebraska, 'Nebraska'),
        (Nevada, 'Nevada'),
        (New_Hampshire, 'New Hampshire'),
        (New_Jersey, 'New Jersey'),
        (New_Mexico, 'New Mexico'),
        (New_York, 'New York'),
        (North_Carolina, 'North Carolina'),
        (North_Dakota, 'North Dakota'),
        (Ohio, 'Ohio'),
        (Oklahoma, 'Oklahoma'),
        (Oregon, 'Oregon'),
        (Pennsylvania, 'Pennsylvania'),
        (Rhode_Island, 'Rhode Island'),
        (South_Carolina, 'South_Carolina'),
        (South_Dakota, 'South_Dakota'),
        (Tennessee, 'Tennessee'),
        (Texas, 'Texas'),
        (Utah, 'Utah'),
        (Vermont, 'Vermont'),
        (Virginia, 'Virginia'),
        (Washington, 'Washington'),
        (West_Virginia, 'West Virginia'),
        (Wisconsin, 'Wisconsin'),
        (Wyoming, 'Wyoming'),
    )

    total_male = models.PositiveIntegerField(default=0)
    total_female = models.PositiveIntegerField(default=0)
    total_private = models.PositiveIntegerField(default=0)
    total_local_jails = models.PositiveIntegerField(default=0)
    total_other_prison = models.PositiveIntegerField(default=0)
    total_non_citizen = models.PositiveIntegerField(default=0)
    total_minor = models.PositiveIntegerField(default=0)

    # Do I want to do race totals?

    year = models.IntegerField(choices=YEARS)
    state = models.CharField(choices=STATES, max_length=100)

    class Meta:
        verbose_name_plural = 'State Data'

    def __str__(self):
        return '{} {}'.format(self.state, self.year)



# will need another table with census data for each state -- or will need to use the percentage columns on the data I already have...









