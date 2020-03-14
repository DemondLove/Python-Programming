'''
Given a year, return the century it is in. The first century spans from the year 1 up to and including the year 100, the second - from the year 101 up to and including the year 200, etc.

Example

For year = 1905, the output should be
centuryFromYear(year) = 20;
For year = 1700, the output should be
centuryFromYear(year) = 17.
Input/Output

[execution time limit] 4 seconds (py3)

[input] integer year

A positive integer, designating the year.

Guaranteed constraints:
1 ≤ year ≤ 2005.

[output] integer

The number of the century the year is in.
'''

def centuryFromYear(year):
    dict = {
            '1': list(range(1,101))
            , '2': list(range(101,201))
            , '3': list(range(201,301))
            , '4': list(range(301,401))
            , '5': list(range(401,501))
            , '6': list(range(501,601))
            , '7': list(range(601,701))
            , '8': list(range(701,801))
            , '9': list(range(801,901))
            , '10': list(range(901,1001))
            , '11': list(range(1001,1101))
            , '12': list(range(1101,1201))
            , '13': list(range(1201,1301))
            , '14': list(range(1301,1401))
            , '15': list(range(1401,1501))
            , '16': list(range(1501,1601))
            , '17': list(range(1601,1701))
            , '18': list(range(1701,1801))
            , '19': list(range(1801,1901))
            , '20': list(range(1901,2001))
            , '21': list(range(2001,2006))
        }
    for x in dict.keys():
        if year in dict[x]:
            return int(x)
