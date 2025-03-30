from django.db import models

class PlantDisease(models.Model):
    name = models.CharField(max_length=200)
    plant_type = models.CharField(max_length=100)
    symptoms = models.TextField()
    causes = models.TextField()
    treatment = models.TextField()
    prevention = models.TextField()
    
    def __str__(self):
        return f"{self.plant_type} - {self.name}"

class LeafImage(models.Model):
    image = models.ImageField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    result = models.ForeignKey(PlantDisease, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return f"Image uploaded at {self.uploaded_at}"