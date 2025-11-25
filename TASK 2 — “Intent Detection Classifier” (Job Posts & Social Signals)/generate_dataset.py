import random
import pandas as pd

random.seed(42)

#Templates
# High Intent Templates (20)
high_intent_templates = [
    [
        "We are evaluating {tool_type} solutions for {use_case}.",
        "Vendors please reach out with your proposals.",
        "Our budget has been finalized.",
        "We want a solution that integrates easily with existing HR systems.",
        "Looking for references from similar companies."
    ],
    [
        "Looking for recommendations for {tool_type} to improve {use_case}.",
        "Please share case studies and pricing.",
        "We are planning implementation next quarter.",
        "Interested vendors can DM.",
        "Prior experience with enterprises preferred."
    ],
    [
        "Seeking {tool_type} for {use_case}.",
        "Contact us if your solution fits our requirements.",
        "We are in a pilot phase and need fast deployment.",
        "Integration with payroll and attendance systems is a must.",
        "References and demos appreciated."
    ],
    [
        "Our company is searching for {tool_type} focused on {use_case}.",
        "We have shortlisted vendors for evaluation.",
        "Implementation expected in next fiscal year.",
        "Integration with SAP and Workday preferred.",
        "Budget approval has been completed."
    ],
    [
        "RFP open: Need {tool_type} for {use_case}.",
        "Interested vendors contact us.",
        "We want analytics and reporting capabilities.",
        "Cloud-based or hybrid solutions considered.",
        "Deadline for submission is next week."
    ],
    [
        "Actively exploring {tool_type} for {use_case}.",
        "Our HR team has identified key requirements.",
        "Please provide implementation roadmap.",
        "Security and compliance are critical.",
        "Vendor references must include similar-sized enterprises."
    ],
    [
        "Need a platform to handle {use_case}.",
        "Looking to implement it soon.",
        "Solution must support multi-location offices.",
        "API access and integration is important.",
        "Vendor demos will be scheduled next month."
    ],
    [
        "Evaluating {tool_type} for {use_case}.",
        "Must handle large employee datasets efficiently.",
        "Cloud or SaaS preferred over on-premise.",
        "Interested vendors can schedule demo calls.",
        "Please include pricing tiers."
    ],
    [
        "Searching for {tool_type} for {use_case}.",
        "Need solution with AI-based insights.",
        "Integration with current HRIS required.",
        "Timeline: 3 months for rollout.",
        "Demo accounts for testing should be provided."
    ],
    [
        "Looking for {tool_type} to improve {use_case}.",
        "Implementation team is ready.",
        "System should support mobile and web access.",
        "Existing workflow must be maintained.",
        "Reference implementations preferred."
    ],
    [
        "RFP: {tool_type} for {use_case}.",
        "Must support multiple currencies and timezones.",
        "Vendor selection within 30 days.",
        "Demo and trial periods required.",
        "Focus on automation and efficiency."
    ],
    [
        "Seeking {tool_type} with best practices for {use_case}.",
        "Integration with ERP is a must.",
        "Need automated reporting features.",
        "Pilot program before full deployment.",
        "Vendor support and SLA expected."
    ],
    [
        "Exploring {tool_type} to optimize {use_case}.",
        "Need a secure cloud solution.",
        "Analytics dashboard is required.",
        "Implementation roadmap should include training.",
        "Vendor references preferred from similar companies."
    ],
    [
        "Requesting proposals for {tool_type} for {use_case}.",
        "Must include workflow automation.",
        "Solution should be scalable to 10,000+ employees.",
        "Training and onboarding support required.",
        "Security audits must be compliant."
    ],
    [
        "Evaluating vendors for {tool_type}.",
        "Use case: {use_case}.",
        "Must provide seamless integration with existing tools.",
        "Timeline: 2–3 months.",
        "Pricing and licensing details mandatory."
    ],
    [
        "Need {tool_type} for efficient {use_case}.",
        "Our HR team requires AI insights.",
        "Cloud deployment preferred.",
        "Demo sessions will be scheduled.",
        "References from multinational clients preferred."
    ],
    [
        "Searching for {tool_type} to enhance {use_case}.",
        "Integration with payroll and HRIS is required.",
        "Security and compliance checks mandatory.",
        "Vendor support should include training.",
        "Pilot testing before full rollout."
    ],
    [
        "Looking for {tool_type} for {use_case} processes.",
        "Must provide automation and analytics.",
        "Easy integration with existing platforms.",
        "Implementation timeline: 3 months.",
        "Reference clients preferred."
    ],
    [
        "Requesting information for {tool_type} in {use_case}.",
        "Must include workflow optimization.",
        "Vendor references required.",
        "Demo accounts for testing preferred.",
        "Training and support mandatory."
    ],
    [
        "Exploring {tool_type} for {use_case}.",
        "Implementation expected in next quarter.",
        "Integration with existing HRIS required.",
        "Automation and reporting features needed.",
        "Vendor demos appreciated."
    ]
]

