"""
Adaptive Wireless Power Transfer (WPT) Controller for EV Charging
Simulates dynamic impedance matching, coupling coefficient estimation,
and frequency tuning to maintain peak power transfer efficiency under varying air gaps.
"""

import time
import math

class WPTSystemController:
    def __init__(self, target_frequency_hz=85000.0, target_power_kw=11.0):
        self.resonant_freq = target_frequency_hz  # SAE J2954 standard operating frequency (85 kHz)
        self.target_power = target_power_kw * 1000.0
        self.coupling_coefficient = 0.35  # Initial estimated magnetic coupling (k)
        self.air_gap_mm = 150.0          # Nominal ground clearance

    def estimate_coupling(self, mutual_inductance: float, primary_inductance: float, secondary_inductance: float) -> float:
        """Estimates the magnetic coupling coefficient 'k' between transmitter and receiver pads."""
        self.coupling_coefficient = mutual_inductance / math.sqrt(primary_inductance * secondary_inductance)
        return self.coupling_coefficient

    def adaptive_frequency_tuning(self, measured_efficiency: float) -> float:
        """Adjusts operating frequency dynamically to compensate for detuning caused by misalignment."""
        optimal_freq = self.resonant_freq
        if measured_efficiency < 0.85:
            freq_offset = (0.85 - measured_efficiency) * 2000.0
            optimal_freq += freq_offset
        return optimal_freq

    def regulate_power(self, dc_input_voltage: float, actual_power: float) -> float:
        """Calculates PWM duty cycle adjustments for inverter control to match target charging power."""
        power_error = self.target_power - actual_power
        duty_adjustment = min(max(power_error * 0.00005, -0.1), 0.1)
        return duty_adjustment

if __name__ == "__main__":
    wpt = WPTSystemController()
    print(f"Initialized WPT Controller at standard frequency: {wpt.resonant_freq / 1000.0} kHz")
    
    k_est = wpt.estimate_coupling(mutual_inductance=15.2e-6, primary_inductance=45.0e-6, secondary_inductance=45.0e-6)
    freq = wpt.adaptive_frequency_tuning(measured_efficiency=0.82)
    duty_delta = wpt.regulate_power(dc_input_voltage=400.0, actual_power=9500.0)
    
    print(f"Estimated Coupling (k): {k_est:.3f}")
    print(f"Adjusted Operating Frequency: {freq / 1000.0:.2f} kHz")
    print(f"Inverter Duty Cycle Adjustment Delta: {duty_delta:+.4f}")
