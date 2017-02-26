# Description

Difficulty may be higher than easy,
(((3))) is an expression with too many parentheses.
The rule for "too many parentheses" around part of an expression is that if removing matching parentheses around a section of text still leaves that section enclosed by parentheses, then those parentheses should be removed as extraneous.
(3) is the proper stripping of extra parentheses in above example.
((a((bc)(de)))f) does not have any extra parentheses. Removing any matching set of parentheses does not leave a "single" parenthesesed group that was previously enclosed by the parentheses in question.

## Inputs

((a((bc)(de)))f)  
(((zbcd)(((e)fg))))
ab((c))

## Outputs

((a((bc)(de)))f)  
((zbcd)((e)fg))
ab(c)

## Link to Challenge

https://www.reddit.com/r/dailyprogrammer/comments/5llkbj/2017012_challenge_298_easy_too_many_parentheses/