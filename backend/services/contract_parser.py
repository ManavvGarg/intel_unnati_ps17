import re
import chardet

def parse(file_path: str) -> dict:
    text = read_file(file_path)
    parsed_data = extract_clauses(text)
    return parsed_data

def read_file(file_path: str) -> str:
    raw_data = []
    with open(file_path, 'r', errors="ignore") as file:
        for line in file:
            raw_data.append(line)
    
    try:
        raw_data = ''.join(raw_data)
        return raw_data
    except:
        raise ValueError(f"Failed to decode the file with the detected encoding")

def extract_clauses(text: str) -> dict:
    clauses = {
        "Security Deposit": extract_security_deposit(text),
        "Termination Rights": extract_termination_rights(text),
        "Rent": extract_rent(text),
        "Property Description": extract_property_description(text),
        "Tenant Name": extract_tenant_name(text),
        "Lease Period": extract_lease_period(text),
        "Dispute Resolution": extract_dispute_resolution(text),
        "Responsibilities of Landlord and Tenant": extract_responsibilities(text),
        "Timeline to Pay Rent": extract_timeline_to_pay_rent(text),
        "Lease Term": extract_lease_term(text),
        "Terms for Renewal and Brokerage": extract_terms_for_renewal(text),
        "Utilities": extract_utilities(text),
        "Duration of Tenancy": extract_duration_of_tenancy(text),
        "Lock-in Period": extract_lock_in_period(text),
        "Formalizing the Agreement": extract_formalizing_agreement(text),
        "Maintenance": extract_maintenance(text),
        "Maintenance Charges": extract_maintenance_charges(text),
        "List of Fittings and Fixtures": extract_fittings_and_fixtures(text),
        "Notice Period": extract_notice_period(text),
        "Indemnity Clause": extract_indemnity_clause(text),
        "Rules and Regulations": extract_rules_and_regulations(text),
        "Pets": extract_pets(text),
        "Collaboration Between Parties": extract_collaboration_between_parties(text),
    }
    return clauses

def extract_security_deposit(text: str) -> str:
    pattern = r"security\s*deposit\s*of\s*(₹?\s*\d+,\d+|\d+\s*rupees)"
    match = re.search(pattern, text, re.IGNORECASE)
    return match.group(1).strip() if match else "Not found"

def extract_termination_rights(text: str) -> str:
    pattern = r"termination\s*rights\s*:\s*(.*?)(?=\n\n|$)"
    match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
    return match.group(1).strip() if match else "Not found"

def extract_rent(text: str) -> str:
    pattern = r"rent\s*of\s*(₹?\s*\d+,\d+|\d+\s*rupees)"
    match = re.search(pattern, text, re.IGNORECASE)
    return match.group(1).strip() if match else "Not found"

def extract_property_description(text: str) -> str:
    pattern = r"property\s*description\s*:\s*(.*?)(?=\n\n|$)"
    match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
    return match.group(1).strip() if match else "Not found"

def extract_tenant_name(text: str) -> str:
    pattern = r"(?:between|among)\s*(.*?)(?:referred|called)"
    match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
    return match.group(1).strip() if match else "Not found"

def extract_lease_period(text: str) -> str:
    pattern = r"lease\s*period\s*of\s*(\d+\s*(?:months?|years?))"
    match = re.search(pattern, text, re.IGNORECASE)
    return match.group(1).strip() if match else "Not found"

def extract_dispute_resolution(text: str) -> str:
    pattern = r"dispute\s*resolution\s*:\s*(.*?)(?=\n\n|$)"
    match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
    return match.group(1).strip() if match else "Not found"

def extract_responsibilities(text: str) -> str:
    pattern = r"responsibilities\s*of\s*the\s*landlord\s*and\s*tenant\s*:\s*(.*?)(?=\n\n|$)"
    match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
    return match.group(1).strip() if match else "Not found"

def extract_timeline_to_pay_rent(text: str) -> str:
    pattern = r"timeline\s*to\s*pay\s*rent\s*:\s*(.*?)(?=\n\n|$)"
    match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
    return match.group(1).strip() if match else "Not found"

def extract_lease_term(text: str) -> str:
    pattern = r"lease\s*term\s*:\s*(.*?)(?=\n\n|$)"
    match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
    return match.group(1).strip() if match else "Not found"

def extract_terms_for_renewal(text: str) -> str:
    pattern = r"terms\s*for\s*renewal\s*and\s*brokerage\s*:\s*(.*?)(?=\n\n|$)"
    match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
    return match.group(1).strip() if match else "Not found"

def extract_utilities(text: str) -> str:
    pattern = r"utilities\s*:\s*(.*?)(?=\n\n|$)"
    match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
    return match.group(1).strip() if match else "Not found"

def extract_duration_of_tenancy(text: str) -> str:
    pattern = r"duration\s*of\s*tenancy\s*:\s*(.*?)(?=\n\n|$)"
    match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
    return match.group(1).strip() if match else "Not found"

def extract_lock_in_period(text: str) -> str:
    pattern = r"lock-in\s*period\s*:\s*(.*?)(?=\n\n|$)"
    match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
    return match.group(1).strip() if match else "Not found"

def extract_formalizing_agreement(text: str) -> str:
    pattern = r"formalizing\s*the\s*agreement\s*:\s*(.*?)(?=\n\n|$)"
    match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
    return match.group(1).strip() if match else "Not found"

def extract_maintenance(text: str) -> str:
    pattern = r"maintenance\s*:\s*(.*?)(?=\n\n|$)"
    match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
    return match.group(1).strip() if match else "Not found"

def extract_maintenance_charges(text: str) -> str:
    pattern = r"maintenance\s*charges\s*:\s*(.*?)(?=\n\n|$)"
    match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
    return match.group(1).strip() if match else "Not found"

def extract_fittings_and_fixtures(text: str) -> str:
    pattern = r"list\s*of\s*fittings\s*and\s*fixtures\s*:\s*(.*?)(?=\n\n|$)"
    match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
    return match.group(1).strip() if match else "Not found"

def extract_notice_period(text: str) -> str:
    pattern = r"notice\s*period\s*:\s*(.*?)(?=\n\n|$)"
    match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
    return match.group(1).strip() if match else "Not found"

def extract_indemnity_clause(text: str) -> str:
    pattern = r"indemnity\s*clause\s*:\s*(.*?)(?=\n\n|$)"
    match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
    return match.group(1).strip() if match else "Not found"

def extract_rules_and_regulations(text: str) -> str:
    pattern = r"rules\s*and\s*regulations\s*:\s*(.*?)(?=\n\n|$)"
    match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
    return match.group(1).strip() if match else "Not found"

def extract_pets(text: str) -> str:
    pattern = r"pets\s*:\s*(.*?)(?=\n\n|$)"
    match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
    return match.group(1).strip() if match else "Not found"

def extract_collaboration_between_parties(text: str) -> str:
    pattern = r"collaboration\s*between\s*parties\s*:\s*(.*?)(?=\n\n|$)"
    match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
    return match.group(1).strip() if match else "Not found"
