from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class CustomUserManager(BaseUserManager):
    def create_user(self, emp_id, consultant_name, company_email, password=None, role="consultant"):
        if not emp_id:
            raise ValueError("Employee ID is required")
        if not company_email:
            raise ValueError("Company Email is required")

        user = self.model(
            emp_id=emp_id,
            consultant_name=consultant_name,
            company_email=self.normalize_email(company_email),
            role=role
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, emp_id, consultant_name, company_email, password=None):
        user = self.create_user(
            emp_id=emp_id,
            consultant_name=consultant_name,
            company_email=company_email,
            password=password,
            role="admin"
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = (
        ("admin", "Admin"),
        ("consultant", "Consultant"),
    )

    emp_id = models.CharField(max_length=50, unique=True)
    consultant_name = models.CharField(max_length=150)
    company_email = models.EmailField(unique=True)

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="consultant")

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "emp_id"
    REQUIRED_FIELDS = ["consultant_name", "company_email"]

    def __str__(self):
        return self.emp_id