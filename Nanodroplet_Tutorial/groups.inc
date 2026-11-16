# Define regions and groups

# Water
group H2O type OW HW
group oxygen type OW
group hydrogen type HW

# Substrate and ceiling
region bottom_wall block INF INF INF INF INF -45
region top_wall block INF INF INF INF 57 INF
region middle block INF INF INF INF -45 57
group vac region middle
group substrate region bottom_wall
group ceiling region top_wall
group GOLD union substrate ceiling

# Droplet Subregions
region bot_vac_int block INF INF INF INF -44.5 -43
region top_vac block INF INF INF INF -42 -20
group Prefilm region bot_vac_int
group bulk region top_vac
group PF_rel_only dynamic H2O region bot_vac_int every 500


