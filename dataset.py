# [INSERT YOUR DATASET HERE - all the questions from phq9_questions through hiri_msm_questions]
# For brevity, I'm not including the full dataset in this response, but you would paste your complete dataset here
# Define all questionnaire data with purposes
# I.) Mental Health Assessment
phq9_questions = [
    {"id": "phq1", "question": "Little interest or pleasure in doing things", "domain": "depression", "purpose": "Screens for depression severity"},
    {"id": "phq2", "question": "Feeling down, depressed, or hopeless", "domain": "depression", "purpose": "Screens for depression severity"},
    {"id": "phq3", "question": "Trouble falling or staying asleep, or sleeping too much", "domain": "depression", "purpose": "Screens for depression severity"},
    {"id": "phq4", "question": "Feeling tired or having little energy", "domain": "depression", "purpose": "Screens for depression severity"},
    {"id": "phq5", "question": "Poor appetite or overeating", "domain": "depression", "purpose": "Screens for depression severity"},
    {"id": "phq6", "question": "Feeling bad about yourself or that you are a failure", "domain": "depression", "purpose": "Screens for depression severity"},
    {"id": "phq7", "question": "Trouble concentrating on things, such as reading or watching television", "domain": "depression", "purpose": "Screens for depression severity"},
    {"id": "phq8", "question": "Moving or speaking so slowly that other people could have noticed", "domain": "depression", "purpose": "Screens for depression severity"},
    {"id": "phq9", "question": "Thoughts that you would be better off dead, or of hurting yourself", "domain": "depression", "purpose": "Screens for depression severity"}
]

gad7_questions = [
    {"id": "gad1", "question": "Feeling nervous, anxious, or on edge", "domain": "anxiety", "purpose": "Assesses severity of generalized anxiety disorder"},
    {"id": "gad2", "question": "Not being able to stop or control worrying", "domain": "anxiety", "purpose": "Assesses severity of generalized anxiety disorder"},
    {"id": "gad3", "question": "Worrying too much about different things", "domain": "anxiety", "purpose": "Assesses severity of generalized anxiety disorder"},
    {"id": "gad4", "question": "Trouble relaxing", "domain": "anxiety", "purpose": "Assesses severity of generalized anxiety disorder"},
    {"id": "gad5", "question": "Being so restless that it's hard to sit still", "domain": "anxiety", "purpose": "Assesses severity of generalized anxiety disorder"},
    {"id": "gad6", "question": "Becoming easily annoyed or irritable", "domain": "anxiety", "purpose": "Assesses severity of generalized anxiety disorder"},
    {"id": "gad7", "question": "Feeling afraid as if something awful might happen", "domain": "anxiety", "purpose": "Assesses severity of generalized anxiety disorder"}
]

