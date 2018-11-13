# nba-drafting
Model and UI for DraftKing's NBA Daily Lineup Challenge.

# Problem Statement:
Our goal is to try and produce a modeling tool that outperforms an average DraftKings player in picking lineups for the Classic NBA daily Lineup Challenge. Every player drafts a **lineup** using $50,000, to score the most fantasy points (**FPT**).

## Plan of Action:

### 1. Gather Data
First we want to gather information that will help us set goals and benchmark our model's performance. We need to gather performance that will help us gauge our performance. Namely we want to learn:
* The average drafter's performance (FP) in a contest
* The average score (FP) a drafter's lineup must achieve in order to receive a payout
* The average 1st place score (FP) in a contest

Second, we will need to gather the actual data for our model. We need to determine what information significantly impacts a player's value in a fantasy lineup. This will be a mix of individual player statistics, various team statistics, and the salary DraftKing assigns to the player.

##### Individual
* Average FPT
* Injury-status
* Individual matchup
* DraftKings Salary

##### Team
* Pace
* Opposing Team Defense
* Playing back-to-back


### 2. Create a Model to Evaluate Players
The critical key problem we must solve is how to accurately rate and evaluate players. Our model should score players such that those with the highest potential to exceed there average FPT, with reasonable salaries, are scored highly. We need to take into account potential injuries that may shift a lineup on a given night, potential matchups between players that may be particularly favorable for one side, and of course, player and team statistics.


### 3. Devise Methodology for Picking Optimal Lineup
This component should not be too difficult. Given that we have a reliable method of evaluating and scoring players, this is simply a matter of picking the best lineup given the constraints of DrafKing's lineup structure (1 player for each of the 5 traditional positions, 1 additional guard and forward, and 1 utility player of any position). This seems like a permutation of the knapsack problem.


### 4. Create Friendly User Interface (UI)
Finally, we would like to create a friendly UI that will be easy to use everyday. Rather than reading output in terminal, we would like to produce output in a readable and easy to use web format.  