# Medium Intent Templates (20)
medium_intent_templates = [
    [
        "Hiring a new {hr_role} for our {location} office.",
        "Candidate must have 5+ years experience.",
        "Competitive salary and benefits offered.",
        "Interview process will be 2 stages.",
        "Apply online or share resume with HR."
    ],
    [
        "We are expanding the HR team. Open roles: {hr_role}.",
        "Work from office or hybrid options available.",
        "Looking for skilled professionals.",
        "Candidates with certifications preferred.",
        "Submit your applications via our portal."
    ],
    [
        "Looking for experienced {hr_role}. Apply now.",
        "Must have knowledge in HR analytics.",
        "Team-oriented candidates encouraged.",
        "Interview will include technical and HR case study.",
        "Flexible working hours offered."
    ],
    [
        "Our company is searching for a skilled {hr_role}.",
        "Remote work possible for right candidates.",
        "Competitive compensation package.",
        "Join a supportive HR team.",
        "Applications accepted till end of month."
    ],
    [
        "Vacancy open: {hr_role}. Competitive salary.",
        "Candidate must manage employee engagement programs.",
        "Experience with HR software preferred.",
        "Interview rounds include HR and behavioral assessment.",
        "Reference checks mandatory."
    ],
    [
        "We are onboarding multiple HR positions including {hr_role}.",
        "Work closely with HR operations team.",
        "Salary negotiable based on experience.",
        "Online application portal is available.",
        "Team activities and development programs included."
    ],
    [
        "Recruiting an experienced {hr_role} to join our team.",
        "Must handle performance management tools.",
        "Competitive benefits and training offered.",
        "Interview to include leadership assessment.",
        "Relocation assistance provided if needed."
    ],
    [
        "Looking to hire {hr_role} in our {location} branch.",
        "Experience in recruitment automation required.",
        "Team collaboration important.",
        "Flexible schedule options available.",
        "Apply via email or HR portal."
    ],
    [
        "Opening for {hr_role} position.",
        "Must be able to manage HRIS systems.",
        "Salary package is competitive.",
        "Interview includes scenario-based questions.",
        "Training support provided."
    ],
    [
        "Hiring {hr_role} to strengthen HR department.",
        "Experience in employee onboarding preferred.",
        "Team environment with growth potential.",
        "Submit resumes online.",
        "Interviews scheduled next month."
    ],
    [
        "Recruiting {hr_role} for immediate start.",
        "Must be familiar with compliance regulations.",
        "Competitive compensation.",
        "Work from office or hybrid.",
        "Resume submission online."
    ],
    [
        "We are looking for {hr_role}.",
        "Candidates should have HR experience.",
        "Salary and benefits discussed in interview.",
        "Team collaboration skills required.",
        "Apply through our careers page."
    ],
    [
        "Join our team as {hr_role}.",
        "Experience in talent acquisition required.",
        "Salary negotiable based on experience.",
        "Training and mentorship included.",
        "Applications accepted immediately."
    ],
    [
        "We are hiring {hr_role}.",
        "Must manage employee engagement programs.",
        "Competitive salary offered.",
        "Interview includes assessment tasks.",
        "Submit resume online."
    ],
    [
        "Vacancy: {hr_role} in {location}.",
        "Experience with HR analytics tools preferred.",
        "Flexible schedule options.",
        "Interview via video call possible.",
        "Apply on our website."
    ],
    [
        "Hiring {hr_role} to join HR operations.",
        "Must have strong organizational skills.",
        "Competitive benefits.",
        "Interview process is two-step.",
        "Applications via email."
    ],
    [
        "Looking for qualified {hr_role}.",
        "Experience in payroll and HR compliance preferred.",
        "Salary discussed on offer.",
        "Team collaboration emphasized.",
        "Submit resumes online."
    ],
    [
        "We are recruiting {hr_role}.",
        "Candidate must have HR management experience.",
        "Remote work optional.",
        "Interview includes HR case study.",
        "Apply via portal."
    ],
    [
        "Opening for {hr_role}.",
        "Experience in HRIS and recruitment required.",
        "Competitive benefits and salary.",
        "Submit application before deadline.",
        "Interview to include behavioral assessment."
    ],
    [
        "We need {hr_role} for {location}.",
        "Candidate should handle employee engagement.",
        "Work from office preferred.",
        "Interview includes scenario-based questions.",
        "Apply online immediately."
    ]
]

