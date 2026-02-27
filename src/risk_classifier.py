def Classification_Competition_Risk(hhi):
    if hhi >2500:
        return "Highly Concentrated"
    elif hhi >1500:
        return "Moderately Competitive"
    else:
        return "Competitive"