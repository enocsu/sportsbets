"""

convert american odds to decimal odds

"""


def to_decimal_odds(american_odds):
    """
    Parameters:
        american_odds (int): a positive or negative integer

    Returns:
        decimal_odds (float): a positive float
    """
    if american_odds < 0:
        return (100 / (-1 * american_odds)) + 1
    else:
        return (american_odds / 100) + 1


"""

calculate implied propability from decimal odds

"""


def implied_odds(decimal_odds):
    """
    Parameters:
        decimal_odds (float): a positive float

    Returns:
        implied_odds (float): a positive float representing a probability
    """
    return 1 / decimal_odds


"""

calculate the amount to bet based on moneyline in decimal odds,
model predictions, and predetermined kelly criterion

"""


def bet_size_pct(decimal_odds,
                 team_prediction,
                 opponent_prediction,
                 kelly_factor):
    """
    Parameters:
        decimal_odds (float): a positive float
        team_prediction (float): a positive float less than 1
        opponent_prediction (float): a positive float less than 1
        kelly_factor (float): a positive float less than 1

    Returns:
        bet_size_pct (float): a positive or negative float
        which represents the percentage of bank roll to wager
    """
    return (((decimal_odds - 1) * team_prediction) - opponent_prediction) / (decimal_odds - 1) * kelly_factor


"""

convert bet size percentage into dollars

"""


def bet_size_dollars(bank_balance, bet_size_pct):
    """
    Parameters:
        bank_balance (float): a positive float
        bet_size_pct (float): a positive or negative float

    Returns bet_size_dollars (float): a positive or negative float
    """
    return bank_balance * bet_size_pct


"""

calculate predicted payout on bet

"""


def bet_payout(bet_size_dollars, decimal_odds):
    """
    Parameters:
        bet_size_dollars (float): a positive or negative float
        decimal_odds (float): a positive float

    Returns
        bet_payout (float): a positive or negative float
    """
    return bet_size_dollars * decimal_odds


"""

determine if a bet should be placed based on kelly criterion

"""


def bet_decision(bet_size_dollars, min_bet_size):
    """
    Parameters:
        bet_size_dollars (float): a positive or negative float
        min_bet_size (float): a positive float
    Returns (int): 1 or 0
    """
    if bet_size_dollars >= min_bet_size:
        return 1
    return 0


"""

calculate expected payout on bet based on the projected bet payout and the
teams prediction. used to calculated the expected value of a bet slip.

"""


def expected_payout(projected_payout, team_prediction):
    """
    Parameters:
        projected_payout (float): a positive or negative float
        team_prediction (float): a positive float
    """
    return projected_payout * team_prediction
