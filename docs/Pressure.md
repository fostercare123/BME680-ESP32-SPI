### 1. Pressure in hPa (hectopascals)

**What the unit means**  
- 1 hPa = 100 Pa = ≈ 0.001 atm ≈ 0.0295 inHg.  
- Meteorologists love hPa because it lines up nicely with sea‑level pressure (1013 hPa is “standard” atmospheric pressure).

**How to read it**  
- Typical sea‑level values: **1010 – 1030 hPa** on a clear day, lower when a low‑pressure system passes (maybe 990 hPa or less).  
- Higher elevations give lower numbers: at 1 km altitude you’ll see ~ 900 hPa, at 3 km ~ 700 hPa.

**What it tells you**  
- A **rise** in pressure generally signals improving weather (high‑pressure ridge).  
- A **drop** usually precedes clouds, rain, or storms (low‑pressure trough).  
- Because the BME680 measures absolute pressure, you can also estimate altitude if you know the local sea‑level reference (the classic barometric formula).

**Practical tip**  
If you just want “how high am I?” you can convert the reading to meters:

```python
import math
def pressure_to_altitude(p_hpa, sea_level_hpa=1013.25):
    # Simple barometric equation (valid up to ~10 km)
    return 44330 * (1 - (p_hpa / sea_level_hpa) ** (1/5.255))
```

Plug your `sensor.pressure` into that function and you’ll get an approximate altitude in metres.

- **hPa** tells you how much atmosphere is pressing down on you—use it for weather trends or altitude estimates.