# Low Intent Templates (20)
low_intent_templates = [
    [
        "Good {hr_topic} practices can significantly improve retention.",
        "Companies should share knowledge and best practices.",
        "Training programs improve employee skills.",
        "Regular feedback and reviews are essential.",
        "Strong leadership helps HR outcomes."
    ],
    [
        "Companies should invest more in {hr_topic} to build better culture.",
        "Communication and transparency matter.",
        "Recognition programs boost morale.",
        "Learning initiatives improve productivity.",
        "Team collaboration enhances results."
    ],
    [
        "New HR policies require more focus on {hr_topic}.",
        "Employee engagement improves satisfaction.",
        "Regular check-ins are recommended.",
        "Talent development programs are beneficial.",
        "Clear career paths enhance retention."
    ],
    [
        "Strong emphasis on {hr_topic} leads to better employee outcomes.",
        "Training and mentorship are essential.",
        "HR technology can support analytics.",
        "Feedback culture improves performance.",
        "Recognition improves motivation."
    ],
    [
        "This year’s HR trend: more investment in {hr_topic}.",
        "Companies adopting analytics see better results.",
        "Continuous learning is key.",
        "Employee satisfaction surveys are helpful.",
        "Career development initiatives enhance retention."
    ],
    [
        "A healthy workplace depends heavily on {hr_topic}.",
        "Open communication channels improve culture.",
        "HR policies must be consistent.",
        "Employee wellness programs support engagement.",
        "Leadership commitment is crucial."
    ],
    [
        "Best practices for improving {hr_topic} across teams.",
        "Regular evaluations improve efficiency.",
        "Employee feedback is essential.",
        "Professional development matters.",
        "Engagement programs boost performance."
    ],
    [
        "Investing in {hr_topic} leads to better employee experience.",
        "Structured onboarding helps retention.",
        "Mentorship improves skills.",
        "Recognition programs motivate teams.",
        "Training and analytics support decision making."
    ],
    [
        "Enhancing {hr_topic} creates more productive teams.",
        "Team collaboration encourages innovation.",
        "Clear policies prevent confusion.",
        "Feedback loops are essential.",
        "Employee satisfaction surveys help improvement."
    ],
    [
        "Focusing on {hr_topic} improves workplace culture.",
        "Regular workshops increase engagement.",
        "Employee recognition matters.",
        "Leadership involvement is important.",
        "Surveys guide better decisions."
    ],
    [
        "Continuous improvement in {hr_topic} leads to success.",
        "HR tech can assist in tracking.",
        "Team morale improves with recognition.",
        "Training programs enhance skillsets.",
        "Employee retention increases."
    ],
    [
        "Implementing {hr_topic} strategies boosts performance.",
        "Feedback and coaching are essential.",
        "Engagement programs help retention.",
        "Employee development matters.",
        "Workplace culture is enhanced."
    ],
    [
        "Prioritizing {hr_topic} improves HR outcomes.",
        "Mentorship programs increase productivity.",
        "Recognition improves morale.",
        "Analytics helps track performance.",
        "Continuous learning is encouraged."
    ],
    [
        "Strong {hr_topic} practices foster employee satisfaction.",
        "Clear goals support engagement.",
        "Training programs are beneficial.",
        "Regular check-ins improve performance.",
        "HR analytics helps optimize processes."
    ],
    [
        "Investing in {hr_topic} yields better outcomes.",
        "Team collaboration enhances engagement.",
        "Feedback is essential.",
        "Leadership involvement improves culture.",
        "Workplace initiatives support learning."
    ],
    [
        "Focus on {hr_topic} improves employee satisfaction.",
        "Recognition programs boost morale.",
        "Training helps skill development.",
        "Mentorship supports growth.",
        "Analytics track improvements."
    ],
    [
        "Enhancing {hr_topic} strengthens workforce.",
        "Continuous learning is important.",
        "Feedback loops increase engagement.",
        "Policies should be transparent.",
        "Employee recognition motivates teams."
    ],
    [
        "Effective {hr_topic} improves productivity.",
        "Mentorship and training programs help.",
        "Regular evaluations track performance.",
        "Employee satisfaction surveys guide decisions.",
        "Leadership engagement is essential."
    ],
    [
        "Developing {hr_topic} processes supports growth.",
        "Recognition and feedback enhance engagement.",
        "Training programs are beneficial.",
        "Analytics help in decision making.",
        "Team collaboration is key."
    ],
    [
        "Focusing on {hr_topic} creates better work environment.",
        "Mentorship improves skills.",
        "Recognition programs boost motivation.",
        "Regular training is essential.",
        "Employee feedback guides improvements."
    ]
]

