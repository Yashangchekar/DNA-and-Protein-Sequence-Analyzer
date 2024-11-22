from django.shortcuts import render,redirect
from .models import protein_sequence,ProteinProperties
from Bio.SeqUtils import molecular_weight, IsoelectricPoint

# Create your views here.

from Bio.SeqUtils.ProtParam import ProteinAnalysis

def aliphatic_index(sequence):
    seq_upper = sequence.upper()
    num_A = seq_upper.count('A')
    num_V = seq_upper.count('V')
    num_I = seq_upper.count('I')
    num_L = seq_upper.count('L')
    total_length = len(seq_upper)

    # Aliphatic index formula
    ai = (100 * (num_A + 2.9 * num_V + 3.9 * (num_I + num_L))) / total_length
    return ai

# Custom function to calculate the aromatic ratio
def aromatic_ratio(sequence):
    seq_upper = sequence.upper()
    num_aromatic = seq_upper.count('W') + seq_upper.count('Y') + seq_upper.count('F')
    total_length = len(seq_upper)
    
    return num_aromatic / total_length if total_length > 0 else 0

# Custom function to calculate hydrophobic polarity
def hydrophobic_polarity(sequence):
    seq_upper = sequence.upper()
    hydrophobic_count = sum(seq_upper.count(aa) for aa in 'AVILMFWP')
    polar_count = sum(seq_upper.count(aa) for aa in 'RNDQEHKSYCT')
    total_length = len(seq_upper)

    if total_length == 0:
        return 0  # Handle empty sequence

    return hydrophobic_count / polar_count if polar_count > 0 else float('inf')  # Avoid division by zero



def calculate_properties(sequence):
    # Calculate the molecular weight
    weight = molecular_weight(sequence, seq_type='protein')
    
    # Analyze the sequence using ProteinAnalysis
    analysis = ProteinAnalysis(sequence)
    print(analysis)
    ip = analysis.isoelectric_point()
    extinction_coefficient=analysis.molar_extinction_coefficient()

    instability_index =analysis.instability_index()
    gravy =analysis.gravy()

        # Custom calculations
    aliphatic_idx = aliphatic_index(sequence)
    aromatic_ratio_value = aromatic_ratio(sequence)
    hydrophobic_polarity_value = hydrophobic_polarity(sequence)


    return weight, ip, extinction_coefficient,instability_index,gravy,aliphatic_idx,aromatic_ratio_value,hydrophobic_polarity_value
    

def extract_protein_sequence(data):
    # Split the input text by whitespace and filter out any non-sequence lines
    lines = data.split()
    sequence = ''.join([line for line in lines if line.isalpha() and line.isupper()])
    return sequence




def index(request):
    if request.method == "POST":
        sequence = request.POST.get('protein_sequence')  # Correct way to access POST data
        seq_info=request.POST.get('info_sequence')

        if sequence and seq_info:  # Check if sequence is not empty
            # Save the sequence to the database

            new_sequence = protein_sequence(protein_sequence=sequence,seq_info=seq_info)
            

            

            new_sequence.save()

            extract=extract_protein_sequence(sequence)
            weight, ip ,extinction_coefficient,instability_index,gravy,aliphatic_idx,aromatic_ratio_value,hydrophobic_polarity_value= calculate_properties(extract)
             # Save calculated properties and link them to the protein_sequence instance
            protein_properties = ProteinProperties(
                protein=new_sequence,
                molecular_weight=weight,
                isoelectric_point=ip,
                extinction_coefficient=str(extinction_coefficient),
                instability_index=instability_index,
                gravy=gravy,
                aliphatic_index=aliphatic_idx,
                aromatic_ratio=aromatic_ratio_value,
                hydrophobic_polarity=hydrophobic_polarity_value
            )
            protein_properties.save()
            


            return render(request, 'myprotein/index.html',{'new_sequence':new_sequence,
                                                           'extract':extract,
                                                           'weight':weight,
                                                           'ip':ip,'extinction_coefficient':extinction_coefficient,
                                                           'instability_index':instability_index,
                                                           'gravy':gravy,
                                                           'aliphatic_idx':aliphatic_idx,'aromatic_ratio_value':aromatic_ratio_value,
                                                           'hydrophobic_polarity_value':hydrophobic_polarity_value})
        
    return render(request, 'myprotein/index.html')