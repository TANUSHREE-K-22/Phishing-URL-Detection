import re
import urllib.parse

def is_ip(url):
    """Check if URL contains an IP address"""
    return 1 if re.search(r"(\d{1,3}\.){3}\d{1,3}", url) else 0


def count_dots(url):
    return url.count(".")


def has_suspicious_words(url):
    suspicious_keywords = [
        "login", "verify", "update", "free", "password", "bank",
        "secure", "security", "account", "support", "confirm",
        "check", "mail", "gift", "offer"
    ]
    return 1 if any(word in url.lower() for word in suspicious_keywords) else 0


def brand_mismatch(url, domain):
    """Detect fake brand usage"""
    brand_names = ["yahoo", "google", "gmail", "facebook",
                   "instagram", "amazon", "bank", "paypal"]

    for brand in brand_names:
        if brand in url.lower():
            # Must match real domain
            correct_domain = f"{brand}.com"
            if correct_domain not in domain:
                return 1
    return 0


def suspicious_tld(domain):
    """Check for dangerous top-level domains used in phishing"""
    bad_tlds = [".info", ".xyz", ".top", ".online", ".support", ".click", ".shop"]
    return 1 if any(domain.endswith(tld) for tld in bad_tlds) else 0


def detect_phishing(url):
    score = 0
    parsed = urllib.parse.urlparse(url)
    domain = parsed.netloc

    # FIXED RULE 1: No HTTPS
    if not url.lower().startswith("https://"):
        score += 1

    # Rule 2: Too long URL
    if len(url) > 75:
        score += 1

    # Rule 3: Contains IP address
    score += is_ip(url)

    # ❌ BUG FIX: Your code added a score for "https" (wrong!)
    # Removing this rule completely.

    # Rule 4: Contains @ symbol    
    if "@" in url:
        score += 1

    # Rule 5: Many dots
    if count_dots(url) > 4:
        score += 1

    # Rule 6: Hyphens in domain
    if "-" in domain:
        score += 1

    # Rule 7: Suspicious keywords
    score += has_suspicious_words(url)

    # Rule 8: Fake brand usage
    score += brand_mismatch(url, domain)

    # Rule 9: Suspicious domain ending
    score += suspicious_tld(domain)

    # FINAL DECISION
    if score >= 3:
        return "⚠️ Phishing URL"
    else:
        return "✅ Safe URL"


# -------- MAIN PROGRAM ----------
print("\n=== PHISHING URL DETECTOR (ACCURATE VERSION) ===\n")

while True:
    url = input("Enter URL (or type exit): ")

    if url.lower() == "exit":
        print("\nGoodbye! Stay safe online. 🛡️")
        break

    # Avoid empty input
    if url.strip() == "":
        print("❌ Please enter a valid URL.\n")
        continue

    result = detect_phishing(url)
    print("Result:", result, "\n")