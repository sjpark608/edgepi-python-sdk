import logging
from time import perf_counter_ns

from edgepi.adc.adc_constants import (
    ADCNum,
    ADCReg,
    ADCChannel as CH,
    ConvMode,
    ADC1DataRate,
    ADC2DataRate,
    FilterMode,
    CheckMode,
    ADCPower,
    IDACMUX,
    IDACMAG,
    REFMUX,
    DiffMode,
    RTDModes,
    ADC1PGA,
)
from edgepi.adc.edgepi_adc import EdgePiADC

_logger = logging.getLogger(__name__)

if __name__ == "__main__":
    adc_m = EdgePiADC()
    adc_m.set_config(adc_1_data_rate=ADC1DataRate.SPS_38400, conversion_mode=ConvMode.CONTINUOUS, adc_2_data_rate=ADC2DataRate.SPS_10, adc_1_pga=ADC1PGA.ENABLED)
    adc_m.start_conversions(ADCNum.ADC_1)
    t1 = perf_counter_ns()
    out = adc_m.read_voltage(ADCNum.ADC_1)
    _logger.info(f"voltage: {out}, period:{perf_counter_ns() - t1}")
