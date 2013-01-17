from django.db import models

DIVISION_CHOICES = (
        (u'P', u'Premier $450'),
        (u'M', u'Mens/Collegiate $375'),
        (u'O', u'Oldboys $350'),
        (u'W', u'Women/Collegiate $300'),
    )

class Team(models.Model):
    teamname = models.CharField('Team Name', blank=False, max_length=60,
            help_text='Please enter a valid team name')
    division = models.CharField(max_length=1, choices=DIVISION_CHOICES, default=u'P')
    captain = models.CharField('Primary Contact', blank=False, max_length=60, help_text='Please enter a valid name')
    email = models.EmailField('Contact Email', blank=False, max_length=256, help_text='Please enter a valid email')
    phone_number = models.CharField('Phone Number', blank=False, max_length=20, null=True,
                                          help_text='Please enter a valid phone number')
    date = models.DateTimeField('Registration Date', auto_now_add=True)
    paid = models.BooleanField(blank=True, default=False)
    def __unicode__(self):
        return self.teamname
