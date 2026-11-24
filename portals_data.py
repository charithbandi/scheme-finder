"""
Official Government Websites & Portals Directory for Scheme Finder.
Comprehensive database of verified Central and State Government portals
across all Indian States (Andhra Pradesh, Telangana, Tamil Nadu, Karnataka,
Maharashtra, West Bengal, Uttar Pradesh, Kerala, Bihar, Rajasthan, Gujarat,
Madhya Pradesh, Delhi, Punjab, Odisha, Assam, Haryana) and Central / Pan-India.
"""

from typing import List, Dict, Any


def get_all_portals() -> List[Dict[str, Any]]:
    """
    Returns verified official government portals covering Central and all Indian states.
    All links point to official .gov.in / .nic.in / state government domains.
    """
    return [
        # =========================================================================
        # 🇮🇳 CENTRAL / NATIONAL GOVERNMENT PORTALS
        # =========================================================================
        {
            "id": "central-nsp",
            "name": "National Scholarship Portal (NSP)",
            "state": "Central",
            "category": "Scholarships & Education",
            "department": "Ministry of Electronics & IT / Ministry of Education, Govt. of India",
            "url": "https://scholarships.gov.in",
            "domain": "scholarships.gov.in",
            "badge": "Central Govt",
            "icon": "🎓",
            "description": "The official Government of India single-window platform for application, verification, and disbursement of over 100 Central, UGC, AICTE, and State scholarship programs.",
            "services": [
                "Pre-Matric & Post-Matric Central Scholarships",
                "Central Sector Scheme for College Students (CSSS)",
                "AICTE Pragati, Saksham & Swanath Scholarships",
                "Merit-cum-Means Scholarships for Minorities",
                "Direct Benefit Transfer (DBT) tracking"
            ],
            "popular": True
        },
        {
            "id": "central-myscheme",
            "name": "myScheme Portal (National Schemes Gateway)",
            "state": "Central",
            "category": "National Gateways",
            "department": "National e-Governance Division (NeGD) & MeitY, Government of India",
            "url": "https://www.myscheme.gov.in",
            "domain": "myscheme.gov.in",
            "badge": "Central Govt",
            "icon": "🏛️",
            "description": "National e-Governance marketplace helping citizens discover welfare eligibility for 1,200+ Central and State government schemes based on demographic and economic criteria.",
            "services": [
                "Universal Search across 1,200+ Central & State Schemes",
                "Multi-criteria citizen eligibility evaluation",
                "Direct links to departmental application forms",
                "Guidance on required documents & certificates"
            ],
            "popular": True
        },
        {
            "id": "central-digilocker",
            "name": "DigiLocker (National Document Wallet)",
            "state": "Central",
            "category": "Identity & Records",
            "department": "Digital India Corporation, Ministry of Electronics & IT (MeitY)",
            "url": "https://www.digilocker.gov.in",
            "domain": "digilocker.gov.in",
            "badge": "Digital India",
            "icon": "📁",
            "description": "Flagship digital document repository legally valid under IT Act 2000. Allows citizens to store, fetch, and digitally verify authentic marksheets, Aadhaar, Caste, and Income certificates.",
            "services": [
                "Issue authentic 10th & 12th Board Marksheets (CBSE, State Boards)",
                "Fetch verified Aadhaar, PAN, and Ration Cards",
                "Store Tahsildar Income & Community/Caste certificates",
                "Instant paperless verification for college admissions"
            ],
            "popular": True
        },
        {
            "id": "central-pmkisan",
            "name": "PM-KISAN Samman Nidhi Portal",
            "state": "Central",
            "category": "Agriculture",
            "department": "Department of Agriculture & Farmers Welfare, Ministry of Agriculture, Govt. of India",
            "url": "https://pmkisan.gov.in",
            "domain": "pmkisan.gov.in",
            "badge": "Central Govt",
            "icon": "🌾",
            "description": "Direct financial transfer portal providing ₹6,000 annually to all landholder farmer families across India in three equal four-monthly installments.",
            "services": [
                "New Farmer Registration",
                "Beneficiary Status & Payment Installment Tracking",
                "Mandatory OTP / Biometric e-KYC Verification",
                "Aadhaar & Bank Account Seeding Verification"
            ],
            "popular": True
        },
        {
            "id": "central-pmjay",
            "name": "Ayushman Bharat - PM-JAY Portal",
            "state": "Central",
            "category": "Healthcare",
            "department": "National Health Authority (NHA), Ministry of Health & Family Welfare",
            "url": "https://pmjay.gov.in",
            "domain": "pmjay.gov.in",
            "badge": "Central Govt",
            "icon": "🏥",
            "description": "World's largest government-funded healthcare assurance scheme offering cashless hospital coverage of ₹5,00,000 per family per year for secondary and tertiary treatment.",
            "services": [
                "Check Am I Eligible / SECC 2011 Household verification",
                "Create and download Ayushman / ABHA Cards",
                "Empanelled Public & Private Hospital Search",
                "Cashless Treatment Claim Tracking"
            ],
            "popular": True
        },
        {
            "id": "central-uidai",
            "name": "myAadhaar (UIDAI Official Citizen Portal)",
            "state": "Central",
            "category": "Identity & Records",
            "department": "Unique Identification Authority of India (UIDAI), Govt. of India",
            "url": "https://myaadhaar.uidai.gov.in",
            "domain": "myaadhaar.uidai.gov.in",
            "badge": "UIDAI",
            "icon": "🆔",
            "description": "Official Aadhaar portal to manage identity records, download electronic Aadhaar (e-Aadhaar), update address, and verify NPCI bank account direct benefit transfer (DBT) mapping.",
            "services": [
                "Download Password-Protected e-Aadhaar PDF",
                "Verify Aadhaar - Bank Account Seeding / NPCI DBT Status",
                "Online Address & Demographic Information Update",
                "Order Secure Aadhaar PVC Card"
            ],
            "popular": True
        },
        {
            "id": "central-umang",
            "name": "UMANG (Unified Mobile App for New-age Governance)",
            "state": "Central",
            "category": "National Gateways",
            "department": "Ministry of Electronics and Information Technology (MeitY)",
            "url": "https://web.umang.gov.in",
            "domain": "web.umang.gov.in",
            "badge": "Digital India",
            "icon": "📱",
            "description": "All-in-one web and mobile governance gateway integrating 1,200+ Central and State government citizen services including EPFO, scholarships, gas booking, and utility bills.",
            "services": [
                "Access Central & State Welfare Programs",
                "EPFO EPF Passbook & UAN claim tracking",
                "National Pension System (NPS) and Atal Pension Yojana",
                "Online certificate applications and fee payments"
            ],
            "popular": True
        },
        {
            "id": "central-indiagov",
            "name": "National Portal of India",
            "state": "Central",
            "category": "National Gateways",
            "department": "National Informatics Centre (NIC), Ministry of Electronics & IT",
            "url": "https://www.india.gov.in",
            "domain": "india.gov.in",
            "badge": "NIC India",
            "icon": "🇮🇳",
            "description": "The official single-entry window to access all Indian Government services, gazettes, acts, schemes, and portals across all Ministries and Departments.",
            "services": [
                "Access 13,000+ Online Government Services",
                "Central and State Government Acts & Rules repository",
                "Directory of Government Departments, Ministers & Officials",
                "Latest government job circulars & tender notices"
            ],
            "popular": False
        },
        {
            "id": "central-aicte",
            "name": "AICTE Student Development Schemes Portal",
            "state": "Central",
            "category": "Scholarships & Education",
            "department": "All India Council for Technical Education (AICTE), Ministry of Education",
            "url": "https://www.aicte-india.org/schemes/students-development-schemes",
            "domain": "aicte-india.org",
            "badge": "AICTE",
            "icon": "🎓",
            "description": "Official technical education scholarship portal providing Pragati (for girl students), Saksham (for differently abled students), and Swanath scholarships (₹50,000/yr).",
            "services": [
                "AICTE Pragati Scholarship for Girls in Degree/Diploma",
                "AICTE Saksham Scholarship for Specially Abled Students",
                "AICTE Swanath Scholarship for Orphans & Wards of Martyrs",
                "PG Scholarship (GATE / GPAT qualified students)"
            ],
            "popular": False
        },

        # =========================================================================
        # 🟡 ANDHRA PRADESH STATE GOVERNMENT PORTALS
        # =========================================================================
        {
            "id": "ap-jnanabhumi",
            "name": "JnanaBhumi AP (Higher Education & Scholarships)",
            "state": "Andhra Pradesh",
            "category": "Scholarships & Education",
            "department": "Higher Education & Social Welfare Department, Government of Andhra Pradesh",
            "url": "https://jnanabhumi.ap.gov.in",
            "domain": "jnanabhumi.ap.gov.in",
            "badge": "Govt of AP",
            "icon": "🟡",
            "description": "Andhra Pradesh's dedicated digital platform for student welfare, managing 100% Fee Reimbursement (Jagananna Vidya Deevena) and Hostel Allowance (Vasathi Deevena).",
            "services": [
                "Jagananna Vidya Deevena (RTF - Full Tuition Fee Reimbursement)",
                "Jagananna Vasathi Deevena (MTF - Boarding & Hostel Allowance)",
                "Post-Matric Scholarship Fresh & Renewal Registrations",
                "College Biometric Attendance & Disbursal Status Tracking"
            ],
            "popular": True
        },
        {
            "id": "ap-meeseva",
            "name": "MeeSeva AP (Online Citizen Service Portal)",
            "state": "Andhra Pradesh",
            "category": "e-Governance & Certificates",
            "department": "Information Technology, Electronics & Communications Dept, Govt. of AP",
            "url": "https://onlineap.meeseva.gov.in",
            "domain": "onlineap.meeseva.gov.in",
            "badge": "Govt of AP",
            "icon": "📜",
            "description": "Official AP government citizen services portal for applying and downloading digitally signed Tahsildar certificates required for all welfare schemes.",
            "services": [
                "Integrated Community, Nativity & Date of Birth Certificate (Caste)",
                "Tahsildar Income Certificate (for fee reimbursement & pensions)",
                "Residence / Domicile Certificate",
                "Family Member & Legal Heir Certificates"
            ],
            "popular": True
        },
        {
            "id": "ap-aarogyasri",
            "name": "Dr. YSR Aarogyasri Health Care Trust",
            "state": "Andhra Pradesh",
            "category": "Healthcare",
            "department": "Dr. YSR Aarogyasri Health Care Trust, Government of Andhra Pradesh",
            "url": "https://ysraarogyasri.ap.gov.in",
            "domain": "ysraarogyasri.ap.gov.in",
            "badge": "Govt of AP",
            "icon": "🏥",
            "description": "Pioneering state health insurance initiative providing 100% cashless medical and surgical treatment up to ₹25,00,000 per family per year across 3,257 procedures.",
            "services": [
                "Dr. YSR Aarogyasri Health Card download & verification",
                "Network Empanelled Hospital directory (AP, HYD, BLR, CHN)",
                "Pre-authorization & treatment package tariff search",
                "Aarogya Mithra hospital assistance contacts"
            ],
            "popular": True
        },
        {
            "id": "ap-navasakam",
            "name": "Navasakam AP (Welfare Schemes Delivery Portal)",
            "state": "Andhra Pradesh",
            "category": "National Gateways",
            "department": "Department of Village Secretariats, Govt. of AP",
            "url": "https://navasakam.ap.gov.in",
            "domain": "navasakam.ap.gov.in",
            "badge": "Govt of AP",
            "icon": "📋",
            "description": "Beneficiary identification and service delivery portal coordinating doorstep governance and social audit for all AP welfare schemes.",
            "services": [
                "Beneficiary verification for JVD, Cheyutha, Aasara & Amma Vodi",
                "Grama / Ward Sachivalayam Social Audit Lists",
                "Rice Card (Food Security Card) & Pension Eligibility Status",
                "Grievance redressal (Spandana 1902) integration"
            ],
            "popular": False
        },

        # =========================================================================
        # 🔵 TELANGANA STATE GOVERNMENT PORTALS
        # =========================================================================
        {
            "id": "ts-epass",
            "name": "Telangana ePASS (Scholarships & Welfare Portal)",
            "state": "Telangana",
            "category": "Scholarships & Education",
            "department": "Scheduled Castes, BC, Tribal & Minority Welfare Departments, Govt. of Telangana",
            "url": "https://telanganaepass.cgg.gov.in",
            "domain": "telanganaepass.cgg.gov.in",
            "badge": "Govt of TS",
            "icon": "🔵",
            "description": "Comprehensive scholarships and marriage assistance gateway managing Post-Matric Fee Reimbursement (RTF/MTF), Overseas Vidya Nidhi, and Kalyana Lakshmi.",
            "services": [
                "Post-Matric Scholarship & Full Fee Reimbursement (RTF)",
                "Hostel & Mess Maintenance Allowance (MTF)",
                "Telangana Overseas Vidya Nidhi (up to ₹20 Lakhs for foreign study)",
                "Kalyana Lakshmi & Shaadi Mubarak (₹1,00,116 bride marriage grant)",
                "Corporate College Admissions & Pre-Matric Scholarships"
            ],
            "popular": True
        },
        {
            "id": "ts-meeseva",
            "name": "MeeSeva Telangana Citizen Portal",
            "state": "Telangana",
            "category": "e-Governance & Certificates",
            "department": "ITE&C Department & MeeSeva Directorate, Government of Telangana",
            "url": "https://ts.meeseva.telangana.gov.in",
            "domain": "ts.meeseva.telangana.gov.in",
            "badge": "Govt of TS",
            "icon": "📜",
            "description": "Telangana government's unified citizen portal for applying and securing digitally signed revenue and community certificates required for college and job admissions.",
            "services": [
                "MeeSeva Integrated Caste / Community Certificate",
                "Tahsildar Income Certificate (mandatory for TS ePASS)",
                "Residence & Local Candidate Certificate",
                "Encumbrance (EC) and Revenue Extract services"
            ],
            "popular": True
        },
        {
            "id": "ts-aarogyasri",
            "name": "Rajiv Aarogyasri Telangana Health Care Trust",
            "state": "Telangana",
            "category": "Healthcare",
            "department": "Aarogyasri Health Care Trust, Government of Telangana",
            "url": "https://aarogyasri.telangana.gov.in",
            "domain": "aarogyasri.telangana.gov.in",
            "badge": "Govt of TS",
            "icon": "🏥",
            "description": "State health insurance platform providing cashless medical treatment and surgery up to ₹10,00,000 per family per year across 1,672 procedures.",
            "services": [
                "Check Aarogyasri Card status with Ration Card / FSC Number",
                "Find Network Hospitals & Specialty Doctors in Telangana",
                "Treatment pre-authorization status tracking",
                "Dial 104 / Aarogyasri toll-free helpdesk"
            ],
            "popular": True
        },
        {
            "id": "ts-rythubandhu",
            "name": "Rythu Bandhu & Rythu Bima Portal",
            "state": "Telangana",
            "category": "Agriculture",
            "department": "Department of Agriculture & Cooperation, Government of Telangana",
            "url": "https://rythubandhu.telangana.gov.in",
            "domain": "rythubandhu.telangana.gov.in",
            "badge": "Govt of TS",
            "icon": "🌾",
            "description": "Telangana's agricultural investment support portal providing direct transfers of ₹12,000–₹15,000 per acre per year and ₹5 Lakh farmer group life insurance.",
            "services": [
                "Farmer Investment Support disbursement status",
                "Rythu Bima (₹5 Lakh Group Life Insurance) enrollment & claim tracking",
                "Cheque / Direct Bank Transfer transaction reconciliation",
                "Agricultural Extension Officer (AEO) cluster contacts"
            ],
            "popular": False
        },

        # =========================================================================
        # 🔴 TAMIL NADU STATE GOVERNMENT PORTALS
        # =========================================================================
        {
            "id": "tn-esevai",
            "name": "Tamil Nadu e-Sevai (TNeGA Citizen Portal)",
            "state": "Tamil Nadu",
            "category": "e-Governance & Certificates",
            "department": "Tamil Nadu e-Governance Agency (TNeGA), Information Technology Dept, Govt of TN",
            "url": "https://www.tnesevai.tn.gov.in",
            "domain": "tnesevai.tn.gov.in",
            "badge": "Govt of TN",
            "icon": "🔴",
            "description": "Unified online service portal for citizens of Tamil Nadu to apply for, track, and download Revenue Department certificates required for higher education and quotas.",
            "services": [
                "Community / Caste Certificate (BC, MBC, SC, ST)",
                "Income Certificate (Revenue Authority)",
                "Nativity / Domicile Certificate",
                "First Graduate Certificate (for tuition fee exemption)",
                "No Male Child / Single Girl Child Certificate"
            ],
            "popular": True
        },
        {
            "id": "tn-pudhumai",
            "name": "Pudhumai Penn Scheme Portal",
            "state": "Tamil Nadu",
            "category": "Scholarships & Education",
            "department": "Social Welfare & Women Empowerment Department, Government of Tamil Nadu",
            "url": "https://pudhumaipenn.tn.gov.in",
            "domain": "pudhumaipenn.tn.gov.in",
            "badge": "Govt of TN",
            "icon": "👩",
            "description": "Official portal for Moovalur Ramamirtham Ammaiyar Higher Education Assurance Scheme providing ₹1,000 monthly cash assistance to girls from TN government schools entering college.",
            "services": [
                "New Student Registration with EMIS School Code",
                "College Verification and Approval workflow",
                "Direct Benefit Transfer (DBT) monthly payment status",
                "Grievance submission for missing payment credits"
            ],
            "popular": True
        },
        {
            "id": "tn-kmut",
            "name": "Kalaignar Magalir Urimai Thittam (KMUT Portal)",
            "state": "Tamil Nadu",
            "category": "Women & Social Welfare",
            "department": "Special Programme Implementation Department, Government of Tamil Nadu",
            "url": "https://kmut.tn.gov.in",
            "domain": "kmut.tn.gov.in",
            "badge": "Govt of TN",
            "icon": "🤝",
            "description": "Flagship universal basic income initiative acknowledging women's unpaid household labor by providing ₹1,000 monthly rights grant directly to women heads of families.",
            "services": [
                "Check Beneficiary Eligibility Status with Smart Ration Card",
                "Aadhaar-seeded Bank Account verification",
                "Appeal & re-verification submission for rejected applicants",
                "Helpdesk & Tahsildar camp schedule lookup"
            ],
            "popular": True
        },
        {
            "id": "tn-tnea",
            "name": "TNEA Online (Tamil Nadu Engineering Admissions)",
            "state": "Tamil Nadu",
            "category": "Scholarships & Education",
            "department": "Directorate of Technical Education (DoTE), Higher Education Dept, Govt of TN",
            "url": "https://www.tneaonline.org",
            "domain": "tneaonline.org",
            "badge": "Govt of TN",
            "icon": "🎓",
            "description": "Single-window online engineering counseling portal facilitating admissions to all engineering colleges in TN and implementing the 7.5% Government School 100% Fee Waiver quota.",
            "services": [
                "B.E. / B.Tech Single Window Counseling Registration",
                "7.5% Preferential Reservation & 100% Fee Waiver allotment",
                "First Graduate Fee Concession verification",
                "Cut-off marks & College seat vacancy matrix"
            ],
            "popular": True
        },

        # =========================================================================
        # 🟡 KARNATAKA STATE GOVERNMENT PORTALS
        # =========================================================================
        {
            "id": "ka-sevasindhu",
            "name": "Seva Sindhu Karnataka (Citizen Services Portal)",
            "state": "Karnataka",
            "category": "e-Governance & Certificates",
            "department": "Department of Personnel and Administrative Reforms (e-Governance), Govt. of Karnataka",
            "url": "https://sevasindhu.karnataka.gov.in",
            "domain": "sevasindhu.karnataka.gov.in",
            "badge": "Govt of KA",
            "icon": "🟡",
            "description": "Unified citizen portal delivering 800+ services including Gruha Lakshmi, Yuva Nidhi, Caste & Income certificates, and bus passes in Karnataka.",
            "services": [
                "Gruha Lakshmi (₹2,000/mo) Application & Status",
                "Yuva Nidhi (Graduate Unemployment Allowance) Registration",
                "Income & Caste Certificates (Nadakacheri)",
                "Shakti Scheme Smart Card for free bus travel"
            ],
            "popular": True
        },
        {
            "id": "ka-ssp",
            "name": "State Scholarship Portal Karnataka (SSP Post-Matric)",
            "state": "Karnataka",
            "category": "Scholarships & Education",
            "department": "Centre for e-Governance, Government of Karnataka",
            "url": "https://ssp.postmatric.karnataka.gov.in",
            "domain": "ssp.postmatric.karnataka.gov.in",
            "badge": "Govt of KA",
            "icon": "🎓",
            "description": "Centralized scholarship portal for all post-matric students of Karnataka offering complete fee concession, hostel fees, and farmer child scholarships.",
            "services": [
                "Post-Matric Fee Reimbursement for SC, ST, OBC & Minorities",
                "Raitha Vidya Nidhi Scholarship for children of farmers",
                "Hostel E-Attestation and Mess Charges Reimbursement",
                "Direct Benefit Transfer (DBT) payment status"
            ],
            "popular": True
        },

        # =========================================================================
        # 🟠 MAHARASHTRA STATE GOVERNMENT PORTALS
        # =========================================================================
        {
            "id": "mh-mahadbt",
            "name": "MahaDBT (Maharashtra Direct Benefit Transfer Portal)",
            "state": "Maharashtra",
            "category": "Scholarships & Education",
            "department": "Directorate of Higher Education (DHE) & Social Justice Dept, Govt. of Maharashtra",
            "url": "https://mahadbt.maharashtra.gov.in",
            "domain": "mahadbt.maharashtra.gov.in",
            "badge": "Govt of MH",
            "icon": "🟠",
            "description": "Unified scholarship and fee reimbursement portal offering Rajarshi Shahu Maharaj fee concessions, post-matric scholarships, and hostels.",
            "services": [
                "Rajarshi Chhatrapati Shahu Maharaj Tuition Fee Reimbursement",
                "Post-Matric Scholarship for SC, ST, VJNT, OBC & SBC",
                "Dr. Panjabrao Deshmukh Hostel Maintenance Allowance",
                "DBT Application Tracking & Disbursement Status"
            ],
            "popular": True
        },
        {
            "id": "mh-aaplesarkar",
            "name": "Aaple Sarkar (Government of Maharashtra Citizen Portal)",
            "state": "Maharashtra",
            "category": "e-Governance & Certificates",
            "department": "Information Technology Department, Government of Maharashtra",
            "url": "https://aaplesarkar.mahaonline.gov.in",
            "domain": "aaplesarkar.mahaonline.gov.in",
            "badge": "Govt of MH",
            "icon": "📜",
            "description": "Maharashtra's right to services portal providing digitally signed Caste, Non-Creamy Layer, Income, and Domicile certificates.",
            "services": [
                "Tahsildar Income Certificate (for fee concessions)",
                "Caste & Non-Creamy Layer (NCL) Certificate",
                "Maharashtra Domicile & Nationality Certificate",
                "7/12 Land Utara and Revenue records"
            ],
            "popular": True
        },
        {
            "id": "mh-ladkibahin",
            "name": "Majhi Ladki Bahin Yojana Official Portal",
            "state": "Maharashtra",
            "category": "Women & Social Welfare",
            "department": "Women and Child Development Department, Govt. of Maharashtra",
            "url": "https://ladkibahin.maharashtra.gov.in",
            "domain": "ladkibahin.maharashtra.gov.in",
            "badge": "Govt of MH",
            "icon": "👩",
            "description": "Official online registration and installment verification portal for the ₹1,500 monthly financial aid scheme for women aged 21-65 in Maharashtra.",
            "services": [
                "Online Application for Ladki Bahin Scheme",
                "Aadhaar-seeded Bank Account Status Check",
                "Monthly ₹1,500 installment credit tracking",
                "District level grievance resolution"
            ],
            "popular": True
        },

        # =========================================================================
        # 🟣 WEST BENGAL STATE GOVERNMENT PORTALS
        # =========================================================================
        {
            "id": "wb-svmcm",
            "name": "Swami Vivekananda Merit-cum-Means Portal (SVMCM)",
            "state": "West Bengal",
            "category": "Scholarships & Education",
            "department": "Higher Education Department, Government of West Bengal",
            "url": "https://svmcm.wbhed.gov.in",
            "domain": "svmcm.wbhed.gov.in",
            "badge": "Govt of WB",
            "icon": "🟣",
            "description": "Higher education scholarship portal providing annual grants up to ₹60,000 for meritorious students from low-income families in West Bengal.",
            "services": [
                "SVMCM Merit-cum-Means Scholarship application & renewal",
                "Aikyashree (Minority Scholarship) integration",
                "Taruner Swapno (Class 12 Tablet Grant) information",
                "Direct Bank Transfer payment tracking"
            ],
            "popular": True
        },
        {
            "id": "wb-kanyashree",
            "name": "Kanyashree Prakalpa Official Portal",
            "state": "West Bengal",
            "category": "Women & Social Welfare",
            "department": "Women & Child Development and Social Welfare Dept, Govt. of West Bengal",
            "url": "https://www.wbkanyashree.gov.in",
            "domain": "wbkanyashree.gov.in",
            "badge": "Govt of WB",
            "icon": "👩",
            "description": "Official portal of the award-winning Kanyashree scheme managing annual scholarship (K1) and ₹25,000 one-time grant (K2) for girl students.",
            "services": [
                "K1 Annual Scholarship (₹1,000/yr) tracking",
                "K2 One-time Grant (₹25,000 at age 18) verification",
                "Kanyashree ID generation and school transfer",
                "Grievance and direct benefit credit verification"
            ],
            "popular": True
        },

        # =========================================================================
        # 🟢 UTTAR PRADESH STATE GOVERNMENT PORTALS
        # =========================================================================
        {
            "id": "up-scholarship",
            "name": "UP Scholarship & Fee Reimbursement Portal (Saksham UP)",
            "state": "Uttar Pradesh",
            "category": "Scholarships & Education",
            "department": "Social Welfare & Backward Classes Welfare Dept, Government of Uttar Pradesh",
            "url": "https://scholarship.up.gov.in",
            "domain": "scholarship.up.gov.in",
            "badge": "Govt of UP",
            "icon": "🟢",
            "description": "Centralized scholarship portal for all post-matric and professional college students in UP managing full tuition fee reimbursement.",
            "services": [
                "Post-Matric Scholarship for General, SC, ST, OBC & Minorities",
                "Fee Reimbursement (Shulk Pratipoorti) status check",
                "PFMS Direct Benefit Transfer tracking",
                "Institute master verification and attendance monitoring"
            ],
            "popular": True
        },
        {
            "id": "up-esathi",
            "name": "eSathi UP (Citizen Service Portal)",
            "state": "Uttar Pradesh",
            "category": "e-Governance & Certificates",
            "department": "Centre for e-Governance, Government of Uttar Pradesh",
            "url": "https://esathi.up.gov.in",
            "domain": "esathi.up.gov.in",
            "badge": "Govt of UP",
            "icon": "📜",
            "description": "Uttar Pradesh government online service portal for instant application and download of digital Tahsildar certificates.",
            "services": [
                "Jati Praman Patra (Caste Certificate)",
                "Aay Praman Patra (Income Certificate)",
                "Niwas Praman Patra (Domicile / Residence Certificate)",
                "Khatuni (Land Record) extraction"
            ],
            "popular": True
        },

        # =========================================================================
        # 🌴 KERALA STATE GOVERNMENT PORTALS
        # =========================================================================
        {
            "id": "kl-egrantz",
            "name": "E-Grantz 3.0 Kerala (Educational Assistance Portal)",
            "state": "Kerala",
            "category": "Scholarships & Education",
            "department": "Scheduled Castes Development & Backward Classes Welfare Dept, Govt. of Kerala",
            "url": "https://egrantz.kerala.gov.in",
            "domain": "egrantz.kerala.gov.in",
            "badge": "Govt of KL",
            "icon": "🌴",
            "description": "Unified portal providing complete tuition fee reimbursement and monthly stipends for post-matric students of SC, ST, OEC, and OBC in Kerala.",
            "services": [
                "Post-Matric Tuition Fee Reimbursement",
                "Monthly Pocket Money & Day Scholar Maintenance Allowance",
                "Hostel Mess & Accommodation Fee Reimbursement",
                "Akshaya Center assisted registration"
            ],
            "popular": True
        },

        # =========================================================================
        # 🔷 BIHAR STATE GOVERNMENT PORTALS
        # =========================================================================
        {
            "id": "br-serviceplus",
            "name": "ServicePlus Bihar (RTPS Online Citizen Services)",
            "state": "Bihar",
            "category": "e-Governance & Certificates",
            "department": "General Administration Department, Government of Bihar",
            "url": "https://serviceonline.bihar.gov.in",
            "domain": "serviceonline.bihar.gov.in",
            "badge": "Govt of BR",
            "icon": "🔷",
            "description": "Bihar Right to Public Services portal for digital application and certificate download of Caste, Income, and Residential certificates.",
            "services": [
                "Jati Praman Patra (Caste Certificate)",
                "Aay Praman Patra (Income Certificate)",
                "Awasiya Praman Patra (Residential / Domicile Certificate)",
                "Non-Creamy Layer (NCL) Certificate for OBC/EBC"
            ],
            "popular": True
        },
        {
            "id": "br-medhasoft",
            "name": "Medhasoft Bihar (Education Department Portal)",
            "state": "Bihar",
            "category": "Scholarships & Education",
            "department": "Education Department, Government of Bihar",
            "url": "https://medhasoft.bih.nic.in",
            "domain": "medhasoft.bih.nic.in",
            "badge": "Govt of BR",
            "icon": "🎓",
            "description": "Manages Mukhyamantri Kanya Utthan Yojana (₹50,000 for female graduates), bicycle grants, and school uniform allowances across Bihar.",
            "services": [
                "Mukhyamantri Kanya Utthan Yojana (Graduate ₹50,000 Grant)",
                "Class 10th & 12th Board Merit Protsahan Grants",
                "Direct Bank Transfer payment status check"
            ],
            "popular": True
        },

        # =========================================================================
        # 🟤 RAJASTHAN STATE GOVERNMENT PORTALS
        # =========================================================================
        {
            "id": "rj-jansoochna",
            "name": "Jan Soochna Portal Rajasthan (Public Services & Schemes)",
            "state": "Rajasthan",
            "category": "National Gateways",
            "department": "Department of Information Technology & Communication, Govt. of Rajasthan",
            "url": "https://jansoochna.rajasthan.gov.in",
            "domain": "jansoochna.rajasthan.gov.in",
            "badge": "Govt of RJ",
            "icon": "🟤",
            "description": "Pioneering public information portal offering transparent details on Chiranjeevi health benefits, social pensions, and Jan Aadhaar cards.",
            "services": [
                "Jan Aadhaar Card search & family verification",
                "Chiranjeevi Health Insurance entitlement status",
                "Social Security Pension disbursal details",
                "Ration Card and PDS entitlement lookup"
            ],
            "popular": True
        },

        # =========================================================================
        # 🦁 GUJARAT STATE GOVERNMENT PORTALS
        # =========================================================================
        {
            "id": "gj-digitalgujarat",
            "name": "Digital Gujarat (Citizen Services & Scholarships)",
            "state": "Gujarat",
            "category": "Scholarships & Education",
            "department": "Science and Technology Department, Government of Gujarat",
            "url": "https://www.digitalgujarat.gov.in",
            "domain": "digitalgujarat.gov.in",
            "badge": "Govt of GJ",
            "icon": "🦁",
            "description": "Unified platform for post-matric scholarships, Mukhyamantri Yuva Swavalamban Yojana (MYSY), and revenue certificates in Gujarat.",
            "services": [
                "Mukhyamantri Yuva Swavalamban Yojana (MYSY Tuition Grant)",
                "Post-Matric Scholarships for SC, ST, SEBC & EWS",
                "Tahsildar Income & Caste Certificates",
                "Digital locker and e-Seva services"
            ],
            "popular": True
        },

        # =========================================================================
        # 🐯 MADHYA PRADESH STATE GOVERNMENT PORTALS
        # =========================================================================
        {
            "id": "mp-samagra",
            "name": "Samagra Samajik Suraksha Mission (MP Samagra Portal)",
            "state": "Madhya Pradesh",
            "category": "e-Governance & Certificates",
            "department": "Social Justice & Disabled Persons Welfare Dept, Govt. of Madhya Pradesh",
            "url": "https://samagra.gov.in",
            "domain": "samagra.gov.in",
            "badge": "Govt of MP",
            "icon": "🐯",
            "description": "Madhya Pradesh's foundational citizen registry enabling Aadhaar eKYC, Ladli Behna enrollment, and educational fee scholarships.",
            "services": [
                "Samagra Family ID & Member ID Search",
                "Aadhaar e-KYC Verification for Ladli Behna Scheme",
                "Mukhyamantri Medhavi Chhatra Yojana (MMVY) linkage",
                "BPL verification and social pensions"
            ],
            "popular": True
        },

        # =========================================================================
        # 🏛️ DELHI (NCT) GOVERNMENT PORTALS
        # =========================================================================
        {
            "id": "dl-edistrict",
            "name": "e-District Delhi (Citizen Services Portal)",
            "state": "Delhi",
            "category": "e-Governance & Certificates",
            "department": "Revenue Department, Government of NCT of Delhi",
            "url": "https://edistrict.delhigovt.nic.in",
            "domain": "edistrict.delhigovt.nic.in",
            "badge": "Govt of DL",
            "icon": "🏛️",
            "description": "Online service portal for Delhi residents to apply for Domicile, SC/ST/OBC certificates, higher education loan guarantee, and Jai Bhim coaching.",
            "services": [
                "Delhi Higher Education & Skill Development Guarantee Loan",
                "Jai Bhim Mukhyamantri Pratibha Vikas Yojana Registration",
                "Income & Caste Certificates issued by SDM",
                "Delhi Domicile Certificate"
            ],
            "popular": True
        },

        # =========================================================================
        # 🌾 PUNJAB STATE GOVERNMENT PORTALS
        # =========================================================================
        {
            "id": "pb-scholarship",
            "name": "Dr. Ambedkar Scholarship Portal Punjab",
            "state": "Punjab",
            "category": "Scholarships & Education",
            "department": "Department of Social Justice, Empowerment and Minorities, Govt. of Punjab",
            "url": "https://scholarships.punjab.gov.in",
            "domain": "scholarships.punjab.gov.in",
            "badge": "Govt of PB",
            "icon": "🌾",
            "description": "Centralized scholarship portal managing Post-Matric fee concessions and Ashirwad marriage assistance in Punjab.",
            "services": [
                "Post-Matric Scholarship for SC and BC students",
                "Punjab Ashirwad Scheme (₹51,000 Marriage Grant) tracking",
                "Free Bus Pass for Students",
                "Institute registration and verification"
            ],
            "popular": True
        },

        # =========================================================================
        # 🏖️ ODISHA STATE GOVERNMENT PORTALS
        # =========================================================================
        {
            "id": "od-scholarship",
            "name": "Odisha State Scholarship Portal",
            "state": "Odisha",
            "category": "Scholarships & Education",
            "department": "Electronics & IT Department, Government of Odisha",
            "url": "https://scholarship.odisha.gov.in",
            "domain": "scholarship.odisha.gov.in",
            "badge": "Govt of OD",
            "icon": "🏖️",
            "description": "Unified platform managing 25+ scholarship schemes across Higher Education, SC/ST, and Agriculture departments in Odisha.",
            "services": [
                "Post-Matric Scholarship for ST/SC/OBC/SEBC/General",
                "e-Medhabruti (Higher Education Merit Scholarship)",
                "KALIA Scholarship for children of farmers",
                "Direct Bank Transfer payment tracking"
            ],
            "popular": True
        },

        # =========================================================================
        # 🍃 ASSAM & NORTH EAST GOVERNMENT PORTALS
        # =========================================================================
        {
            "id": "as-sewasetu",
            "name": "Sewa Setu Assam (Right to Public Services Portal)",
            "state": "Assam",
            "category": "e-Governance & Certificates",
            "department": "Administrative Reforms and Training Department, Government of Assam",
            "url": "https://sewasetu.assam.gov.in",
            "domain": "sewasetu.assam.gov.in",
            "badge": "Govt of AS",
            "icon": "🍃",
            "description": "Unified citizen portal delivering 500+ services including Orunodoi basic income, Caste & Income certificates, and Pragyan Bharati fee concessions.",
            "services": [
                "Orunodoi 2.0 Direct Income Assistance Status",
                "Permanent Resident Certificate (PRC)",
                "Income & Caste Certificates",
                "Pragyan Bharati Higher Education Fee Waiver"
            ],
            "popular": True
        },

        # =========================================================================
        # 🌲 JHARKHAND STATE GOVERNMENT PORTALS
        # =========================================================================
        {
            "id": "jh-ekalyan",
            "name": "E-Kalyan Jharkhand (Scholarship & Welfare Portal)",
            "state": "Jharkhand",
            "category": "Scholarships & Education",
            "department": "Scheduled Tribe, SC, Minority and BC Welfare Dept, Govt. of Jharkhand",
            "url": "https://ekalyan.cgg.gov.in",
            "domain": "ekalyan.cgg.gov.in",
            "badge": "Govt of JH",
            "icon": "🌲",
            "description": "Post-Matric scholarship portal managing full fee reimbursement and maintenance allowances for SC, ST, and BC students of Jharkhand.",
            "services": [
                "Post-Matric Scholarship within & outside state",
                "Pre-Matric Scholarship tracking",
                "DBT bank account seeding check"
            ],
            "popular": True
        },

        # =========================================================================
        # 🌾 CHHATTISGARH STATE GOVERNMENT PORTALS
        # =========================================================================
        {
            "id": "cg-mahtari",
            "name": "Mahtari Vandan Yojana Official Portal",
            "state": "Chhattisgarh",
            "category": "Women & Social Welfare",
            "department": "Women & Child Development Department, Govt. of Chhattisgarh",
            "url": "https://mahtarivandan.cgstate.gov.in",
            "domain": "mahtarivandan.cgstate.gov.in",
            "badge": "Govt of CG",
            "icon": "🌾",
            "description": "Official citizen portal for registration, beneficiary status, and ₹1,000 monthly DBT tracking for married women in Chhattisgarh.",
            "services": [
                "Mahtari Vandan Application Status Search",
                "Aadhaar-linked Bank Account DBT check",
                "Objection & Grievance redressal"
            ],
            "popular": True
        },

        # =========================================================================
        # 🏖️ GOA STATE GOVERNMENT PORTALS
        # =========================================================================
        {
            "id": "ga-services",
            "name": "Goa Online Services Portal (e-District Goa)",
            "state": "Goa",
            "category": "e-Governance & Certificates",
            "department": "Department of Information Technology, Government of Goa",
            "url": "https://services.goa.gov.in",
            "domain": "services.goa.gov.in",
            "badge": "Govt of GA",
            "icon": "🏖️",
            "description": "Unified platform for 150+ Goa government citizen services: Griha Aadhar, DSSS pension, Residence, Caste, and Income certificates.",
            "services": [
                "Griha Aadhar Scheme for Homemakers",
                "Dayanand Social Security Scheme (DSSS)",
                "Residence & Income Certificates",
                "Caste and Community certificates"
            ],
            "popular": True
        },

        # =========================================================================
        # 🏔️ HIMACHAL PRADESH STATE GOVERNMENT PORTALS
        # =========================================================================
        {
            "id": "hp-eseva",
            "name": "eSewa Himachal Pradesh (Citizen Services Portal)",
            "state": "Himachal Pradesh",
            "category": "e-Governance & Certificates",
            "department": "Department of Digital Technologies and Governance, Govt. of HP",
            "url": "https://eseva.hp.gov.in",
            "domain": "eseva.hp.gov.in",
            "badge": "Govt of HP",
            "icon": "🏔️",
            "description": "Online service delivery for Pyari Behna Sukh Samman Nidhi, Bonafide Himachali, Income, and Agricultural certificates.",
            "services": [
                "Indira Gandhi Pyari Behna Scheme (₹1,500/mo) status",
                "Bonafide Himachali Certificate",
                "Income & Agriculturist Certificates"
            ],
            "popular": True
        },

        # =========================================================================
        # ⛰️ UTTARAKHAND STATE GOVERNMENT PORTALS
        # =========================================================================
        {
            "id": "uk-nandagaura",
            "name": "Nanda Gaura Yojana Official Portal",
            "state": "Uttarakhand",
            "category": "Women & Social Welfare",
            "department": "Women Empowerment & Child Development Department, Govt. of Uttarakhand",
            "url": "https://nandagaura.uk.gov.in",
            "domain": "nandagaura.uk.gov.in",
            "badge": "Govt of UK",
            "icon": "⛰️",
            "description": "Official portal managing ₹51,000 financial assistance grants for girl students completing Class 12 entering higher education in Uttarakhand.",
            "services": [
                "Nanda Gaura Online Application & Status",
                "Document verification and approval workflow",
                "DBT fund disbursement tracking"
            ],
            "popular": True
        },

        # =========================================================================
        # ❄️ JAMMU AND KASHMIR (UT) GOVERNMENT PORTALS
        # =========================================================================
        {
            "id": "jk-sehat",
            "name": "PM-JAY SEHAT Portal (Universal Health J&K)",
            "state": "Jammu and Kashmir",
            "category": "Healthcare",
            "department": "State Health Agency, Government of Jammu and Kashmir",
            "url": "https://sehat.jk.gov.in",
            "domain": "sehat.jk.gov.in",
            "badge": "Govt of JK",
            "icon": "❄️",
            "description": "Universal health coverage portal for 100% families of J&K providing Golden Card generation and cashless hospital searches.",
            "services": [
                "SEHAT Golden Card Verification & Download",
                "Empanelled Public & Private Hospital search",
                "Treatment pre-authorization status"
            ],
            "popular": True
        },

        # =========================================================================
        # 🏖️ PUDUCHERRY (UT) GOVERNMENT PORTALS
        # =========================================================================
        {
            "id": "py-dhte",
            "name": "DHTE Puducherry (Higher & Technical Education)",
            "state": "Puducherry",
            "category": "Scholarships & Education",
            "department": "Directorate of Higher & Technical Education, Govt. of Puducherry",
            "url": "https://dhte.py.gov.in",
            "domain": "dhte.py.gov.in",
            "badge": "Govt of PY",
            "icon": "🏖️",
            "description": "Manages the Perunthalaivar Kamarajar Financial Assistance Scheme providing 100% tuition reimbursement for CENTAC students in Puducherry.",
            "services": [
                "Perunthalaivar Kamarajar Tuition Reimbursement",
                "CENTAC counseling financial concessions",
                "Post-Matric scholarship disbursals"
            ],
            "popular": True
        },

        # =========================================================================
        # 🥛 HARYANA STATE GOVERNMENT PORTALS
        # =========================================================================
        {
            "id": "hr-chhatravratti",
            "name": "Har-Chhatravratti Haryana (State Scholarship Portal)",
            "state": "Haryana",
            "category": "Scholarships & Education",
            "department": "Higher Education Department, Government of Haryana",
            "url": "https://harchhatravratti.highereduhry.ac.in",
            "domain": "harchhatravratti.highereduhry.ac.in",
            "badge": "Govt of HR",
            "icon": "🥛",
            "description": "Centralized scholarship portal for all post-matric and higher education scholarships integrated with Parivar Pehchan Patra (PPP).",
            "services": [
                "Post-Matric Scholarship for SC, BC & Meritorious",
                "Parivar Pehchan Patra (PPP) verification",
                "Direct Bank Transfer payment tracking"
            ],
            "popular": True
        }
    ]