# No Intent Templates (20)
no_intent_templates = [
    [
        "The weather today is absolutely amazing.",
        "I went for a long walk this morning.",
        "Coffee tastes better with a good book.",
        "Planning a weekend trip to the mountains.",
        "Can't wait to try the new restaurant in town."
    ],
    [
        "Can't believe the match last night, what a comeback!",
        "The team played exceptionally well.",
        "Fans are excited for the next game.",
        "Tickets sold out quickly.",
        "Looking forward to the championship next month."
    ],
    [
        "Trying out a new recipe this evening.",
        "Ingredients were fresh and local.",
        "The dish turned out amazing.",
        "Friends and family loved it.",
        "Cooking is so therapeutic."
    ],
    [
        "Anyone recommend a good sci-fi movie?",
        "I just finished watching a classic one.",
        "Storyline was engaging and futuristic.",
        "Visual effects were stunning.",
        "Looking for more recommendations."
    ],
    [
        "Traffic was horrible today.",
        "Left office late due to jam.",
        "Public transport was crowded.",
        "Next time I will plan an alternate route.",
        "Patience is key in city traffic."
    ],
    [
        "New phone launch looks fantastic.",
        "Excited about the camera improvements.",
        "Battery life seems promising.",
        "Waiting to try the device in person.",
        "Pre-orders have already started."
    ],
    [
        "Working on my photography skills this week.",
        "Practiced street and portrait photography.",
        "Learned new editing techniques.",
        "Sharing my shots on social media.",
        "Feedback from community is helpful."
    ],
    [
        "Weekend plan: mountains or beach?",
        "Considering outdoor activities.",
        "Friends are joining for the trip.",
        "Packing essentials for the adventure.",
        "Looking forward to refreshing weekend."
    ],
    [
        "The new open-source project was released.",
        "Developers are excited to try it.",
        "Documentation is detailed.",
        "Community contributions welcomed.",
        "Hope it improves productivity."
    ],
    [
        "Local soccer team won their match yesterday.",
        "Fans celebrated in the streets.",
        "Team captain praised the efforts.",
        "Next match will be crucial for league.",
        "Celebration continued till late evening."
    ],
    [
        "Tried a new coffee shop downtown.",
        "Ambience was cozy and welcoming.",
        "The latte was excellent.",
        "Friendly staff and quick service.",
        "Planning to visit again soon."
    ],
    [
        "Read an interesting book on AI this week.",
        "Concepts were mind-blowing.",
        "Taking notes for future projects.",
        "Author gave practical examples.",
        "Highly recommended for enthusiasts."
    ],
    [
        "Attended a local music concert.",
        "Band performed classics and new songs.",
        "Crowd was energetic and lively.",
        "Sound quality was superb.",
        "Looking forward to next show."
    ],
    [
        "Gardening has become my new hobby.",
        "Planted vegetables and flowers.",
        "Daily watering and care needed.",
        "Enjoy seeing growth each day.",
        "Feeling productive and relaxed."
    ],
    [
        "Started a coding challenge this week.",
        "Solving problems on algorithmic sites.",
        "Learning new techniques.",
        "Tracking progress daily.",
        "Excited to complete all levels."
    ],
    [
        "Exploring city’s historical landmarks.",
        "Photographed architecture.",
        "Learned about local history.",
        "Visited museums and parks.",
        "Documented experiences in a blog."
    ],
    [
        "Planning a hiking trip next month.",
        "Checking weather conditions.",
        "Gathering equipment and gear.",
        "Inviting friends to join.",
        "Excited for the adventure."
    ],
    [
        "Trying out meditation and mindfulness routines.",
        "Practicing daily for focus.",
        "Helps reduce stress.",
        "Guided sessions are useful.",
        "Feeling more relaxed and productive."
    ],
    [
        "Baking bread at home this weekend.",
        "Used fresh ingredients and traditional recipe.",
        "Loaves turned out fluffy and delicious.",
        "Sharing with friends and family.",
        "Plan to try new flavors next time."
    ],
    [
        "Watching documentary on space exploration.",
        "Learned about missions to Mars.",
        "Fascinating engineering achievements.",
        "Hope for more discoveries soon.",
        "Inspiring for future generations."
    ]
]


