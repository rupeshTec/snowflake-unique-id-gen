# test.py

from snowflake import SnowflakeGenerator

gen = SnowflakeGenerator(machine_id=1)

for _ in range(10):
    print(gen.generate_id())
