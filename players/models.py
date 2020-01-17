from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings
import datetime

'''
"required", "label", label_suffix, initial, "widget", "help_text", "error_messages", "validators", localize,
 disabled
 *******************************************************************************************************8
 Built-in Field classes=>
 BooleanField, CharField, ChoiceField, TypedChoiceField, DateField, DateTimeField, DecimalField, DurationField,
 EmailField, "FileField", FilePathField, FloatField, ImageField, IntegerField, GenericIPAddressField,\
MultipleChoiceField, TypedMultipleChoiceField, NullBooleanField, RegexField, SlugField, SmallAutoField, \
SmallIntegerField, TextField, TimeField, URLField, UUIDField, 
**************************************************************************************************************
Relationship fields=>
ForeignKey, 
'''
# Create your models here.
INPUT_FORMATS = ['%Y-%m-%d',      # '2006-10-25'
                 '%m/%d/%Y',      # '10/25/2006'
                 '%m/%d/%y']      # '10/25/06'
NATIONS = [('NN','None'), ('afg','Afghanistan'), ('aus','Australia'),('bng', 'Bangladesh'), ('eng','England'),
           ('ind',"India"),('irl','Ireland'), ('nz','New Zealand'), ('pak','Pakistan'),('sl',"Sri Lanka"),\
           ('saf',"South Africa"), ('wi',"West Indies"),('zim',"Zimbabwe")]


class Player(models.Model):
    # label='First Name', strip=True, empty_value='Not Available
    f_name = models.CharField("First Name",help_text="Player's First Name", max_length=50, primary_key=True)
    m_name = models.CharField("Middle Name", help_text="Player's Middle Name", max_length=50)
    l_name = models.CharField("Last Name",help_text="Player's Last Name", max_length=50)
    pic = models.ImageField(upload_to='player_pic', default='/default_player_pic.jpg')
    age = models.IntegerField(help_text="Player's age")
    dob = models.DateField(default=datetime.date.today)
    nationality = models.CharField("Nationality",choices=NATIONS, default='None',max_length=3)
    is_batsman = models.BooleanField(default=False)
    is_bowler = models.BooleanField(default=False)
    is_keeper = models.BooleanField(default=False)
    value = models.FloatField(default=0.0, validators=[MinValueValidator(0.0), MaxValueValidator(11.0)])
    country_flag = models.FilePathField(path="/static/country")#,match="nation.*\.jpeg$")
    def __str__(self):
        return self.f_name

# class Nation(models.Model):
#     nation_player = models.ForeignKey(Player, on_delete=models.CASCADE, null=True)
#     #, recursive=True, allow_files=True)
#
#     def __str__(self):
#         return self.nation_player.f_name
#
#     class Meta:
#         ordering = ['country_flag']
#
#