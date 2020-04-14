from data import data1


def covid19ImpactEstimator(data):

    impact = {}
    severeImpact = {}
    estimate = {
        "impact": impact,
        "severeImpact": severeImpact
    }

    factor = 3
    period = data['timeToElapse']
    reportedCases = data['reportedCases']
    periodType = data['periodType']

    if periodType == 'days':
        val = 1
    elif periodType == 'weeks':
        val = 7
    elif periodType == 'months':
        val = 30

    impact['currentlyInfected'] = data['reportedCases'] * 10
    severeImpact['currentlyInfected'] = data['reportedCases'] * 50

    impact['infectionsByRequestedTime'] = impact['currentlyInfected'] * \
        (2 ** ((val * period) // factor))
    severeImpact['infectionsByRequestedTime'] = severeImpact['currentlyInfected'] * \
        (2 ** ((val * period) // factor))

    output1 = {
        "data": data,
        "impact": impact,
        "severeImpact": severeImpact
    }

    return output1


covid19ImpactEstimator(data1)
