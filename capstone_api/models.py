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
    South_Carolina = 'South Carolina'
    South_Dakota = 'South Dakota'
    Tennessee = 'Tennessee'
    Texas = 'Texas'
    Utah = 'Utah'
    Vermont = 'Vermont'
    Virginia = 'Virginia'
    Washington = 'Washington'
    West_Virginia = 'West Virginia'
    Wisconsin = 'Wisconsin'
    Wyoming = 'Wyoming'
    Federal = 'Federal Total'
    US_Total = 'US Total'
    Total = 'Total for Prisons'
    State = 'State Total'
    American_Samoa = 'American Samoa'
    Guam = 'Guam'
    Northern_Mariana_Islands = 'Northern Mariana Islands'
    Puerto_Rico = 'Puerto Rico'
    Virgin_Islands = 'Virgin Islands'

    STATESTERRITORIES = (
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
        (Federal, 'Federal Total'),
        (US_Total, 'US Total'),
        (Total, 'Total for Prisons'),
        (State, 'State Total'),
        (American_Samoa, 'American Samoa'),
        (Guam, 'Guam'),
        (Northern_Mariana_Islands, 'Northern Mariana Islands'),
        (Puerto_Rico, 'Puerto Rico'),
        (Virgin_Islands, 'Virgin Islands'),
    )

    # American_Samoa = 'American Samoa'
    # Guam = 'Guam'
    # Northern_Mariana_Islands = 'Northern Mariana Islands'
    # Puerto_Rico = 'Puerto Rico'
    # Virgin_Islands = 'Virgin Islands'

    # TERRITORIES = (
    #     (American_Samoa, 'American Samoa'),
    #     (Guam, 'Guam'),
    #     (Northern_Mariana_Islands, 'Northern Mariana Islands'),
    #     (Puerto_Rico, 'Puerto Rico'),
    #     (Virgin_Islands, 'Virgin Islands'),
    # )

    total_male_supervised = models.PositiveIntegerField(blank=True, null=True)
    total_female_supervised = models.PositiveIntegerField(blank=True, null=True)
    total_male_incarcerated = models.PositiveIntegerField(blank=True, null=True)
    total_female_incarcerated = models.PositiveIntegerField(blank=True, null=True)

    total_private = models.PositiveIntegerField(blank=True, null=True)
    total_local_jail = models.PositiveIntegerField(blank=True, null=True)
    total_other_prison = models.PositiveIntegerField(blank=True, null=True)

    total_noncitizen = models.PositiveIntegerField(blank=True, null=True)
    total_minor = models.PositiveIntegerField(blank=True, null=True)

    year = models.IntegerField(choices=YEARS, blank=True, null=True)

    state_or_territory = models.CharField(choices=STATESTERRITORIES, max_length=100, null=True, blank=True)
    abbreviation = models.CharField(null=True, blank=True, max_length=5)

    race_white = models.PositiveIntegerField(blank=True, null=True)
    race_black = models.PositiveIntegerField(blank=True, null=True)
    race_hispanic = models.PositiveIntegerField(blank=True, null=True)
    race_american_indian_alaska_native = models.PositiveIntegerField(blank=True, null=True)
    race_asian = models.PositiveIntegerField(blank=True, null=True)
    race_native_hawaiian_pacific_islander = models.PositiveIntegerField(blank=True, null=True)
    race_two_or_more = models.PositiveIntegerField(blank=True, null=True)
    race_other = models.PositiveIntegerField(blank=True, null=True)
    race_unknown = models.PositiveIntegerField(blank=True, null=True)

    total_correction_pop = models.PositiveIntegerField(blank=True, null=True)
    total_pop_incarcerated = models.PositiveIntegerField(blank=True, null=True)

    total_correction_pop_per_one_hundred_thou_residents_all = models.PositiveIntegerField(blank=True, null=True)
    total_pop_incarcerated_per_one_hundred_thou_residents_all = models.PositiveIntegerField(blank=True, null=True)


    class Meta:
        verbose_name_plural = 'State Data'

    def __str__(self):
        return '{} {}'.format(self.state, self.year)