dass21_questions = [
    # Depression items
    {"id": "dass1", "question": "I couldn't seem to experience any positive feeling at all", "domain": "depression", "purpose": "Measures depression, anxiety, and stress levels"},
    {"id": "dass2", "question": "I found it difficult to work up the initiative to do things", "domain": "depression", "purpose": "Measures depression, anxiety, and stress levels"},
    {"id": "dass3", "question": "I felt that I had nothing to look forward to", "domain": "depression", "purpose": "Measures depression, anxiety, and stress levels"},
    {"id": "dass4", "question": "I felt down-hearted and blue", "domain": "depression", "purpose": "Measures depression, anxiety, and stress levels"},
    {"id": "dass5", "question": "I was unable to become enthusiastic about anything", "domain": "depression", "purpose": "Measures depression, anxiety, and stress levels"},
    {"id": "dass6", "question": "I felt I wasn't worth much as a person", "domain": "depression", "purpose": "Measures depression, anxiety, and stress levels"},
    {"id": "dass7", "question": "I felt that life was meaningless", "domain": "depression", "purpose": "Measures depression, anxiety, and stress levels"},
    
    # Anxiety items
    {"id": "dass8", "question": "I was aware of dryness of my mouth", "domain": "anxiety", "purpose": "Measures depression, anxiety, and stress levels"},
    {"id": "dass9", "question": "I experienced breathing difficulty", "domain": "anxiety", "purpose": "Measures depression, anxiety, and stress levels"},
    {"id": "dass10", "question": "I experienced trembling (e.g., in the hands)", "domain": "anxiety", "purpose": "Measures depression, anxiety, and stress levels"},
    {"id": "dass11", "question": "I was worried about situations in which I might panic", "domain": "anxiety", "purpose": "Measures depression, anxiety, and stress levels"},
    {"id": "dass12", "question": "I felt I was close to panic", "domain": "anxiety", "purpose": "Measures depression, anxiety, and stress levels"},
    {"id": "dass13", "question": "I was aware of the action of my heart in the absence of physical exertion", "domain": "anxiety", "purpose": "Measures depression, anxiety, and stress levels"},
    {"id": "dass14", "question": "I felt scared without any good reason", "domain": "anxiety", "purpose": "Measures depression, anxiety, and stress levels"},
    
    # Stress items
    {"id": "dass15", "question": "I found it hard to wind down", "domain": "stress", "purpose": "Measures depression, anxiety, and stress levels"},
    {"id": "dass16", "question": "I tended to over-react to situations", "domain": "stress", "purpose": "Measures depression, anxiety, and stress levels"},
    {"id": "dass17", "question": "I felt that I was using a lot of nervous energy", "domain": "stress", "purpose": "Measures depression, anxiety, and stress levels"},
    {"id": "dass18", "question": "I found myself getting agitated", "domain": "stress", "purpose": "Measures depression, anxiety, and stress levels"},
    {"id": "dass19", "question": "I found it difficult to relax", "domain": "stress", "purpose": "Measures depression, anxiety, and stress levels"},
    {"id": "dass20", "question": "I was intolerant of anything that kept me from getting on with what I was doing", "domain": "stress", "purpose": "Measures depression, anxiety, and stress levels"},
    {"id": "dass21", "question": "I felt that I was rather touchy", "domain": "stress", "purpose": "Measures depression, anxiety, and stress levels"}
]

audit_questions = [
    {"id": "audit1", "question": "How often do you have a drink containing alcohol?", "domain": "substance_use", "purpose": "Screens for hazardous and harmful alcohol consumption"},
    {"id": "audit2", "question": "How many drinks containing alcohol do you have on a typical day when you are drinking?", "domain": "substance_use", "purpose": "Screens for hazardous and harmful alcohol consumption"},
    {"id": "audit3", "question": "How often do you have six or more drinks on one occasion?", "domain": "substance_use", "purpose": "Screens for hazardous and harmful alcohol consumption"},
    {"id": "audit4", "question": "How often during the last year have you found that you were not able to stop drinking once you had started?", "domain": "substance_use", "purpose": "Screens for hazardous and harmful alcohol consumption"},
    {"id": "audit5", "question": "How often during the last year have you failed to do what was normally expected of you because of drinking?", "domain": "substance_use", "purpose": "Screens for hazardous and harmful alcohol consumption"},
    {"id": "audit6", "question": "How often during the last year have you needed a first drink in the morning to get yourself going after a heavy drinking session?", "domain": "substance_use", "purpose": "Screens for hazardous and harmful alcohol consumption"},
    {"id": "audit7", "question": "How often during the last year have you had a feeling of guilt or remorse after drinking?", "domain": "substance_use", "purpose": "Screens for hazardous and harmful alcohol consumption"},
    {"id": "audit8", "question": "How often during the last year have you been unable to remember what happened the night before because of your drinking?", "domain": "substance_use", "purpose": "Screens for hazardous and harmful alcohol consumption"},
    {"id": "audit9", "question": "Have you or someone else been injured because of your drinking?", "domain": "substance_use", "purpose": "Screens for hazardous and harmful alcohol consumption"},
    {"id": "audit10", "question": "Has a relative, friend, doctor, or other health care worker been concerned about your drinking or suggested you cut down?", "domain": "substance_use", "purpose": "Screens for hazardous and harmful alcohol consumption"}
]

