def classify_company(signals):
    """
    Classifies company based on extracted signals.

    Input:
        signals (dict):
        {
            "manual_roles": int,
            "manual_keywords": int,
            "scaling": bool
        }

    Output:
        str: HIGH_MANUAL / MEDIUM_MANUAL / LOW_MANUAL
    """

    manual_roles = signals.get("manual_roles", 0)
    manual_keywords = signals.get("manual_keywords", 0)
    scaling = signals.get("scaling", False)

    if manual_roles >= 5:
        category = "HIGH_MANUAL"
    elif manual_roles >= 3 or manual_keywords >= 2:
        category = "MEDIUM_MANUAL"
    else:
        category = "LOW_MANUAL"

    if scaling and category == "MEDIUM_MANUAL":
        category = "HIGH_MANUAL"

    return category


def cluster_roles(job_titles):
    """
    Groups similar job roles into one cluster
    """
    keywords = ["data entry", "back office", "operations", "admin"]

    count = 0
    for job in job_titles:
        job = job.lower()
        if any(k in job for k in keywords):
            count += 1

    return count
