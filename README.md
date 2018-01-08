# What's Changed?

Where we list the set of "actionable" attributes. That is, changes usually made by software developers in while updating code.

## Projects

## How the changes were measured?

+ For every project, take pairs of releases (v1, v2).
+ In each release pair, for every [metric](), compute if there is statistically significant differences (based on A12 effect size test) between releases. 
+ Rank the features from most changed to least changed.

#### FAQs
+ Why A12? Are there things that are 0 or 100% of the time? Or, more or less than 50%?

If I checked every *.class file between pairs of projects to see if it was changed, then all the metrics seems to have been changed almost all the time. 

## Rankings

<img width="870" alt="screen shot 2018-01-08 at 6 03 27 pm" src="https://user-images.githubusercontent.com/1433964/34671808-eeb0c5ca-f4a1-11e7-9c11-46fb39cd12ab.png">
