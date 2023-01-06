from django.core.mail import send_mail
from django.db import models
import telepot
from django.shortcuts import render



class Dht(models.Model):
       temp = models.FloatField(null=True)
       hum = models.FloatField(null=True)
       dt = models.DateTimeField(auto_now_add=True,null=True)

       def __str__(self):
              return str(self.temp)

       def save (self,*args,**kwargs):
              if self.temp > 8:
                     token = '5886521636:AAGBsI3zK0k-D2vy36PBuoSsOln6_PXKR5Q'
                     rece_id = 5647926127
                     bot = telepot.Bot(token)
                     bot.sendMessage(rece_id, 'anomalie.')
                     print(bot.sendMessage(rece_id, 'temperature dépasse la normale / temperature critique ' +str(self.temp)))
                     send_mail(
                            'temperature dépasse la normale / temperature critique' +str(self.temp),
                            'anomalie dans la machine le,' + str(self.dt),
                            'meriem.tahri@ump.ac.ma',
                            ['safae.kaddouri@ump.ac.ma'],
                            fail_silently=False,
                     )
              if self.temp < 2:
                     token = '5886521636:AAGBsI3zK0k-D2vy36PBuoSsOln6_PXKR5Q'
                     rece_id = 5647926127
                     bot = telepot.Bot(token)
                     bot.sendMessage(rece_id, 'anomalie.')
                     print(bot.sendMessage(rece_id, 'temperature dépasse la normale / temperature severe' + str(self.temp)))
                     send_mail(
                            'temperature dépasse la normale / temperature severe ' + str(self.temp),
                            'anomalie dans la machine le,' + str(self.dt),
                            'meriem.tahri@ump.ac.ma',
                            ['safae.kaddouri@ump.ac.ma'],
                            fail_silently=False,
                     )
              if self.temp <= -127:
                     token = '5886521636:AAGBsI3zK0k-D2vy36PBuoSsOln6_PXKR5Q'
                     rece_id = 5647926127
                     bot = telepot.Bot(token)
                     bot.sendMessage(rece_id, 'anomalie.')
                     print(bot.sendMessage(rece_id, 'Merci de verifier votre sonde ' + str(self.temp)))
                     send_mail(
                            'Merci de verifier votre sonde ' + str(self.temp),
                            'anomalie dans la machine le,' + str(self.dt),
                            'meriem.tahri@ump.ac.ma',
                            ['safae.kaddouri@ump.ac.ma'],
                            fail_silently=False,
                     )


              return super().save(*args,**kwargs)