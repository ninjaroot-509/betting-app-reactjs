from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField
from django.core.mail import send_mail, BadHeaderError, mail_admins

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    phone = PhoneNumberField()
    photo = models.ImageField(default='photo.jpg', upload_to='profile_pics/', null=True, blank=True)
    
    class Meta:
        verbose_name = 'Profile Liste'
        verbose_name_plural = 'Listes des profiles'

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


# def email_new_user(sender, **kwargs):
#     if kwargs["created"]:  # only for new users
#         new_user = kwargs["instance"] 
#         print(new_user.email)
#         subject = "New user (%s)" % sender.username
#         message = "l'utisateur %s vient juste de creer un compte." % sender.username
#         message_to_user = "Bienvenue et merci d'avoir faire confiance a notre site"
#         email_user = "%s" % new_user.email
#         mail_admins(subject, message)
#         # send_mail(subject, message_to_user, 'stanleycastin@gmail.com', email_user, fail_silently=False)
# post_save.connect(email_new_user, sender=settings.AUTH_USER_MODEL)


class questions(models.Model):
    question = models.CharField(max_length=500, null=False)
    option_a = models.CharField(max_length=100, null=False)
    option_b = models.CharField(max_length=100, null=False)
    option_c = models.CharField(max_length=100, null=True, blank=True)
    option_d = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    correct_option = models.CharField(max_length=1, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    is_live = models.BooleanField(default=True)
    is_true_or_false = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Question Liste'
        verbose_name_plural = 'Listes des Questions'

    def __str__(self):
        return '{}'.format(self.question)

class Wallet(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    montant = models.FloatField(default=0)

    class Meta:
        verbose_name = 'Portefeuille Liste'
        verbose_name_plural = 'Listes des portefeuilles'

    def __str__(self):
        return '{} a {} Gourdes'.format(self.user.username, self.montant) # TODO

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_wallet(sender, instance, created, **kwargs):
    if created:
        Wallet.objects.create(user=instance)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_user_wallet(sender, instance, **kwargs):
    instance.wallet.save()
    
class Retrait(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    montant = models.FloatField(default=0)
    is_done = models.BooleanField(default=True)
    envoyer = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Retrait Liste'
        verbose_name_plural = 'Listes des retraits'
    
    def __str__(self):
        return '{} a retire {} Gourdes a son portefeuille le {}'.format(self.user.username, self.montant, self.date) # TODO
