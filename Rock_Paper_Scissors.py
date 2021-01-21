# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
from RPS_game import play, mrugesh, abbey, quincy, kris, human, random_player
def player(prev_play,opponent_history=[],my_history=[],play_order=[{
"RRR": 0,
"RRP": 0,
"RRS": 0,
"RPR": 0,
"RPP": 0,
"RPS": 0,
"RSR": 0,
"RSP": 0,
"RSS": 0,
"PRR": 0,
"PRP": 0,
"PRS": 0,
"PPR": 0,
"PPP": 0,
"PPS": 0,
"PSR": 0,
"PSP": 0,
"PSS": 0,
"SRR": 0,
"SRP": 0,
"SPR": 0,
"SPP": 0,
"SPS": 0,
"SSR": 0,
"SSP": 0,
"SSS": 0,
}]):
    opponent_history.append(prev_play)
    winning_set = { 
      "R":"P",
      "P":"S",
      "S":"R"
    }

    counter_set = { 
      "R":"P",
      "P":"S",
      "S":"R"
    }

    if (len(my_history)>1) and (len(opponent_history)>1):
      if ((opponent_history[-3]!="") and(opponent_history[-2]!="") and (opponent_history[-1]!="") and (opponent_history[-3]=="P") and (opponent_history[-2]=="R") and (opponent_history[-1]=="S") and (my_history[-3]!="") and(my_history[-2]!="") and (my_history[-1]!="") and (my_history[-3]=="R") and (my_history[-2]=="S") and (my_history[-1]=="P")):
        values_view = counter_set.values()
        value_iterator = iter(values_view)
        first_value = next(value_iterator)
        guess = first_value
      elif ((opponent_history[-3]!="") and(opponent_history[-2]!="") and (opponent_history[-1]!="") and (opponent_history[-3]=="S") and(opponent_history[-2]=="P") and (opponent_history[-1]=="R") and (my_history[-3]!="") and(my_history[-2]!="") and (my_history[-1]!="") and (my_history[-3]=="P") and (my_history[-2]=="R") and (my_history[-1]=="S")):
        guess = counter_set["P"]
      elif ((opponent_history[-3]!="") and(opponent_history[-2]!="") and (opponent_history[-1]!="") and (opponent_history[-3]=="R") and (opponent_history[-2]=="S") and (opponent_history[-1]=="P") and (my_history[-3]!="") and(my_history[-2]!="") and (my_history[-1]!="") and (my_history[-3]=="S") and (my_history[-2]=="P") and (my_history[-1]=="R")):
        guess = counter_set["S"]
      elif (winning_set[my_history[-1]]==prev_play):
        guess = winning_set[prev_play]
      else:
        if not prev_play:
          prev_play = 'R'
        opponent_history.append(prev_play)

        last_three = "".join(opponent_history[-3:])
        if len(last_three) == 3:
          play_order[0][last_three] += 1

        potential_plays = [
            prev_play + "R" + "R",
            prev_play + "R" + "P",
            prev_play + "R" + "S",
            prev_play + "P" + "R",
            prev_play + "P" + "P",
            prev_play + "P" + "S",
            prev_play + "S" + "R",
            prev_play + "S" + "P",
            prev_play + "S" + "S",
        ]

        sub_order = {
            k: play_order[0][k]
            for k in potential_plays if k in play_order[0]
        }

        prediction = max(sub_order, key=sub_order.get)[-1:]

        ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
        guess = ideal_response[prediction]

      
               
    else:
      guess = "P"
    my_history.append(guess)
    return guess