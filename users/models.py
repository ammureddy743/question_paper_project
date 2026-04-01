from django.db import models


# ---------------- USER MODEL ---------------- #
class UserRegistrationModel(models.Model):
    name = models.CharField(max_length=100)
    loginid = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=100)
    mobile = models.CharField(unique=True, max_length=100)
    email = models.CharField(unique=True, max_length=100)
    locality = models.CharField(max_length=100)
    address = models.CharField(max_length=1000)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

    # ✅ IMPORTANT FIX
    status = models.CharField(max_length=100, default='pending')

    def __str__(self):
        return self.loginid

    class Meta:
        db_table = 'UserRegistrations'


# ---------------- TRANSLATION HISTORY ---------------- #
class TranslationHistory(models.Model):
    user_id = models.IntegerField()
    file_name = models.CharField(max_length=255)
    file_path = models.CharField(max_length=500)
    language = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.file_name} ({self.language})"

    class Meta:
        db_table = 'TranslationHistory'