dast10_questions = [
    {"id": "dast1", "question": "Have you used drugs other than those required for medical reasons?", "domain": "substance_use", "purpose": "Assesses drug use and related problems"},
    {"id": "dast2", "question": "Do you abuse more than one drug at a time?", "domain": "substance_use", "purpose": "Assesses drug use and related problems"},
    {"id": "dast3", "question": "Are you always able to stop using drugs when you want to?", "domain": "substance_use", "purpose": "Assesses drug use and related problems"},
    {"id": "dast4", "question": "Have you had blackouts or flashbacks as a result of drug use?", "domain": "substance_use", "purpose": "Assesses drug use and related problems"},
    {"id": "dast5", "question": "Do you ever feel bad or guilty about your drug use?", "domain": "substance_use", "purpose": "Assesses drug use and related problems"},
    {"id": "dast6", "question": "Does your spouse (or parents) ever complain about your involvement with drugs?", "domain": "substance_use", "purpose": "Assesses drug use and related problems"},
    {"id": "dast7", "question": "Have you neglected your family because of your use of drugs?", "domain": "substance_use", "purpose": "Assesses drug use and related problems"},
    {"id": "dast8", "question": "Have you engaged in illegal activities in order to obtain drugs?", "domain": "substance_use", "purpose": "Assesses drug use and related problems"},
    {"id": "dast9", "question": "Have you ever experienced withdrawal symptoms (felt sick) when you stopped taking drugs?", "domain": "substance_use", "purpose": "Assesses drug use and related problems"},
    {"id": "dast10", "question": "Have you had medical problems as a result of your drug use?", "domain": "substance_use", "purpose": "Assesses drug use and related problems"}
]

minority_stress_questions = [
    {"id": "ms1", "question": "I have been rejected by family members because of my sexual orientation or gender identity", "domain": "minority_stress", "purpose": "Evaluates stressors unique to minority populations, particularly LGBTQ+ individuals"},
    {"id": "ms2", "question": "I have been verbally insulted because of my sexual orientation or gender identity", "domain": "minority_stress", "purpose": "Evaluates stressors unique to minority populations, particularly LGBTQ+ individuals"},
    {"id": "ms3", "question": "I have been discriminated against in employment because of my sexual orientation or gender identity", "domain": "minority_stress", "purpose": "Evaluates stressors unique to minority populations, particularly LGBTQ+ individuals"},
    {"id": "ms4", "question": "I worry about being treated differently because of my sexual orientation or gender identity", "domain": "minority_stress", "purpose": "Evaluates stressors unique to minority populations, particularly LGBTQ+ individuals"},
    {"id": "ms5", "question": "I hide my sexual orientation or gender identity from others", "domain": "minority_stress", "purpose": "Evaluates stressors unique to minority populations, particularly LGBTQ+ individuals"},
    {"id": "ms6", "question": "I feel the need to be constantly vigilant about my safety", "domain": "minority_stress", "purpose": "Evaluates stressors unique to minority populations, particularly LGBTQ+ individuals"}
]

mspss_questions = [
    {"id": "mspss1", "question": "There is a special person who is around when I am in need", "domain": "social_support", "purpose": "Measures perceived social support from family, friends, and significant others"},
    {"id": "mspss2", "question": "There is a special person with whom I can share my joys and sorrows", "domain": "social_support", "purpose": "Measures perceived social support from family, friends, and significant others"},
    {"id": "mspss3", "question": "My family really tries to help me", "domain": "social_support", "purpose": "Measures perceived social support from family, friends, and significant others"},
    {"id": "mspss4", "question": "I get the emotional help and support I need from my family", "domain": "social_support", "purpose": "Measures perceived social support from family, friends, and significant others"},
    {"id": "mspss5", "question": "I have a special person who is a real source of comfort to me", "domain": "social_support", "purpose": "Measures perceived social support from family, friends, and significant others"},
    {"id": "mspss6", "question": "My friends really try to help me", "domain": "social_support", "purpose": "Measures perceived social support from family, friends, and significant others"},
    {"id": "mspss7", "question": "I can count on my friends when things go wrong", "domain": "social_support", "purpose": "Measures perceived social support from family, friends, and significant others"},
    {"id": "mspss8", "question": "I can talk about my problems with my family", "domain": "social_support", "purpose": "Measures perceived social support from family, friends, and significant others"},
    {"id": "mspss9", "question": "I have friends with whom I can share my joys and sorrows", "domain": "social_support", "purpose": "Measures perceived social support from family, friends, and significant others"},
    {"id": "mspss10", "question": "There is a special person in my life who cares about my feelings", "domain": "social_support", "purpose": "Measures perceived social support from family, friends, and significant others"},
    {"id": "mspss11", "question": "My family is willing to help me make decisions", "domain": "social_support", "purpose": "Measures perceived social support from family, friends, and significant others"},
    {"id": "mspss12", "question": "I can talk about my problems with my friends", "domain": "social_support", "purpose": "Measures perceived social support from family, friends, and significant others"}
]

