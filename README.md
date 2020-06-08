
# T3020   Repo for ELEN3020

Name: Amy Pegram
Date: 7 June


# Description of code -- for question 1.1 and 1.2

The program `datamunger.py` is used to quality check data files. A
sample data file is given. The first row consists of headings which
the program ignores. The quality checks are

* The column TALL should be the sum of T1 through T8 inclusive
* For each of columns TALL and T1 through T7 inclusive (not T8),  the values increase monotonically. For example if in row 13, column T3 there's a value 49 (for example), then in row 14, column T3 the value should be 49 or greater.

Note, however, there is some missing data in some of the rows. The first few lines only contain values for TALL and only the latter half has values for OTHER.  If there are missing data for any row in columns TALL and T1 through T8 then that row should not be checked. However, we keep track of how many rows there are with missing data


### Errors

There are three deliberate errors, marked E1, E2 and E3. Finding other (non-deliberate and unknown to me)  errors will get a bonus -- clearly add below this line in your copy of the README what the errors are and how you fixed them.

### My Changes

E1 Changed curr[2:9] to curr[1:9] as it wasnt counting column 1
E2 Changed curr[i] <= prev[i] to curr[i] < prev[i] as monotonic means numbers can be equal
E3 I could not see an obvious error here

Others:
Data on line 36 was unused, deleted it
Changed for i in range(9) for check monotomic to for i in range(8) as T8 does not have to be monotomic.
