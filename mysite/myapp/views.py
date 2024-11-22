from django.shortcuts import render
from .models import dna_sequence,dna_info  # Import the model

import Bio
import re
from Bio.Seq import Seq

from Bio.SeqUtils import gc_fraction as GC




def information(data):
    header_match = re.match(r'^>.*', data.strip())  # Match the header part

    if header_match:
        return header_match.group(0)  # Return the header as a string
    else:
        return None  # Return None if no header is found
   

def only_sequence(data):
    cleaned_sequence =re.sub(r'[^ATGC]', '',data)
    return cleaned_sequence

def complimentary(data):
    sequence = Seq(data)
    return sequence.complement()
    

def reverse_compliment(data):
    sequence = Seq(data)
    reverse = sequence.reverse_complement()
    return reverse

def trancription(data):
    sequence = Seq(data)
    trans=sequence.transcribe()
    rever_trans=sequence.back_transcribe()
    return trans,rever_trans


def translation(data):
    sequence = Seq(data)
    return sequence.translate()


def translation_stop_codon(data):
    sequence = Seq(data)
    return sequence.translate(table='Standard',to_stop=True)


def gc_content(data):
    sequence = Seq(data)
    content=GC(sequence)
    
    return round(content,2)



def index(request):
    if request.method == "POST":
        sequence = request.POST.get('dna_sequence')  # Correct way to access POST data
        seq_info=request.POST.get('info_sequence')
        
        if sequence and seq_info:  # Check if sequence is not empty
            # Save the sequence to the database

            new_sequence = dna_sequence(dna_sequence=sequence,seq_info=seq_info)
            

            

            new_sequence.save()
            sequence_info=information(new_sequence.dna_sequence)
            clean_sequence1=only_sequence(new_sequence.dna_sequence)
            reverse_comp=reverse_compliment(clean_sequence1)
            comp=complimentary(clean_sequence1)
            trans, rever_trans=trancription(clean_sequence1)
            translat_protein=translation(trans)
            translat_protein_stop=translation_stop_codon(trans)
            gc=gc_content(clean_sequence1)


            dna_info_obj=dna_info(
                dna_sequence=new_sequence,  # Properly assign the foreign key reference
                clean_sequence1=clean_sequence1,
                seq_info=seq_info,  # Assuming seq_info is passed through POST data
                reverse_comp=reverse_comp,
                comp=comp,
                trans=trans,
                translat_protein=translat_protein,
                translat_protein_stop=translat_protein_stop,
                gc=gc



                
            )
            dna_info_obj.save()
            
            # Optionally, you can pass the saved sequence to the template or handle the response
            return render(request, 'myapp/index.html', {'new_sequence': new_sequence,
                                                        'sequence_info':sequence_info,
                                                        'clean_sequence1':clean_sequence1,
                                                        'reverse_comp':reverse_comp,'comp':comp,
                                                        'trans':trans,'rever_trans':rever_trans,
                                                        'translat_protein':translat_protein,
                                                        'translat_protein_stop':translat_protein_stop
                                                        ,'gc':gc})
        

    
    
    return render(request, 'myapp/index.html')



def processing(request):
    sequence=dna_sequence.objects().all()
