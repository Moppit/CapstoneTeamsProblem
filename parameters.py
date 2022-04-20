"""
PARAMETERS DASHBOARD

Are you unable to find team configurations that fit your constraints?
You can adjust the parameters your capstone teams need to fit below as needed.

NOTE: some constraints are more important than others. 
Try to edit the non-critical constraints to find a feasible solution before changing important ones!
"""
# ----- Consider Constraint -----
CONSIDER_PROJECT_PREFERENCES = True
CONSIDER_TEAMMATE_DISLIKES= True
CONSIDER_TEAMMATE_LIKES= True
CONSIDER_MIN_TEAM_SIZE = False
CONSIDER_MAX_TEAM_SIZE = True
CONSIDER_SPONSOR_REQUESTS = True
CONSIDER_GROUP_DYNAMIC = True

# ----- Adjustable Values Parameters ----- 
MIN_TEAM_SIZE = 4
MAX_TEAM_SIZE = 8   # Can change this to 10 if we want more flexibility

# ----- Critical Parameters -- Modify with caution! -----

# ----- LP Formulation Parameters -- DO NOT Modify -----

PROJECTS_PER_STUDENT = 1                          # default: the student gets assigned 1 project