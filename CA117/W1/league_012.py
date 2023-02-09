#!/usr/bin/env python3

import sys

teamnames = []
teams = []

for team in sys.stdin:
   team = team.strip().split()
   teamname = " ".join(team[1:-8])
   teamnames.append(teamname)
   teams.append(team)

longest_team = 0
for name in teamnames:
   if len(name) > longest_team:
      longest_team = len(name)

toplineclub = f"{'POS':>3} {'CLUB':<{longest_team}} "
toplinepwdl = f"{'P':>2} {'W':>3} {'D':>3} {'L':>3} "
toplinegoals = f"{'GF':>3} {'GA':>3} {'GD':>3} {'PTS':>3}"
print(toplineclub + toplinepwdl + toplinegoals)
for team in teams:
   teamname = " ".join(team[1:-8])
   p, w, d, l, gf, ga, gd, pts = team[-8], team[-7], team[-6], team[-5], team[-4], team[-3], team[-2], team[-1]

   posclub = f"{team[0]:>3} {teamname:<{longest_team}} "
   pwdl = f"{p:>2} {w:>3} {d:>3} {l:>3} "
   goals_pts = f"{gf:>3} {ga:>3} {gd:>3} {pts:>3}"
   print(posclub + pwdl + goals_pts)
