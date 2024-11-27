-- model level materialization
-- incremental materialization will fail if the schema of the source changed
{{
  config(
    materialized = 'incremental',
    on_schema_change='fail'
    )
}}
with src_reviews as (
    select * from {{ ref("src_reviews") }}
)
select 
  {{ dbt_utils.generate_surrogate_key(['listing_id', 'review_date', 'reviewer_name', 'review_text'])}} as review_id
  , * 
from src_reviews
where review_text is not null
{% if is_incremental() %}
  and review_date > (select max(review_date) from {{ this }}) -- this refer to this model - fct_reviews
{% endif %}

/*
- is_incremental() is evaluated at runtime, not during compilation

  + by default, this model will run in incremental mode,
  dbt will automatically add output of the compiled query as insertion into the target table
  
  + if we run the command $ dbt run --full-refresh, 
  dbt compile the sql code ignoring the {if is_incremental()} block,
  dbt will drop the existing table and re-create the table with the result of the compiled query
*/