#Non-HR job roles and generic topics for No-Intent
non_hr_roles = [
    "Software Engineer", "Frontend Developer", "Data Scientist",
    "Product Manager", "Marketing Specialist", "Sales Representative",
    "Customer Support Agent", "Graphic Designer", "Accountant", "Business Analyst"
]

non_hr_job_templates = [
    [
        "Hiring: {role} for our {location} office. Apply within.",
        "Experience in relevant domain required.",
        "Salary is competitive based on experience.",
        "Interview process is 2 rounds.",
        "Apply online or via email."
    ],
    [
        "We have an opening for a {role}—competitive pay and benefits.",
        "Remote work options may be available.",
        "Candidates with portfolio preferred.",
        "Submit applications before end of month.",
        "Reference checks will be conducted."
    ],
    [
        "Looking for an experienced {role} to join our team remotely.",
        "Must be proficient in relevant tools and software.",
        "Flexible working hours can be discussed.",
        "Interview includes technical assessment.",
        "Submit resume and cover letter online."
    ],
    [
        "Job opening: {role}. Please share resume and portfolio.",
        "Work location can be hybrid or fully remote.",
        "Candidates should have minimum 3 years of experience.",
        "Salary negotiable based on skills and experience.",
        "Reference letters required from previous employers."
    ],
    [
        "We are recruiting {role} for immediate start.",
        "Experience with project management is preferred.",
        "Competitive compensation package offered.",
        "Interview will include HR and technical rounds.",
        "Applications accepted via online portal only."
    ],
    [
        "Hiring {role} to strengthen our {location} office.",
        "Candidates must be self-motivated and proactive.",
        "Salary package is competitive with benefits.",
        "Two-stage interview including technical assessment.",
        "Resume submission online is mandatory."
    ],
    [
        "Opening for {role} position in {location}.",
        "Must have expertise in domain-related software.",
        "Flexible schedule and hybrid work options available.",
        "Interview process involves team discussion.",
        "Submit applications through company portal."
    ],
    [
        "We are looking for {role} to join our growing team.",
        "Candidates should demonstrate strong problem-solving skills.",
        "Salary and benefits are above market standards.",
        "Interview includes technical, HR, and behavioral rounds.",
        "Applications must be submitted before deadline."
    ],
    [
        "Hiring {role} for our {location} branch.",
        "Experience in leading projects is preferred.",
        "Work culture emphasizes teamwork and growth.",
        "Interview process includes case study and discussion.",
        "Apply via email or company career page."
    ],
    [
        "We have a vacancy for {role}.",
        "Candidates must have hands-on experience in the field.",
        "Competitive salary and annual bonus offered.",
        "Two-round interview including practical assessment.",
        "Submit CV and portfolio online."
    ],
    [
        "Looking to recruit {role} for immediate joining.",
        "Must have strong analytical and communication skills.",
        "Salary depends on experience and expertise.",
        "Interview rounds include technical and managerial discussion.",
        "Applications accepted through official portal."
    ],
    [
        "Opening for {role} in {location}.",
        "Prior experience in similar role required.",
        "Work-life balance is a priority in this role.",
        "Interview process is structured in 3 stages.",
        "Candidates must submit resume and portfolio."
    ],
    [
        "Hiring {role} with expertise in {location} region.",
        "Candidate must be able to work independently.",
        "Competitive pay and benefits provided.",
        "Interviews will cover technical and situational questions.",
        "Apply online through the company website."
    ],
    [
        "We are looking for a {role} to join our team.",
        "Experience in project execution is essential.",
        "Salary package includes health and other benefits.",
        "Interview includes technical test and panel discussion.",
        "Submission via online portal only."
    ],
    [
        "Recruiting {role} for our {location} office.",
        "Must be skilled in domain-specific software.",
        "Team collaboration and communication skills important.",
        "Interview rounds include HR, technical, and scenario-based questions.",
        "Resume and cover letter submission required."
    ],
    [
        "Hiring {role} for long-term engagement.",
        "Candidate should have leadership experience.",
        "Salary negotiable depending on experience.",
        "Interview includes HR and technical assessments.",
        "Apply via company career page."
    ],
    [
        "We have an opening for {role} immediately.",
        "Must be able to handle multiple projects simultaneously.",
        "Competitive salary package offered.",
        "Interview rounds include written test and panel discussion.",
        "Applications accepted through online submission."
    ],
    [
        "Looking for {role} to join our office in {location}.",
        "Experience in relevant software tools preferred.",
        "Flexible working hours and hybrid options available.",
        "Interview includes technical and behavioral rounds.",
        "Submit resume online via the company portal."
    ],
    [
        "Opening for {role} position with immediate start.",
        "Must demonstrate strong analytical and teamwork skills.",
        "Salary package is market-competitive.",
        "Interview will include case study and technical evaluation.",
        "Application submission online is mandatory."
    ],
    [
        "Hiring {role} to support our growing team.",
        "Candidate should have domain-specific certifications.",
        "Competitive compensation and benefits offered.",
        "Interview involves HR, technical, and practical tests.",
        "Submit applications through the official company website."
    ]
]



