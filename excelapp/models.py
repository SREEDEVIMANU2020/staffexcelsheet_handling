from django.db import models
from django.conf import settings
from accounts.models import CustomUser


# ==========================================================
# EXCEL FILE UPLOAD MODEL (Optional)
# ==========================================================
class ExcelFile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    file = models.FileField(upload_to="excel_files/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.emp_id} - {self.file.name}"


# ==========================================================
# CONSULTANT SHEET MODEL
# ==========================================================
class ConsultantSheet(models.Model):
    SHEET_TYPES = (
        ("STUDENT", "Student Details"),
        ("ATTENDANCE", "Attendance"),
        ("COMPLETED", "Completed Batch"),
    )

    consultant = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    sheet_name = models.CharField(max_length=200)
    sheet_type = models.CharField(max_length=20, choices=SHEET_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("consultant", "sheet_type")

    def __str__(self):
        return f"{self.sheet_name} ({self.consultant.emp_id})"


# ==========================================================
# SHEET ROW MODEL (col1-col33 for all 3 sheets)
# ==========================================================
class SheetRow(models.Model):
    sheet = models.ForeignKey(
        ConsultantSheet,
        on_delete=models.CASCADE,
        related_name="rows"
    )

    col1 = models.CharField(max_length=255, blank=True, null=True)
    col2 = models.CharField(max_length=255, blank=True, null=True)
    col3 = models.CharField(max_length=255, blank=True, null=True)
    col4 = models.CharField(max_length=255, blank=True, null=True)
    col5 = models.CharField(max_length=255, blank=True, null=True)
    col6 = models.CharField(max_length=255, blank=True, null=True)
    col7 = models.CharField(max_length=255, blank=True, null=True)
    col8 = models.CharField(max_length=255, blank=True, null=True)
    col9 = models.CharField(max_length=255, blank=True, null=True)
    col10 = models.CharField(max_length=255, blank=True, null=True)
    col11 = models.CharField(max_length=255, blank=True, null=True)
    col12 = models.CharField(max_length=255, blank=True, null=True)
    col13 = models.CharField(max_length=255, blank=True, null=True)
    col14 = models.CharField(max_length=255, blank=True, null=True)
    col15 = models.CharField(max_length=255, blank=True, null=True)
    col16 = models.CharField(max_length=255, blank=True, null=True)
    col17 = models.CharField(max_length=255, blank=True, null=True)
    col18 = models.CharField(max_length=255, blank=True, null=True)
    col19 = models.CharField(max_length=255, blank=True, null=True)
    col20 = models.CharField(max_length=255, blank=True, null=True)
    col21 = models.CharField(max_length=255, blank=True, null=True)
    col22 = models.CharField(max_length=255, blank=True, null=True)
    col23 = models.CharField(max_length=255, blank=True, null=True)
    col24 = models.CharField(max_length=255, blank=True, null=True)
    col25 = models.CharField(max_length=255, blank=True, null=True)
    col26 = models.CharField(max_length=255, blank=True, null=True)
    col27 = models.CharField(max_length=255, blank=True, null=True)
    col28 = models.CharField(max_length=255, blank=True, null=True)
    col29 = models.CharField(max_length=255, blank=True, null=True)
    col30 = models.CharField(max_length=255, blank=True, null=True)
    col31 = models.CharField(max_length=255, blank=True, null=True)
    col32 = models.CharField(max_length=255, blank=True, null=True)
    col33 = models.CharField(max_length=255, blank=True, null=True)
    col34 = models.CharField(max_length=255, blank=True, null=True)
    col35 = models.CharField(max_length=255, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Row for {self.sheet.sheet_name} ({self.sheet.sheet_type})"