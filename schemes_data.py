"""
Scheme & Document Database for Scheme Finder.
Comprehensive registry of verified Central & State Government Welfare and Scholarship programs
across all Indian States (Andhra Pradesh, Telangana, Tamil Nadu, Karnataka, Maharashtra,
Uttar Pradesh, West Bengal, Kerala, Bihar, Rajasthan, Gujarat, Madhya Pradesh, Delhi,
Punjab, Odisha, Assam, Haryana) and Pan-India / Central Government.
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
        # 🟡 KARNATAKA STATE SCHEMES
        # =========================================================================
        Scheme(
            id="ka-gruha-01",
            name="Gruha Lakshmi Scheme (Monthly Basic Income for Women)",
            department="Women & Child Development Department, Government of Karnataka",
            category_type="Women Empowerment",
            state="Karnataka",
            description="Flagship welfare guarantee providing ₹2,000 monthly cash transfers directly into the bank accounts of women heads of households in Karnataka.",
            benefit="₹2,000 per month (₹24,000/year) direct benefit transfer to women heads of family",
            official_portal_url="https://sevasindhu.karnataka.gov.in",
            documents=[
                "Antyodaya, BPL, or APL Ration Card with woman as Head of Household",
                "Aadhaar Card linked to Bank Account (NPCI enabled)",
                "Husband's Aadhaar Card (if married)"
            ],
            rules=[
                Rule("gender", "==", "Female", "Applicant must be a female head of family"),
                Rule("income", "<=", 400000, "Eligible families without GST/Income Tax filings")
            ],
            priority_weight=98
        ),

        Scheme(
            id="ka-yuva-02",
            name="Yuva Nidhi Scheme (Unemployment Allowance for Graduates)",
            department="Skill Development, Entrepreneurship and Livelihood Dept, Govt. of Karnataka",
            category_type="Social Welfare",
            state="Karnataka",
            description="Provides monthly financial assistance to unemployed degree and diploma holders who graduated in Karnataka to support their job search and skill development.",
            benefit="₹3,000/month for degree graduates; ₹1,500/month for diploma holders for up to 2 years",
            official_portal_url="https://sevasindhuservices.karnataka.gov.in",
            documents=[
                "Degree or Diploma Marks Card / Passing Certificate from Karnataka University",
                "Aadhaar Card linked to Bank Account",
                "Domicile / Study Certificate proving Karnataka residence for ≥ 6 years",
                "Declaration of unemployment / not enrolled in higher education"
            ],
            rules=[
                Rule("course_level", "in", ["UG", "Degree", "Diploma", "B.Tech", "PG"], "Completed Graduation Degree or Diploma course"),
                Rule("income", "<=", 500000, "Unemployed youth seeking career placement")
            ],
            priority_weight=94
        ),

        Scheme(
            id="ka-ssp-03",
            name="Karnataka State Scholarship Portal (SSP Post-Matric)",
            department="Social Welfare & Backward Classes Welfare Dept, Government of Karnataka",
            category_type="Education",
            state="Karnataka",
            description="Single unified scholarship portal offering full tuition fee reimbursement and academic maintenance to SC, ST, OBC, and EBC students in Karnataka.",
            benefit="100% Tuition Fee Concession + Monthly Student Maintenance Allowance",
            official_portal_url="https://ssp.postmatric.karnataka.gov.in",
            documents=[
                "Student & Parent Aadhaar Cards",
                "Revenue RD Caste & Income Certificate (from Seva Sindhu / Nadakacheri)",
                "College Registration Number / Admission Acknowledgement",
                "Hostel E-Attestation Number (if residential student)"
            ],
            rules=[
                Rule("income", "<=", 250000, "Family income within ₹2.5 Lakh limit (₹1.5 Lakh for Cat-1 OBC)"),
                Rule("course_level", "in", ["UG", "PG", "Diploma", "B.Tech", "Degree", "Medicine"], "Enrolled in recognized Post-Matric Degree or Diploma")
            ],
            priority_weight=96
        ),

        Scheme(
            id="ka-raitha-04",
            name="Raitha Vidya Nidhi Scholarship (Farmer Children Education Grant)",
            department="Department of Agriculture, Government of Karnataka",
            category_type="Education",
            state="Karnataka",
            description="Encourages children of farmers to pursue higher education by providing direct annual scholarship grants ranging from ₹2,500 to ₹11,000 per year.",
            benefit="Annual scholarship of ₹2,500 to ₹11,000 directly credited via DBT to student accounts",
            official_portal_url="https://ssp.karnataka.gov.in",
            documents=[
                "Farmer ID (FID) of Parent registered in FRUITS portal",
                "Student Aadhaar Card & College Bonafide",
                "Bank Account seeded with NPCI Aadhaar"
            ],
            rules=[
                Rule("is_farmer", "==", True, "Parent must be a registered agricultural farmer in FRUITS database", is_mandatory=False),
                Rule("course_level", "in", ["Class 11", "Class 12", "UG", "PG", "Diploma", "B.Tech"], "Enrolled in Post-Matric or Higher Education")
            ],
            priority_weight=89
        ),

        # =========================================================================
        # 🟠 MAHARASHTRA STATE SCHEMES
        # =========================================================================
        Scheme(
            id="mh-ladki-01",
            name="Mukhyamantri Majhi Ladki Bahin Yojana",
            department="Women and Child Development Department, Government of Maharashtra",
            category_type="Women Empowerment",
            state="Maharashtra",
            description="Flagship financial independence initiative providing ₹1,500 monthly cash aid to married, widowed, divorced, and destitute women aged 21 to 65 years.",
            benefit="₹1,500 per month (₹18,000/year) direct bank transfer to women beneficiaries",
            official_portal_url="https://ladkibahin.maharashtra.gov.in",
            documents=[
                "Maharashtra Domicile Certificate or Ration Card issued before 15 years",
                "Aadhaar Card linked to Bank Account (DBT active)",
                "Yellow or Orange Ration Card / Income Certificate (≤ ₹2.5 Lakh/yr)"
            ],
            rules=[
                Rule("gender", "==", "Female", "Exclusively designed for women aged 21-65 years"),
                Rule("income", "<=", 250000, "Annual family income does not exceed ₹2,50,000")
            ],
            priority_weight=98
        ),

        Scheme(
            id="mh-mahadbt-02",
            name="Rajarshi Chhatrapati Shahu Maharaj Shikshan Shulkh Shishyavrutti (MahaDBT)",
            department="Directorate of Higher Education (DHE) & DTE, Govt. of Maharashtra",
            category_type="Education",
            state="Maharashtra",
            description="Provides 50% to 100% reimbursement of tuition and examination fees to economically backward class (EBC) and open category students in Maharashtra.",
            benefit="50% to 100% Tuition Fee & Exam Fee Waiver across professional college courses",
            official_portal_url="https://mahadbt.maharashtra.gov.in",
            documents=[
                "Maharashtra Domicile Certificate",
                "Tahsildar Income Certificate (Family income ≤ ₹8.0 Lakh/year)",
                "CAP Allotment Letter for professional engineering, degree, or medical seats",
                "Previous Year Marksheet (minimum 50% marks)"
            ],
            rules=[
                Rule("income", "<=", 800000, "Annual family income is within ₹8 Lakh ceiling"),
                Rule("marks", ">=", 50, "Passing score satisfies minimum 50% requirement"),
                Rule("course_level", "in", ["UG", "PG", "Diploma", "B.Tech", "Engineering", "Medicine"], "Enrolled through CAP counseling in approved college")
            ],
            priority_weight=95
        ),

        Scheme(
            id="mh-mjpjay-03",
            name="Mahatma Jyotirao Phule Jan Arogya Yojana (MJPJAY)",
            department="Public Health Department, Government of Maharashtra",
            category_type="Healthcare",
            state="Maharashtra",
            description="Universal health insurance scheme for all citizens of Maharashtra providing cashless secondary and tertiary hospitalization across 996 medical procedures.",
            benefit="100% Cashless medical treatment cover up to ₹5,00,000 per family per year",
            official_portal_url="https://www.jeevandayee.gov.in",
            documents=[
                "Maharashtra Ration Card (Yellow, Orange, or White) / Domicile Certificate",
                "Aadhaar Card of all family members",
                "Referral from Network Empanelled Hospital"
            ],
            rules=[
                Rule("category", "in", ["General", "OBC", "BC", "SC", "ST", "EWS"], "Open to all residents of Maharashtra holding valid Ration Card")
            ],
            priority_weight=93
        ),

        Scheme(
            id="mh-namo-04",
            name="Namo Shetkari Mahasanman Nidhi Yojana",
            department="Department of Agriculture, Government of Maharashtra",
            category_type="Agriculture",
            state="Maharashtra",
            description="Provides an additional top-up grant of ₹6,000/year to all PM-KISAN eligible farmers in Maharashtra, bringing total farmer aid to ₹12,000 per year.",
            benefit="₹6,000 per year paid in three equal installments of ₹2,000 alongside PM-KISAN",
            official_portal_url="https://krishi.maharashtra.gov.in",
            documents=[
                "7/12 Land Utara & 8-A Extract showing agricultural landholding",
                "Aadhaar Card linked to Bank Account with NPCI approval",
                "Active PM-KISAN Beneficiary ID"
            ],
            rules=[
                Rule("is_farmer", "==", True, "Must be an active landholding farmer in Maharashtra", is_mandatory=False),
                Rule("income", "<=", 400000, "Small and marginal farmer income bracket")
            ],
            priority_weight=88
        ),

        # =========================================================================
        # 🟢 UTTAR PRADESH STATE SCHEMES
        # =========================================================================
        Scheme(
            id="up-scholarship-01",
            name="UP Post-Matric Scholarship & Fee Reimbursement Scheme (Saksham UP)",
            department="Social Welfare & Backward Classes Welfare Dept, Government of Uttar Pradesh",
            category_type="Education",
            state="Uttar Pradesh",
            description="Comprehensive scholarship and non-refundable fee reimbursement for UP students studying in Class 11, 12, Degree, Engineering, and Medical programs.",
            benefit="100% Tuition Fee Reimbursement + Monthly Living Allowance up to ₹10,000/yr",
            official_portal_url="https://scholarship.up.gov.in",
            documents=[
                "UP Domicile / Niwas Praman Patra",
                "Tahsildar Income Certificate (≤ ₹2.5 Lakh for SC/ST; ≤ ₹2.0 Lakh for General/OBC/Minority)",
                "Caste Certificate (Jati Praman Patra)",
                "Previous Academic Marksheet & Fee Receipt"
            ],
            rules=[
                Rule("income", "<=", 250000, "Family income does not exceed ₹2.5 Lakh for SC/ST or ₹2 Lakh for others"),
                Rule("course_level", "in", ["Class 11", "Class 12", "UG", "PG", "Diploma", "B.Tech", "Degree"], "Pursuing Post-Matriculation education")
            ],
            priority_weight=97
        ),

        Scheme(
            id="up-kanya-02",
            name="Mukhyamantri Kanya Sumangala Yojana",
            department="Women & Child Development Department, Government of Uttar Pradesh",
            category_type="Women Empowerment",
            state="Uttar Pradesh",
            description="Offers ₹25,000 conditional cash assistance to girl children in UP across 6 educational and developmental stages from birth to college graduation.",
            benefit="Total ₹25,000 financial assistance deposited in stages until college admission",
            official_portal_url="https://mksy.up.gov.in",
            documents=[
                "UP Domicile Certificate of Parent",
                "Income Certificate (Family income below ₹3.0 Lakh/annum)",
                "Girl Child Birth Certificate & Immunization Card",
                "School / College Admission Verification Slip"
            ],
            rules=[
                Rule("gender", "==", "Female", "Targeted exclusively for girl children and female students"),
                Rule("income", "<=", 300000, "Family annual income is within ₹3 Lakh limit")
            ],
            priority_weight=94
        ),

        Scheme(
            id="up-abhyudaya-03",
            name="Mukhyamantri Abhyudaya Yojana (Free Competitive Exam Coaching)",
            department="Social Welfare Department, Government of Uttar Pradesh",
            category_type="Education",
            state="Uttar Pradesh",
            description="Free offline and online mentoring, physical study centers, and tablet assistance to prepare students for UPSC, UPPSC, JEE, NEET, NDA, and CDS exams.",
            benefit="Free high-quality coaching by IAS/IPS officers and subject experts + Free Tablet",
            official_portal_url="https://abhyuday.up.gov.in",
            documents=[
                "UP Domicile Certificate",
                "Graduation or 10+2 Marksheet",
                "Aadhaar Card",
                "Abhyudaya Entrance Exam Online Admit Card"
            ],
            rules=[
                Rule("course_level", "in", ["Class 12", "UG", "PG", "Degree"], "Completed Class 12 or pursuing graduation degree"),
                Rule("income", "<=", 400000, "Economically weaker and aspiring students of UP")
            ],
            priority_weight=92
        ),

        # =========================================================================
        # 🟣 WEST BENGAL STATE SCHEMES
        # =========================================================================
        Scheme(
            id="wb-kanyashree-01",
            name="Kanyashree Prakalpa (UN Award-Winning Girl Child Empowerment)",
            department="Department of Women & Child Development and Social Welfare, Govt. of West Bengal",
            category_type="Women Empowerment",
            state="West Bengal",
            description="Flagship UN Public Service First Prize initiative preventing child marriage and promoting education of adolescent girls through annual and one-time grants.",
            benefit="Annual scholarship of ₹1,000 (K1) and One-time cash grant of ₹25,000 (K2) at age 18",
            official_portal_url="https://www.wbkanyashree.gov.in",
            documents=[
                "West Bengal Resident Certificate",
                "Birth Certificate of Girl Child (Age 13 to 19 years)",
                "School / College Bonafide Certificate",
                "Unmarried Status Declaration signed by Parent",
                "Bank Account Passbook in applicant's sole name"
            ],
            rules=[
                Rule("gender", "==", "Female", "Exclusively designed for unmarried girl students"),
                Rule("income", "<=", 200000, "Family income does not exceed ₹1,20,000 (waived for orphans & PwD)"),
                Rule("course_level", "in", ["Class 10", "Class 12", "UG", "Diploma", "Degree"], "Enrolled in regular school, college, or university")
            ],
            priority_weight=99
        ),

        Scheme(
            id="wb-svmcm-02",
            name="Swami Vivekananda Merit-cum-Means Scholarship (SVMCM)",
            department="Higher Education Department, Government of West Bengal",
            category_type="Education",
            state="West Bengal",
            description="Generous merit scholarship providing financial assistance up to ₹60,000 per year to meritorious students from economically weaker families in West Bengal.",
            benefit="₹12,000 to ₹60,000 per year based on course level directly credited to student's account",
            official_portal_url="https://svmcm.wbhed.gov.in",
            documents=[
                "West Bengal Domicile Certificate",
                "Madhyamik (Class 10) or Higher Secondary Marksheet with minimum 60% marks",
                "Family Income Certificate issued by Joint BDO / Executive Officer (≤ ₹2.5 Lakh/yr)",
                "College Admission Fee Receipt"
            ],
            rules=[
                Rule("marks", ">=", 60, "Satisfies minimum 60% score in qualifying board examination"),
                Rule("income", "<=", 250000, "Family income is within ₹2.5 Lakh per annum"),
                Rule("course_level", "in", ["Class 11", "Class 12", "UG", "PG", "Diploma", "B.Tech", "PhD"], "Studying in higher secondary, college, or doctorate level")
            ],
            priority_weight=97
        ),

        Scheme(
            id="wb-lakshmir-03",
            name="Lakshmir Bhandar (Basic Monthly Income for Women)",
            department="Department of Women & Child Development, Government of West Bengal",
            category_type="Women Empowerment",
            state="West Bengal",
            description="Provides assured monthly basic income grant of ₹1,000 to ₹1,200 to all female heads of families aged 25 to 60 years in West Bengal.",
            benefit="₹1,200/month for SC/ST women; ₹1,000/month for General & OBC women (₹12,000-₹14,400/yr)",
            official_portal_url="https://socialwelfare.wb.gov.in",
            documents=[
                "Swasthya Sathi Card",
                "Aadhaar Card",
                "SC / ST Certificate (for ₹1,200/mo enhanced benefit)",
                "Bank Account Passbook"
            ],
            rules=[
                Rule("gender", "==", "Female", "Targeted for female family heads aged 25-60 years"),
                Rule("category", "in", ["General", "OBC", "SC", "ST", "EWS"], "Open to all women meeting age criteria")
            ],
            priority_weight=96
        ),

        Scheme(
            id="wb-swasthya-04",
            name="Swasthya Sathi Scheme (Universal Cashless Health Cover)",
            department="Department of Health & Family Welfare, Government of West Bengal",
            category_type="Healthcare",
            state="West Bengal",
            description="Pioneering universal health insurance providing cashless medical care for secondary and tertiary hospitalization issued in the name of the female head of family.",
            benefit="100% Cashless treatment cover up to ₹5,00,000 per family per year",
            official_portal_url="https://swasthyasathi.gov.in",
            documents=[
                "Swasthya Sathi Smart Card",
                "Aadhaar Cards of all enrolled household members"
            ],
            rules=[
                Rule("category", "in", ["General", "OBC", "SC", "ST", "EWS"], "Universal scheme covering all residents of West Bengal")
            ],
            priority_weight=93
        ),

        # =========================================================================
        # 🌴 KERALA STATE SCHEMES
        # =========================================================================
        Scheme(
            id="kl-kasp-01",
            name="Karunya Arogya Suraksha Padhathi (KASP Health Assurance)",
            department="State Health Agency (SHA), Health & Family Welfare Dept, Govt. of Kerala",
            category_type="Healthcare",
            state="Kerala",
            description="Comprehensive cashless healthcare assurance scheme providing high-quality secondary and tertiary medical treatment in empanelled network hospitals.",
            benefit="Cashless hospitalization cover up to ₹5,00,000 per family per year",
            official_portal_url="https://sha.kerala.gov.in",
            documents=[
                "Kerala BPL / Priority Ration Card",
                "Aadhaar Card of all family members",
                "Treatment referral from Network Hospital"
            ],
            rules=[
                Rule("income", "<=", 300000, "Economically weaker or BPL household income bracket"),
                Rule("category", "in", ["General", "OBC", "SC", "ST", "EWS"], "Eligible category for KASP healthcare benefits")
            ],
            priority_weight=95
        ),

        Scheme(
            id="kl-egrantz-02",
            name="E-Grantz 3.0 Post-Matric Educational Assistance",
            department="Scheduled Castes Development & Backward Classes Welfare Dept, Govt. of Kerala",
            category_type="Education",
            state="Kerala",
            description="Direct benefit educational support for SC, ST, OEC, and socially backward students pursuing post-matric courses in recognized colleges in Kerala.",
            benefit="100% Tuition Fee Reimbursement + Pocket Money & Hostel Allowance",
            official_portal_url="https://egrantz.kerala.gov.in",
            documents=[
                "Kerala SSLC Book / Marksheet",
                "Caste & Income Certificate from Akshaya Center",
                "College Allotment Memo & Fee Receipt",
                "Aadhaar seeded Bank Passbook"
            ],
            rules=[
                Rule("income", "<=", 250000, "Annual family income does not exceed ₹2.5 Lakh limit (₹1.0 Lakh for OBC)"),
                Rule("course_level", "in", ["UG", "PG", "Diploma", "B.Tech", "Degree", "PhD"], "Enrolled in recognized Post-Matriculation course")
            ],
            priority_weight=94
        ),

        # =========================================================================
        # 🔷 BIHAR STATE SCHEMES
        # =========================================================================
        Scheme(
            id="br-kanya-01",
            name="Mukhyamantri Kanya Utthan Yojana (Graduate Incentive)",
            department="Education Department, Government of Bihar",
            category_type="Women Empowerment",
            state="Bihar",
            description="Promotes women's higher education by providing a one-time cash incentive of ₹50,000 to unmarried female students upon graduating from recognized Bihar universities.",
            benefit="One-time direct financial grant of ₹50,000 credited to student's bank account",
            official_portal_url="https://medhasoft.bih.nic.in",
            documents=[
                "Bihar Domicile Certificate",
                "Graduation Marksheet / Degree Passing Certificate",
                "Student Aadhaar Card & Bank Account in Bihar branch",
                "Unmarried Certificate / Self-Declaration"
            ],
            rules=[
                Rule("gender", "==", "Female", "Beneficiary must be an unmarried female graduate"),
                Rule("course_level", "in", ["UG", "Degree", "B.Tech", "Medicine"], "Successfully completed undergraduate degree")
            ],
            priority_weight=97
        ),

        Scheme(
            id="br-credit-02",
            name="Bihar Student Credit Card Scheme (BSCCS)",
            department="Bihar State Education Finance Corporation (BSEFC), Govt. of Bihar",
            category_type="Education",
            state="Bihar",
            description="Provides collateral-free education loans up to ₹4 Lakh at a highly subsidized 1% to 4% simple interest to pursue technical and professional degrees.",
            benefit="Collateral-free Education Loan up to ₹4,00,000 at 1% (women/disabled) or 4% interest",
            official_portal_url="https://www.7nishchay-yuvaupmission.bihar.gov.in",
            documents=[
                "Bihar Domicile Certificate",
                "Class 10th and 12th Marksheets",
                "College Admission Offer Letter & Fee Structure",
                "Co-Applicant (Parent) Aadhaar and PAN Card"
            ],
            rules=[
                Rule("course_level", "in", ["UG", "Diploma", "B.Tech", "Engineering", "Medicine", "Degree"], "Admitted to recognized higher education institution"),
                Rule("income", "<=", 600000, "Eligible youth seeking educational loan support")
            ],
            priority_weight=93
        ),

        # =========================================================================
        # 🟤 RAJASTHAN STATE SCHEMES
        # =========================================================================
        Scheme(
            id="rj-chiranjeevi-01",
            name="Mukhyamantri Ayushman Swasthya Bima (Chiranjeevi Scheme)",
            department="Medical & Health Department, Government of Rajasthan",
            category_type="Healthcare",
            state="Rajasthan",
            description="Universal healthcare initiative providing cashless hospitalization coverage for notified therapy procedures in government and empanelled private hospitals in Rajasthan.",
            benefit="Cashless medical coverage up to ₹25,00,000 per family per year",
            official_portal_url="https://chiranjeevi.rajasthan.gov.in",
            documents=[
                "Jan Aadhaar Card / Jan Aadhaar Registration Receipt",
                "Aadhaar Card of all family members",
                "Income Certificate or NFSA / SECC entitlement proof"
            ],
            rules=[
                Rule("category", "in", ["General", "OBC", "SC", "ST", "EWS"], "Open to all Jan Aadhaar cardholders in Rajasthan")
            ],
            priority_weight=96
        ),

        Scheme(
            id="rj-anuprati-02",
            name="Mukhyamantri Anuprati Coaching Yojana",
            department="Social Justice & Empowerment Department, Government of Rajasthan",
            category_type="Education",
            state="Rajasthan",
            description="Provides 100% free coaching at premier institutes along with an annual living allowance of ₹40,000 for competitive exams (UPSC, RPSC, JEE, NEET, CA, CLAT).",
            benefit="100% Free Premier Coaching + ₹40,000/year living allowance for residential students",
            official_portal_url="https://sso.rajasthan.gov.in",
            documents=[
                "Rajasthan Domicile / Jan Aadhaar Card",
                "Caste Certificate (SC/ST/OBC/MBC/EWS)",
                "Tahsildar Income Certificate (≤ ₹8.0 Lakh/annum)",
                "Class 10th and 12th Board Marksheets"
            ],
            rules=[
                Rule("income", "<=", 800000, "Annual family income within ₹8 Lakh threshold"),
                Rule("marks", ">=", 60, "Board marks meet minimum 60% requirement"),
                Rule("course_level", "in", ["Class 12", "UG", "PG", "Degree"], "Aspiring for competitive examinations")
            ],
            priority_weight=95
        ),

        # =========================================================================
        # 🦁 GUJARAT STATE SCHEMES
        # =========================================================================
        Scheme(
            id="gj-mysy-01",
            name="Mukhyamantri Yuva Swavalamban Yojana (MYSY)",
            department="Education Department, Government of Gujarat",
            category_type="Education",
            state="Gujarat",
            description="Provides 50% tuition fee assistance (up to ₹2 Lakh/year) and hostel allowances to bright students from economically weaker sections pursuing higher education in Gujarat.",
            benefit="50% Tuition Fee Reimbursement (up to ₹2,00,000/yr) + ₹12,000/yr Hostel Aid",
            official_portal_url="https://mysy.guj.nic.in",
            documents=[
                "Gujarat Domicile Certificate",
                "Class 10th or 12th Board Marksheet with ≥ 80 percentile",
                "Competent Authority Income Certificate (≤ ₹6.0 Lakh/year)",
                "Admission Letter & Fee Receipt"
            ],
            rules=[
                Rule("income", "<=", 600000, "Family income does not exceed ₹6 Lakh per annum"),
                Rule("marks", ">=", 80, "Secured minimum 80 percentile in 10th or 12th Board"),
                Rule("course_level", "in", ["UG", "Diploma", "B.Tech", "Engineering", "Medicine", "Degree"], "Enrolled in recognized undergraduate professional course")
            ],
            priority_weight=96
        ),

        # =========================================================================
        # 🐯 MADHYA PRADESH STATE SCHEMES
        # =========================================================================
        Scheme(
            id="mp-ladli-01",
            name="Mukhyamantri Ladli Behna Yojana",
            department="Women and Child Development Department, Government of Madhya Pradesh",
            category_type="Women Empowerment",
            state="Madhya Pradesh",
            description="Empowers women aged 21 to 60 years in Madhya Pradesh with direct monthly cash transfers of ₹1,250 to support their nutrition and financial independence.",
            benefit="₹1,250 per month (₹15,000/year) direct deposit into Aadhaar-linked bank accounts",
            official_portal_url="https://cmladlibehna.mp.gov.in",
            documents=[
                "Samagra Family ID & Member ID",
                "Aadhaar Card seeded with Bank Account (eKYC completed)",
                "Self-declaration confirming family land < 5 acres and income < ₹2.5 Lakh"
            ],
            rules=[
                Rule("gender", "==", "Female", "Applicable for married/widowed/divorced women aged 21-60"),
                Rule("income", "<=", 250000, "Family annual income is below ₹2.5 Lakh")
            ],
            priority_weight=97
        ),

        Scheme(
            id="mp-medhavi-02",
            name="Mukhyamantri Medhavi Chhatra Yojana (MMVY)",
            department="Department of Technical Education & Skill Development, Govt. of Madhya Pradesh",
            category_type="Education",
            state="Madhya Pradesh",
            description="The MP government pays the complete 100% tuition fees of meritorious students who score 70%+ in MP Board or 85%+ in CBSE entering IIT, NIT, Medical, or National Law colleges.",
            benefit="100% Complete Tuition Fees Paid directly to college by MP Government",
            official_portal_url="https://scholarshipportal.mp.nic.in",
            documents=[
                "MP Domicile Certificate",
                "Class 12th Marksheet (≥ 70% in MP Board or ≥ 85% in CBSE/ICSE)",
                "Family Income Certificate (≤ ₹6.0 Lakh/year)",
                "Entrance Exam Rank Card (JEE Mains, NEET, CLAT) & College Allotment"
            ],
            rules=[
                Rule("income", "<=", 600000, "Family income is within ₹6 Lakh ceiling"),
                Rule("marks", ">=", 70, "Secured minimum 70% in state board or 85% in national board"),
                Rule("course_level", "in", ["UG", "B.Tech", "Engineering", "Medicine", "Degree"], "Admitted to recognized undergraduate degree")
            ],
            priority_weight=98
        ),

        # =========================================================================
        # 🏛️ DELHI (NCT) STATE SCHEMES
        # =========================================================================
        Scheme(
            id="dl-guarantee-01",
            name="Delhi Higher Education & Skill Development Guarantee Scheme",
            department="Directorate of Training & Technical Education, Government of NCT of Delhi",
            category_type="Education",
            state="Delhi",
            description="Provides collateral-free educational loans up to ₹10 Lakh with a comprehensive credit guarantee from the Delhi Government to pursue college in Delhi.",
            benefit="Collateral-free Education Loan up to ₹10,00,000 with 1-year post-completion moratorium",
            official_portal_url="https://edistrict.delhigovt.nic.in",
            documents=[
                "Proof of completing Class 10th and 12th from Delhi schools",
                "College Admission Offer Letter & Fee Structure",
                "Student and Co-borrower (Parent) Aadhaar and PAN Card"
            ],
            rules=[
                Rule("course_level", "in", ["UG", "PG", "Diploma", "B.Tech", "Degree"], "Pursuing recognized higher education in Delhi NCR")
            ],
            priority_weight=94
        ),

        Scheme(
            id="dl-jaibhim-02",
            name="Jai Bhim Mukhyamantri Pratibha Vikas Yojana",
            department="Department for the Welfare of SC/ST/OBC/Minority, Govt. of NCT of Delhi",
            category_type="Education",
            state="Delhi",
            description="Provides 100% free coaching at top private coaching institutes in Delhi for UPSC, SSC, Banking, JEE, and NEET along with a monthly student stipend of ₹2,500.",
            benefit="100% Free Coaching Fees + ₹2,500/month stipend for study materials",
            official_portal_url="https://scstwelfare.delhigovt.nic.in",
            documents=[
                "Delhi Domicile Certificate / Delhi Ration Card",
                "Caste Certificate (SC/ST/OBC) or EWS Certificate",
                "Class 10th and 12th Passing Certificates from Delhi",
                "Tahsildar Income Certificate (≤ ₹8.0 Lakh/annum)"
            ],
            rules=[
                Rule("income", "<=", 800000, "Annual family income does not exceed ₹8 Lakh"),
                Rule("course_level", "in", ["Class 12", "UG", "PG", "Degree"], "Aspiring candidate for competitive examinations")
            ],
            priority_weight=96
        ),

        # =========================================================================
        # 🌾 PUNJAB STATE SCHEMES
        # =========================================================================
        Scheme(
            id="pb-ashirwad-01",
            name="Punjab Ashirwad Scheme (Shagun Scheme for Marriage)",
            department="Department of Social Security, Women & Child Development, Govt. of Punjab",
            category_type="Social Welfare",
            state="Punjab",
            description="Provides a one-time financial grant of ₹51,000 for the marriage of daughters belonging to SC, BC, and economically weaker families in Punjab.",
            benefit="One-time direct financial grant of ₹51,000 transferred to beneficiary's account",
            official_portal_url="https://socialsecurity.punjab.gov.in",
            documents=[
                "Punjab Domicile Certificate",
                "Caste Certificate (SC/BC) or BPL proof",
                "Bride Age Proof (≥ 18 years)",
                "Annual Family Income Certificate (≤ ₹32,790/year)",
                "Bank Account Passbook"
            ],
            rules=[
                Rule("gender", "==", "Female", "Targeted for unmarried daughters aged 18+"),
                Rule("income", "<=", 150000, "Economically weaker household income limit")
            ],
            priority_weight=91
        ),

        # =========================================================================
        # 🏖️ ODISHA STATE SCHEMES
        # =========================================================================
        Scheme(
            id="od-kalia-01",
            name="KALIA Scheme (Krushak Assistance for Livelihood & Income Augmentation)",
            department="Department of Agriculture & Farmers' Empowerment, Government of Odisha",
            category_type="Agriculture",
            state="Odisha",
            description="Comprehensive income support and livelihood package providing ₹10,000/year to small/marginal farmers and landless agricultural households in Odisha.",
            benefit="₹10,000 per year direct financial transfer (₹4,000 Kharif + ₹4,000 Rabi + ₹2,000 top-up)",
            official_portal_url="https://kalia.odisha.gov.in",
            documents=[
                "Aadhaar Card linked to Bank Account",
                "Ration Card (NFSA / SFSS)",
                "Agricultural Land record or Landless Agricultural Laborer certificate"
            ],
            rules=[
                Rule("is_farmer", "==", True, "Must be an active cultivator or landless agricultural laborer", is_mandatory=False),
                Rule("income", "<=", 300000, "Small and marginal farming household")
            ],
            priority_weight=92
        ),

        Scheme(
            id="od-bsky-02",
            name="Biju Swasthya Kalyan Yojana (BSKY Health Assurance)",
            department="Health & Family Welfare Department, Government of Odisha",
            category_type="Healthcare",
            state="Odisha",
            description="Cashless healthcare scheme covering secondary and tertiary treatments across 4,000+ empanelled hospitals, offering higher coverage for female family members.",
            benefit="Cashless hospitalization up to ₹5,00,000 for male and ₹10,00,000 for female family members",
            official_portal_url="https://bsky.odisha.gov.in",
            documents=[
                "BSKY Smart Health Card / Ration Card (BPL/NFSA)",
                "Aadhaar Card of all enrolled family members"
            ],
            rules=[
                Rule("income", "<=", 300000, "Low-income family threshold satisfied"),
                Rule("category", "in", ["General", "OBC", "SC", "ST", "EWS"], "Open to all BSKY cardholder families")
            ],
            priority_weight=95
        ),

        # =========================================================================
        # 🍃 ASSAM & NORTH EAST SCHEMES
        # =========================================================================
        Scheme(
            id="as-orunodoi-01",
            name="Orunodoi Scheme 2.0 (Direct Basic Income for Women)",
            department="Finance Department, Government of Assam",
            category_type="Women Empowerment",
            state="Assam",
            description="Assam's largest direct benefit transfer scheme providing ₹1,250 every month directly to female heads of economically disadvantaged households.",
            benefit="₹1,250 per month (₹15,000/year) direct credit on 10th of every month",
            official_portal_url="https://orunodoi.assam.gov.in",
            documents=[
                "Assam Domicile Certificate",
                "Ration Card / Proof of low income (< ₹2.0 Lakh/yr)",
                "Aadhaar Card seeded with Bank Account (DBT enabled)"
            ],
            rules=[
                Rule("gender", "==", "Female", "Targeted for female family heads"),
                Rule("income", "<=", 200000, "Family income does not exceed ₹2 Lakh per annum")
            ],
            priority_weight=96
        ),

        # =========================================================================
        # 🥛 HARYANA STATE SCHEMES
        # =========================================================================
        Scheme(
            id="hr-scholarship-01",
            name="Har-Chhatravratti (Haryana Post-Matric Scholarship Portal)",
            department="Higher Education Department, Government of Haryana",
            category_type="Education",
            state="Haryana",
            description="Centralized scholarship portal managing full fee reimbursement and maintenance allowances for SC, BC, and meritorious students of Haryana.",
            benefit="100% Tuition Fee Reimbursement + Monthly Maintenance Allowance",
            official_portal_url="https://harchhatravratti.highereduhry.ac.in",
            documents=[
                "Parivar Pehchan Patra (PPP / Family ID) with verified income",
                "Haryana Domicile Certificate",
                "Caste Certificate (SC/BC)",
                "Class 10th & 12th Marksheets and College Admission Receipt"
            ],
            rules=[
                Rule("income", "<=", 250000, "Verified Family Income in PPP is within ₹2.5 Lakh"),
                Rule("course_level", "in", ["UG", "PG", "Diploma", "B.Tech", "Degree"], "Pursuing regular higher education degree")
            ],
            priority_weight=94
        ),

        # =========================================================================
        # 🇮🇳 CENTRAL / ALL-INDIA / PAN-INDIA SCHEMES
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
            id="central-saksham-03",
            name="AICTE Saksham Scholarship Scheme for Specially Abled Students",
            department="All India Council for Technical Education (AICTE), Ministry of Education",
            category_type="Education",
            state="All India",
            description="Encourages differently-abled students with ≥ 40% disability to pursue technical degree or diploma courses in AICTE-recognized institutions.",
            benefit="₹50,000 per annum for every year of study towards college fees and assistive devices",
            official_portal_url="https://www.aicte-india.org",
            documents=[
                "Disability Certificate issued by competent medical authority (≥ 40% disability)",
                "Aadhaar Card",
                "Family Income Certificate (below ₹8 Lakh per annum)",
                "AICTE Approved College Admission Allotment Letter"
            ],
            rules=[
                Rule("is_disabled", "==", True, "Valid disability certification (PwD ≥ 40%)"),
                Rule("income", "<=", 800000, "Family income is within ₹8 Lakh per annum"),
                Rule("course_level", "in", ["UG", "Diploma", "B.Tech", "Engineering"], "Enrolled in technical degree or diploma course")
            ],
            priority_weight=96
        ),

        Scheme(
            id="central-post-matric-sc-04",
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
            id="central-post-matric-obc-05",
            name="Post-Matric Scholarship for Other Backward Classes (OBC) Students",
            department="Ministry of Social Justice and Empowerment, Govt. of India",
            category_type="Education",
            state="All India",
            description="Provides financial assistance to OBC students studying at post-matriculation or post-secondary stages to enable them to complete higher education.",
            benefit="Tuition Fee Reimbursement + Annual Academic Maintenance Allowance up to ₹10,000",
            official_portal_url="https://scholarships.gov.in",
            documents=[
                "OBC Non-Creamy Layer (NCL) Certificate",
                "Tahsildar Income Certificate (≤ ₹2.5 Lakh/annum)",
                "Previous Examination Marksheet",
                "College Bonafide and Fee Receipt"
            ],
            rules=[
                Rule("category", "in", ["OBC", "BC"], "Applicant belongs to Other Backward Classes (OBC/BC)"),
                Rule("income", "<=", 250000, "Annual family income does not exceed ₹2,50,000"),
                Rule("course_level", "in", ["Class 11", "Class 12", "UG", "PG", "Diploma", "B.Tech"], "Enrolled in recognized Post-Matric course")
            ],
            priority_weight=93
        ),

        Scheme(
            id="central-pmjay-06",
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
            id="central-pmkisan-07",
            name="Pradhan Mantri Kisan Samman Nidhi (PM-KISAN)",
            department="Department of Agriculture and Farmers Welfare, Govt. of India",
            category_type="Agriculture",
            state="All India",
            description="Income support scheme providing direct financial transfers to all landholding farmer families across India for purchasing agricultural inputs.",
            benefit="₹6,000 per year paid in three equal four-monthly installments of ₹2,00,0 directly to bank accounts",
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
        ),

        Scheme(
            id="central-pmvishwakarma-08",
            name="PM Vishwakarma Scheme (Support for Traditional Artisans & Craftsmen)",
            department="Ministry of Micro, Small and Medium Enterprises (MSME), Govt. of India",
            category_type="Social Welfare",
            state="All India",
            description="Comprehensive institutional support for traditional artisans across 18 family-based trades: PM Vishwakarma Certificate, ID, collateral-free credit at 5%, and ₹15,000 toolkit grant.",
            benefit="₹15,000 Toolkit Incentive + Collateral-free Credit up to ₹3,00,000 at 5% interest + ₹500/day training stipend",
            official_portal_url="https://pmvishwakarma.gov.in",
            documents=[
                "Aadhaar Card & Active Mobile Number",
                "Ration Card / Proof of family traditional craft trade",
                "Bank Account Details seeded with Aadhaar"
            ],
            rules=[
                Rule("income", "<=", 350000, "Traditional artisan and craftspersons income bracket"),
                Rule("category", "in", ["General", "OBC", "BC", "SC", "ST", "EWS"], "Open to all verified traditional trade practitioners")
            ],
            priority_weight=92
        ),

        Scheme(
            id="central-pmay-09",
            name="Pradhan Mantri Awas Yojana (PMAY-Urban / Gramin - Housing for All)",
            department="Ministry of Housing and Urban Affairs / Ministry of Rural Development, Govt. of India",
            category_type="Social Welfare",
            state="All India",
            description="Provides financial assistance and interest subvention for construction of pucca houses equipped with basic civic amenities to all homeless and kutcha house residents.",
            benefit="Direct financial grant of ₹1,20,000 to ₹1,30,000 (Rural) or up to ₹2.67 Lakh interest subsidy (Urban)",
            official_portal_url="https://pmaymis.gov.in",
            documents=[
                "Aadhaar Card of all family members",
                "Ration Card / BPL Card / SECC 2011 Household verification",
                "Bank Account Passbook",
                "Affidavit stating no pucca house owned anywhere in India"
            ],
            rules=[
                Rule("income", "<=", 300000, "EWS / Low Income Group (annual income ≤ ₹3 Lakh)"),
                Rule("category", "in", ["General", "OBC", "BC", "SC", "ST", "EWS"], "Open to all eligible homeless or kutcha house dwellers")
            ],
            priority_weight=87
        ),

        Scheme(
            id="central-nmmss-10",
            name="National Means-cum-Merit Scholarship Scheme (NMMSS)",
            department="Department of School Education & Literacy, Ministry of Education, Govt. of India",
            category_type="Education",
            state="All India",
            description="Awards scholarships to meritorious students of economically weaker sections from Class 9 to 12 to arrest dropout rates after elementary school.",
            benefit="₹12,000 per annum (₹1,000 per month) from Class 9 to Class 12",
            official_portal_url="https://scholarships.gov.in",
            documents=[
                "Class 7th & 8th Marksheet (minimum 55% marks, 50% for SC/ST)",
                "Income Certificate (Family income ≤ ₹3.5 Lakh/annum)",
                "Study Certificate from Government or Aided School",
                "Aadhaar-linked Bank Account Passbook"
            ],
            rules=[
                Rule("income", "<=", 350000, "Parental income from all sources does not exceed ₹3,50,000"),
                Rule("marks", ">=", 55, "Secured minimum 55% marks in Class 8 examination"),
                Rule("course_level", "in", ["Class 10", "Class 12", "Secondary", "Higher Secondary"], "Enrolled in Class 9 to 12 in Govt/Aided school")
            ],
            priority_weight=90
        ),

        Scheme(
            id="central-mudra-11",
            name="Pradhan Mantri MUDRA Yojana (PMMY Enterprise Loans)",
            department="Department of Financial Services, Ministry of Finance, Govt. of India",
            category_type="Social Welfare",
            state="All India",
            description="Provides collateral-free institutional micro-credit up to ₹10 Lakh (Shishu, Kishore, Tarun) to non-corporate, non-farm small/micro enterprises and startups.",
            benefit="Collateral-free business loan up to ₹10,00,000 at competitive bank interest rates",
            official_portal_url="https://www.mudra.org.in",
            documents=[
                "Identity Proof (Aadhaar / Voter ID / PAN Card)",
                "Business Address Proof & Enterprise Registration / Udyam Certificate",
                "Bank Account Statement for past 6 months",
                "Detailed Business Quotation / Project Report"
            ],
            rules=[
                Rule("income", "<=", 800000, "Micro-entrepreneurs, traders, and small business operators")
            ],
            priority_weight=86
        ),

        # =========================================================================
        # 🌄 ARUNACHAL PRADESH SCHEMES
        # =========================================================================
        Scheme(
            id="ar-apst-01",
            name="Arunachal Pradesh APST Post-Matric Scholarship Scheme",
            department="Directorate of Higher & Technical Education, Government of Arunachal Pradesh",
            category_type="Education",
            state="Arunachal Pradesh",
            description="Provides 100% tuition fee reimbursement and monthly maintenance allowances to indigenous APST students pursuing higher education.",
            benefit="100% Tuition Fee Reimbursement + Annual Book Grant & Monthly Maintenance Allowance",
            official_portal_url="https://scholarships.gov.in",
            documents=[
                "Arunachal Pradesh Scheduled Tribe (APST) Certificate",
                "PRC (Permanent Resident Certificate) of Arunachal Pradesh",
                "Income Certificate (≤ ₹2.5 Lakh/annum)",
                "Class 10th & 12th Marksheets and College Admission Receipt"
            ],
            rules=[
                Rule("income", "<=", 250000, "Family income does not exceed ₹2.5 Lakh per annum"),
                Rule("course_level", "in", ["UG", "PG", "Diploma", "B.Tech", "Degree", "PhD"], "Enrolled in recognized Post-Matriculation course")
            ],
            priority_weight=94
        ),

        # =========================================================================
        # 🌾 CHHATTISGARH STATE SCHEMES
        # =========================================================================
        Scheme(
            id="cg-mahtari-01",
            name="Mahtari Vandan Yojana (Direct Financial Support for Women)",
            department="Women & Child Development Department, Government of Chhattisgarh",
            category_type="Women Empowerment",
            state="Chhattisgarh",
            description="Flagship welfare scheme providing ₹1,000 monthly cash assistance directly to married women aged 21+ in Chhattisgarh to foster health and empowerment.",
            benefit="Direct monthly bank deposit of ₹1,000 (₹12,000/year) via DBT",
            official_portal_url="https://mahtarivandan.cgstate.gov.in",
            documents=[
                "Chhattisgarh Domicile / Niwas Certificate",
                "Marriage Certificate / Ration Card / Panchayat Verification",
                "Aadhaar Card linked to Bank Account (DBT active)",
                "Age Proof (Bride must be ≥ 21 years)"
            ],
            rules=[
                Rule("gender", "==", "Female", "Targeted exclusively for married women aged 21+"),
                Rule("income", "<=", 300000, "Eligible families not in government service or paying income tax")
            ],
            priority_weight=98
        ),

        Scheme(
            id="cg-postmatric-02",
            name="Chhattisgarh Post-Matric Scholarship (SC/ST/OBC)",
            department="Tribal and Scheduled Caste Development Department, Govt. of Chhattisgarh",
            category_type="Education",
            state="Chhattisgarh",
            description="Provides complete tuition fee reimbursement and living maintenance allowances to SC, ST, and OBC students in Chhattisgarh.",
            benefit="100% Tuition Fee Reimbursement + Monthly Maintenance Allowance",
            official_portal_url="https://postmatric-scholarship.cg.nic.in",
            documents=[
                "Caste Certificate (ST/SC/OBC)",
                "Chhattisgarh Niwas Praman Patra",
                "Income Certificate (≤ ₹2.5 Lakh for SC/ST; ≤ ₹1.5 Lakh for OBC)",
                "College Admission Receipt and Marksheets"
            ],
            rules=[
                Rule("income", "<=", 250000, "Family income within ₹2.5 Lakh limit"),
                Rule("course_level", "in", ["UG", "PG", "Diploma", "B.Tech", "Degree"], "Pursuing Post-Matric degree")
            ],
            priority_weight=95
        ),

        # =========================================================================
        # 🏖️ GOA STATE SCHEMES
        # =========================================================================
        Scheme(
            id="ga-griha-01",
            name="Griha Aadhar Scheme (Support for Homemakers)",
            department="Directorate of Women and Child Development, Government of Goa",
            category_type="Women Empowerment",
            state="Goa",
            description="Provides monthly financial assistance of ₹1,500 to homemakers from poor and middle-income families to cushion against rising living costs.",
            benefit="₹1,500 per month (₹18,000/year) direct cash transfer to homemakers",
            official_portal_url="https://services.goa.gov.in",
            documents=[
                "15 Years Residence Certificate in Goa",
                "Aadhaar Card of Applicant & Husband",
                "Income Certificate (Family income below ₹3.0 Lakh/annum)",
                "Bank Account Passbook"
            ],
            rules=[
                Rule("gender", "==", "Female", "Targeted for married homemakers resident in Goa for ≥ 15 years"),
                Rule("income", "<=", 300000, "Annual family income does not exceed ₹3 Lakh")
            ],
            priority_weight=96
        ),

        Scheme(
            id="ga-dsss-02",
            name="Dayanand Social Security Scheme (DSSS Goa)",
            department="Directorate of Social Welfare, Government of Goa",
            category_type="Social Welfare",
            state="Goa",
            description="Provides monthly pension and financial assistance up to ₹2,500 to senior citizens, widows, and persons with severe disabilities in Goa.",
            benefit="Monthly financial pension of ₹2,000 to ₹2,500 credited via DBT",
            official_portal_url="https://socialwelfare.goa.gov.in",
            documents=[
                "15 Years Residence Certificate in Goa",
                "Age Proof (Senior Citizen ≥ 60 yrs, or Disability / Widow certificate)",
                "Income Certificate (Family income below ₹2.0 Lakh/year)"
            ],
            rules=[
                Rule("income", "<=", 200000, "Family income is within ₹2 Lakh per annum"),
                Rule("category", "in", ["General", "OBC", "SC", "ST", "EWS"], "Open to all low-income residents of Goa")
            ],
            priority_weight=92
        ),

        # =========================================================================
        # 🏔️ HIMACHAL PRADESH STATE SCHEMES
        # =========================================================================
        Scheme(
            id="hp-pyari-01",
            name="Indira Gandhi Pyari Behna Sukh Samman Nidhi",
            department="Social Justice & Empowerment Department, Government of Himachal Pradesh",
            category_type="Women Empowerment",
            state="Himachal Pradesh",
            description="Empowers adult women in Himachal Pradesh aged 18 to 59 years with direct monthly cash transfers of ₹1,500.",
            benefit="₹1,500 per month (₹18,000/year) deposited directly into women's bank accounts",
            official_portal_url="https://eseva.hp.gov.in",
            documents=[
                "Himachal Bonafide / Domicile Certificate",
                "Aadhaar Card linked to Bank Account (DBT enabled)",
                "Ration Card copy",
                "Self-declaration confirming no family member in government job"
            ],
            rules=[
                Rule("gender", "==", "Female", "Targeted for women residents of HP aged 18 to 59 years"),
                Rule("income", "<=", 300000, "Eligible non-government household category")
            ],
            priority_weight=97
        ),

        Scheme(
            id="hp-rin-02",
            name="Dr. Y.S. Parmar Vidyarthi Rin Yojana (Subsidized Education Loan)",
            department="Higher Education Department, Government of Himachal Pradesh",
            category_type="Education",
            state="Himachal Pradesh",
            description="Offers highly subsidized educational loans up to ₹20 Lakh at a nominal 1% simple interest to pursue engineering, medicine, and higher professional education.",
            benefit="Subsidized Education Loan up to ₹20,00,000 at 1% interest rate",
            official_portal_url="https://highereducation.hp.gov.in",
            documents=[
                "Himachal Bonafide Certificate",
                "Marksheets of Class 10th and 12th with minimum 60% marks",
                "Income Certificate (Family income ≤ ₹4.0 Lakh/annum)",
                "College Admission Offer Letter and Fee Structure"
            ],
            rules=[
                Rule("income", "<=", 400000, "Family income does not exceed ₹4 Lakh per annum"),
                Rule("marks", ">=", 60, "Qualifying board examination score meets 60% requirement"),
                Rule("course_level", "in", ["UG", "PG", "Diploma", "B.Tech", "Engineering", "Medicine"], "Enrolled in professional higher education")
            ],
            priority_weight=95
        ),

        # =========================================================================
        # 🌲 JHARKHAND STATE SCHEMES
        # =========================================================================
        Scheme(
            id="jh-maiyan-01",
            name="Jharkhand Mukhyamantri Maiyan Samman Yojana (JMMSY)",
            department="Women, Child Development and Social Security Dept, Govt. of Jharkhand",
            category_type="Women Empowerment",
            state="Jharkhand",
            description="Flagship women's financial security initiative transferring ₹1,000 monthly cash assistance to women aged 18 to 50 years in Jharkhand.",
            benefit="₹1,000 per month (₹12,000/year) direct cash transfer into Aadhaar-linked accounts",
            official_portal_url="https://mmmsy.jharkhand.gov.in",
            documents=[
                "Jharkhand Residential Certificate",
                "Aadhaar Card linked to Bank Account (DBT seeded)",
                "Ration Card (Antyodaya / BPL / Green Card)",
                "Age Proof (18 to 50 years)"
            ],
            rules=[
                Rule("gender", "==", "Female", "Targeted for women residents of Jharkhand aged 18-50"),
                Rule("income", "<=", 250000, "Family income is within ₹2.5 Lakh per annum")
            ],
            priority_weight=98
        ),

        Scheme(
            id="jh-guruji-02",
            name="Guru Ji Student Credit Card Scheme",
            department="Higher and Technical Education Department, Government of Jharkhand",
            category_type="Education",
            state="Jharkhand",
            description="Provides collateral-free educational loans up to ₹15 Lakh at a subsidized 4% simple interest with a 15-year repayment tenure for higher studies.",
            benefit="Collateral-free Education Loan up to ₹15,00,000 at 4% interest rate",
            official_portal_url="https://gurujiscc.jharkhand.gov.in",
            documents=[
                "Jharkhand Domicile Certificate",
                "Class 10th and 12th Marksheets from Jharkhand recognized boards",
                "Admission Letter in NIRF-ranked or accredited institutions",
                "Co-borrower Aadhaar and PAN Card"
            ],
            rules=[
                Rule("course_level", "in", ["UG", "PG", "Diploma", "B.Tech", "Engineering", "Medicine"], "Pursuing technical or professional graduation"),
                Rule("income", "<=", 800000, "Eligible Jharkhand youth seeking higher education loan")
            ],
            priority_weight=94
        ),

        # =========================================================================
        # 🌺 MANIPUR STATE SCHEMES
        # =========================================================================
        Scheme(
            id="mn-cmht-01",
            name="Chief Minister-gi Hakshelgi Tengbang (CMHT Health Scheme)",
            department="Health Department, Government of Manipur",
            category_type="Healthcare",
            state="Manipur",
            description="Provides cashless hospitalization coverage up to ₹5,00,000 per family per year for secondary and tertiary care in network hospitals in Manipur.",
            benefit="100% Cashless medical treatment cover up to ₹5,00,000 per family per year",
            official_portal_url="https://cmhtmanipur.gov.in",
            documents=[
                "CMHT Health Card / Ration Card",
                "Aadhaar Card of all family members",
                "Income Certificate (≤ ₹1.5 Lakh/annum) or BPL card"
            ],
            rules=[
                Rule("income", "<=", 200000, "Economically weaker household income limit"),
                Rule("category", "in", ["General", "OBC", "SC", "ST", "EWS"], "Open to low-income residents of Manipur")
            ],
            priority_weight=95
        ),

        # =========================================================================
        # ☁️ MEGHALAYA STATE SCHEMES
        # =========================================================================
        Scheme(
            id="ml-mhis-01",
            name="Meghalaya Health Insurance Scheme (MHIS Phase 5)",
            department="Department of Health and Family Welfare, Government of Meghalaya",
            category_type="Healthcare",
            state="Meghalaya",
            description="Universal health insurance scheme converging with PM-JAY to provide ₹5,30,000 cashless medical cover for all citizens of Meghalaya.",
            benefit="Comprehensive cashless hospitalization up to ₹5,30,000 per family per year",
            official_portal_url="https://mhis.org.in",
            documents=[
                "MHIS Smart Card",
                "Meghalaya Permanent Residential Proof",
                "Aadhaar Card of all enrolled family members"
            ],
            rules=[
                Rule("category", "in", ["General", "OBC", "SC", "ST", "EWS"], "Universal health coverage for all Meghalaya residents")
            ],
            priority_weight=95
        ),

        # =========================================================================
        # 🌄 MIZORAM STATE SCHEMES
        # =========================================================================
        Scheme(
            id="mz-mshcs-01",
            name="Mizoram State Health Care Scheme (MSHCS)",
            department="Health and Family Welfare Department, Government of Mizoram",
            category_type="Healthcare",
            state="Mizoram",
            description="State-sponsored health assurance scheme providing cashless hospital reimbursement up to ₹5,00,000 per family per year.",
            benefit="Cashless medical hospitalization reimbursement up to ₹5,00,000/yr",
            official_portal_url="https://health.mizoram.gov.in",
            documents=[
                "MSHCS Beneficiary Card",
                "Mizoram Domicile / Tribal Certificate",
                "Aadhaar Card and Hospital Discharge Summary"
            ],
            rules=[
                Rule("income", "<=", 300000, "Low-income family threshold satisfied"),
                Rule("category", "in", ["General", "ST", "OBC", "SC"], "Open to all eligible families in Mizoram")
            ],
            priority_weight=94
        ),

        # =========================================================================
        # 🦅 NAGALAND STATE SCHEMES
        # =========================================================================
        Scheme(
            id="nl-cmhis-01",
            name="Chief Minister's Health Insurance Scheme (CMHIS Nagaland)",
            department="Department of Health & Family Welfare, Government of Nagaland",
            category_type="Healthcare",
            state="Nagaland",
            description="Universal cashless health insurance protecting all indigenous and permanent residents of Nagaland up to ₹5,00,000 per family per year.",
            benefit="Cashless hospitalization cover up to ₹5,00,000 per family per year",
            official_portal_url="https://cmhis.nagaland.gov.in",
            documents=[
                "Indigenous Inhabitant Certificate (IIC) of Nagaland",
                "Nagaland Permanent Residence Certificate",
                "Aadhaar Card of all enrolled family members"
            ],
            rules=[
                Rule("category", "in", ["ST", "General", "OBC", "SC"], "Open to all indigenous residents of Nagaland")
            ],
            priority_weight=95
        ),

        # =========================================================================
        # 🏔️ SIKKIM STATE SCHEMES
        # =========================================================================
        Scheme(
            id="sk-aama-01",
            name="Aama Yojana (Direct Financial Assistance for Mothers)",
            department="Women and Child Development Department, Government of Sikkim",
            category_type="Women Empowerment",
            state="Sikkim",
            description="Pioneering financial welfare scheme providing an annual cash grant of ₹40,000 to all unemployed, non-working mothers in Sikkim.",
            benefit="Annual direct grant of ₹40,000 deposited directly into mother's bank account",
            official_portal_url="https://sikkim.gov.in",
            documents=[
                "Certificate of Identification (COI) / Sikkim Subject Certificate",
                "Mother's Aadhaar Card",
                "Unemployed Non-Working Declaration verified by Ward Panchayat",
                "Bank Account Passbook"
            ],
            rules=[
                Rule("gender", "==", "Female", "Targeted for non-working mothers resident in Sikkim"),
                Rule("income", "<=", 400000, "Eligible household category in Sikkim")
            ],
            priority_weight=97
        ),

        # =========================================================================
        # 🌿 TRIPURA STATE SCHEMES
        # =========================================================================
        Scheme(
            id="tr-kanya-01",
            name="Mukhyamantri Kanya Atmanirbhar Yojana (Girl Child Higher Ed)",
            department="Higher Education Department, Government of Tripura",
            category_type="Education",
            state="Tripura",
            description="Incentivizes top meritorious girl students in Class 12 board exams by providing free two-wheelers (scooters) or financial scholarships for college.",
            benefit="Free Electric/Petrol Scooter or Higher Education Cash Grant",
            official_portal_url="https://highereducation.tripura.gov.in",
            documents=[
                "Permanent Resident of Tripura Certificate (PRTC)",
                "Class 12th Board Marksheet with top percentile score",
                "College Admission Receipt",
                "Aadhaar Card"
            ],
            rules=[
                Rule("gender", "==", "Female", "Designed exclusively for female students"),
                Rule("marks", ">=", 75, "Secured high marks in Class 12 board examination"),
                Rule("course_level", "in", ["UG", "Degree", "B.Tech", "Medicine"], "Enrolled in higher education degree")
            ],
            priority_weight=93
        ),

        # =========================================================================
        # ⛰️ UTTARAKHAND STATE SCHEMES
        # =========================================================================
        Scheme(
            id="uk-nanda-01",
            name="Nanda Gaura Devi Kanya Dhan Yojana",
            department="Women Empowerment & Child Development Department, Govt. of Uttarakhand",
            category_type="Women Empowerment",
            state="Uttarakhand",
            description="Provides a cash grant of ₹51,000 to girl students from low-income families upon passing Class 12 and enrolling into higher education.",
            benefit="One-time direct financial grant of ₹51,000 credited to girl student's account",
            official_portal_url="https://nandagaura.uk.gov.in",
            documents=[
                "Uttarakhand Domicile / Sthai Niwas Certificate",
                "Class 12th Passing Marksheet from Uttarakhand Board",
                "Tehsildar Income Certificate (≤ ₹72,000/yr for rural, ₹84,000/yr for urban)",
                "College Admission Bonafide / Fee Receipt",
                "Aadhaar-linked Bank Account Passbook"
            ],
            rules=[
                Rule("gender", "==", "Female", "Targeted for girl students"),
                Rule("income", "<=", 120000, "Economically weaker household income limit satisfied"),
                Rule("course_level", "in", ["UG", "Diploma", "B.Tech", "Degree"], "Pursuing higher education degree or diploma")
            ],
            priority_weight=96
        ),

        # =========================================================================
        # ❄️ JAMMU AND KASHMIR (UT) SCHEMES
        # =========================================================================
        Scheme(
            id="jk-sehat-01",
            name="Ayushman Bharat PM-JAY SEHAT Scheme (Universal Healthcare J&K)",
            department="State Health Agency, Health & Medical Education Dept, Govt. of J&K",
            category_type="Healthcare",
            state="Jammu and Kashmir",
            description="Provides 100% universal cashless healthcare coverage up to ₹5,00,000 per family per year to all residents of Jammu and Kashmir without income ceiling.",
            benefit="100% Cashless medical treatment cover up to ₹5,00,000 per family per year",
            official_portal_url="https://sehat.jk.gov.in",
            documents=[
                "J&K Domicile Certificate",
                "Golden Card / Ayushman Bharat SEHAT Card",
                "Aadhaar Card of all family members",
                "Ration Card"
            ],
            rules=[
                Rule("category", "in", ["General", "OBC", "SC", "ST", "EWS"], "Universal health coverage for 100% residents of Jammu & Kashmir")
            ],
            priority_weight=98
        ),

        Scheme(
            id="jk-mumkin-02",
            name="Mumkin Scheme (Mission Youth Livelihood Program)",
            department="Mission Youth, Government of Jammu and Kashmir",
            category_type="Social Welfare",
            state="Jammu and Kashmir",
            description="Empowers unemployed youth aged 18 to 35 years in J&K by providing a 100% on-road commercial vehicle subsidy with zero down payment for self-employment.",
            benefit="Commercial Vehicle with ₹80,000 + 10% vehicle cost subsidy from Govt of J&K",
            official_portal_url="https://missionyouth.jk.gov.in",
            documents=[
                "J&K Domicile Certificate",
                "Commercial Driving License",
                "Unemployed youth declaration",
                "Aadhaar Card & PAN Card"
            ],
            rules=[
                Rule("income", "<=", 400000, "Unemployed youth seeking transport entrepreneurship")
            ],
            priority_weight=92
        ),

        # =========================================================================
        # 🏔️ LADAKH (UT) SCHEMES
        # =========================================================================
        Scheme(
            id="la-rewa-01",
            name="Rewa Scheme Ladakh (Competitive Exam Financial Grant)",
            department="Higher Education Department, Administration of UT of Ladakh",
            category_type="Education",
            state="Ladakh",
            description="Provides financial grants up to ₹1,00,000 to meritorious students of Ladakh who qualify preliminary stages of civil services or enter top colleges.",
            benefit="Financial grant of ₹1,00,000 for UPSC/State PSC and ₹50,000 for NEET/JEE qualifiers",
            official_portal_url="https://ladakh.gov.in",
            documents=[
                "Resident Certificate of Ladakh",
                "ST Certificate of Ladakh",
                "Preliminary Exam Qualification Admit Card / College Admission Order",
                "Student Bank Account Passbook"
            ],
            rules=[
                Rule("course_level", "in", ["Class 12", "UG", "PG", "Degree"], "Qualified national competitive exam preliminary stage")
            ],
            priority_weight=95
        ),

        # =========================================================================
        # 🏖️ PUDUCHERRY (UT) SCHEMES
        # =========================================================================
        Scheme(
            id="py-kamarajar-01",
            name="Perunthalaivar Kamarajar Financial Assistance Scheme",
            department="Directorate of Higher & Technical Education, Government of Puducherry",
            category_type="Education",
            state="Puducherry",
            description="Reimburses 100% of college tuition fees for Puducherry resident students selected through CENTAC into professional courses (Engineering, Medical, Nursing).",
            benefit="100% Tuition Fee Reimbursement for entire duration of professional course",
            official_portal_url="https://dhte.py.gov.in",
            documents=[
                "Puducherry Residence Certificate (Continuous 5 years)",
                "CENTAC Allotment Order",
                "Income Certificate (≤ ₹6.0 Lakh/annum for General; no limit for SC/ST)",
                "Fee Receipt from Professional College"
            ],
            rules=[
                Rule("income", "<=", 600000, "Annual family income does not exceed ₹6 Lakh (waived for SC/ST)"),
                Rule("course_level", "in", ["UG", "B.Tech", "Engineering", "Medicine", "Degree"], "Enrolled through CENTAC single window counseling")
            ],
            priority_weight=96
        ),

        # =========================================================================
        # 🏛️ CHANDIGARH (UT) SCHEMES
        # =========================================================================
        Scheme(
            id="ch-merit-01",
            name="Chandigarh Administration Post-Matric Scholarship Scheme",
            department="Directorate of Higher Education, Chandigarh Administration",
            category_type="Education",
            state="Chandigarh",
            description="Provides full tuition fee concession and living allowances to SC, OBC, and meritorious students pursuing higher studies in Chandigarh.",
            benefit="100% Tuition Fee Concession + Monthly Living Maintenance Allowance",
            official_portal_url="https://chdeducation.gov.in",
            documents=[
                "Chandigarh Domicile / Study Certificate",
                "Caste Certificate (SC/OBC)",
                "Income Certificate (≤ ₹2.5 Lakh/annum)",
                "College Admission Receipt and Marksheets"
            ],
            rules=[
                Rule("income", "<=", 250000, "Annual family income within ₹2.5 Lakh ceiling"),
                Rule("course_level", "in", ["UG", "PG", "Diploma", "B.Tech", "Degree"], "Enrolled in recognized college in Chandigarh")
            ],
            priority_weight=94
        ),

        # =========================================================================
        # 🌴 ANDAMAN AND NICOBAR ISLANDS (UT) SCHEMES
        # =========================================================================
        Scheme(
            id="an-highered-01",
            name="Andaman & Nicobar Higher Education Financial Assistance",
            department="Directorate of Higher Education, Andaman & Nicobar Administration",
            category_type="Education",
            state="Andaman and Nicobar Islands",
            description="Assists islander students pursuing degree and professional courses in mainland universities with hostel allowance, tuition fee aid, and annual ship airfare.",
            benefit="Annual Financial Grant of ₹20,000 to ₹50,000 + Subsidized Travel Allowance",
            official_portal_url="https://andaman.gov.in",
            documents=[
                "Local Certificate / Tribal Certificate of Andaman & Nicobar",
                "Higher Education Admission Letter (Mainland or Island Institute)",
                "Family Income Certificate (≤ ₹3.0 Lakh/annum)",
                "Student Bank Account Passbook"
            ],
            rules=[
                Rule("income", "<=", 300000, "Family income does not exceed ₹3 Lakh per annum"),
                Rule("course_level", "in", ["UG", "PG", "Diploma", "B.Tech", "Degree"], "Enrolled in recognized higher education")
            ],
            priority_weight=94
        ),

        # =========================================================================
        # 🏖️ DADRA AND NAGAR HAVELI AND DAMAN AND DIU (UT) SCHEMES
        # =========================================================================
        Scheme(
            id="dd-sadhana-01",
            name="Saraswati Sadhana & Higher Education Assistance (DNHDD)",
            department="Department of Higher and Technical Education, Administration of DNH & DD",
            category_type="Education",
            state="Dadra and Nagar Haveli and Daman and Diu",
            description="Provides free bicycles, full tuition fee reimbursement, and book grants to female and tribal students pursuing higher secondary and college education.",
            benefit="100% Tuition Fee Reimbursement + Annual Book Grant & Free Transport Allowance",
            official_portal_url="https://daman.nic.in",
            documents=[
                "DNH & DD Domicile Certificate",
                "Caste Certificate (ST/SC/OBC)",
                "Income Certificate (≤ ₹2.5 Lakh/annum)",
                "College Bonafide Certificate"
            ],
            rules=[
                Rule("income", "<=", 250000, "Family income does not exceed ₹2.5 Lakh per annum"),
                Rule("course_level", "in", ["Class 12", "UG", "Diploma", "B.Tech", "Degree"], "Enrolled in college education")
            ],
            priority_weight=93
        ),

        # =========================================================================
        # 🌊 LAKSHADWEEP (UT) SCHEMES
        # =========================================================================
        Scheme(
            id="ld-scholarship-01",
            name="Lakshadweep Island Higher Education Scholarship Scheme",
            department="Department of Education, Administration of UT of Lakshadweep",
            category_type="Education",
            state="Lakshadweep",
            description="Provides 100% full tuition fees, free hostel accommodation, and annual flight/ship transport allowances to native islander students studying in mainland colleges.",
            benefit="100% Complete College Fees + Monthly Hostel Allowance + Annual Mainland Travel Grant",
            official_portal_url="https://lakshadweep.gov.in",
            documents=[
                "Native Inhabitant of Lakshadweep Certificate",
                "ST Certificate of Lakshadweep",
                "Admission Allotment Order in recognized mainland/island college",
                "Aadhaar-linked Bank Passbook"
            ],
            rules=[
                Rule("course_level", "in", ["UG", "PG", "Diploma", "B.Tech", "Degree", "Medicine"], "Enrolled in recognized higher education course"),
                Rule("category", "in", ["ST", "General"], "Eligible native islander student")
            ],
            priority_weight=95
        )
    ]
    return schemes
