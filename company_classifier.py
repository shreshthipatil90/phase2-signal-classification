"""
File: company_classifier.py

Description:
This module contains the classification logic for identifying
automation opportunities based on company hiring signals.

Includes:
- Role clustering (Day 10)
- Role counting logic (Day 9)
- Final classification function (Day 14)
"""

def cluster_roles(job_titles):
    """
    Day 10: Role Clustering

    Groups similar job titles into one cluster.
    Example:
    'data entry', 'back office', 'ops assistant' → same category
    """

    clusters = {
        "data_ops": ["data entry", "back office", "operations", "ops assistant", "admin"]
    }

    cluster_count = {"data_ops": 0}

    for job in job_titles:
        job = job.lower()

        for cluster, keywords in clusters.items():
            if any(k in job for k in keywords):
                cluster_count[cluster] += 1

    return cluster_count


def classify_company(signals):
    """
    Day 8 + Day 9 + Day 14: Final Classification Function

    Uses output from extract_signals()

    signals example:
    {
        "manual_roles": int,
        "manual_keywords": int,
        "scaling": bool
    }

    Returns:
        HIGH_MANUAL / MEDIUM_MANUAL / LOW_MANUAL
    """

    # Extract values safely
    manual_roles = signals.get("manual_roles", 0)
    manual_keywords = signals.get("manual_keywords", 0)
    scaling = signals.get("scaling", False)

    # Day 9: High manual workload priority rule
    if manual_roles >= 5:
        category = "HIGH_MANUAL"

    # Medium workload
    elif manual_roles >= 3 or manual_keywords >= 2:
        category = "MEDIUM_MANUAL"

    # Low workload
    else:
        category = "LOW_MANUAL"

    # Boost rule (scaling companies)
    if scaling and category == "MEDIUM_MANUAL":
        category = "HIGH_MANUAL"

    return category
