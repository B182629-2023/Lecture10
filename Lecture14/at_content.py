#!/usr/bin/python3

def get_at_content(some_dna):
    length = len(some_dna)
    a_count = some_dna.upper().count('A')
    t_count = some_dna.upper().count('T')
    at_content = (a_count + t_count) / length
    return at_content
