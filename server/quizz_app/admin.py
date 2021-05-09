from django.contrib import admin
from .models import *
# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'phone',
    ]
admin.site.register(Profile, ProfileAdmin)

def copy_quest(modeladmin, request, queryset):
    for object in queryset:
        object.id = None
        object.save()


copy_quest.short_description = 'Dupliquer question'


class QuestionAdmin(admin.ModelAdmin):
    list_display = [
        'question',
        'is_true_or_false'
    ]
    actions = [copy_quest]
    list_filter = ['is_true_or_false', 'is_live']
    search_fields = ['question',]
admin.site.register(questions, QuestionAdmin)

class WalletAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'montant',
    ]
    search_fields = ['montant', 'user']
admin.site.register(Wallet, WalletAdmin)

class RetraitAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'montant',
        'envoyer',
        'is_done'
    ]
    list_editable = ['is_done',]
    list_filter = ['date', 'user', 'envoyer', 'is_done']
    search_fields = ['montant', 'user', 'date']
admin.site.register(Retrait, RetraitAdmin)
