from django.db import models

# Create your models here.


class dna_sequence(models.Model):
    id = models.AutoField(primary_key=True)
    seq_info=models.CharField(max_length=10000000,default=id)
    dna_sequence=models.CharField(max_length=10000000)



    def __str__(self):
        return self.seq_info
    
class dna_info(models.Model):
    dna_sequence = models.ForeignKey(dna_sequence, on_delete=models.CASCADE, related_name='properties')
    seq_info=models.CharField(max_length=10000000)
    clean_sequence1=models.CharField(max_length=10000000)
    reverse_comp=models.CharField(max_length=10000000)
    comp=models.CharField(max_length=10000000)
    trans=models.CharField(max_length=1000000)
    translat_protein=models.CharField(max_length=100000)
    translat_protein_stop=models.CharField(max_length=100000)
    gc=models.FloatField()


    def __str__(self):
        return self.dna_sequence.seq_info
