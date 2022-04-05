import re


class CDateConfig(object):
    MIN_ADR: int = -1_718_100
    MAX_ADR: int = 170_091_999

    DAYS_per_GRAND_CYCLE: int = 1_718_101
    DAYS_per_CYCLE: float = DAYS_per_GRAND_CYCLE / 700

    GCN_DATE_STRING_RE = re.compile('^([0-9]{2})-([0-7][0-9]{2})-([1-7])-([0-5][0-9])-([1-8])$')
    CSN_DATE_STRING_RE = re.compile('^([1-9]?[0-9]{3})-([1-7])-([0-5][0-9])-([1-8]) *(BZ|BH|CE)?$', re.IGNORECASE)

    TEMP_BASELINE_ADR: int = 1_907_093  # New Cycle Day 778
    APOCALYPSE_EPOCH_ADR: int = TEMP_BASELINE_ADR
    # TODO: Determine the correct epoch day for Apocalypse Reckoning:
    #  the day Jennifer and Colette arrived on Calmarendi.
