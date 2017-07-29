
"""
Spectral Convolution Problem: Compute the convolution of a spectrum.
     Input: A collection of integers Spectrum.
     Output: The list of elements in the convolution of Spectrum. If an element has multiplicity k, it should appear exactly k times;
     you may return the elements in any order.
"""

def spectral_convolution(spectrum):
    spectrum = sorted(spectrum)
    convolution_dict = {}
    for i in range(len(spectrum)-1):
        for j in range(i, len(spectrum)):
            mass = spectrum[j] - spectrum[i]
            if mass == 0: continue
            if mass in convolution_dict:
                convolution_dict[mass] += 1
            else:
                convolution_dict[mass] = 1
    convolution = []
    for mass in convolution_dict.keys():
        for k in range(convolution_dict[mass]):
            convolution.append(mass)
    return convolution


def spectral_convolution_quiz():
    with open('DataSets\SpectralConvolution\quiz.txt', 'r') as datafile:
        lines = [line.strip() for line in datafile.readlines()]
        spectrum = [int(mass) for mass in lines[0].split(' ')]
    print(' '.join([str(mass) for mass in spectral_convolution(spectrum)]))


#spectral_convolution_quiz()