/*
Author : Ranaji Krishna
Date: 28 May 2015
Notes: 2-week behavior.
The number of users imported during thw 2-week trial.

Columns:
(1) app_id - ID of the app.
(2) tot_dur - total duration spent by admins on the app during trial period.
(3) avg_user - average number of users during the trial period.
(4) avg_msgs - average number of messages during the trial period.
(5) avg_cmts - average number of comments during the trial period.
(6) avg_mails - average number of  emails during the trial period.
(7) avg_admins - average number of admins on the app daily during the trial period. 
(8) mrr_scnd - mrr at the end of the 2nd billing cycle. 
(9) time_to_trial - time between creating an account and starting the trial.

*/

/*
SELECT *
FROM pg_table_def
WHERE tablename = 'billing_invoices'
AND schemaname = 'public';
*/

/* --- --- */
/* Notes: In the sessions table:
(1) Some duration_in_seconds are -ve, hence absolute values are taken.
(2) Some duration_in_seconds are NULL so we exclude them. 

*/
select app_id, sum(cast(abs(duration_in_seconds) as real)) as tot_dur, avg_user, avg_msgs, avg_cmts, avg_mails, avg_admins, mrr_scnd, sub_trial_st, trial_ed, sessions_app_id, time_to_trial  from ( -- t11

/* --- Join with Sessions --- */
select t10.app_id, avg_user, avg_msgs, avg_cmts, avg_mails, avg_admins, mrr_scnd, sub_trial_st, 
trial_ed, duration_in_seconds, sessions.app_id as sessions_app_id, time_to_trial  from( -- t10

/* --- Join t6 and sessions on app_id --- */
/*
Notes: 
(1) This is done to get the average time spent by app during the 14-day trial.
*/

select * from ( -- t7 / t9

select distinct app_id, round(avg(cast(daily_users as real)),2) as avg_user, round(avg(cast(daily_messages as double precision)),2) as avg_msgs, round(avg(cast(daily_comments as double precision)), 2) as avg_cmts, round(avg(cast(daily_emails as double precision)),2) as avg_mails, round(avg(cast(admins as double precision)),2) as avg_admins, round(avg(cast(mrr_sec as double precision)),2) as mrr_scnd, sub_trial_st, trial_ed, time_to_trial from ( -- t6

/* --- Join t4 and daily_app_stats on app_id --- */
/*
Notes: 
(1) This is done to get daily_users, daily_messages, daily_comments, daily_emails, admins,
during the 14-day trial.
*/

select * from( -- t4 / t5

/* --- Join t1 and apps on customer_id --- */
/*
Notes: 
(1) This is done to get the time of first deployment (vjs - not required for 'the 2 week behavior'), the number of users up to the 2nd billing cycle ( -- not required for 'the 2 week behavior') and the app_id.
(2) Get the subscription trial start date (min. across all sub. start dates) and compute the subscription trial end date.
(3) sum(mrr_aount) gives the total mrr_amount till the 2nd billing cycle.
*/

select app_cust_id, app_id, app_name, min(subs_trial_st) as sub_trial_st, to_char(to_date(min(subs_trial_st),'YYYYmmdd') + interval '14 days', 'YYYYmmdd') as trial_ed, avg(datediff(days,to_date(app_created_at,'YYYYmmdd'), to_date(subs_trial_st,'YYYYmmdd'))) as time_to_trial, mrr_amount as mrr_sec from ( -- t3
-- datediff(seconds,to_date(app_created_at,'YYYYmmdd'), to_date(subs_trial_st,'YYYYmmdd')) as time_to_trial,
/* --- t1: Join billing_invoices and billing_subscriptions.id on billing_invoices.subscription_id --- */
/* Notes: 
(1) The mrr_amount is taken from the billin_invoices table, at the 2nd billing cycle.
(2) Apps that cancelled between the 1st and 2nd billing cycle ARE INCLUDED; their corresponding mrr_amount = 0.
(3) An upper bound on the mrr_amount of $10,000 is applied.
*/
select * from ( -- t1 / t2
select billing_subscriptions.id as subs_id, customer_id as subs_cust_id, to_char(billing_subscriptions.created_at, 'YYYYmmdd') as subs_created_at, to_char(billing_subscriptions.cancelled_at, 'YYYYmmdd') as subs_cancelled_at, to_char(billing_subscriptions.started_at, 'YYYYmmdd') as subs_trial_st, billing_invoices.id as invo_id, to_char(billing_invoices.period_end, 'YYYYmmdd') as invo_issue_at, billing_invoices.billing_cycle_number as cycle_number, billing_invoices.total_amount, billing_invoices.mrr_amount, to_char(billing_invoices.cancelled_at,'YYYYmmdd') as invo_cancelled_at, billing_invoices.subscription_id as inv_subs_id
from billing_subscriptions  
left join billing_invoices
on billing_subscriptions.id = billing_invoices.subscription_id where cycle_number = 2 and mrr_amount <= 1000000 or (cycle_number = 1 and billing_invoices.cancelled_at is not Null)
) as t1 

left join(
select apps.id as app_id, apps.name as app_name, to_char(apps.created_at, 'YYYYmmdd') as app_created_at, to_char(apps.installed_at, 'YYYYmmdd') as app_install_at, apps.customer_id as app_cust_id, user_count as no_users, to_char(first_production_vjs_request_at,'YYYYmmdd') as app_vjs
from apps 
) as t2 on t2.app_cust_id = t1.subs_cust_id 
) as t3 group by app_cust_id, app_id, app_name, mrr_sec
) as t4

left join(
select app_id as daily_app_id, daily_users, daily_messages, daily_comments, daily_emails, admins, to_char(daily_app_stats.created_at, 'YYYYmmdd') as daily_start
from daily_app_stats
) as t5 on t4.app_id = daily_app_id where daily_start between t4.sub_trial_st and t4.trial_ed
) as t6 group by app_id, sub_trial_st, trial_ed, time_to_trial
) as t7

left join(

/* --- Join t8 with admin_user_records --*/
/* Notes:
(1) To get user_id's so that we can join with sessions.
*/
select perm_app_id, perm_admin_id, user_id as records_user_id from ( -- t8
select app_id as perm_app_id, admin_id as perm_admin_id from "permissions"
) as t8

left join admin_user_records on t8.perm_admin_id = admin_user_records.admin_id
) as t9 on t9.perm_app_id = t7.app_id

) as t10 

left join sessions 
on t10.records_user_id = user_id where sessions_app_id = 6 and to_char(started_at,'YYYYmmdd') between t10.sub_trial_st and t10.trial_ed and sessions.duration_in_seconds is not Null
) as t11 group by app_id, avg_user, avg_msgs, avg_cmts, avg_mails, avg_admins, mrr_scnd, sub_trial_st, trial_ed, time_to_trial, sessions_app_id 

