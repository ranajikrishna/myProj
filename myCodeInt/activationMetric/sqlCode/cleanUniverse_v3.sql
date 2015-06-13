/*
Author : Ranaji Krishna
Date: 28 May 2015
Notes: 2-week behavior.
The number of users imported during thw 2-week trial.

Columns:
(1) app_id - ID of the app.*
(2) sum_tot_dur - total duration spent by admins on the app during trial period.*
(3) **avg_daily_user - average number of users during the trial period.*
(4) avg_daily_msgs - average number of messages during the trial period.*
(5) avg_daily_cnvs - average number of conversations during the trial period.*
(6) avg_daily_cmts - average number of comments during the trial period.*
(7) **avg_daily_mails - average number of  emails during the trial period.*
* To excluude
(8) avg_daily_admins - average number of admins on the app daily during the trial period.* 
(9) mrr_scnd - mrr at the end of the 2nd billing cycle.*
(10) time_to_trial - time between creating an account and starting the trial.*

*/

/*
SELECT *
FROM pg_table_def
WHERE tablename = 'subscriptions'
AND schemaname = 'public';
*/


/*
select 
app.id as app_id,
subs.app_id as sub_app_id
from subscriptions as subs
left join apps as app on app.customer_id = subs.customer_id
*/  






select 
t1.app_id,
t1.first_payment,
t1.second_payment,
t2.tot_users,
t2.avg_daily_users,
t2.avg_daily_admins,
t2.avg_daily_msgs,
t2.avg_daily_cmts,
t2.avg_daily_mails,
t2.avg_daily_cnvs,
t3.sum_tot_dur,
t2.old_id,
t4.time_to_trial
from (

select distinct 
aps.id as app_id,
min(bs.started_at) as subs_st,
aps.created_at as app_ct,
sum (case when bi.billing_cycle_number = 1 then bi.mrr_amount else 0 end) as first_payment,
sum (case when bi.billing_cycle_number = 2 then bi.mrr_amount else 0 end) as second_payment
from billing_subscriptions as bs
left join billing_invoices as bi on bs.id = bi.subscription_id
left join apps as aps on aps.customer_id = bs.customer_id
where aps.contains_any_intercomrades = 0 
and aps.approved_to_send_email_status_id <> 3
and to_char(bs.created_at, 'YYYY-MM-DD') > '2013-00-00'
and bs.started_at is not null
group by aps.id, app_ct

) as t1


left join 


(


select distinct
das.app_id as app_id,
--osub.created_at as osub_ct,
min(osub.id) as old_id,
avg(das.daily_users) as avg_daily_users,
max(das.users) as tot_users,
round(avg(cast(daily_messages as double precision)),2) as avg_daily_msgs, 
round(avg(cast(daily_comments as double precision)), 2) as avg_daily_cmts, 
round(avg(cast(daily_conversations as double precision)),2) as avg_daily_cnvs, 
round(avg(cast(daily_emails as double precision)),2) as avg_daily_mails, 
round(avg(cast(admins as double precision)),2) as avg_daily_admins 
from daily_app_stats as das 
left join apps as aps on aps.id = das.app_id
left join subscriptions as osub on osub.app_id = das.app_id
left join billing_subscriptions as subs on subs.customer_id = aps.customer_id
where to_char(das.created_at, '%Y%m%d') >= to_char(subs.started_at, '%Y%m%d') 
and case when osub.id <= 5675
then 
to_char(das.created_at, '%Y%m%d') <= to_char(subs.started_at + INTERVAL '30 days', '%Y%m%d')
else 
to_char(das.created_at, '%Y%m%d') <= to_char(subs.started_at + INTERVAL '14 days', '%Y%m%d') 
end
and subs.id is not null 
and aps.contains_any_intercomrades = 0
and aps.approved_to_send_email_status_id <> 3
group by das.app_id--, osub.id, osub_ct 


)  

as t2 on t2.app_id = t1.app_id

left join (


select 
pm.app_id as app_id,
sum(abs(ss.duration_in_seconds)) as sum_tot_dur
from "permissions" as pm
left join apps as aps on aps.id = pm.app_id
left join subscriptions as osub on osub.app_id = pm.app_id
left join billing_subscriptions as subs on subs.customer_id = aps.customer_id
left join admin_user_records as aur on aur.admin_id = pm.admin_id
left join sessions as ss on ss.user_id = aur.user_id
where subs.id is not null
and ss.created_at > subs.started_at -- INTERVAL '1 days'
and case when osub.id <= 5675
then 
ss.created_at < subs.started_at + INTERVAL '30 days'
else
ss.created_at < subs.started_at + INTERVAL '14 days'
end
and ss.app_id = 6
group by pm.app_id

) 

as t3 on t3.app_id = t1.app_id


left join(

select
aps.id as app_id, 
aps.created_at as app_ct,
abs(datediff(days,to_date(app_ct,'YYYYmmdd'), to_date(min(bs.started_at),'YYYYmmdd'))) as time_to_trial -- app_st - sub_st
from billing_subscriptions as bs
left join apps as aps on aps.customer_id = bs.customer_id
group by app_id, app_ct

) 

as t4 on t4.app_id = t1.app_id



--select * from daily_app_stats as das limit 10000
