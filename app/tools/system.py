def build(sensor):

    return f"""

Status PC

GPU : {sensor["gpu_temp"]}°C

CPU : {sensor["cpu_temp"]}°C

RAM : {sensor["ram_used"]}/{sensor["ram_total"]} GB

Berikan kesimpulan singkat.

Jawab santai.
"""