ihp_questions = [
    {"id": "ihp1", "question": "I have tried to stop being attracted to people of the same sex", "domain": "internalized_homophobia", "purpose": "Assesses internalized negative attitudes toward one's own homosexuality"},
    {"id": "ihp2", "question": "I wish I weren't gay/lesbian/bisexual", "domain": "internalized_homophobia", "purpose": "Assesses internalized negative attitudes toward one's own homosexuality"},
    {"id": "ihp3", "question": "I feel alienated from myself because of being gay/lesbian/bisexual", "domain": "internalized_homophobia", "purpose": "Assesses internalized negative attitudes toward one's own homosexuality"},
    {"id": "ihp4", "question": "I wish I could develop more erotic feelings about people of the opposite sex", "domain": "internalized_homophobia", "purpose": "Assesses internalized negative attitudes toward one's own homosexuality"},
    {"id": "ihp5", "question": "I feel that being gay/lesbian/bisexual is a personal shortcoming for me", "domain": "internalized_homophobia", "purpose": "Assesses internalized negative attitudes toward one's own homosexuality"}
]

# II.) Vitality and Wellness Assessments
psqi_questions = [
    {"id": "psqi1", "question": "During the past month, how would you rate your sleep quality overall?", "domain": "sleep", "purpose": "Evaluates sleep quality and disturbances over a one-month interval"},
    {"id": "psqi2", "question": "During the past month, how long has it usually taken you to fall asleep each night?", "domain": "sleep", "purpose": "Evaluates sleep quality and disturbances over a one-month interval"},
    {"id": "psqi3", "question": "During the past month, how many hours of actual sleep did you get at night?", "domain": "sleep", "purpose": "Evaluates sleep quality and disturbances over a one-month interval"},
    {"id": "psqi4", "question": "During the past month, how often have you had trouble sleeping because you cannot get to sleep within 30 minutes?", "domain": "sleep", "purpose": "Evaluates sleep quality and disturbances over a one-month interval"},
    {"id": "psqi5", "question": "During the past month, how often have you had trouble sleeping because you wake up in the middle of the night or early morning?", "domain": "sleep", "purpose": "Evaluates sleep quality and disturbances over a one-month interval"},
    {"id": "psqi6", "question": "During the past month, how often have you had trouble sleeping because you have to get up to use the bathroom?", "domain": "sleep", "purpose": "Evaluates sleep quality and disturbances over a one-month interval"},
    {"id": "psqi7", "question": "During the past month, how often have you had trouble sleeping because you cannot breathe comfortably?", "domain": "sleep", "purpose": "Evaluates sleep quality and disturbances over a one-month interval"},
    {"id": "psqi8", "question": "During the past month, how often have you had trouble sleeping because you cough or snore loudly?", "domain": "sleep", "purpose": "Evaluates sleep quality and disturbances over a one-month interval"},
    {"id": "psqi9", "question": "During the past month, how often have you had trouble sleeping because you feel too hot or too cold?", "domain": "sleep", "purpose": "Evaluates sleep quality and disturbances over a one-month interval"},
    {"id": "psqi10", "question": "During the past month, how often have you had trouble sleeping because you have bad dreams?", "domain": "sleep", "purpose": "Evaluates sleep quality and disturbances over a one-month interval"},
    {"id": "psqi11", "question": "During the past month, how often have you taken medicine to help you sleep?", "domain": "sleep", "purpose": "Evaluates sleep quality and disturbances over a one-month interval"},
    {"id": "psqi12", "question": "During the past month, how often have you had trouble staying awake while driving, eating meals, or engaging in social activity?", "domain": "sleep", "purpose": "Evaluates sleep quality and disturbances over a one-month interval"},
    {"id": "psqi13", "question": "During the past month, how much of a problem has it been for you to keep up enough enthusiasm to get things done?", "domain": "sleep", "purpose": "Evaluates sleep quality and disturbances over a one-month interval"}
]