#options
tool_types = [
    "HR automation tools", "recruitment automation platforms", "HR analytics systems",
    "employee onboarding software", "payroll automation tools",
    "performance management systems", "AI-driven HR optimization tools"
]

use_cases = [
    "talent acquisition", "employee onboarding", "payroll processing",
    "performance tracking", "workforce planning", "HR compliance automation",
    "employee engagement analysis"
]

hr_roles = [
    "HR Manager", "Talent Acquisition Specialist", "People Operations Lead",
    "Recruitment Manager", "HRBP", "Compensation & Benefits Specialist",
    "Training & Development Manager"
]

locations = [
    "Dhaka", "Chittagong", "Cumilla", "Khulna", "Sylhet", "Cox's Bazar",
    "Rangpur", "Singapore", "London", "Toronto", "Berlin", "Kuala Lumpur", "Cyberjaya"
]

hr_topics = [
    "employee engagement", "performance evaluation", "workplace culture",
    "learning & development", "talent retention", "HR compliance",
    "skills development"
]

source_types = ["indeed", "linkedin_post", "tweet", "glassdoor"]

#helper functions
def add_noise(text):
    if random.random() < 0.30:
        text += " " + random.choice(["DM for details.", "Any recommendations welcome.", "Thanks!", "Looking forward to responses."])
    return text

