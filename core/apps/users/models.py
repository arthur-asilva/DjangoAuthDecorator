from django.db import models



class User(models.Model):
    name = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    password = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Permission(models.Model):
    user = models.ForeignKey(User, related_name='user_permission', on_delete=models.CASCADE)
    view_access = models.CharField(max_length=50)
    permission_date = models.DateField(blank=True, null=True, auto_now_add=True)

    def __str__(self):
        return f"{self.user.name}, {self.view_access}. Since {self.permission_date}" 