ipaq_questions = [
    {"id": "ipaq1", "question": "During the last 7 days, on how many days did you do vigorous physical activities like heavy lifting, digging, aerobics, or fast bicycling?", "domain": "physical_activity", "purpose": "Assesses physical activity levels"},
    {"id": "ipaq2", "question": "How much time did you usually spend doing vigorous physical activities on one of those days?", "domain": "physical_activity", "purpose": "Assesses physical activity levels"},
    {"id": "ipaq3", "question": "During the last 7 days, on how many days did you do moderate physical activities like carrying light loads, bicycling at a regular pace, or doubles tennis?", "domain": "physical_activity", "purpose": "Assesses physical activity levels"},
    {"id": "ipaq4", "question": "How much time did you usually spend doing moderate physical activities on one of those days?", "domain": "physical_activity", "purpose": "Assesses physical activity levels"},
    {"id": "ipaq5", "question": "During the last 7 days, on how many days did you walk for at least 10 minutes at a time?", "domain": "physical_activity", "purpose": "Assesses physical activity levels"},
    {"id": "ipaq6", "question": "How much time did you usually spend walking on one of those days?", "domain": "physical_activity", "purpose": "Assesses physical activity levels"},
    {"id": "ipaq7", "question": "During the last 7 days, how much time did you spend sitting on a week day?", "domain": "physical_activity", "purpose": "Assesses physical activity levels"}
]

ffq_questions = [
    {"id": "ffq1", "question": "How often do you eat fruits (fresh, frozen, or canned)?", "domain": "nutrition", "purpose": "Evaluates dietary intake over a specified period"},
    {"id": "ffq2", "question": "How often do you eat vegetables (excluding potatoes)?", "domain": "nutrition", "purpose": "Evaluates dietary intake over a specified period"},
    {"id": "ffq3", "question": "How often do you eat whole grain foods (bread, cereals, rice)?", "domain": "nutrition", "purpose": "Evaluates dietary intake over a specified period"},
    {"id": "ffq4", "question": "How often do you eat processed or fast foods?", "domain": "nutrition", "purpose": "Evaluates dietary intake over a specified period"},
    {"id": "ffq5", "question": "How often do you drink sugar-sweetened beverages (soda, sports drinks)?", "domain": "nutrition", "purpose": "Evaluates dietary intake over a specified period"},
    {"id": "ffq6", "question": "How often do you eat fish or seafood?", "domain": "nutrition", "purpose": "Evaluates dietary intake over a specified period"},
    {"id": "ffq7", "question": "How often do you eat red meat (beef, pork, lamb)?", "domain": "nutrition", "purpose": "Evaluates dietary intake over a specified period"},
    {"id": "ffq8", "question": "How often do you consume dairy products (milk, cheese, yogurt)?", "domain": "nutrition", "purpose": "Evaluates dietary intake over a specified period"}
]

