import pandas as pd
census_df = pd.read_csv('./course1_downloads/census.csv')
census_df.head()
census_df.set_index(['STNAME', 'CTYNAME'])


#Question 5

# Which state has the most counties in it? (hint: consider the sumlevel key carefully! You'll need this for future questions too...)
#
# This function should return a single string value.

def answer_five():
    return census_df[(census_df['SUMLEV'] == 50)].groupby('STNAME')['COUNTY'].nunique().idxmax()


# Question 6
# Only looking at the three most populous counties for each state, what are the three most populous states (in order of highest population to lowest population)? Use CENSUS2010POP.
#
# This function should return a list of string values.

def answer_six():
    return census_df[(census_df['SUMLEV'] == 50)].groupby('STNAME')['CENSUS2010POP'].apply(
    lambda x: x.nlargest(3).sum()).nlargest(
    3).index.values.tolist()



# Question 7
# Which county has had the largest absolute change in population within the period 2010-2015? (Hint: population values are stored in columns POPESTIMATE2010 through POPESTIMATE2015, you need to consider all six columns.)
#
# e.g. If County Population in the 5 year period is 100, 120, 80, 105, 100, 130, then its largest change in the period would be |130-80| = 50.
#
# This function should return a single string value.


def answer_seven():
    class CensusVariables:
        state_name = "STNAME"
        county_name = "CTYNAME"
        census_population = "CENSUS2010POP"
        region = "REGION"
        population_2014 = "POPESTIMATE2014"
        population_2015 = "POPESTIMATE2015"
        population_estimates = ["POPESTIMATE2010",
    			    "POPESTIMATE2011",
    			    "POPESTIMATE2012",
    			    "POPESTIMATE2013",
    			    population_2014,
    			    population_2015]
        county_level = 50
        summary_level = "SUMLEV"

    counties = census_df[census_df[
        CensusVariables.summary_level]==CensusVariables.county_level]
    counties = counties.reset_index()

    return counties.iloc[
	(counties[
	    CensusVariables.population_estimates].max(axis=1) -
	 counties[
	     CensusVariables.population_estimates].min(axis=1)
	).idxmax()][CensusVariables.county_name]

print(answer_seven())


# Question 8
# In this datafile, the United States is broken up into four regions using the "REGION" column.
#
# Create a query that finds the counties that belong to regions 1 or 2, whose name starts with 'Washington', and whose POPESTIMATE2015 was greater than their POPESTIMATE 2014.
#
# This function should return a 5x2 DataFrame with the columns = ['STNAME', 'CTYNAME'] and the same index ID as the census_df (sorted ascending by index)


def answer_eight():
    class CensusVariables:
        state_name = "STNAME"
        county_name = "CTYNAME"
        census_population = "CENSUS2010POP"
        region = "REGION"
        population_2014 = "POPESTIMATE2014"
        population_2015 = "POPESTIMATE2015"
        population_estimates = ["POPESTIMATE2010",
    			    "POPESTIMATE2011",
    			    "POPESTIMATE2012",
    			    "POPESTIMATE2013",
    			    population_2014,
    			    population_2015]
        county_level = 50
        summary_level = "SUMLEV"

    counties_original_index = census_df[census_df[
        CensusVariables.summary_level]==CensusVariables.county_level]
    regions = counties_original_index[
	(counties_original_index[CensusVariables.region]==1) |
	(counties_original_index[CensusVariables.region]==2)]
    washingtons = regions[
	regions[CensusVariables.county_name].str.startswith("Washington")]
    grew = washingtons[washingtons[CensusVariables.population_2015] >
		       washingtons[CensusVariables.population_2014]]
    return grew[[CensusVariables.state_name,
		 CensusVariables.county_name]]
