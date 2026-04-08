def generate_pitch(company_name, signals, score):
    """
    Generates personalized outreach email based on company signals
    """

    # Convert signals list to readable text
    signal_text = ", ".join(signals)

    # Determine urgency based on score
    if score >= 80:
        urgency = "strong indicators of operational inefficiencies"
    elif score >= 60:
        urgency = "some signs of process inefficiencies"
    else:
        urgency = "potential areas for optimization"

    # Email template
    pitch = f"""
Hi {company_name} Team,

We noticed that your company is currently dealing with {signal_text}, which indicates {urgency}.

Many companies in your space face similar challenges with manual workflows, reporting, and operational coordination. At GarunaCDX, we specialize in automating such processes using AI-driven solutions.

For example, we’ve helped similar companies reduce manual effort by 40–60% by automating data handling, reporting, and internal workflows.

Would you be open to a quick 15-minute discussion to explore how automation can improve your current processes?

Looking forward to your response.

Best regards,  
Shreshthi Patil
"""
    return pitch
