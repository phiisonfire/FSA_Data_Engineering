{% macro learn_logging() %}
  {{ log("log message 2", info=True) }}
{% endmacro %}