"""
Scheme & Document Database for Scheme Finder.
Comprehensive registry of verified Central & State Government Welfare and Scholarship programs
across Andhra Pradesh, Telangana, Tamil Nadu, and All-India (Central).
"""

from engine import Scheme, Rule


def get_all_schemes():
    schemes = [
        # =========================================================================
        # 🟡 ANDHRA PRADESH STATE SCHEMES
        # =========================================================================
        Scheme(
            id="ap-jvd-01",
            name="Jagananna Vidya Deevena (RTF - Full Fee Reimbursement)",
            department="Higher Education & Social Welfare Department, Govt. of Andhra Pradesh",
            category_type="Education",
            state="Andhra Pradesh",
            description="Provides 100% total tuition fee reimbursement to eligible students pursuing ITI, Polytechnic, Degree, B.Tech, Pharmacy, MBA, MCA, and Medicine in Andhra Pradesh.",
            benefit="100% Complete Tuition Fee Reimbursement credited directly to college/mother's bank account",
            official_portal_url="https://jnanabhumi.ap.gov.in",
            documents=[
                "Rice Card / White Ration Card",
                "Meeseva Income Certificate (Family income ≤ ₹2.5 Lakh/annum)",
                "Integrated Community / Caste Certificate (SC/ST/BC/EBC/Minority/Kapu)",
                "Class 10th (SSC) & Intermediate Marks Memo",
                "College Admission Allotment Order (Convenor Quota)",
                "Mother's Aadhaar Card & Active Bank Passbook"
            ],
            rules=[
                Rule("income", "<=", 250000, "Annual family income does not exceed ₹2,50,000"),
                Rule("course_level", "in", ["UG", "PG", "Diploma", "Degree", "B.Tech", "Engineering", "Medicine", "MBA", "MCA"], "Enrolled in recognized Post-Matric Degree or Diploma course"),
                Rule("category", "in", ["SC", "ST", "BC", "OBC", "EBC", "Kapu", "Minority", "General", "EWS"], "Social category eligible for fee reimbursement")
            ],
            priority_weight=99
        ),

        Scheme(
            id="ap-jvd-mtf-02",
            name="Jagananna Vasathi Deevena (MTF - Food & Hostel Allowance)",
            department="Social Welfare & Backward Classes Welfare Dept., Govt. of Andhra Pradesh",
            category_type="Education",
            state="Andhra Pradesh",
            description="Provides direct financial aid to meet boarding, mess, and hostel expenses for post-matric college students in Andhra Pradesh.",
            benefit="₹10,000/yr for ITI, ₹15,000/yr for Polytechnic, ₹20,000/yr for Degree/B.Tech/MBBS (in 2 installments)",
            official_portal_url="https://jnanabhumi.ap.gov.in",
            documents=[
                "White Ration Card / Rice Card copy",
                "College Bonafide & Hostel Stay Certificate (signed by Principal/Warden)",
                "Student & Mother's Aadhaar Cards",
                "Biometric Attendance record (≥ 75% college attendance)",
                "Mother's NPCI Aadhaar-seeded Bank Passbook"
            ],
            rules=[
                Rule("income", "<=", 250000, "Household annual income within ₹2.5 Lakh limit"),
                Rule("course_level", "in", ["UG", "PG", "Diploma", "B.Tech", "Degree"], "Pursuing regular Degree or Professional course")
            ],
            priority_weight=97
        ),

        Scheme(
            id="ap-aarogyasri-03",
            name="Dr. YSR Aarogyasri Health Scheme",
            department="Dr. YSR Aarogyasri Health Care Trust, Govt. of Andhra Pradesh",
            category_type="Healthcare",
            state="Andhra Pradesh",
            description="Premier health insurance offering universal cashless medical and surgical care across empanelled super-specialty hospitals in AP, Hyderabad, Chennai, and Bengaluru.",
            benefit="100% Cashless treatment up to ₹25,00,000 per family per year covering 3,257 treatments",
            official_portal_url="https://ysraarogyasri.ap.gov.in",
            documents=[
                "Dr. YSR Aarogyasri Health Card / Rice Card / BPL Ration Card",
                "Aadhaar Card of all family members",
                "Income Certificate or Proof of Land Holding (< 12 wet acres / < 35 dry acres)",
                "Medical Diagnosis / Referral Slip from Network Hospital"
            ],
            rules=[
                Rule("income", "<=", 500000, "Annual family income does not exceed ₹5,00,000 ceiling"),
                Rule("category", "in", ["General", "OBC", "BC", "SC", "ST", "EWS"], "Open to all socioeconomic categories with valid BPL/Rice card")
            ],
            priority_weight=96
        ),

        Scheme(
            id="ap-rythu-04",
            name="YSR Rythu Bharosa - PM KISAN",
            department="Department of Agriculture & Cooperation, Govt. of Andhra Pradesh",
            category_type="Agriculture",
            state="Andhra Pradesh",
            description="Financial investment support scheme providing direct assistance to farmer and tenant families (including SC/ST/BC/Minority tenant farmers) before crop sowing seasons.",
            benefit="₹13,500 per year per farmer family paid in three seasonal installments",
            official_portal_url="https://ysrrythubharosa.ap.gov.in",
            documents=[
                "Pattadar Passbook / Land 1B Record (or Tenant CCRC Card for tenant farmers)",
                "Farmer Aadhaar Card",
                "Active Bank Account seeded with Aadhaar",
                "Crop Sowing e-Crop registration confirmation"
            ],
            rules=[
                Rule("is_farmer", "==", True, "Must be an active agricultural landholder or tenant cultivator", is_mandatory=False),
                Rule("income", "<=", 400000, "Small and marginal farming household income bracket")
            ],
            priority_weight=90
        ),

        Scheme(
            id="ap-cheyutha-05",
            name="YSR Cheyutha (Livelihood Assistance for Women)",
            department="Panchayati Raj & Rural Development Dept., Govt. of Andhra Pradesh",
            category_type="Women Empowerment",
            state="Andhra Pradesh",
            description="Direct financial empowerment for women belonging to SC, ST, BC, and Minority communities to establish sustainable micro-enterprises and grocery stores.",
            benefit="₹18,750 per year (total ₹75,000 over 4 years) direct financial grant",
            official_portal_url="https://navasakam.ap.gov.in",
            documents=[
                "Integrated Community / Caste Certificate (SC/ST/BC/Minority)",
                "White Ration Card / Rice Card",
                "Date of Birth Proof (Age 45 to 60 years)",
                "Aadhaar Card",
                "Bank Account Passbook"
            ],
            rules=[
                Rule("gender", "==", "Female", "Targeted exclusively for women beneficiaries"),
                Rule("category", "in", ["SC", "ST", "BC", "OBC", "Minority"], "Eligible backward or marginalized community"),
                Rule("income", "<=", 300000, "Family income is within ₹3 Lakh per annum")
            ],
            priority_weight=89
        ),

        Scheme(
            id="ap-amma-vodi-06",
            name="Jagananna Amma Vodi (School Education Incentive)",
            department="School Education Department, Govt. of Andhra Pradesh",
            category_type="Education",
            state="Andhra Pradesh",
            description="Incentivizes mothers to send their children to school from Class 1 to Class 12 by providing annual direct cash transfers to eliminate school dropouts.",
            benefit="₹15,000 per year credited directly into the mother's bank account",
            official_portal_url="https://jnanabhumi.ap.gov.in",
            documents=[
                "White Ration Card / Rice Card",
                "Mother & Child Aadhaar Cards",
                "School Admission / Bonafide Certificate with Child Info ID",
                "Child Attendance Record (≥ 75% in school)",
                "Mother's Bank Account Passbook"
            ],
            rules=[
                Rule("income", "<=", 250000, "Annual family income does not exceed ₹2.5 Lakh"),
                Rule("course_level", "in", ["Class 10", "Class 12", "Secondary", "Higher Secondary", "School"], "Enrolled in school education (Class 1 to 12)")
            ],
            priority_weight=93
        ),

        # =========================================================================
        # 🔵 TELANGANA STATE SCHEMES
        # =========================================================================
        Scheme(
            id="ts-epass-01",
            name="Telangana ePASS Post-Matric Scholarship & Fee Reimbursement (RTF & MTF)",
            department="Scheduled Castes, BC, Tribal & Minority Welfare Departments, Govt. of Telangana",
            category_type="Education",
            state="Telangana",
            description="Reimburses 100% of college tuition fees (RTF) and pays monthly maintenance allowance (MTF) to SC, ST, BC, EBC, and Minority students in Telangana.",
            benefit="100% Tuition Fee Reimbursement + up to ₹12,000/yr Hostel & Mess Maintenance Allowance",
            official_portal_url="https://telanganaepass.cgg.gov.in",
            documents=[
                "Meeseva Caste Certificate with CND Number",
                "Meeseva Income Certificate issued by Tahsildar (after April 1st)",
                "SSC (Class 10) Memo / Hall Ticket Number",
                "Intermediate / Previous Degree Marks Memo",
                "College Allotment Order & Joining Report (DOST / TS EAMCET / TS ICET)",
                "Student Aadhaar-linked Bank Account Passbook"
            ],
            rules=[
                Rule("income", "<=", 200000, "Family income within ₹2,00,000 (SC/ST/Rural BC) or ₹1,50,000 (Urban BC)"),
                Rule("course_level", "in", ["UG", "PG", "Diploma", "B.Tech", "Engineering", "Degree", "MBA", "MCA", "Medicine"], "Enrolled in recognized Post-Matriculation degree"),
                Rule("category", "in", ["SC", "ST", "BC", "OBC", "EBC", "Minority", "EWS"], "Eligible category for Telangana fee reimbursement")
            ],
            priority_weight=99
        ),

        Scheme(
            id="ts-mahalakshmi-02",
            name="Mahalakshmi Scheme (Free Bus Travel & Financial Aid for Women)",
            department="Transport Department & Women Development & Child Welfare, Govt. of Telangana",
            category_type="Women Empowerment",
            state="Telangana",
            description="Empowers women, girls, and transgender persons in Telangana with 100% free bus travel across TSRTC buses, and provides ₹2,500/month financial aid to eligible women heads of families.",
            benefit="100% Free Travel in TSRTC Express & Palle Velugu buses + ₹2,500/month financial aid",
            official_portal_url="https://telangana.gov.in",
            documents=[
                "Telangana Domicile Aadhaar Card with residential address",
                "Food Security Card (FSC) / White Ration Card",
                "Active Bank Account seeded with Aadhaar (for monthly financial aid)",
                "Recent Passport-size Photograph"
            ],
            rules=[
                Rule("gender", "==", "Female", "Targeted for girls, women, and female heads of household"),
                Rule("category", "in", ["General", "OBC", "BC", "SC", "ST", "EWS"], "Open to all women residents of Telangana")
            ],
            priority_weight=98
        ),

        Scheme(
            id="ts-aarogyasri-03",
            name="Rajiv Aarogyasri Telangana (Universal Health Coverage)",
            department="Aarogyasri Health Care Trust, Government of Telangana",
            category_type="Healthcare",
            state="Telangana",
            description="Comprehensive cashless healthcare scheme protecting poor and low-income families from catastrophic health expenditures across 1,672 treatments in network hospitals.",
            benefit="Cashless medical hospitalization and surgery cover up to ₹10,00,000 per family per year",
            official_portal_url="https://aarogyasri.telangana.gov.in",
            documents=[
                "Telangana Food Security Card (White Ration Card) / Aarogyasri Card",
                "Aadhaar Card of patient and family members",
                "Emergency / Outpatient consultation memo from Network Hospital"
            ],
            rules=[
                Rule("income", "<=", 500000, "Annual family income within ₹5 Lakh threshold"),
                Rule("category", "in", ["General", "OBC", "BC", "SC", "ST", "EWS"], "Open to all residents holding Food Security Cards")
            ],
            priority_weight=95
        ),

        Scheme(
            id="ts-rythu-04",
            name="Rythu Bharosa / Rythu Bandhu (Farmer Investment Support)",
            department="Department of Agriculture & Farmers Welfare, Govt. of Telangana",
            category_type="Agriculture",
            state="Telangana",
            description="Pioneering investment support providing financial grants per acre directly into farmers' bank accounts for purchasing agricultural inputs like seeds, fertilizer, and plowing.",
            benefit="₹12,000 to ₹15,000 per acre per year direct benefit transfer for two agricultural seasons",
            official_portal_url="https://rythubandhu.telangana.gov.in",
            documents=[
                "Dharani Digital Pattadar Passbook / Land Title record",
                "Farmer Aadhaar Card",
                "Bank Account seeded with Aadhaar NPCI",
                "Crop Sowing declaration"
            ],
            rules=[
                Rule("is_farmer", "==", True, "Must own agricultural land recorded in Dharani portal", is_mandatory=False),
                Rule("income", "<=", 500000, "Eligible agricultural landholders in Telangana")
            ],
            priority_weight=88
        ),

        Scheme(
            id="ts-kalyana-05",
            name="Kalyana Lakshmi & Shaadi Mubarak Scheme",
            department="Scheduled Castes Development & BC Welfare Dept., Govt. of Telangana",
            category_type="Social Welfare",
            state="Telangana",
            description="Provides one-time financial assistance to unmarried brides aged 18+ from underprivileged families to prevent child marriage and alleviate marriage distress.",
            benefit="One-time direct financial grant of ₹1,00,116 credited to the bride's mother's account",
            official_portal_url="https://telanganaepass.cgg.gov.in",
            documents=[
                "Bride & Groom Age Proof / SSC Certificate (Bride must be ≥ 18 years)",
                "Marriage Invitation Card / Marriage Registration Receipt",
                "Tahsildar Income Certificate (≤ ₹2,00,000/annum)",
                "Meeseva Caste Certificate (SC/ST/BC/Minority)",
                "Bride & Mother's Aadhaar Cards and Joint Bank Passbook"
            ],
            rules=[
                Rule("gender", "==", "Female", "Beneficiary is an unmarried bride aged 18+"),
                Rule("income", "<=", 200000, "Annual family income does not exceed ₹2 Lakh limit"),
                Rule("category", "in", ["SC", "ST", "BC", "OBC", "Minority", "EBC"], "Reserved for backward and economically weaker communities")
            ],
            priority_weight=91
        ),

        Scheme(
            id="ts-overseas-06",
            name="Telangana Overseas Vidya Nidhi Scholarship",
            department="Welfare of Scheduled Castes, BC & Minority Dept., Govt. of Telangana",
            category_type="Education",
            state="Telangana",
            description="Offers substantial financial grants to meritorious SC, ST, BC, and Minority students to pursue Post Graduate (MS/MBA/PhD) studies in world-class foreign universities.",
            benefit="Scholarship grant up to ₹20,00,000 plus one-way economy airfare and visa fees",
            official_portal_url="https://telanganaepass.cgg.gov.in",
            documents=[
                "Valid Indian Passport & Foreign University I-20 / Admission Letter (USA/UK/Australia/Canada/Germany)",
                "GRE / GMAT and TOEFL / IELTS Scorecard",
                "Degree Consolidated Marks Memo with minimum 60% marks",
                "Meeseva Caste & Income Certificate (≤ ₹5.0 Lakh/annum)",
                "Student Bank Account Details"
            ],
            rules=[
                Rule("income", "<=", 500000, "Family income does not exceed ₹5 Lakh per annum"),
                Rule("marks", ">=", 60, "Undergraduate marks meet minimum 60% requirement"),
                Rule("course_level", "in", ["PG", "PhD", "Postgraduate"], "Enrolled in foreign Postgraduate / Doctorate program"),
                Rule("category", "in", ["SC", "ST", "BC", "OBC", "Minority"], "Applicant belongs to notified affirmative action category")
            ],
            priority_weight=94
        ),

        # =========================================================================
        # 🔴 TAMIL NADU STATE SCHEMES
        # =========================================================================
        Scheme(
            id="tn-pudhumai-01",
            name="Moovalur Ramamirtham Ammaiyar Pudhumai Penn Scheme",
            department="Social Welfare & Women Empowerment Dept., Government of Tamil Nadu",
            category_type="Women Empowerment",
            state="Tamil Nadu",
            description="Incentivizes female education by providing ₹1,000 monthly cash assistance to girls who studied in Tamil Nadu Government schools from Class 6 to 12 upon entering higher education.",
            benefit="₹1,000 per month deposited directly into student's bank account until degree completion",
            official_portal_url="https://pudhumaipenn.tn.gov.in",
            documents=[
                "Tamil Nadu Domicile / Nativity Certificate",
                "Government School Study Certificate (Class 6th to 12th in TN Govt School)",
                "College Admission Card / Bonafide Certificate",
                "Aadhaar Card",
                "Student's individual Bank Passbook copy"
            ],
            rules=[
                Rule("gender", "==", "Female", "Applicable for female students"),
                Rule("course_level", "in", ["UG", "Diploma", "B.Tech", "Degree", "Engineering", "Medicine"], "Pursuing Undergraduate degree or Polytechnic Diploma"),
                Rule("is_govt_school", "==", True, "Studied Class 6 to 12 in Tamil Nadu Government Schools", is_mandatory=False)
            ],
            priority_weight=98
        ),

        Scheme(
            id="tn-first-grad-02",
            name="Tamil Nadu First Graduate (FG) Tuition Fee Concession",
            department="Directorate of Technical Education (DoTE), Tamil Nadu",
            category_type="Education",
            state="Tamil Nadu",
            description="Complete waiver of tuition fees for students who are the first person in their entire immediate family to pursue an undergraduate professional degree.",
            benefit="Complete Tuition Fee Waiver (up to ₹25,000 - ₹50,000 per year throughout the course)",
            official_portal_url="https://www.tndte.gov.in",
            documents=[
                "First Graduate Certificate issued by Headquarter Deputy Tahsildar",
                "Joint Declaration signed by Parent and Student",
                "No Graduate in Family Verification from Village Administrative Officer (VAO)",
                "Ration Card / Smart Family Card copy",
                "Allotment Order from Single Window Counseling (TNEA)"
            ],
            rules=[
                Rule("is_first_graduate", "==", True, "Must be the verified first graduate in the entire family"),
                Rule("course_level", "in", ["UG", "B.Tech", "Engineering", "Degree", "Medicine"], "Enrolled in First Year Undergraduate Professional Course")
            ],
            priority_weight=96
        ),

        Scheme(
            id="tn-kmut-03",
            name="Kalaignar Magalir Urimai Thittam (KMUT - Monthly Basic Income for Women)",
            department="Special Programme Implementation Dept., Government of Tamil Nadu",
            category_type="Women Empowerment",
            state="Tamil Nadu",
            description="Flagship universal basic income initiative acknowledging women's unpaid household labor by providing ₹1,000 monthly rights grant to women heads of families.",
            benefit="Direct monthly bank deposit of ₹1,000 (₹12,000 per year) directly to women heads of family",
            official_portal_url="https://kmut.tn.gov.in",
            documents=[
                "Tamil Nadu Smart Family Card (Ration Card) with woman as Head of Family",
                "Aadhaar Card",
                "Electricity Consumer Number (Annual usage below 3,600 units)",
                "Bank Account Passbook seeded with Aadhaar NPCI"
            ],
            rules=[
                Rule("gender", "==", "Female", "Recipient must be a female head of household"),
                Rule("income", "<=", 250000, "Annual family income is less than ₹2.5 Lakh"),
                Rule("category", "in", ["General", "OBC", "BC", "MBC", "SC", "ST", "EWS"], "Open to all women meeting economic and electricity consumption criteria")
            ],
            priority_weight=95
        ),

        Scheme(
            id="tn-cmchis-04",
            name="Chief Minister's Comprehensive Health Insurance Scheme (CMCHIS)",
            department="Health & Family Welfare Department, Government of Tamil Nadu",
            category_type="Healthcare",
            state="Tamil Nadu",
            description="Pioneering public health insurance providing cashless medical and surgical care for 1,090 notified therapy procedures across government and empanelled private hospitals.",
            benefit="Cashless hospitalization cover up to ₹5,00,000 per family per year",
            official_portal_url="https://www.cmchistn.com",
            documents=[
                "Tamil Nadu Smart Family Card / Ration Card",
                "Income Certificate from Revenue Authority (≤ ₹1.2 Lakh/yr) or Smart Card",
                "Aadhaar Cards of all enrolled family members"
            ],
            rules=[
                Rule("income", "<=", 120000, "Annual family income does not exceed ₹1,20,000 ceiling"),
                Rule("category", "in", ["General", "OBC", "BC", "MBC", "SC", "ST", "EWS"], "Open to all low-income residents of Tamil Nadu")
            ],
            priority_weight=92
        ),

        Scheme(
            id="tn-govt-school-quota-05",
            name="7.5% Preferential Reservation & 100% Fee Waiver for Govt School Students",
            department="Directorate of Technical Education (DoTE) & Health Dept, Govt. of Tamil Nadu",
            category_type="Education",
            state="Tamil Nadu",
            description="Provides 7.5% preferential horizontal reservation and 100% complete waiver of tuition fees, hostel fees, and counseling fees for engineering and medical seats for government school students.",
            benefit="100% Free Higher Education: Zero Tuition fee, Zero Hostel fee, Zero Mess charges",
            official_portal_url="https://www.tneaonline.org",
            documents=[
                "Tamil Nadu Government School Study Certificate (Class 6th to 12th verified on EMIS)",
                "TNEA / TN Medical Counseling Allotment Order under 7.5% Quota",
                "Community Certificate (BC/MBC/SC/ST)",
                "Class 10th and 12th Marksheets",
                "Aadhaar Card"
            ],
            rules=[
                Rule("is_govt_school", "==", True, "Must have studied continuously in TN Govt schools from 6th to 12th"),
                Rule("course_level", "in", ["UG", "B.Tech", "Engineering", "Medicine", "Agriculture"], "Pursuing professional Undergraduate degree via counseling")
            ],
            priority_weight=97
        ),

        Scheme(
            id="tn-free-laptop-06",
            name="Tamil Nadu Free Laptop Scheme for Higher Secondary & College Students",
            department="Special Programme Implementation & School Education Dept., Govt. of Tamil Nadu",
            category_type="Education",
            state="Tamil Nadu",
            description="Distributes free state-of-the-art laptops with licensed OS and software to students completing Class 12 in government and government-aided schools entering college.",
            benefit="Free high-speed Laptop pre-loaded with educational software & operating system",
            official_portal_url="https://elcot.in",
            documents=[
                "Class 12th Passing Marksheet from TN State Board (Govt/Aided School)",
                "School Leaving Transfer Certificate (TC)",
                "School / College Student ID Card",
                "Aadhaar Card"
            ],
            rules=[
                Rule("course_level", "in", ["Class 12", "Diploma", "UG", "Degree"], "Passed Class 12 or enrolled in college/polytechnic"),
                Rule("category", "in", ["General", "OBC", "BC", "MBC", "SC", "ST", "EWS"], "Open to all students of Tamil Nadu Government and Aided institutions")
            ],
            priority_weight=87
        ),

        # =========================================================================
        # 🇮🇳 CENTRAL / ALL-INDIA SCHEMES
        # =========================================================================
        Scheme(
            id="central-csss-01",
            name="Central Sector Scheme of Scholarship for College & University Students",
            department="Department of Higher Education, Ministry of Education, Govt. of India",
            category_type="Education",
            state="All India",
            description="Provides financial assistance to meritorious students from low-income families across all states to meet day-to-day expenses while pursuing graduation and post-graduation.",
            benefit="₹12,000/year for first 3 years of UG; ₹20,000/year for PG degree",
            official_portal_url="https://scholarships.gov.in",
            documents=[
                "Aadhaar Card (linked with bank account)",
                "Income Certificate (Issued by competent Revenue Authority)",
                "Class 12th Board Marksheet (Top 20th percentile)",
                "College Admission Bonafide / Enrollment Certificate",
                "Bank Account Passbook (DBT enabled)",
                "Recent Passport-size Photograph"
            ],
            rules=[
                Rule("income", "<=", 450000, "Annual family income is within ₹4.5 Lakh ceiling"),
                Rule("marks", ">=", 80, "Class 12 board marks meet 80% percentile threshold"),
                Rule("course_level", "in", ["UG", "PG", "Degree", "B.Tech", "Engineering"], "Enrolled in regular Undergraduate or Postgraduate degree"),
                Rule("category", "in", ["General", "OBC", "BC", "SC", "ST", "EWS"], "All social categories are eligible")
            ],
            priority_weight=95
        ),

        Scheme(
            id="central-pragati-02",
            name="AICTE Pragati Scholarship Scheme for Girl Students (Technical Degree)",
            department="All India Council for Technical Education (AICTE), Ministry of Education",
            category_type="Women Empowerment",
            state="All India",
            description="Assists female students pursuing technical education (B.Tech, Pharmacy, Architecture, Diploma) in AICTE-approved institutions across India.",
            benefit="₹50,000 per annum for every year of study towards college tuition and equipment",
            official_portal_url="https://www.aicte-india.org/schemes/students-development-schemes/pragati",
            documents=[
                "Aadhaar Card",
                "Family Income Certificate (below ₹8 Lakh per annum)",
                "Class 10th and 12th Marksheets",
                "Admission Letter to 1st year Degree/Diploma (AICTE approved institute)",
                "Tuition Fee Receipt for current academic year",
                "Bank Account Passbook in applicant's name",
                "Declaration by Parents confirming maximum two girls per family"
            ],
            rules=[
                Rule("gender", "==", "Female", "Exclusively designed for female students"),
                Rule("income", "<=", 800000, "Family income is within ₹8 Lakh per annum"),
                Rule("course_level", "in", ["UG", "Diploma", "B.Tech", "Engineering"], "Pursuing technical degree or diploma course"),
                Rule("marks", ">=", 60, "Qualifying board examination score satisfies minimum 60%")
            ],
            priority_weight=98
        ),

        Scheme(
            id="central-post-matric-sc-03",
            name="Post-Matric Scholarship for Scheduled Caste (SC) Students",
            department="Ministry of Social Justice and Empowerment, Govt. of India",
            category_type="Education",
            state="All India",
            description="Supports Scheduled Caste students studying at post-secondary and higher education levels with full compulsory non-refundable fees and academic maintenance allowance.",
            benefit="100% Tuition Fee Reimbursement + up to ₹13,500/year living maintenance allowance",
            official_portal_url="https://scholarships.gov.in",
            documents=[
                "Permanent Community / Caste Certificate (SC)",
                "Income Certificate (not exceeding ₹2.5 Lakh/annum)",
                "Previous Year Academic Marksheet / Passing Certificate",
                "Fee Receipt of current academic institution",
                "Aadhaar Card linked to active Bank Account",
                "Hostel Stay Certificate (if residential scholar)"
            ],
            rules=[
                Rule("category", "==", "SC", "Applicant belongs to Scheduled Caste (SC)"),
                Rule("income", "<=", 250000, "Annual family income does not exceed ₹2,50,000"),
                Rule("course_level", "in", ["Class 11", "Class 12", "UG", "PG", "Diploma", "B.Tech", "PhD"], "Studying in Post-Matric or Higher Education")
            ],
            priority_weight=94
        ),

        Scheme(
            id="central-pmjay-04",
            name="Ayushman Bharat - Pradhan Mantri Jan Arogya Yojana (PM-JAY)",
            department="National Health Authority (NHA), Ministry of Health & Family Welfare",
            category_type="Healthcare",
            state="All India",
            description="The world's largest health assurance scheme providing secondary and tertiary care hospitalization across public and empanelled private hospitals nationwide.",
            benefit="Cashless health insurance cover up to ₹5,00,000 per family per year",
            official_portal_url="https://pmjay.gov.in",
            documents=[
                "Aadhaar Card of all family members",
                "Ration Card / BPL Card / SECC 2011 Household ID",
                "Income Certificate or Proof of Deprivation category",
                "Active Mobile Number linked to Aadhaar"
            ],
            rules=[
                Rule("income", "<=", 300000, "Economically weaker or low-income household (≤ ₹3.0L)"),
                Rule("category", "in", ["General", "OBC", "BC", "SC", "ST", "EWS"], "Open to all categories meeting socioeconomic criteria")
            ],
            priority_weight=91
        ),

        Scheme(
            id="central-pmkisan-05",
            name="Pradhan Mantri Kisan Samman Nidhi (PM-KISAN)",
            department="Department of Agriculture and Farmers Welfare, Govt. of India",
            category_type="Agriculture",
            state="All India",
            description="Income support scheme providing direct financial transfers to all landholding farmer families across India for purchasing agricultural inputs.",
            benefit="₹6,000 per year paid in three equal four-monthly installments of ₹2,000 directly to bank accounts",
            official_portal_url="https://pmkisan.gov.in",
            documents=[
                "Land Ownership Record / Patta / Chitta / RoR copy",
                "Aadhaar Card",
                "Bank Account Passbook with Aadhaar NPCI seeding",
                "Kisan Credit Card (if available)"
            ],
            rules=[
                Rule("is_farmer", "==", True, "Must be an active landholder agricultural family", is_mandatory=False),
                Rule("income", "<=", 400000, "Small and marginal farming household income bracket")
            ],
            priority_weight=85
        )
    ]
    return schemes
