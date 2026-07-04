-- tests/stg_users_valid_accept_rate.sql
select *
from {{ ref('stg_users') }}
where (accept_rate < 0 or accept_rate > 100)
