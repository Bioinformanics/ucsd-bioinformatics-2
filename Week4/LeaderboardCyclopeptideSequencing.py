"""
LeaderboardCyclopeptideSequencing(Spectrum, N)
    Leaderboard ← set containing only the empty peptide
    LeaderPeptide ← empty peptide
    while Leaderboard is non-empty
        Leaderboard ← Expand(Leaderboard)
        for each Peptide in Leaderboard
            if Mass(Peptide) = ParentMass(Spectrum)
                if Score(Peptide, Spectrum) > Score(LeaderPeptide, Spectrum)
                    LeaderPeptide ← Peptide
            else if Mass(Peptide) > ParentMass(Spectrum)
                remove Peptide from Leaderboard
        Leaderboard ← Trim(Leaderboard, Spectrum, N)
    output LeaderPeptide
"""

amino_acid_mass_table = {'G':57,'A':71,'S':87,'P':97,'V':99,'T':101,'C':103,'I':113,'L':113,'N':114,'D':115,'K':128,'Q':128,'E':129,'M':131,'H':137,'F':147,'R':156,'Y':163,'W':186}


def _expand(peptides):
    return [peptide + amino_acid for amino_acid in amino_acid_mass_table.keys() for peptide in peptides]


def _get_peptide_mass(peptide):
    return sum([amino_acid_mass_table[amino_acid] for amino_acid in peptide])


def _get_parent_mass(spectrum):
    return spectrum[-1]


def linear_spectrum(peptide):
    prefix_mass = [0]
    for i in range(len(peptide)):
        prefix_mass.append(prefix_mass[i]+amino_acid_mass_table[peptide[i]])

    theoretical_spectrum = [0]
    for i in range(len(prefix_mass)-1):
        for j in range(i+1, len(prefix_mass)):
            theoretical_spectrum.append(prefix_mass[j]-prefix_mass[i])
    return sorted(theoretical_spectrum)


def _linear_score(peptide, spectrum):
    theoretical_spectrum = linear_spectrum(peptide)
    all = set(theoretical_spectrum).union(set(spectrum))
    return sum([min(theoretical_spectrum.count(mass), spectrum.count(mass)) for mass in all])