def gen_non_hr_job_post(min_sentences=5):
    """Generate a non-HR job post with variability and intent-like filler"""
    template = random.choice(non_hr_job_templates)
    role = random.choice(non_hr_roles)
    n_sentences = random.randint(min_sentences, min(len(template), 7))
    sentences = random.sample(template, n_sentences)
    post = " ".join([sentence.format(role=role, location=random.choice(locations)) for sentence in sentences])

    # Optional filler for non-HR job posts
    non_hr_filler = [
        "Apply quickly!", "Positions are limited.", "Submit resume online.",
        "Looking for top talent.", "Immediate joining preferred.",
        "Send your portfolio.", "Shortlisting candidates soon."
    ]
    for _ in range(random.randint(0,2)):
        post += " " + random.choice(non_hr_filler)

    return post

def generate_post(template_list, intent=None, min_sentences=5, max_sentences=7, **kwargs):
    """Generate a multi-sentence post from a template with variable filler sentences"""
    template = random.choice(template_list)
    n_sentences = random.randint(min_sentences, min(max_sentences, len(template)))
    sentences = random.sample(template, n_sentences)
    post = " ".join([sentence.format(**kwargs) for sentence in sentences])

    # Add intent-appropriate filler sentences
    filler_sentences = {
        "high_intent": [
            "Contact us if interested.", "Proposals welcome.", "We value vendor expertise.",
            "Please provide pricing details.", "Demo sessions available upon request."
        ],
        "medium_intent": [
            "Apply now to be considered.", "We are reviewing resumes continuously.",
            "Interested candidates should reach out.", "Send your CV online.", 
            "Interview slots are limited."
        ],
        "low_intent": [
            "Sharing some HR tips.", "Hope this helps your team.", "Regular updates recommended.",
            "Thoughts welcome.", "Check your policies regularly."
        ],
        "no_intent": [
            "Enjoy your day!", "Thought I would share this.", "Random update for everyone.",
            "Fun fact: stay productive!", "Just sharing some news."
        ]
    }

    if intent in filler_sentences:
        for _ in range(random.randint(0, 2)):
            post += " " + random.choice(filler_sentences[intent])

    return post


def generate_and_save_dataset(counts, save_csv=False, csv_path=None):

    rows = []

    for intent, n_samples in counts.items():
        for _ in range(n_samples):
            if intent == "high_intent":
                t = generate_post(high_intent_templates, tool_type=random.choice(tool_types), use_case=random.choice(use_cases))
            elif intent == "medium_intent":
                t = generate_post(medium_intent_templates, hr_role=random.choice(hr_roles), location=random.choice(locations))
            elif intent == "low_intent":
                t = generate_post(low_intent_templates, hr_topic=random.choice(hr_topics))
            else:  # no_intent
                r = random.random()
                if r < 0.6:
                    t = gen_non_hr_job_post()
                else:
                    t = generate_post(no_intent_templates)
            rows.append({"text": add_noise(t), "intent": intent, "source_type": random.choice(source_types)})

    df = pd.DataFrame(rows).sample(frac=1, random_state=42).reset_index(drop=True)

    if save_csv and csv_path is not None:
        df.to_csv(csv_path, index=False)
        print(f"Saved dataset to {csv_path}")

    return df

