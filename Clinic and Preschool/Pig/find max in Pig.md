A = LOAD 'clinic_score/part-r-00000' USING PigStorage(' ')
AS (zipcode:int, count:int, weightedcnt:float);

B = GROUP A ALL;

C = FOREACH B GENERATE MAX(A.weightedcnt);

STORE C INTO 'clinic_max_score';