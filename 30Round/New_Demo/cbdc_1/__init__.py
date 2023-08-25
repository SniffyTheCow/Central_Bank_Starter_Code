from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'cbdc_1'
    PLAYERS_PER_GROUP = 3
    NUM_ROUNDS = 1
    # switch according to table A = 1, etc
    A_ROLE = 'a Blue Player'
    B_ROLE = 'A Blue Player'
    C_ROLE = 'the Red Player'
    TradeValue = 29
    NullTrade = 30
    TradeBonus = 50


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
#These are variables ive set for use in the results table or in the payoff function
    Participation_Count = models.IntegerField()
    Outcome = models.StringField()


class Player(BasePlayer):
    value = models.FloatField()

    trade = models.BooleanField(
        label="Would you like to Trade?",
        choices=
        [[True, "Yes"], [False, "No"]],
    )

    vote = models.BooleanField(
        label="You are the Decision Maker. Do you want to assign the trade bonus to the Red Player?",
        choices=
        [[True, "Yes"], [False, "No"]],
    )

    empty = models.StringField(
        label="Please Select Next. The Decision Maker is Making Their Decision."
    )


# PAGES
class Waiting(WaitPage):
    pass


class Chat1(Page):
    timer_text = 'Time left in chat segment:'
    timeout_seconds = 120


class Participate(Page):
    form_model = 'player'
    form_fields = ['trade']


class PWaitPage(WaitPage):
#This code calculates the payoffs before decision making
    @staticmethod
    def after_all_players_arrive(group: Group):
        participation_count = 0
        player_list = group.get_players()
        player1 = player_list[0]
        player2 = player_list[1]
        player3 = player_list[2]
        players = [player1, player2, player3]
        for p in players:
            if p.trade:
                participation_count += 1
        group.Participation_Count = participation_count
        if player3.trade: # player who gets bonus (also switch the number you replaced like if 3 -> 1 also 1 -> 3)
            player3.payoff = (int(participation_count) - 1) * (int(C.TradeValue) + int(C.TradeBonus)) + (int(3 - participation_count) * int(C.NullTrade))
        else:
            player3.payoff = int(C.PLAYERS_PER_GROUP - 1) * int(C.NullTrade)
        if player2.trade:
            player2.payoff = int(participation_count - 1) * int(C.TradeValue) + (int(3 - participation_count) * int(C.NullTrade))
        else:
            player2.payoff = int(C.PLAYERS_PER_GROUP - 1) * int(C.NullTrade)
        if player1.trade:
            player1.payoff = int(participation_count - 1) * int(C.TradeValue) + (int(3 - participation_count) * int(C.NullTrade))
        else:
            player1.payoff = int(C.PLAYERS_PER_GROUP - 1) * int(C.NullTrade)

class Vote(Page):
### This Code Shows the Vote page to only the decision maker:
    form_model = 'player'
    @staticmethod
    def get_form_fields(player):
        if player.role == C.C_ROLE: # change to player with the voting role
            return ['vote']
        else:
            pass


class ResultsWaitPage(WaitPage):
### This code redefines the payoff and sets the result table values based on the decision
    def after_all_players_arrive(group: Group):
        player_list = group.get_players()
        player1 = player_list[0]
        player2 = player_list[1]
        player3 = player_list[2]
        if player3.trade: # player who gets the bonus
            if not player3.vote: # change to player with voting roll
                bonus = (int(group.Participation_Count - 1) * int(C.TradeBonus))
                player3.payoff -= int(bonus) # player who gets the bonus
                player3.payoff += int(bonus)/2 # change to player with voting roll
                group.Outcome = 'Not Awarded'
            else:
                group.Outcome = 'Awarded'
        else:
            if not player3.vote: # change to player with voting roll
                group.Outcome = 'Not Awarded'
            else:
                group.Outcome = 'Awarded'


class Results(Page):
    pass


page_sequence = [Waiting, Participate, PWaitPage, Vote, ResultsWaitPage, Results]
