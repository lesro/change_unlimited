<h1> <img src="/images/image4.png"
  width="250"
  height="75"
  style="float:left;"></h1>

<div class="boxBorder">

##### TL;DR
* Researched how non-profit functions within different industries, how fundraising is done, the government involvement, and the structure of non-profit.
* Coordinated with the founder to help focus business resources on enhancing social impact, by state and cities.
* Scraped data from IRS website for all nNon-profits in the US for the year 2019 and census data for individuals through API.
* Had to clean and wrangle with data to be able to merge the IRS non-profit dataframe with Census data frame, done by averaging the income by zip codes to match the non-profit data frame.
* Conducted exploratory data analysis (EDA) & feature extraction.
* Narrowed research into only analyzing 501-C-3 organizations by state and cities, concluding there was no statistical significance if income impacts revenues for NPOs within each region.
* Concluded, NPO revenues are impacted by individual income at national level, rejecting the null in favor of the alternative hypothesis. When conducting the same analysis at state and city level, we rejected the null hypothesis in several cities and states. 

#### Analysis: Are revenues for non-profit organizations impacted by household income?
**H<sub>0</sub>:** mean of NPs’ revenue ***are the same*** in lower & upper-half of mean household income. <br>
**H<sub>A</sub>:** mean of NPs’ revenue ***are NOT the same*** in lower & upper-half of mean household income.
</div>

### Summary
The goal for this analysis was to identify regions of interest within the United States that would benefit from Change Unlimited's fundraising platform, helping focus business resources on enhancing social impact. 

Non-profit organizations spend an excessive amount of resources harvesting busienss relationships, many times at the expense  of driving real impact. One can make the argument that raising funds allows for increased impact, and although true, a platform that has reach and scale for donors and fundraisers  allows for both, increased revenues and increased impact. 

This is **Change Unlimited's** objective. 

### Background & Inspiration
With a background in finance and wealth management, I always carry a deep personal interest in understanding how money impacts decision making across busnesses and individuals. Money/Finance is one of the few instruments in life which is found in every human interaction, practically tied into time. 

Constinently carrying this view, I look for ways to apply different analysis in areas that I don't fully understand. Shortly after moving to Austin, TX I met Change Unlimited's Founder, a startup looking to change the way non-profit organizations fundraise. As a default skeptic of non-profit organizations, I had many questions. 

My skepticism stems mainly from the mismanagement of funds and the difficulty to measure the true social impact an organization makes. Having these doubts, Change Unlimited kindly allowed me to analyze the organzations data and help develop ideas on possible paths forward.

#### Analysis: Are revenues for non-profit organizations impacted by household income?

## Hypothesis
The first question to understand was very high level. Having little domain knowdlege of the non-profit industry, I started at a point that is most familiar, money/finance. Hoping to uncover more questions than answers, the data definitely did not disappoint. 

**H<sub>0</sub>:** mean of NPs’ revenue ***are the same*** in lower & upper-half of mean household income. <br>
**H<sub>A</sub>:** mean of NPs’ revenue ***are NOT the same*** in lower & upper-half of mean household income.

The t-test was conducted on revenues between the NPs operating in areas below the mean household income and those above the mean household income. Considering this was an initial dive, not having many biases going into this project, and understand the realities of distribution of income, alpha was set to .10. This increased the chances of observing Type I errors.

## Data

There were three sources of information, data directly from Change Unlimited, income and nonprofit data from www.irs.gov, and demographic and income data from www.census.gov. 

Change Unlimited's data was mainly pre-structured and formatted, same as IRS data, the information existed as csv files. 
* individual income reported to IRS 
* all non-profit orgs registered in US, with financial data

Census data required connecting to the site via API and pulling in the information necessary to run my test. 
* mean household income by city and state, also pulled in additional information such as, age, sex, employment status, and industry worked.

## Exploratory Data Analysis

Here I finally dive into the data I've gathered. The original dataset from Change Unlimited and the IRS of non-profit orgs registered, within US, was appx 1.7M. The IRS dataset for individual incomes included ~166K datapoints, while the census data pulled included demographic information for 630 US cities.

