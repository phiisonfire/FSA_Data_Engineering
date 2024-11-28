must include dbt_profiles.yml in this directory
```yaml
dbtlearn:
  outputs:
    dev:
      account: <SNOWFLAKE_ACCOUNT>
      database: <SNOWFLAKE_DATABASE>
      password: <SNOWFLAKE_PASSWORD>
      role: transform
      schema: DEV
      threads: 1
      type: snowflake
      user: <SNOWFLAKE_USERNAME>
      warehouse: COMPUTE_WH
  target: dev
```