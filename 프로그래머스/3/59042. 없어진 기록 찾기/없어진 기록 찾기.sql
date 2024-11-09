SELECT o.ANIMAL_ID, o.NAME
from ANIMAL_OUTS o left join ANIMAL_INS i on o.ANIMAL_ID = i.ANIMAL_ID
where i.ANIMAL_ID is null and o.ANIMAL_ID is not null
order by 1