In order to merge data, I needed to establish the mean income within the area a nonprofit operates in. I did this by cross validating the information I attained from IRS income and census data and assigning each non-profit's zip code with a mean HH income. Subsequently, I needed to ensure the data was not skewed by the thousands of reported non-profits that were not operating, to accomplish this I only analyzed the organizations that reported revenues larger than $0. Then, I merged the tables between income and non-profit orgs, dropping any areas in the US that did not have a reported mean income within our IRS/Census data. 

That brought our scope from ~1.7M to ~410K organizations. 

Following this step, I began some preliminary graphs to visually identify any points of interest that may be worth inspecting. 

#### How are organizations distributed across the US? Which states account for what portion of NP and revenues?
![npsregistered](/images/num_nps2.png)
**Actionable thoughts:** 
* What's going on in Oregon? Low number of orgs massive jump in revenues.  
* Why the big difference between the top states? Immediate intutition, most expensive states to live in, what kind of nps are shown here?.

#### What does a scatter of revenues on income look like? Any indications of correlation?
![revonincscat](images/rev_on_inc_scatter2.png)
**Actionable thoughts:** 
* No clear sign of correlation, strong density concentrations on lower left sides of scatter. Zoom into NPs at lower range of revenues?
**Note:** Original scatters had issues representing relationship due to wide range of revenues, updated scatter 

#### Look at Cities by revenue size, are they equally represented by state graph?
![revonincscat](images/num_nps_cityrevsort.png)
**Actionable thoughts:** 
* Portland, OR shows up as number 2, why is there such a concentration in this city? Does it come from mulitple or single sources?
* **Note:** Interestingly enough, CA cities take up only 3 spots and are lower in the rankings. Does marijuana legalization have something to do with this? NYC, as expected, takes the number 1 spot, the financial capital of the world. 

Next, I wanted to take a look at how the IRS classifies organizations and see if there are any categories that stand out. Two things to note about these classifications, the IRS uses 2 categories to identify non-profit organizations, Subsections and Foundation. 

* **Subsection:** are the codes shown under section 501(c) of the Internal Revenue Code of 1986, which define the category under which an organization may be exempt.

* **Foundation:** are codes for Recognition of Exemption, and is used to specify the statutory reason why an organization qualifies as a 501(c)(3) public charity or private foundation.

Since some of these codes have very long descriptions, below I will use some appreviated versions of these explanations and do my best to provide light on details that may not fit within the visualizations. 

#### What is the breakdown by subsection category?
![npsubsection](images/npsubsection.png)
**Actionable thoughts:** 
* A significant concentration on organizations classified as 501(c)3, accounting for over 75% of all revenues, 1.75T in revenues. Focus in on these and understand why majority of the organizations fall under this category. 
* **NOTE:** 501(c)3 code are Religious, Educational, Charitable, Scientific, Literary, Testing for Public Safety, to Foster National or International Amateur Sports Competition, or Prevention of Cruelty to Children or Animals Organizations. Donations are tax exempt. 

#### What is the breakdown by foundation category?
![npfoundation](images/npfoundation.png)
**Actionable thoughts:** 
* Things got really interesting here, focusing in on the top 2 categories, I see a massive concentration between 12-Hospital/Research facilities and 15-Orgs receiving substantial amount of funding from government and general public. The storys of each seem to be completely disconnected. Category 12, seems to be a handful of organizations in relation to category 15, where reveneus come from a large pool of organizations. Find out what's going on in category 12. 
* Another interesting catch in this graph is how the IRS bundles funding within category 15. Reflecting both government funded orgs and public funded orgs together. Technically, the grouping is correct, the government i receives funding through the general public, via taxes, the then decide how to allocate some of those funds to non-profit organizations. But, this can be a slippery slope, one is funding at the discretion of the government, while the other is discretion of the US tax payer. A future project may be to apply NLP to government documents to identify which programs are funded at the discretion of the government.

At this stage I had a decent idea to identify which groups I wanted to run our testing for, 501(c)3-15. that 

![501c3state](images/501c3top10.png)


![501c315state](images/501c315top10.png)



## Results

![allUSrevs](images/allUSrev.png)

![statetop4](images/top4null.png)

![state4to8](images/top4to8null.png)

![states9to12](images/top9to12null.png)

## Additional Factors to Consider

## Moving Forward



# Data
----------
www.irs.gov <br>
www.census.gov <br>
https://www.consumerfinance.gov <br>
