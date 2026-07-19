from pprint import pprint

from ranking.ranking_engine import rank_repository

report = rank_repository(

    ".",

    "Login fails after password reset"

)

pprint(report)