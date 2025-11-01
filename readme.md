BME680 SPI – What the Numbers Mean
==========================================

This sketch reads temperature, humidity, pressure, and VOC (Volatile Organic Compounds) data from a
BME680 connected via SPI to an ESP32. The raw values are useful, but they’re
even more helpful when you understand what they represent.

--------------------------------------------------------------------
1️⃣ Pressure (hPa)
--------------------------------------------------------------------
• Unit: hectopascal (hPa) – 1 hPa = 100 Pa ≈ 0.001 atm.  
• Typical sea‑level pressure: 1010 – 1030 hPa on a clear day.  
• Lower values indicate low‑pressure systems (clouds, rain); higher
  values signal high‑pressure ridges (fair weather).  
• At altitude the reading drops (≈ 900 hPa at 1 km, ≈ 700 hPa at 3 km).

Quick altitude estimate (Python):

```python
def pressure_to_altitude(p_hpa, sea_level_hpa=1013.25):
    # Simple barometric formula (valid up to ~10 km)
    return 44330 * (1 - (p_hpa / sea_level_hpa) ** (1/5.255))
```

```python
# Example:
# altitude_m = pressure_to_altitude(sensor.pressure)
```


--------------------------------------------------------------------
2️⃣ VOC (Volatile Organic Compounds) – Gas resistance (kΩ)
--------------------------------------------------------------------
The BME680 does NOT output a direct “ppm VOC” value. Instead it reports the
electrical resistance of its heating element when VOC molecules are present.
The resistance (sensor.gas) is shown in kilo‑ohms after you divide by 1000.

Interpretation (rough guide – actual numbers depend on temperature,
humidity, and sensor calibration):

| Air quality                                                 | Approx. gas resistance |
| ----------------------------------------------------------- | ---------------------- |
| Very clean indoor air                                       | **> 200 kΩ**           |
| Normal indoor environment                                   | **50 – 200 kΩ**        |
| Polluted indoor air (cooking smoke, strong cleaning agents) | **< 50 kΩ**            |

Simple “air‑quality” flag (Python):

```python
def voc_quality(gas_resistance_kohm):
    if gas_resistance_kohm > 200:
        return "Good (clean air)"
    elif gas_resistance_kohm > 50:
        return "Moderate (typical indoor air)"
    else:
        return "Poor (high VOCs)"
```

--------------------------------------------------------------------
Example output

| Temp: 23.45 °C                             |
| ------------------------------------------ |
| Hum : 48.20 %                              |
| Pres: 1012.34 hPa                          |
| VOC : 132.00 kΩ                            |
| Air quality: Moderate (typical indoor air) |

--------------------------------------------------------------------
Usage notes
--------------------------------------------------------------------
* The resistance values are relative, not absolute ppm counts.  
* For precise VOC quantification you’d need a calibrated curve against
  known gas concentrations.  
* Adjust the threshold numbers in voc_quality() to suit the environment
  you’re monitoring (e.g., kitchen vs. bedroom).

For a full explanation of the pressure reading and how to convert it to altitude, see
[`docs/pressure.md`](docs/pressure.md).

For a deeper look at the VOC resistance values and how to calibrate them, check
[`docs/volatile organic compounds.md`](docs/voc.md).

Feel free to adapt the code snippets and explanations to fit your own
project documentation style. Happy hacking!