sf36_questions = [
    {"id": "sf1", "question": "In general, would you say your health is excellent, very good, good, fair, or poor?", "domain": "quality_of_life", "purpose": "Measures health-related quality of life across multiple domains"},
    {"id": "sf2", "question": "Compared to one year ago, how would you rate your health in general now?", "domain": "quality_of_life", "purpose": "Measures health-related quality of life across multiple domains"},
    {"id": "sf3", "question": "Does your health now limit you in vigorous activities, such as running, lifting heavy objects, participating in strenuous sports?", "domain": "quality_of_life", "purpose": "Measures health-related quality of life across multiple domains"},
    {"id": "sf4", "question": "Does your health now limit you in moderate activities, such as moving a table, pushing a vacuum cleaner, bowling, or playing golf?", "domain": "quality_of_life", "purpose": "Measures health-related quality of life across multiple domains"},
    {"id": "sf5", "question": "Does your health now limit you in lifting or carrying groceries?", "domain": "quality_of_life", "purpose": "Measures health-related quality of life across multiple domains"},
    {"id": "sf6", "question": "Does your health now limit you in climbing several flights of stairs?", "domain": "quality_of_life", "purpose": "Measures health-related quality of life across multiple domains"},
    {"id": "sf7", "question": "Does your health now limit you in climbing one flight of stairs?", "domain": "quality_of_life", "purpose": "Measures health-related quality of life across multiple domains"},
    {"id": "sf8", "question": "Does your health now limit you in bending, kneeling, or stooping?", "domain": "quality_of_life", "purpose": "Measures health-related quality of life across multiple domains"},
    {"id": "sf9", "question": "Does your health now limit you in walking more than a mile?", "domain": "quality_of_life", "purpose": "Measures health-related quality of life across multiple domains"},
    {"id": "sf10", "question": "Does your health now limit you in walking several blocks?", "domain": "quality_of_life", "purpose": "Measures health-related quality of life across multiple domains"}
]

bis_questions = [
    {"id": "bis1", "question": "Have you been feeling self-conscious about your appearance?", "domain": "body_image", "purpose": "Assesses body image perceptions, particularly in patients with cancer"},
    {"id": "bis2", "question": "Have you felt less physically attractive as a result of your disease or treatment?", "domain": "body_image", "purpose": "Assesses body image perceptions, particularly in patients with cancer"},
    {"id": "bis3", "question": "Have you been dissatisfied with your appearance when dressed?", "domain": "body_image", "purpose": "Assesses body image perceptions, particularly in patients with cancer"},
    {"id": "bis4", "question": "Have you been feeling less feminine/masculine as a result of your disease or treatment?", "domain": "body_image", "purpose": "Assesses body image perceptions, particularly in patients with cancer"},
    {"id": "bis5", "question": "Did you find it difficult to look at yourself naked?", "domain": "body_image", "purpose": "Assesses body image perceptions, particularly in patients with cancer"},
    {"id": "bis6", "question": "Have you been feeling less sexually attractive as a result of your disease or treatment?", "domain": "body_image", "purpose": "Assesses body image perceptions, particularly in patients with cancer"},
    {"id": "bis7", "question": "Did you avoid people because of the way you felt about your appearance?", "domain": "body_image", "purpose": "Assesses body image perceptions, particularly in patients with cancer"},
    {"id": "bis8", "question": "Have you been feeling the treatment has left your body less whole?", "domain": "body_image", "purpose": "Assesses body image perceptions, particularly in patients with cancer"},
    {"id": "bis9", "question": "Have you felt dissatisfied with your body?", "domain": "body_image", "purpose": "Assesses body image perceptions, particularly in patients with cancer"},
    {"id": "bis10", "question": "Have you been dissatisfied with the appearance of your scar?", "domain": "body_image", "purpose": "Assesses body image perceptions, particularly in patients with cancer"}
]

# III.) Sexual Health Risk Assessments
msm_sexual_health_questions = [
    {"id": "msm1", "question": "In the past 6 months, how many male partners have you had anal or oral sex with?", "domain": "sexual_health", "purpose": "Evaluates sexual behaviors and STI risk among men who have sex with men (MSM)"},
    {"id": "msm2", "question": "In the past 6 months, how often did you use condoms during anal sex?", "domain": "sexual_health", "purpose": "Evaluates sexual behaviors and STI risk among men who have sex with men (MSM)"},
    {"id": "msm3", "question": "In the past 6 months, have you had sex while under the influence of alcohol or drugs?", "domain": "sexual_health", "purpose": "Evaluates sexual behaviors and STI risk among men who have sex with men (MSM)"},
    {"id": "msm4", "question": "Have you ever been diagnosed with a sexually transmitted infection (STI)?", "domain": "sexual_health", "purpose": "Evaluates sexual behaviors and STI risk among men who have sex with men (MSM)"},
    {"id": "msm5", "question": "When was your last HIV test?", "domain": "sexual_health", "purpose": "Evaluates sexual behaviors and STI risk among men who have sex with men (MSM)"},
    {"id": "msm6", "question": "Are you currently taking PrEP (pre-exposure prophylaxis) for HIV prevention?", "domain": "sexual_health", "purpose": "Evaluates sexual behaviors and STI risk among men who have sex with men (MSM)"}
]

