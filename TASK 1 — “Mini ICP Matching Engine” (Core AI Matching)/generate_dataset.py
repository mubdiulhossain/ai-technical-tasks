import random, pandas as pd

random.seed(1)

#added these templates so that we can randomly assign the discription when we create the companies..
templates = [
    ("healthcare", [
        "Cloud-native analytics for hospitals.",
        "Provides MLOps and clinical analytics.",
        "Focus on HIPAA-compliant data pipelines.",
        "Used by 200 hospitals for patient data management.",
        "Integrates with Epic, Cerner, and cloud EMR systems."
    ]),
    ("fintech", [
        "Fraud detection and risk scoring for payments.",
        "Real-time transaction monitoring using ML.",
        "Integrates with banking APIs.",
        "Processes $50M/month in transactions.",
        "Works with Plaid, Stripe, and PayPal."
    ]),
    ("retail", [
        "Personalization and recommendations.",
        "Real-time inventory forecasting.",
        "Customer analytics across channels.",
        "Used by 500+ e-commerce stores.",
        "Integrates with Shopify, Magento, and AWS."
    ]),
    ("iot", [
        "Industrial IoT analytics for predictive maintenance.",
        "Sensor anomaly detection and fleet monitoring.",
        "Edge-device data aggregation.",
        "Used by 100 factories worldwide.",
        "Works with Azure IoT, AWS IoT Core."
    ]),
    ("edtech", [
        "Adaptive learning platform for K-12 and higher ed.",
        "Student performance modeling using AI.",
        "Automated feedback generation.",
        "Used by 50 universities.",
        "Integrates with Canvas and Moodle LMS."
    ]),
    ("legal", [
        "AI-powered document review and contract analysis.",
        "Automates e-discovery and compliance checks.",
        "Integrates with document management systems.",
        "Used by 100+ law firms.",
        "Works with Salesforce and SharePoint."
    ]),
    ("energy", [
        "Energy grid intelligence for load forecasting.",
        "Outage prediction and distributed resource optimization.",
        "Integrates sensor data for predictive maintenance.",
        "Used by national utilities.",
        "Works with SCADA and AWS IoT."
    ]),
    ("transportation", [
        "Smart city traffic optimization and congestion prediction.",
        "Public transit analytics using real-time data.",
        "AI-powered route planning for fleets.",
        "Used by city municipalities.",
        "Integrates with Google Maps API and AWS IoT."
    ]),
    ("pharma", [
        "Drug discovery and molecular analysis using AI.",
        "Automated lab workflows and predictive modeling.",
        "Clinical trial analytics and regulatory compliance.",
        "Used by 50 pharmaceutical companies.",
        "Works with LabWare, AWS, and Azure."
    ]),
    ("manufacturing", [
        "Predictive maintenance and quality control.",
        "AI-powered production optimization.",
        "Edge-device monitoring and factory automation.",
        "Used by 100 factories worldwide.",
        "Integrates with Siemens, Rockwell, and cloud platforms."
    ]),
    ("cybersecurity", [
        "AI-driven threat detection and incident response.",
        "Behavioral authentication and anomaly monitoring.",
        "Integrates with SIEM and cloud security tools.",
        "Used by 150+ enterprises for cybersecurity.",
        "Works with Splunk, AWS, and Azure Security."
    ]),
    ("hrm", [
        "AI-powered talent acquisition and resume screening platform.",
        "Employee performance tracking and predictive attrition modeling.",
        "Workforce planning and automated HR analytics dashboards.",
        "Used by 100+ companies for recruitment and retention.",
        "Integrates with Workday, SAP SuccessFactors, and BambooHR.",
        "Predictive attrition analytics for enterprises",
        "Employee engagement dashboards and AI-driven feedback",
        "Resume parsing and automated interview scheduling"
    ])
]

#will use these non-existing brand names to generate 200 companies.
brands = ["Medlytics", "FinSight", "Retailio", "IoTAnalytics", "Boogle", "Megasoft", "BRACK", "Uthao", "Grab", "Maxis", "TelekomMalaysia", "Petronas", "LearnSmart", "LegalEye", "EnergyGrid", "HealthAI", "PayCheckAI", "ShopSense"]

all_entities = [
    'Epic','Cerner','cloud EMR systems','Plaid','Stripe','PayPal','Shopify','Magento','AWS',
    'Azure IoT','AWS IoT Core','Canvas','Moodle LMS','Salesforce','SharePoint','SCADA','Google Maps API',
    'LabWare','Siemens','Rockwell','Workday','SAP SuccessFactors','BambooHR','Firebase'
]


def generate_dataset():
    rows = []
    N = 200
    for i in range(N):
        name = random.choice(brands) + f"_{i:03d}"
        ind, fragments = templates[i % len(templates)]

        sent_count = random.randint(3,5)
        desc = " ".join(random.sample(fragments, k=min(sent_count, len(fragments))))

        #typos
        if random.random() < 0.02:
            desc = desc.replace("a", "q", 1)
        if random.random() < 0.01:
            desc = desc.replace("e", "r", 1)
        if random.random() < 0.01:
            desc = desc.replace("o", "i", 1)

        if random.random() < 0.7:
            prefix = random.choice(["Works with", "Integrates with"])
            n_entities = random.randint(1, 3)
            entities_str = ", ".join(random.sample(all_entities, n_entities))
            desc += f" {prefix} {entities_str}."


        size = random.choice(["startup","SMB","enterprise"])
        region = random.choice(["NA","EMEA","APAC","LATAM","CIS","Global"])
        rows.append({"company_name": name, "company_description": desc, "industry": ind, "size": size, "region": region})

    df = pd.DataFrame(rows)
    df.to_csv("companies.csv", index=False)
    return df