#peptide = 'ITCHRTLHFWCRCFLLDKEYYLKSDWIIKWRGLWIV'
#spectrum = '0 57 57 57 71 87 99 101 101 101 103 103 113 113 113 113 113 113 113 113 115 115 128 128 129 129 137 137 137 147 156 156 163 163 163 170 170 170 170 185 186 186 202 208 208 212 213 214 214 214 214 216 216 227 230 240 242 250 250 250 256 259 259 260 276 276 283 284 287 292 298 299 301 311 313 315 321 323 326 326 327 327 329 331 333 340 341 345 345 351 351 356 359 362 363 383 388 393 396 400 405 406 412 414 422 424 426 428 436 439 444 444 446 448 454 455 458 462 464 467 469 469 471 474 484 492 496 499 501 503 508 509 511 517 519 526 537 537 537 537 556 557 558 559 561 568 568 570 575 577 582 582 599 604 607 607 608 612 618 622 624 630 630 638 639 639 639 646 650 650 655 659 662 669 671 674 678 686 687 696 697 704 707 717 717 720 721 727 733 743 745 745 751 751 752 752 759 768 770 770 784 784 787 787 793 798 800 807 809 809 814 815 818 820 825 830 834 836 848 854 858 858 864 867 882 883 883 883 885 888 899 906 913 915 921 922 928 929 937 938 940 943 956 959 963 963 967 967 970 970 972 973 985 995 995 996 1000 1000 1001 1004 1012 1027 1030 1044 1053 1056 1066 1066 1068 1069 1072 1074 1080 1085 1085 1091 1096 1098 1099 1099 1107 1108 1110 1115 1125 1126 1126 1133 1140 1141 1143 1145 1156 1179 1181 1181 1186 1197 1198 1199 1203 1209 1212 1212 1214 1219 1223 1229 1244 1246 1254 1254 1254 1255 1269 1269 1271 1272 1274 1280 1282 1289 1294 1299 1301 1310 1312 1326 1327 1355 1356 1357 1359 1366 1367 1375 1375 1382 1382 1383 1386 1391 1392 1395 1395 1400 1402 1411 1414 1432 1437 1439 1439 1458 1462 1466 1468 1471 1473 1474 1484 1496 1504 1504 1505 1511 1513 1513 1524 1529 1531 1538 1545 1552 1570 1571 1574 1577 1581 1595 1599 1600 1602 1602 1603 1605 1612 1617 1618 1625 1626 1634 1642 1660 1667 1682 1683 1687 1698 1708 1713 1715 1715 1716 1718 1718 1718 1721 1724 1727 1733 1737 1763 1765 1768 1771 1773 1788 1811 1811 1817 1819 1825 1826 1830 1831 1831 1836 1837 1842 1850 1850 1858 1876 1878 1878 1883 1894 1919 1929 1930 1932 1932 1933 1938 1939 1940 1948 1951 1958 1963 1973 1974 1979 1982 1995 2007 2022 2032 2033 2039 2041 2044 2045 2053 2061 2061 2064 2066 2086 2089 2092 2095 2108 2110 2111 2135 2137 2146 2152 2152 2159 2162 2170 2179 2181 2189 2192 2193 2209 2217 2223 2224 2230 2242 2250 2265 2271 2272 2274 2275 2280 2294 2299 2320 2322 2322 2325 2329 2343 2345 2345 2367 2379 2386 2387 2387 2395 2400 2402 2412 2435 2438 2448 2457 2466 2469 2480 2480 2485 2488 2500 2501 2515 2516 2528 2537 2558 2572 2581 2581 2582 2585 2593 2598 2601 2601 2603 2604 2629 2650 2656 2661 2665 2671 2685 2694 2714 2716 2718 2728 2730 2741 2745 2751 2767 2774 2778 2793 2798 2812 2817 2831 2831 2841 2843 2848 2869 2879 2880 2904 2906 2911 2930 2932 2937 2944 2949 2968 2982 3004 3006 3007 3017 3017 3039 3045 3062 3065 3074 3081 3107 3118 3119 3119 3130 3152 3163 3176 3187 3193 3202 3220 3231 3231 3232 3244 3288 3289 3289 3315 3315 3330 3333 3344 3349 3390 3401 3402 3406 3416 3443 3452 3486 3503 3519 3529 3543 3544 3565 3576 3599 3656 3656 3657 3666 3689 3700 3713 3757 3769 3813 3826 3826 3852 3870 3870 3927 3939 3983 3989 4040 4040 4102 4153 4203 4316'
#print(_linear_score(peptide, [int(mass) for mass in spectrum.split(' ')]))

"""
Trim(Leaderboard, Spectrum, N, AminoAcid, AminoAcidMass)
    for j ← 1 to |Leaderboard|
        Peptide ← j-th peptide in Leaderboard
        LinearScores(j) ← LinearScore(Peptide, Spectrum)
    sort Leaderboard according to the decreasing order of scores in LinearScores
    sort LinearScores in decreasing order
    for j ← N + 1 to |Leaderboard|
        if LinearScores(j) < LinearScores(N)
            remove all peptides starting from the j-th peptide from Leaderboard
            return Leaderboard
    return Leaderboard
"""
def trim(leaderboard, spectrum, n):
    if len(leaderboard) <= n:
        return leaderboard
    sorted_leaderboard = [(peptide, _linear_score(peptide, spectrum)) for peptide in leaderboard]
    sorted_leaderboard = sorted(sorted_leaderboard, key=lambda entry: entry[1], reverse=True)
    trim_pos = n-1
    for trim_pos in range(n-1, len(leaderboard)-1):
        if sorted_leaderboard[trim_pos][1] > sorted_leaderboard[trim_pos+1][1]:
            break
    return [entry[0] for entry in sorted_leaderboard[:trim_pos+1]]


def leaderboard_cyclopeptide_sequencing(spectrum, n):
    leaderboard = ['']
    leader_peptide = ''
    leader_peptide_score = 0
    while leaderboard:
        leaderboard = _expand(leaderboard)
        loop = list(leaderboard)
        for peptide in loop:
            mass = _get_peptide_mass(peptide)
            parent_mass = _get_parent_mass(spectrum)
            if mass == parent_mass:
                score = _linear_score(peptide, spectrum)
                if score > leader_peptide_score:
                    leader_peptide = peptide
                    leader_peptide_score = score
            elif mass > parent_mass:
                leaderboard.remove(peptide)
        leaderboard = trim(leaderboard, spectrum, n)
    return leader_peptide


def leaderboard_cyclopeptide(spectrum, n):
    leader_peptide = leaderboard_cyclopeptide_sequencing(spectrum, n)
    return [amino_acid_mass_table[amino_acid] for amino_acid in leader_peptide]