hiri_msm_questions = [
    {"id": "hiri1", "question": "What is your age?", "domain": "hiv_risk", "purpose": "Estimates the risk of HIV acquisition among MSM"},
    {"id": "hiri2", "question": "What is your race/ethnicity?", "domain": "hiv_risk", "purpose": "Estimates the risk of HIV acquisition among MSM"},
    {"id": "hiri3", "question": "In the past 6 months, how many male sex partners have you had?", "domain": "hiv_risk", "purpose": "Estimates the risk of HIV acquisition among MSM"},
    {"id": "hiri4", "question": "In the past 6 months, how many times have you had receptive anal sex without a condom?", "domain": "hiv_risk", "purpose": "Estimates the risk of HIV acquisition among MSM"},
    {"id": "hiri5", "question": "What is the HIV status of your most recent male sex partner?", "domain": "hiv_risk", "purpose": "Estimates the risk of HIV acquisition among MSM"},
    {"id": "hiri6", "question": "Have you ever used poppers (alkyl nitrites) during sex?", "domain": "hiv_risk", "purpose": "Estimates the risk of HIV acquisition among MSM"},
    {"id": "hiri7", "question": "Have you ever been diagnosed with a bacterial STI (gonorrhea, chlamydia, syphilis)?", "domain": "hiv_risk", "purpose": "Estimates the risk of HIV acquisition among MSM"}
]

# Combine all questions
all_questions = (phq9_questions + gad7_questions + dass21_questions + audit_questions + 
                dast10_questions + minority_stress_questions + mspss_questions + ihp_questions +
                psqi_questions + ipaq_questions + ffq_questions + sf36_questions + bis_questions +
                msm_sexual_health_questions + hiri_msm_questions)

# FIXED: Enhanced purpose-to-domain mapping with correct field matching
purpose_mappings = {
    "depression": ["depression", "mental_health", "mood"],
    "anxiety": ["anxiety", "mental_health", "worry"],
    "stress": ["stress", "mental_health", "pressure"],
    "substance_use": ["substance_use", "alcohol", "drugs"],
    "minority_stress": ["minority_stress", "lgbtq", "discrimination"],
    "social_support": ["social_support", "support", "relationships"],
    "internalized_homophobia": ["internalized_homophobia", "lgbtq", "self_acceptance"],
    "sleep": ["sleep", "physical_health", "rest"],
    "physical_activity": ["physical_activity", "exercise", "fitness"],
    "nutrition": ["nutrition", "diet", "eating"],
    "quality_of_life": ["quality_of_life", "wellbeing", "life_satisfaction"],
    "body_image": ["body_image", "self_perception", "appearance"],
    "sexual_health": ["sexual_health", "sexual_behavior", "sti_risk"],
    "hiv_risk": ["hiv_risk", "sexual_health", "risk_assessment"]
}

# Enhanced scoring criteria
scoring_keywords = {
    "never": {
        "score": 0,
        "keywords": ["never", "not at all", "doesn't apply", "no", "not", "none", "nothing", "rarely", "hardly ever", 
                    "didn't experience", "didn't feel", "not once", "0%", "zero", "nope", "not ever", "excellent", 
                    "very good", "not limited at all", "none of the time", "definitely false", "very strongly disagree"]
    },
    "sometimes": {
        "score": 1,
        "keywords": ["sometimes", "some of the time", "occasionally", "a bit", "slightly", "a little", "somewhat", 
                    "mild", "mildly", "every now and then", "once in a while", "25%", "partly", "at times", "kind of",
                    "seldom", "good", "limited a little", "a little of the time", "mostly false", "strongly disagree",
                    "fair", "1-2 times", "monthly"]
    },
    "often": {
        "score": 2,
        "keywords": ["often", "good part of time", "considerable", "a lot", "frequently", "regular", "regularly", 
                    "moderate", "moderately", "quite a bit", "quite often", "common", "commonly", "50%", "half of the time", 
                    "usually", "limited a lot", "a good bit of the time", "don't know", "neither true nor false",
                    "poor", "3-5 times", "weekly"]
    },
    "almost_always": {
        "score": 3,
        "keywords": ["almost always", "very much", "most of the time", "almost all the time", "severe", "severely", 
                    "extremely", "constantly", "always", "every day", "all the time", "completely", "75%", "100%", 
                    "definitely", "absolutely", "limited a lot", "most of the time", "all of the time", 
                    "definitely true", "very strongly agree", "6+ times", "daily"]
    }
}

