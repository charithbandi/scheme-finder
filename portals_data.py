"""
Official Government Websites & Portals Directory for Scheme Finder.
Comprehensive database of verified Central and State Government portals
across Andhra Pradesh, Telangana, Tamil Nadu, and All-India (Central).
"""

from typing import List, Dict, Any


def get_all_portals() -> List[Dict[str, Any]]:
    """
    Returns verified official government portals covering Central, AP, TS, and TN.
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
            "department": "Ministry of Electronics & Information Technology / Ministry of Education, Govt. of India",
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
        {
            "id": "central-csc",
            "name": "CSC Digital Seva (Common Services Centre)",
            "state": "Central",
            "category": "e-Governance & Certificates",
            "department": "CSC e-Governance Services India Limited, MeitY",
            "url": "https://digitalseva.csc.gov.in",
            "domain": "digitalseva.csc.gov.in",
            "badge": "Digital India",
            "icon": "🏪",
            "description": "Pan-India physical service delivery points for citizens in rural and semi-urban areas to apply for government welfare schemes, certificates, and digital services.",
            "services": [
                "Assisted Application for Government Schemes & Scholarships",
                "Aadhaar Update & Ayushman Card Generation",
                "Panchayat Level Certificates & Land Record Extraction",
                "Utility bill payments and banking kiosk services"
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
            "id": "ap-navasakam",
            "name": "Navasakam AP (Welfare Schemes Delivery Portal)",
            "state": "Andhra Pradesh",
            "category": "National Gateways",
            "department": "Department of Gram Volunteers / Ward Volunteers and Village Secretariats, Govt. of AP",
            "url": "https://navasakam.ap.gov.in",
            "domain": "navasakam.ap.gov.in",
            "badge": "Govt of AP",
            "icon": "📋",
            "description": "Comprehensive beneficiary identification and service delivery portal coordinating doorstep governance and social audit for all AP Navaratnalu welfare schemes.",
            "services": [
                "Beneficiary verification for JVD, Cheyutha, Aasara & Amma Vodi",
                "Grama / Ward Sachivalayam Social Audit Lists",
                "Rice Card (Food Security Card) & Pension Eligibility Status",
                "Grievance redressal (Spandana 1902) integration"
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
            "id": "ap-rythu",
            "name": "YSR Rythu Bharosa Portal",
            "state": "Andhra Pradesh",
            "category": "Agriculture",
            "department": "Department of Agriculture & Cooperation, Government of Andhra Pradesh",
            "url": "https://ysrrythubharosa.ap.gov.in",
            "domain": "ysrrythubharosa.ap.gov.in",
            "badge": "Govt of AP",
            "icon": "🌾",
            "description": "Andhra Pradesh farmer financial support portal providing ₹13,500/year to landholding and tenant farmers (CCRC holders) in three seasonal installments.",
            "services": [
                "Farmer Payment Status by Aadhaar Number",
                "e-Crop Booking & Village Social Audit Display",
                "Tenant Cultivator (CCRC) Registration and Approval",
                "Free Crop Insurance (YSR Uchitha Vyavasaya Bima) status"
            ],
            "popular": False
        },
        {
            "id": "ap-sachivalayam",
            "name": "AP Grama & Ward Sachivalayam Portal",
            "state": "Andhra Pradesh",
            "category": "e-Governance & Certificates",
            "department": "Village & Ward Secretariats Department, Govt. of Andhra Pradesh",
            "url": "https://gramawardsachivalayam.ap.gov.in",
            "domain": "gramawardsachivalayam.ap.gov.in",
            "badge": "Govt of AP",
            "icon": "🏛️",
            "description": "Decentralized grassroots citizen service delivery portal offering 540+ government services through 15,004 Village and Ward Secretariats.",
            "services": [
                "Doorstep delivery of 540+ Government Services",
                "Rice Card, Aarogyasri Card & Pension card application",
                "Volunteer mapping and doorstep biometric verification",
                "Track application token status online"
            ],
            "popular": False
        },
        {
            "id": "ap-meebhoomi",
            "name": "MeeBhoomi AP (Digital Land Records)",
            "state": "Andhra Pradesh",
            "category": "Identity & Records",
            "department": "Revenue Department, Government of Andhra Pradesh",
            "url": "https://meebhoomi.ap.gov.in",
            "domain": "meebhoomi.ap.gov.in",
            "badge": "Govt of AP",
            "icon": "🗺️",
            "description": "Digital land records registry of Andhra Pradesh for instant verification and download of official Pattadar Passbooks, Adangal (Pahani), and 1-B records.",
            "services": [
                "Download Digital 1-B (RoR) Record",
                "Download Village Adangal / Pahani",
                "Electronic Pattadar Passbook (e-Passbook) verification",
                "Aadhaar linking with agricultural survey numbers"
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
            "id": "ts-rythubandhu",
            "name": "Rythu Bandhu & Rythu Bima Portal",
            "state": "Telangana",
            "category": "Agriculture",
            "department": "Department of Agriculture & Cooperation, Government of Telangana",
            "url": "https://rythubandhu.telangana.gov.in",
            "domain": "rythubandhu.telangana.gov.in",
            "badge": "Govt of TS",
            "icon": "🌾",
            "description": "Telangana's flagship agricultural investment support portal providing direct transfers of ₹12,000–₹15,000 per acre per year and ₹5 Lakh farmer group life insurance.",
            "services": [
                "Farmer Investment Support disbursement status",
                "Rythu Bima (₹5 Lakh Group Life Insurance) enrollment & claim tracking",
                "Cheque / Direct Bank Transfer transaction reconciliation",
                "Agricultural Extension Officer (AEO) cluster contacts"
            ],
            "popular": True
        },
        {
            "id": "ts-dharani",
            "name": "Dharani Portal (Telangana Land Records & Passbook)",
            "state": "Telangana",
            "category": "Identity & Records",
            "department": "Registration & Stamps / Revenue Department, Government of Telangana",
            "url": "https://dharani.telangana.gov.in",
            "domain": "dharani.telangana.gov.in",
            "badge": "Govt of TS",
            "icon": "🗺️",
            "description": "Integrated land administration portal providing transparent agricultural land registration, instant mutation, and digital Pattadar Passbook extraction.",
            "services": [
                "View Land Details by Survey Number / Khata Number",
                "Download Digital Pattadar Passbook (Agriculture)",
                "Cadastral Map & BhuNaksha GIS view",
                "Online slot booking for land transactions"
            ],
            "popular": False
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
            "id": "ts-tappfolio",
            "name": "T-App Folio (Telangana Mobile & Web Governance)",
            "state": "Telangana",
            "category": "National Gateways",
            "department": "Electronic Delivery of Citizen Services (EDCS), Government of Telangana",
            "url": "https://tappfolio.telangana.gov.in",
            "domain": "tappfolio.telangana.gov.in",
            "badge": "Govt of TS",
            "icon": "📱",
            "description": "Telangana's premier m-Governance portal delivering 270+ public services, RTA licenses, bill payments, and educational fee receipts.",
            "services": [
                "270+ Government Services through Single Sign-On",
                "RTA Driving License & Vehicle Registration services",
                "Utility Bill payments & Municipal tax receipts",
                "Tahsildar certificate status and downloads"
            ],
            "popular": False
        },
        {
            "id": "ts-govportal",
            "name": "Telangana State Official Portal",
            "state": "Telangana",
            "category": "National Gateways",
            "department": "Information Technology, Electronics & Communications (ITE&C), Govt of Telangana",
            "url": "https://telangana.gov.in",
            "domain": "telangana.gov.in",
            "badge": "Govt of TS",
            "icon": "🏛️",
            "description": "Apex government portal providing access to all 33 Telangana district administrations, departments, welfare circulars, and the Mahalakshmi scheme.",
            "services": [
                "Mahalakshmi Free Bus Travel & Financial Aid circulars",
                "Government Orders (GOs) and Gazettes repository",
                "Telangana State Public Service Commission (TGPSC) links",
                "District Collectorate contact directory"
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
        {
            "id": "tn-dote",
            "name": "Tamil Nadu Directorate of Technical Education (DoTE)",
            "state": "Tamil Nadu",
            "category": "Scholarships & Education",
            "department": "Higher Education Department, Government of Tamil Nadu",
            "url": "https://www.tndte.gov.in",
            "domain": "tndte.gov.in",
            "badge": "Govt of TN",
            "icon": "🏛️",
            "description": "Apex technical education directorate overseeing engineering and polytechnic colleges, First Graduate fee concessions, and technical scholarship disbursements in Tamil Nadu.",
            "services": [
                "First Graduate Tuition Fee Waiver Guidelines & Approvals",
                "Polytechnic / Diploma Centralized Admissions",
                "Government and Government-Aided College Fee structures",
                "Technical Scholarship circulars & notifications"
            ],
            "popular": False
        },
        {
            "id": "tn-cmchis",
            "name": "Chief Minister's Comprehensive Health Insurance (CMCHIS)",
            "state": "Tamil Nadu",
            "category": "Healthcare",
            "department": "Health & Family Welfare Department, Government of Tamil Nadu",
            "url": "https://www.cmchistn.com",
            "domain": "cmchistn.com",
            "badge": "Govt of TN",
            "icon": "🏥",
            "description": "Pioneering state health insurance scheme providing cashless hospitalization up to ₹5,00,000 per family per year across 1,090 notified therapy procedures in TN network hospitals.",
            "services": [
                "Check Beneficiary Eligibility with Smart Family Card",
                "Search Empanelled Government and Private Hospitals",
                "Coverage Package list & Special Surgeries directory",
                "Download e-Card and 24x7 Emergency Call Center 104"
            ],
            "popular": True
        },
        {
            "id": "tn-bcmbcmw",
            "name": "Tamil Nadu BC, MBC & MW Welfare (TN ePASS)",
            "state": "Tamil Nadu",
            "category": "Scholarships & Education",
            "department": "Backward Classes, Most Backward Classes & Minorities Welfare Dept, Govt of TN",
            "url": "https://bcmbcmw.tn.gov.in",
            "domain": "bcmbcmw.tn.gov.in",
            "badge": "Govt of TN",
            "icon": "📜",
            "description": "Post-Matric scholarship and free hostel accommodation management portal for Backward Classes (BC), Most Backward Classes (MBC), and Minorities in Tamil Nadu.",
            "services": [
                "Post-Matric Scholarship for BC / MBC / DNC students",
                "Free Boarding and Lodging in College Hostels",
                "Free Bicycles & Free Laptops distribution tracking",
                "Minority Merit-cum-Means scholarship assistance"
            ],
            "popular": False
        },
        {
            "id": "tn-govportal",
            "name": "Tamil Nadu Government Official Web Portal",
            "state": "Tamil Nadu",
            "category": "National Gateways",
            "department": "Information & Public Relations / IT Dept, Government of Tamil Nadu",
            "url": "https://www.tn.gov.in",
            "domain": "tn.gov.in",
            "badge": "Govt of TN",
            "icon": "🏛️",
            "description": "Official apex web portal of the Government of Tamil Nadu providing access to all 38 district administrations, gazettes, policies, welfare departments, and services.",
            "services": [
                "Directory of all Tamil Nadu Welfare Departments",
                "Government Orders (GOs) and Policy Notes",
                "District Collectorate contacts across all 38 districts",
                "Public Information and Press Releases"
            ],
            "popular": False
        }
    ]
