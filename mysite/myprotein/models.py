from django.db import models

# Create your models here.
class protein_sequence(models.Model):
    id = models.AutoField(primary_key=True)
    seq_info=models.CharField(max_length=10000000,default=id)
    protein_sequence=models.CharField(max_length=10000000)



    def __str__(self):
        return self.seq_info
    


# New model for protein properties with a foreign key linking to the protein_sequence model
class ProteinProperties(models.Model):
    protein = models.ForeignKey(protein_sequence, on_delete=models.CASCADE, related_name='properties')
    molecular_weight = models.FloatField()
    isoelectric_point = models.FloatField()
    extinction_coefficient = models.CharField(max_length=255)
    instability_index = models.FloatField()
    gravy = models.FloatField()
    aliphatic_index = models.FloatField()
    aromatic_ratio = models.FloatField()
    hydrophobic_polarity = models.FloatField()

    def __str__(self):
        return f"Properties of {self.protein.seq_info}..."


