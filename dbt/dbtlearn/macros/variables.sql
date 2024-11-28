{% macro learn_variables() %}
  -- Jinja variables
  {% set your_name_jinja = "Phi Nguyen" %}
  {{ log("Hello " ~ your_name_jinja, info=True) }}

  {{ log("Hello dbt user " ~ var("dbt_user", "NO dbt_user SET!") ~ "!", info=True) }}


{% endmacro %}