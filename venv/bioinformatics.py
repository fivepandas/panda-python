def Reverse(Pattern):
    # your code here
    Rpattern = ''
    for char in Pattern:

        Rpattern = char + Rpattern


    return Rpattern
a=Reverse('abcd')
print(a)
Text = '''aactctatacctcctttttgtcgaatttgtgtgatttatagagaaaatcttattaactga
        aactaaaatggtaggtttggtggtaggttttgtgtacattttgtagtatctgatttttaa
        ttacataccgtatattgtattaaattgacgaacaattgcatggaattgaatatatgcaaa
        acaaacctaccaccaaactctgtattgaccattttaggacaacttcagggtggtaggttt
        ctgaagctctcatcaatagactattttagtctttacaaacaatattaccgttcagattca
        agattctacaacgctgttttaatgggcgttgcagaaaacttaccacctaaaatccagtat
        ccaagccgatttcagagaaacctaccacttacctaccacttacctaccacccgggtggta
        agttgcagacattattaaaaacctcatcagaagcttgttcaaaaatttcaatactcgaaa
        cctaccacctgcgtcccctattatttactactactaataatagcagtataattgatctgg'''