def calculate_mchc(hemoglobin, hematocrit):
    """
    Calculate Mean Corpuscular Hemoglobin Concentration (MCHC).

    Arguments:
    hemoglobin -- The amount of hemoglobin in grams (float).
    hematocrit -- The fraction of red blood cells in the total blood volume (float).

    Returns:
    mchc -- The calculated Mean Corpuscular Hemoglobin Concentration (float).
    """

    mchc = (hemoglobin / hematocrit) * 100

    return mchc

# Example usage
hemoglobin_level = 15.2
hematocrit_value = 42.5

mchc_result = calculate_mchc(hemoglobin_level, hematocrit_value)
print("Mean Corpuscular Hemoglobin Concentration (MCHC):", mchc_result)
