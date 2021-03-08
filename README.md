# Election_Analysis
Data Analytics M3 Challenge
## Overview of Election Audit
Tom and his supervisor Seth, Colorado Board of Elections employees, are working on election audit of a recent local congressional election. The election result file is in a comma separated value format file. The script is written to analyze the election result data.

The main objectives are:
- Calculate the total number of votes.
- Tabulate votes from different counties and the percentage of the total votes.
- Find the county which has the largest number of votes.
- Analyze votes that each candidate gained and the percentage of the total votes.
- Determine the winner of the election by number of votes.


## Election-Audit Results
As shown in the printed report(*Graph 1*), there were 369,711 votes cast in this congressional election. This number is calculated by adding data row by row from the input file within a `for` loop in the script. The total votes add 1 per round of the loop from the second line in the input data to the last line.

![Election_Results](https://user-images.githubusercontent.com/78275082/110264969-77f8b580-7f88-11eb-92c1-beac17c23a0f.png)
*(Graph 1 Election Results)*
### Votes by counties
Analysis on votes from each county shows:

- Jefferson: 38,855 (10.5%)
- Denver: 306,055 (82.8%)
- Arapahoe: 24,801 (6.7%)

Clearly Denver had the largest number of votes. These numbers were counted and calculated by using dictionary `county_dict`.

### Votes by Candidates
Using the same method, votes gained by each candidate were analyzed. 

- 23.0% of votes (85,213) went to Charles Casper Stockham, 
- 73.8% (272,892) went to Diana DeGette and 
- 3.1% (11,606) went to Raymon Anthony Doane. 

Obviously, the winner of the election is Diana DeGette by 272,892 votes, which counts for 73.8% of the total votes.

## Election-Audit Summary
The analysis of the election results shows that, basing on the 369,711 votes recorded in the election result data, Diana DeGette won the election by 272,892 votes, which counts for 73.8% of the total votes. The number of votes Diana gained are more than three times of the votes gained by the second-place candidate, Charles Casper Stockham, who received 85,213 votes. Majority of the votes are from Denver, which has 306,055 votes, representing 82.8% of the total votes.

The script has potential to analyze the distribution of votes in each county, which can help to understand who each county mainly supports. The script also has potential to analyze the distribution of votes for each candidate by counties, this can help to understand the strengths and weaknesses of each candidate in terms of counties.

In terms of visualization, the script could plot pie charts or stacked bar charts to have a better presentation of the results.
