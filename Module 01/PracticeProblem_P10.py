# Author:  Manuel Perez
# Date:    09/12/2020
#
# Problem 10 (Hard)
# Using a dictionary of fantasy_weights, find the fantasy points 
# scored for Lamar Jackson with the following stats saved to the 
# following dictionary:
# 
# lamar_jackson_stats = {
#   'passing_yds': 3127,
#   'passing_tds': 36,
#   'passing_int': 6,
#   'rushing_yds': 1206,
#   'rushing_tds': 7,
#   'fumbles': 8,
#   'receiving_yds': 0,
#   'receptions': 0,
#   'receiving_td': 0
# }
# Your fantasy_weights dictionary should look like the following:
# 
# fantasy_weights = {
# 'passing_yds': 0.04,
# 'passing_tds': 4,
# 'passing_int': -2,
# 'rushing_yds': 0.10,
# 'rushing_tds': 6,
# 'fumbles': -2,
# 'receiving_yds': 0.10,
# 'receptions': 1, # adjust for half PPR and standard
# 'receiving_td': 6
# }

####################################################################
# Lamar Jackson's stats
lamar_jackson_stats = {
      'passing_yds': 3127,
      'passing_tds': 36,
      'passing_int': 6,
      'rushing_yds': 1206,
      'rushing_tds': 7,
      'fumbles': 8,
      'receiving_yds': 0,
      'receptions': 0,
      'receiving_td': 0
}

fantasy_weights = {
    'passing_yds': 0.04,
    'passing_tds': 4,
    'passing_int': -2,
    'rushing_yds': 0.10,
    'rushing_tds': 6,
    'fumbles': -2,
    'receiving_yds': 0.10,
    'receptions': 1, # adjust for half PPR and standard
    'receiving_td': 6
}

# Calculate the points
passingYardsPoints   = lamar_jackson_stats['passing_yds']   * fantasy_weights['passing_yds']
passingTDPoints      = lamar_jackson_stats['passing_tds']   * fantasy_weights['passing_tds']
passingIntPoints     = lamar_jackson_stats['passing_int']   * fantasy_weights['passing_int']
rushingYardsPoints   = lamar_jackson_stats['rushing_yds']   * fantasy_weights['rushing_yds']
rushingTDPoints      = lamar_jackson_stats['rushing_tds']   * fantasy_weights['rushing_tds']
fumblePoints         = lamar_jackson_stats['fumbles']       * fantasy_weights['fumbles']
receivingYardsPoints = lamar_jackson_stats['receiving_yds'] * fantasy_weights['receiving_yds']
receptionPoints      = lamar_jackson_stats['receptions']    * fantasy_weights['receptions']
receivingTDPoints    = lamar_jackson_stats['receiving_td']  * fantasy_weights['receiving_td']

fantasyPoints = passingYardsPoints + passingTDPoints  \
+ passingIntPoints + rushingYardsPoints               \
+ rushingTDPoints + fumblePoints                      \
+ receivingYardsPoints + receptionPoints              \
+ receivingTDPoints

print('Lamar Jackson\'s fantasy points scored for 2019:', fantasyPoints)
