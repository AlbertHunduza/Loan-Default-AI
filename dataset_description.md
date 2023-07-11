The Data

The dataset was found at this [webpage](https://datascienceuwl.github.io/Project2018/TheData.html)
This dataset includes 30 variables for 50,000 loans. You can grab the csv file [here](https://datascienceuwl.github.io/Project2018/loans50k.csv)

Details of the variables are given below.

The variables in the data are fully described in a table below. The response variable will be built from the loan status variable status. The total amount repaid to the bank, totalPaid, cannot be used as a predictor variable because it is information that cannot be known before the loan is issue so be sure not to include it as a predictor in your models. All other variables can be used as predictors, but some are not useful.

variable    description <br>
\n
amount	-   loan amount in dollars <br>

term	-   loan term is 36 or 60 months <br>
rate	-   interest rate as a decimal <br>
payment	-   monthly payment amount <br>
grade	-   grade of loan: A is least risk, G is most risk <br>
employment	-   job title of applicant <br>
length	-   time continuously employed <br>
home	-   home ownership: rent, own, mortgage <br>
income	-   annual income in dollars <br>
verified	-   verification status of annual income <br>
status	-   loan status: DEFAULT, CURRENT, CHARGED OFF, etc. <br>
reason	-   applicants purpose for the loan <br>
state	-   two letter state code of applicant <br>
debtIncRat	-   ratio monthly non-mortgage debt payment to monthly income <br>
delinq2yr	-   number of 30+ day late payments in last two years <br>
inq6mth	-   number of credit checks in the past 6 months <br>
openAcc	-   number of open credit lines <br>
pubRec	-   number of derogatory public records including bankruptcy filings, tax liens, etc. <br>
revolRatio	-   proportion of revoling credit in use <br>
totalAcc	-   total number of credit lines in file, includes both open and closed accounts <br>
totalPaid	-   total amount repaid to bank (THIS IS NOT A PREDICTOR SINCE IT CAN ONLY BE DETERMINED AFTER A LOAN IS ISSUED) <br>
totalBal	-   total current balance of all credit accounts <br>
totalRevLim	-   sum of credit limits from all credit lines <br>
accOpen24	-   how many accounts were opened in the past 24 months <br>
avgBal	-   average balance per account <br>
bcOpen	-   total unused credit on credit cards <br>
bcRatio	-   ratio of total credit card balance to total credit card limits <br>
totalLim	-   total credit limits <br>
totalRevBal	-   total credit balance except mortgages <br>
totalBcLim	-   total credit limits of credit cards <br>
totalIlLim	-   total of credit limits for installment accounts <br>