# Add at the top of dataset.py, after the imports
# filepath: c:\heath_screening\dataset.py

# Define static screening questions that are asked to all users
static_questions = [
    {
        "id": "static1",
        "question": "Which of the following outcomes are the most important to you?",
        "type": "multiple_choice",
        "options": [
            "Sleep",
            "Stress reduction",
            "Immune health",
            "Looking younger",
            "Cognition",
            "Energy",
            "Weight loss",
            "Longevity",
            "Physical performance",
            "Other"
        ]
    },
    {
        "id": "static2",
        "question": "Why are the chosen outcomes from the prior question your biggest priorities?",
        "type": "text"
    },
    {
        "id": "static3",
        "question": "Which symptoms are you currently experiencing?",
        "type": "multiple_choice",
        "options": [
            "Weight gain",
            "Regular bloating",
            "Hair loss", 
            "Sleep disturbance",
            "Decreased libido",
            "Fatigue",
            "Stress",
            "Dry skin",
            "None of the above"
        ]
    },
    {
        "id": "static4",
        "question": "Are there any obstacles that may prevent you from achieving your health goals?",
        "type": "multiple_choice",
        "options": [
            "Time constraints (e.g. busy schedules)",
            "Financial limitations (e.g. cost of treatments or supplements)",
            "Lack of motivation or consistency",
            "Limited access to resources (e.g. gym, healthy food)",
            "Uncertainty about where to start",
            "Stress or mental health challenges", 
            "Existing medical conditions or chronic illnesses"
        ]
    },
    {
        "id": "static5",
        "question": "We personalize everything to you. Please select how comprehensive and technical you would like us to be in presenting content to you:",
        "type": "scale",
        "min": 1,
        "max": 10
    }
]

# Add these mappings at the end of dataset.py
static_purpose_mappings = {
    # Outcome priorities (static1)
    "Sleep": ["sleep", "physical_health", "quality_of_life"],
    "Stress reduction": ["stress", "mental_health", "anxiety"],
    "Immune health": ["physical_health", "quality_of_life"],
    "Looking younger": ["body_image", "quality_of_life"],
    "Cognition": ["mental_health", "quality_of_life"],
    "Energy": ["physical_health", "quality_of_life"],
    "Weight loss": ["body_image", "nutrition", "physical_activity"],
    "Longevity": ["quality_of_life", "physical_health"],
    "Physical performance": ["physical_activity", "quality_of_life"],
    
    # Symptoms (static3)
    "Weight gain": ["body_image", "nutrition", "physical_activity"],
    "Regular bloating": ["nutrition", "physical_health"],
    "Hair loss": ["body_image", "physical_health"],
    "Sleep disturbance": ["sleep", "quality_of_life"],
    "Decreased libido": ["sexual_health", "quality_of_life"],
    "Fatigue": ["sleep", "physical_health", "quality_of_life"],
    "Stress": ["stress", "mental_health", "anxiety"],
    "Dry skin": ["body_image", "physical_health"],
    
    # Obstacles (static4)
    "Time constraints": ["stress", "physical_activity"],
    "Financial limitations": ["stress", "quality_of_life"],
    "Lack of motivation": ["mental_health", "depression"],
    "Limited access to resources": ["physical_activity", "nutrition"],
    "Uncertainty about where to start": ["anxiety", "stress"],
    "Stress or mental health challenges": ["mental_health", "anxiety", "depression", "stress"],
    "Existing medical conditions": ["physical_health", "quality_of_life"]
}