/**
 * Scheme Finder - Frontend Client Application
 * Handles user profile submissions, rule evaluation, dynamic results rendering,
 * checklist dialog management, and interactive state & category filtering.
 */

// Global State
let currentSchemesData = [];
let activeSchemeForModal = null;
let currentProfile = {};

// Comprehensive Fallback schemes dataset in case backend is run in static mode
const FALLBACK_SCHEMES = [
  // 🟡 Andhra Pradesh Schemes
  {
    id: "ap-jvd-01",
    name: "Jagananna Vidya Deevena (RTF - Full Fee Reimbursement)",
    department: "Higher Education & Social Welfare Department, Govt. of Andhra Pradesh",
    category_type: "Education",
    state: "Andhra Pradesh",
    description: "100% total tuition fee reimbursement to eligible students pursuing ITI, Polytechnic, Degree, B.Tech, Pharmacy, MBA, MCA, and Medicine in AP.",
    benefit: "100% Complete Tuition Fee Reimbursement directly credited to college/mother's bank account",
    official_portal_url: "https://jnanabhumi.ap.gov.in",
    documents: [
      "Rice Card / White Ration Card",
      "Meeseva Income Certificate (≤ ₹2.5 Lakh/annum)",
      "Integrated Community / Caste Certificate (SC/ST/BC/EBC/Minority/Kapu)",
      "Class 10th (SSC) & Intermediate Marks Memo",
      "College Admission Allotment Order (Convenor Quota)",
      "Mother's Aadhaar Card & Active Bank Passbook"
    ],
    rules: [
      { attr: "income", op: "<=", target: 250000, text: "Annual family income does not exceed ₹2,50,000" }
    ]
  },
  {
    id: "ap-jvd-mtf-02",
    name: "Jagananna Vasathi Deevena (MTF - Food & Hostel Allowance)",
    department: "Social Welfare & Backward Classes Welfare Dept., Govt. of Andhra Pradesh",
    category_type: "Education",
    state: "Andhra Pradesh",
    description: "Direct financial aid to meet boarding, mess, and hostel expenses for post-matric college students in Andhra Pradesh.",
    benefit: "₹10,000/yr for ITI, ₹15,000/yr for Polytechnic, ₹20,000/yr for Degree/B.Tech/MBBS",
    official_portal_url: "https://jnanabhumi.ap.gov.in",
    documents: [
      "White Ration Card / Rice Card copy",
      "College Bonafide & Hostel Stay Certificate",
      "Student & Mother's Aadhaar Cards",
      "Mother's NPCI Aadhaar-seeded Bank Passbook"
    ],
    rules: [
      { attr: "income", op: "<=", target: 250000, text: "Household annual income within ₹2.5 Lakh limit" }
    ]
  },
  {
    id: "ap-aarogyasri-03",
    name: "Dr. YSR Aarogyasri Health Scheme",
    department: "Dr. YSR Aarogyasri Health Care Trust, Govt. of Andhra Pradesh",
    category_type: "Healthcare",
    state: "Andhra Pradesh",
    description: "Premier health insurance offering universal cashless medical care across empanelled super-specialty hospitals.",
    benefit: "100% Cashless treatment up to ₹25,00,000 per family per year covering 3,257 treatments",
    official_portal_url: "https://ysraarogyasri.ap.gov.in",
    documents: [
      "Dr. YSR Aarogyasri Health Card / Rice Card",
      "Aadhaar Card of all family members",
      "Income Certificate or Proof of Land Holding"
    ],
    rules: [
      { attr: "income", op: "<=", target: 500000, text: "Annual family income does not exceed ₹5,00,000 ceiling" }
    ]
  },
  {
    id: "ap-rythu-04",
    name: "YSR Rythu Bharosa - PM KISAN",
    department: "Department of Agriculture & Cooperation, Govt. of Andhra Pradesh",
    category_type: "Agriculture",
    state: "Andhra Pradesh",
    description: "Direct financial assistance to farmer and tenant families (including SC/ST/BC/Minority tenant farmers) before crop sowing.",
    benefit: "₹13,500 per year per farmer family paid in three seasonal installments",
    official_portal_url: "https://ysrrythubharosa.ap.gov.in",
    documents: [
      "Pattadar Passbook / Land 1B Record (or Tenant CCRC Card)",
      "Farmer Aadhaar Card",
      "Active Bank Account seeded with Aadhaar"
    ],
    rules: [
      { attr: "income", op: "<=", target: 400000, text: "Farming household income bracket satisfied" }
    ]
  },

  // 🔵 Telangana Schemes
  {
    id: "ts-epass-01",
    name: "Telangana ePASS Post-Matric Scholarship & Fee Reimbursement (RTF & MTF)",
    department: "Scheduled Castes, BC, Tribal & Minority Welfare Departments, Govt. of Telangana",
    category_type: "Education",
    state: "Telangana",
    description: "Reimburses 100% of college tuition fees (RTF) and pays monthly maintenance allowance (MTF) to students in Telangana.",
    benefit: "100% Tuition Fee Reimbursement + up to ₹12,000/yr Hostel & Mess Allowance",
    official_portal_url: "https://telanganaepass.cgg.gov.in",
    documents: [
      "Meeseva Caste Certificate with CND Number",
      "Meeseva Income Certificate issued by Tahsildar",
      "SSC (Class 10) Memo / Hall Ticket Number",
      "College Allotment Order & Joining Report (DOST / TS EAMCET / TS ICET)",
      "Student Aadhaar-linked Bank Account Passbook"
    ],
    rules: [
      { attr: "income", op: "<=", target: 200000, text: "Family income within ₹2,00,000 ceiling" }
    ]
  },
  {
    id: "ts-mahalakshmi-02",
    name: "Mahalakshmi Scheme (Free Bus Travel & Financial Aid for Women)",
    department: "Transport Department & Women Development & Child Welfare, Govt. of Telangana",
    category_type: "Women Empowerment",
    state: "Telangana",
    description: "Empowers women and girls in Telangana with 100% free bus travel across TSRTC buses, and ₹2,500/month financial aid.",
    benefit: "100% Free Travel in TSRTC Express & Palle Velugu buses + ₹2,500/month financial aid",
    official_portal_url: "https://telangana.gov.in",
    documents: [
      "Telangana Domicile Aadhaar Card with residential address",
      "Food Security Card (FSC) / White Ration Card",
      "Active Bank Account seeded with Aadhaar"
    ],
    rules: [
      { attr: "gender", op: "==", target: "Female", text: "Targeted for girls and women residents of Telangana" }
    ]
  },
  {
    id: "ts-aarogyasri-03",
    name: "Rajiv Aarogyasri Telangana (Universal Health Coverage)",
    department: "Aarogyasri Health Care Trust, Government of Telangana",
    category_type: "Healthcare",
    state: "Telangana",
    description: "Cashless healthcare scheme covering 1,672 treatments in network hospitals across Telangana.",
    benefit: "Cashless medical hospitalization and surgery cover up to ₹10,00,000 per family per year",
    official_portal_url: "https://aarogyasri.telangana.gov.in",
    documents: [
      "Telangana Food Security Card (White Ration Card) / Aarogyasri Card",
      "Aadhaar Card of patient and family members"
    ],
    rules: [
      { attr: "income", op: "<=", target: 500000, text: "Annual family income within ₹5 Lakh threshold" }
    ]
  },
  {
    id: "ts-kalyana-05",
    name: "Kalyana Lakshmi & Shaadi Mubarak Scheme",
    department: "Scheduled Castes Development & BC Welfare Dept., Govt. of Telangana",
    category_type: "Social Welfare",
    state: "Telangana",
    description: "Financial assistance to unmarried brides aged 18+ from underprivileged families to alleviate marriage distress.",
    benefit: "One-time direct financial grant of ₹1,00,116 credited to the bride's mother's account",
    official_portal_url: "https://telanganaepass.cgg.gov.in",
    documents: [
      "Bride & Groom Age Proof / SSC Certificate",
      "Marriage Registration / Invitation Card",
      "Tahsildar Income Certificate (≤ ₹2,00,000)",
      "Meeseva Caste Certificate"
    ],
    rules: [
      { attr: "gender", op: "==", target: "Female", text: "Beneficiary is an unmarried bride aged 18+" },
      { attr: "income", op: "<=", target: 200000, text: "Annual family income does not exceed ₹2 Lakh limit" }
    ]
  },

  // 🔴 Tamil Nadu Schemes
  {
    id: "tn-pudhumai-01",
    name: "Moovalur Ramamirtham Ammaiyar Pudhumai Penn Scheme",
    department: "Social Welfare & Women Empowerment Dept., Government of Tamil Nadu",
    category_type: "Women Empowerment",
    state: "Tamil Nadu",
    description: "Monthly financial incentive to encourage girls who studied in Tamil Nadu Government schools to pursue higher education.",
    benefit: "₹1,000 per month deposited directly into student's bank account until degree completion",
    official_portal_url: "https://pudhumaipenn.tn.gov.in",
    documents: [
      "Tamil Nadu Domicile / Nativity Certificate",
      "Government School Study Certificate (Class 6th to 12th in TN Govt School)",
      "College Admission Card / Bonafide Certificate",
      "Aadhaar Card",
      "Student's individual Bank Passbook copy"
    ],
    rules: [
      { attr: "gender", op: "==", target: "Female", text: "Applicable for female students" }
    ]
  },
  {
    id: "tn-first-grad-02",
    name: "Tamil Nadu First Graduate (FG) Tuition Fee Concession",
    department: "Directorate of Technical Education (DoTE), Tamil Nadu",
    category_type: "Education",
    state: "Tamil Nadu",
    description: "Complete waiver of tuition fees for students who are the first person in their family to complete a professional degree.",
    benefit: "Complete Tuition Fee Waiver (up to ₹25,000 - ₹50,000 per year throughout the course)",
    official_portal_url: "https://www.tndte.gov.in",
    documents: [
      "First Graduate Certificate issued by Headquarter Deputy Tahsildar",
      "Joint Declaration signed by Parent and Student",
      "No Graduate in Family Verification from VAO",
      "Ration Card / Smart Family Card copy",
      "Allotment Order from Single Window Counseling (TNEA)"
    ],
    rules: [
      { attr: "is_first_graduate", op: "==", target: true, text: "First graduate in family verified" }
    ]
  },
  {
    id: "tn-kmut-03",
    name: "Kalaignar Magalir Urimai Thittam (KMUT - Monthly Basic Income)",
    department: "Special Programme Implementation Dept., Government of Tamil Nadu",
    category_type: "Women Empowerment",
    state: "Tamil Nadu",
    description: "Universal basic income rights grant acknowledging women's unpaid household labor with ₹1,000 monthly.",
    benefit: "Direct monthly bank deposit of ₹1,000 (₹12,000 per year) directly to women heads of family",
    official_portal_url: "https://kmut.tn.gov.in",
    documents: [
      "Tamil Nadu Smart Family Card (Ration Card)",
      "Aadhaar Card",
      "Electricity Consumer Number",
      "Bank Account Passbook seeded with Aadhaar"
    ],
    rules: [
      { attr: "gender", op: "==", target: "Female", text: "Recipient must be a female head of household" },
      { attr: "income", op: "<=", target: 250000, text: "Annual family income is less than ₹2.5 Lakh" }
    ]
  },
  {
    id: "tn-cmchis-04",
    name: "Chief Minister's Comprehensive Health Insurance Scheme (CMCHIS)",
    department: "Health & Family Welfare Department, Government of Tamil Nadu",
    category_type: "Healthcare",
    state: "Tamil Nadu",
    description: "Cashless medical and surgical care for 1,090 notified therapy procedures across network hospitals.",
    benefit: "Cashless hospitalization cover up to ₹5,00,000 per family per year",
    official_portal_url: "https://www.cmchistn.com",
    documents: [
      "Tamil Nadu Smart Family Card / Ration Card",
      "Income Certificate from Revenue Authority (≤ ₹1.2 Lakh/yr)",
      "Aadhaar Cards of all enrolled family members"
    ],
    rules: [
      { attr: "income", op: "<=", target: 120000, text: "Annual family income does not exceed ₹1,20,000 ceiling" }
    ]
  },

  // 🇮🇳 Central Schemes
  {
    id: "central-csss-01",
    name: "Central Sector Scheme of Scholarship for College & University Students",
    department: "Department of Higher Education, Ministry of Education, Govt. of India",
    category_type: "Education",
    state: "All India",
    description: "Financial assistance to meritorious students from low-income families to meet expenses while pursuing college studies.",
    benefit: "₹12,000/year (UG) to ₹20,000/year (PG)",
    official_portal_url: "https://scholarships.gov.in",
    documents: [
      "Aadhaar Card (linked with bank account)",
      "Income Certificate (≤ ₹4.5 Lakh ceiling)",
      "Class 12th Board Marksheet (Top 20th percentile)",
      "College Admission Bonafide Certificate",
      "Bank Account Passbook (DBT enabled)"
    ],
    rules: [
      { attr: "income", op: "<=", target: 450000, text: "Annual family income within ₹4.5 Lakh ceiling" },
      { attr: "marks", op: ">=", target: 80, text: "Class 12 marks meet 80% percentile threshold" }
    ]
  },
  {
    id: "central-pragati-02",
    name: "AICTE Pragati Scholarship Scheme for Girl Students (Technical Degree)",
    department: "All India Council for Technical Education (AICTE)",
    category_type: "Women Empowerment",
    state: "All India",
    description: "Empowering female students in AICTE-approved technical engineering and diploma institutions.",
    benefit: "₹50,000 per annum towards college fee & equipment",
    official_portal_url: "https://www.aicte-india.org/schemes/students-development-schemes/pragati",
    documents: [
      "Aadhaar Card",
      "Family Income Certificate (below ₹8 Lakh/annum)",
      "Class 10th and 12th Marksheets",
      "Admission Letter to 1st year Degree/Diploma",
      "Bank Account Passbook in applicant's name"
    ],
    rules: [
      { attr: "gender", op: "==", target: "Female", text: "Targeted exclusively for female students" },
      { attr: "income", op: "<=", target: 800000, text: "Family income within ₹8 Lakh ceiling" },
      { attr: "marks", op: ">=", target: 60, text: "Qualifying examination score ≥ 60%" }
    ]
  },
  {
    id: "central-pmjay-04",
    name: "Ayushman Bharat - Pradhan Mantri Jan Arogya Yojana (PM-JAY)",
    department: "National Health Authority (NHA), Ministry of Health & Family Welfare",
    category_type: "Healthcare",
    state: "All India",
    description: "Cashless secondary and tertiary hospitalization cover across public and empanelled private hospitals nationwide.",
    benefit: "Cashless health insurance cover up to ₹5,00,000 per family per year",
    official_portal_url: "https://pmjay.gov.in",
    documents: [
      "Aadhaar Card of all family members",
      "Ration Card / BPL Card / SECC 2011 Household ID",
      "Income Certificate"
    ],
    rules: [
      { attr: "income", op: "<=", target: 300000, text: "Low-income family threshold satisfied" }
    ]
  }
];

// Presets data for quick testing
const PRESETS = {
  ap_student: {
    state: "Andhra Pradesh",
    income: 200000,
    category: "OBC",
    marks: 85,
    gender: "Male",
    course_level: "UG",
    is_first_graduate: false,
    is_disabled: false,
    is_single_girl_child: false,
    is_govt_school: false,
    is_farmer: false
  },
  ts_student: {
    state: "Telangana",
    income: 180000,
    category: "OBC",
    marks: 80,
    gender: "Female",
    course_level: "UG",
    is_first_graduate: false,
    is_disabled: false,
    is_single_girl_child: true,
    is_govt_school: false,
    is_farmer: false
  },
  tn_student: {
    state: "Tamil Nadu",
    income: 160000,
    category: "OBC",
    marks: 86,
    gender: "Female",
    course_level: "UG",
    is_first_graduate: true,
    is_disabled: false,
    is_single_girl_child: false,
    is_govt_school: true,
    is_farmer: false
  },
  central_scholar: {
    state: "Pan-India",
    income: 250000,
    category: "General",
    marks: 90,
    gender: "Female",
    course_level: "UG",
    is_first_graduate: false,
    is_disabled: false,
    is_single_girl_child: false,
    is_govt_school: false,
    is_farmer: false
  }
};

// =============================================================
// Settings & Profile Management System (Storage, State, Avatar)
// =============================================================
const STORAGE_KEY_PROFILE = "scheme_finder_user_profile";
const STORAGE_KEY_ACCOUNT = "scheme_finder_account_settings";

const DEFAULT_PROFILE = {
  fullName: "Ananya Sharma",
  email: "ananya.sharma@example.com",
  phone: "+91 98765 43210",
  dob: "2003-05-14",
  state: "Andhra Pradesh",
  income: 200000,
  category: "OBC",
  course_level: "UG",
  marks: 85,
  gender: "Female",
  is_first_graduate: false,
  is_govt_school: true,
  is_farmer: false,
  is_single_girl_child: false,
  is_disabled: false
};

const DEFAULT_ACCOUNT = {
  theme: "light",
  autoEval: true,
  compactView: false,
  deadlineAlerts: true,
  newSchemesAlert: true,
  autoSaveChecklist: true,
  savedSchemes: []
};

function showToast(message, duration = 3000) {
  const toast = document.getElementById("toastNotification");
  if (!toast) return;
  toast.textContent = message;
  toast.classList.add("show");
  clearTimeout(window._toastTimeout);
  window._toastTimeout = setTimeout(() => {
    toast.classList.remove("show");
  }, duration);
}

function loadUserProfile() {
  try {
    const raw = localStorage.getItem(STORAGE_KEY_PROFILE);
    if (raw) return { ...DEFAULT_PROFILE, ...JSON.parse(raw) };
  } catch (e) {}
  return { ...DEFAULT_PROFILE };
}

function loadAccountSettings() {
  try {
    const raw = localStorage.getItem(STORAGE_KEY_ACCOUNT);
    if (raw) return { ...DEFAULT_ACCOUNT, ...JSON.parse(raw) };
  } catch (e) {}
  return { ...DEFAULT_ACCOUNT };
}

function saveAccountSettings(settings) {
  try {
    localStorage.setItem(STORAGE_KEY_ACCOUNT, JSON.stringify(settings));
  } catch (e) {}
}

function updateAvatarDisplay(profile) {
  const name = profile.fullName || "Citizen User";
  const parts = name.trim().split(/\s+/);
  let initials = "CU";
  if (parts.length >= 2) {
    initials = (parts[0][0] + parts[1][0]).toUpperCase();
  } else if (parts.length === 1 && parts[0].length > 0) {
    initials = parts[0].substring(0, 2).toUpperCase();
  }

  const navInitials = document.getElementById("navAvatarInitials");
  if (navInitials) navInitials.textContent = initials;

  const bigAvatar = document.getElementById("settingsAvatarBig");
  if (bigAvatar) bigAvatar.textContent = initials;

  const nameDisplay = document.getElementById("settingsUserNameDisplay");
  if (nameDisplay) nameDisplay.textContent = name;

  const emailDisplay = document.getElementById("settingsUserEmailDisplay");
  if (emailDisplay) emailDisplay.textContent = profile.email || "No email provided";
}

function populateProfileSettingsForm(profile) {
  if (!profile) return;
  const setVal = (id, val) => {
    const el = document.getElementById(id);
    if (el && val !== undefined) el.value = val;
  };
  const setChecked = (id, val) => {
    const el = document.getElementById(id);
    if (el) el.checked = !!val;
  };

  setVal("settingFullName", profile.fullName);
  setVal("settingEmail", profile.email);
  setVal("settingPhone", profile.phone);
  setVal("settingDob", profile.dob);
  setVal("settingState", profile.state);
  setVal("settingIncome", profile.income);
  setVal("settingCategory", profile.category);
  setVal("settingCourse", profile.course_level);
  setVal("settingMarks", profile.marks);
  setVal("settingGender", profile.gender);

  setChecked("settingFirstGraduate", profile.is_first_graduate);
  setChecked("settingGovtSchool", profile.is_govt_school);
  setChecked("settingFarmer", profile.is_farmer);
  setChecked("settingSingleGirl", profile.is_single_girl_child);
  setChecked("settingDisabled", profile.is_disabled);
}

function populateAccountSettingsForm(account) {
  if (!account) return;
  const currentTheme = document.documentElement.getAttribute("data-theme") || account.theme || "light";
  const darkToggle = document.getElementById("settingDarkToggle");
  if (darkToggle) darkToggle.checked = (currentTheme === "dark");

  const autoEvalToggle = document.getElementById("settingAutoEvalToggle");
  if (autoEvalToggle) autoEvalToggle.checked = !!account.autoEval;

  const compactToggle = document.getElementById("settingCompactToggle");
  if (compactToggle) compactToggle.checked = !!account.compactView;

  const deadlineToggle = document.getElementById("settingDeadlineAlerts");
  if (deadlineToggle) deadlineToggle.checked = (account.deadlineAlerts !== false);

  const newSchemesToggle = document.getElementById("settingNewSchemesAlert");
  if (newSchemesToggle) newSchemesToggle.checked = (account.newSchemesAlert !== false);

  const autoSaveChecklistToggle = document.getElementById("settingAutoSaveChecklist");
  if (autoSaveChecklistToggle) autoSaveChecklistToggle.checked = (account.autoSaveChecklist !== false);
}

function saveUserProfileFromForm() {
  const profile = {
    fullName: document.getElementById("settingFullName")?.value.trim() || "Citizen User",
    email: document.getElementById("settingEmail")?.value.trim() || "",
    phone: document.getElementById("settingPhone")?.value.trim() || "",
    dob: document.getElementById("settingDob")?.value || "",
    state: document.getElementById("settingState")?.value || "Andhra Pradesh",
    income: parseFloat(document.getElementById("settingIncome")?.value) || 200000,
    category: document.getElementById("settingCategory")?.value || "OBC",
    course_level: document.getElementById("settingCourse")?.value || "UG",
    marks: parseFloat(document.getElementById("settingMarks")?.value) || 85,
    gender: document.getElementById("settingGender")?.value || "Female",
    is_first_graduate: !!document.getElementById("settingFirstGraduate")?.checked,
    is_govt_school: !!document.getElementById("settingGovtSchool")?.checked,
    is_farmer: !!document.getElementById("settingFarmer")?.checked,
    is_single_girl_child: !!document.getElementById("settingSingleGirl")?.checked,
    is_disabled: !!document.getElementById("settingDisabled")?.checked
  };

  localStorage.setItem(STORAGE_KEY_PROFILE, JSON.stringify(profile));
  updateAvatarDisplay(profile);

  const statusNote = document.getElementById("settingsSaveStatus");
  if (statusNote) {
    const timeStr = new Date().toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" });
    statusNote.textContent = `✓ Profile saved at ${timeStr}`;
  }

  return profile;
}

function switchSettingsTab(tabName) {
  const tabBtnProfile = document.getElementById("tabBtnProfile");
  const tabBtnAccount = document.getElementById("tabBtnAccount");
  const tabProfile = document.getElementById("tabProfile");
  const tabAccount = document.getElementById("tabAccount");

  if (tabName === "tabProfile") {
    tabBtnProfile?.classList.add("active");
    tabBtnProfile?.setAttribute("aria-selected", "true");
    tabBtnAccount?.classList.remove("active");
    tabBtnAccount?.setAttribute("aria-selected", "false");
    tabProfile?.classList.add("active");
    tabAccount?.classList.remove("active");
  } else {
    tabBtnAccount?.classList.add("active");
    tabBtnAccount?.setAttribute("aria-selected", "true");
    tabBtnProfile?.classList.remove("active");
    tabBtnProfile?.setAttribute("aria-selected", "false");
    tabAccount?.classList.add("active");
    tabProfile?.classList.remove("active");
    renderSavedSchemes();
  }
}

function openSettingsDialog(tabName = "tabProfile") {
  const dialog = document.getElementById("settingsDialog");
  if (!dialog) return;

  const profile = loadUserProfile();
  populateProfileSettingsForm(profile);
  updateAvatarDisplay(profile);

  const account = loadAccountSettings();
  populateAccountSettingsForm(account);
  renderSavedSchemes();

  switchSettingsTab(tabName);

  if (typeof dialog.showModal === "function") {
    dialog.showModal();
  }
}

function applyCompactCards(isCompact) {
  const container = document.getElementById("schemesResultsContainer");
  if (container) {
    container.classList.toggle("compact-cards", !!isCompact);
  }
}

function isSchemeBookmarked(schemeId) {
  if (!schemeId) return false;
  const account = loadAccountSettings();
  const list = account.savedSchemes || [];
  return list.some(s => (s.id === schemeId || s.scheme_id === schemeId));
}

function toggleBookmarkScheme(schemeId) {
  if (!schemeId) return;
  const account = loadAccountSettings();
  if (!account.savedSchemes) account.savedSchemes = [];

  const existingIdx = account.savedSchemes.findIndex(s => (s.id === schemeId || s.scheme_id === schemeId));
  let isNowBookmarked = false;
  let schemeName = "Scheme";

  if (existingIdx >= 0) {
    schemeName = account.savedSchemes[existingIdx].name || "Scheme";
    account.savedSchemes.splice(existingIdx, 1);
    isNowBookmarked = false;
    showToast(`Removed "${schemeName}" from bookmarks`);
  } else {
    let schemeObj = currentSchemesData.find(s => s.scheme_id === schemeId || s.id === schemeId);
    if (!schemeObj) {
      schemeObj = FALLBACK_SCHEMES.find(s => s.id === schemeId || s.scheme_id === schemeId);
    }
    if (schemeObj) {
      schemeName = schemeObj.name;
      account.savedSchemes.push({
        id: schemeId,
        scheme_id: schemeId,
        name: schemeObj.name,
        state: schemeObj.state,
        category_type: schemeObj.category_type,
        official_portal_url: schemeObj.official_portal_url,
        benefit: schemeObj.benefit,
        documents: schemeObj.documents || []
      });
      isNowBookmarked = true;
      showToast(`✓ Bookmarked "${schemeName}"!`);
    } else {
      account.savedSchemes.push({ id: schemeId, scheme_id: schemeId, name: schemeId });
      isNowBookmarked = true;
      showToast(`✓ Bookmarked scheme to your account!`);
    }
  }

  saveAccountSettings(account);

  // Update button in results and explore grids
  document.querySelectorAll(`.bookmark-scheme-btn[data-id="${schemeId}"]`).forEach(btn => {
    btn.classList.toggle("bookmarked", isNowBookmarked);
    if (btn.closest(".explore-scheme-card")) {
      btn.textContent = isNowBookmarked ? "★" : "☆";
    } else {
      btn.textContent = isNowBookmarked ? "★ Bookmarked" : "☆ Bookmark";
    }
  });

  renderSavedSchemes();
}

function renderSavedSchemes() {
  const container = document.getElementById("savedSchemesContainer");
  const countBadge = document.getElementById("savedSchemesCount");
  if (!container) return;

  const account = loadAccountSettings();
  const list = account.savedSchemes || [];

  if (countBadge) {
    countBadge.textContent = `${list.length} saved`;
  }

  if (list.length === 0) {
    container.innerHTML = `
      <div class="empty-saved-notice">
        <p style="margin-bottom:0.4rem;font-size:1.3rem;">🔖</p>
        <p style="font-weight:600;margin-bottom:0.25rem;">No saved schemes yet</p>
        <span style="font-size:0.75rem;color:var(--text-muted);">Click "☆ Bookmark" on any scheme card to save it to your account for one-click access anytime.</span>
      </div>
    `;
    return;
  }

  container.innerHTML = list.map(item => `
    <div class="saved-scheme-item">
      <div style="flex:1;min-width:0;">
        <div class="saved-scheme-name" style="white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">${item.name}</div>
        <div class="saved-scheme-state">${item.state || "Central / Pan-India"} · ${item.category_type || "Welfare"}</div>
      </div>
      <div style="display:flex;align-items:center;gap:0.45rem;flex-shrink:0;">
        <button type="button" class="btn btn-outline btn-sm view-saved-checklist-btn" data-id="${item.id}" style="padding:0.25rem 0.55rem;font-size:0.75rem;">
          📋 Checklist
        </button>
        ${item.official_portal_url ? `
          <a href="${item.official_portal_url}" target="_blank" rel="noopener noreferrer" class="btn btn-ghost btn-sm" style="padding:0.25rem 0.45rem;font-size:0.75rem;" title="Official Portal">
            ↗
          </a>
        ` : ""}
        <button type="button" class="remove-saved-btn" data-id="${item.id}" title="Remove scheme" aria-label="Remove scheme">
          &times;
        </button>
      </div>
    </div>
  `).join("");

  container.querySelectorAll(".remove-saved-btn").forEach(btn => {
    btn.addEventListener("click", (e) => {
      e.stopPropagation();
      const id = btn.getAttribute("data-id");
      toggleBookmarkScheme(id);
    });
  });

  container.querySelectorAll(".view-saved-checklist-btn").forEach(btn => {
    btn.addEventListener("click", () => {
      const id = btn.getAttribute("data-id");
      const settingsDialog = document.getElementById("settingsDialog");
      if (settingsDialog) settingsDialog.close();
      openChecklistModal(id);
    });
  });
}

function exportUserData() {
  const profile = loadUserProfile();
  const account = loadAccountSettings();

  const checklistData = {};
  for (let i = 0; i < localStorage.length; i++) {
    const key = localStorage.key(i);
    if (key && key.startsWith("checklist_state_")) {
      try {
        checklistData[key] = JSON.parse(localStorage.getItem(key) || "{}");
      } catch (e) {}
    }
  }

  const exportPayload = {
    exportedAt: new Date().toISOString(),
    version: "1.0",
    profile,
    account,
    checklistProgress: checklistData
  };

  const jsonStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(exportPayload, null, 2));
  const downloadAnchor = document.createElement("a");
  downloadAnchor.setAttribute("href", jsonStr);
  downloadAnchor.setAttribute("download", `scheme-finder-profile-${new Date().toISOString().slice(0, 10)}.json`);
  document.body.appendChild(downloadAnchor);
  downloadAnchor.click();
  downloadAnchor.remove();

  showToast("✓ Profile & settings exported as JSON!");
}

function clearAllUserData() {
  if (confirm("Are you sure you want to clear all your saved profile data, bookmarks, and checklist progress? This action cannot be undone.")) {
    localStorage.removeItem(STORAGE_KEY_PROFILE);
    localStorage.removeItem(STORAGE_KEY_ACCOUNT);

    const keysToRemove = [];
    for (let i = 0; i < localStorage.length; i++) {
      const key = localStorage.key(i);
      if (key && key.startsWith("checklist_state_")) {
        keysToRemove.push(key);
      }
    }
    keysToRemove.forEach(k => localStorage.removeItem(k));

    const defaultProf = loadUserProfile();
    populateProfileSettingsForm(defaultProf);
    updateAvatarDisplay(defaultProf);

    const defaultAcc = loadAccountSettings();
    populateAccountSettingsForm(defaultAcc);
    applyCompactCards(false);
    renderSavedSchemes();

    populateForm(defaultProf);
    syncSidebar();
    submitProfile();

    showToast("✓ All local account data cleared successfully.");
  }
}

function initSettingsDialog() {
  const dialog = document.getElementById("settingsDialog");
  const avatarBtn = document.getElementById("navAvatarBtn");
  const navSettingsLink = document.getElementById("navSettingsLink");
  const closeBtn = document.getElementById("closeSettingsDialogBtn");
  const closeFooterBtn = document.getElementById("closeSettingsFooterBtn");

  const tabBtnProfile = document.getElementById("tabBtnProfile");
  const tabBtnAccount = document.getElementById("tabBtnAccount");

  if (avatarBtn) avatarBtn.addEventListener("click", () => openSettingsDialog("tabProfile"));
  if (navSettingsLink) {
    navSettingsLink.addEventListener("click", (e) => {
      e.preventDefault();
      openSettingsDialog("tabProfile");
    });
  }

  if (closeBtn && dialog) closeBtn.addEventListener("click", () => dialog.close());
  if (closeFooterBtn && dialog) closeFooterBtn.addEventListener("click", () => dialog.close());

  if (dialog) {
    dialog.addEventListener("click", (e) => {
      const rect = dialog.getBoundingClientRect();
      const inDialog = (
        rect.top <= e.clientY && e.clientY <= rect.top + rect.height &&
        rect.left <= e.clientX && e.clientX <= rect.left + rect.width
      );
      if (!inDialog) dialog.close();
    });
  }

  if (tabBtnProfile && tabBtnAccount) {
    tabBtnProfile.addEventListener("click", () => switchSettingsTab("tabProfile"));
    tabBtnAccount.addEventListener("click", () => switchSettingsTab("tabAccount"));
  }

  const saveProfileBtn = document.getElementById("saveProfileBtn");
  if (saveProfileBtn) {
    saveProfileBtn.addEventListener("click", () => {
      saveUserProfileFromForm();
      showToast("✓ Profile settings saved!");
    });
  }

  const applyBtn = document.getElementById("applyProfileToFormBtn");
  if (applyBtn) {
    applyBtn.addEventListener("click", () => {
      const profile = saveUserProfileFromForm();
      populateForm(profile);
      syncSidebar();
      submitProfile();
      if (dialog) dialog.close();
      document.getElementById("finderSection")?.scrollIntoView({ behavior: "smooth" });
      showToast("✓ Form synced with your profile!");
    });
  }

  const resetProfileBtn = document.getElementById("resetProfileBtn");
  if (resetProfileBtn) {
    resetProfileBtn.addEventListener("click", () => {
      localStorage.removeItem(STORAGE_KEY_PROFILE);
      const defaultProf = loadUserProfile();
      populateProfileSettingsForm(defaultProf);
      updateAvatarDisplay(defaultProf);
      showToast("Profile reset to sample values");
    });
  }

  const darkToggle = document.getElementById("settingDarkToggle");
  if (darkToggle) {
    darkToggle.addEventListener("change", () => {
      const isDark = darkToggle.checked;
      const theme = isDark ? "dark" : "light";
      document.documentElement.setAttribute("data-theme", theme);
      localStorage.setItem("scheme_finder_theme", theme);
      updateThemeIcon(theme);
      const acc = loadAccountSettings();
      acc.theme = theme;
      saveAccountSettings(acc);
      showToast(isDark ? "🌙 Dark mode enabled" : "☀️ Light mode enabled");
    });
  }

  const autoEvalToggle = document.getElementById("settingAutoEvalToggle");
  if (autoEvalToggle) {
    autoEvalToggle.addEventListener("change", () => {
      const acc = loadAccountSettings();
      acc.autoEval = autoEvalToggle.checked;
      saveAccountSettings(acc);
      showToast(acc.autoEval ? "Auto-evaluation enabled" : "Auto-evaluation disabled");
    });
  }

  const compactToggle = document.getElementById("settingCompactToggle");
  if (compactToggle) {
    compactToggle.addEventListener("change", () => {
      const acc = loadAccountSettings();
      acc.compactView = compactToggle.checked;
      saveAccountSettings(acc);
      applyCompactCards(acc.compactView);
      showToast(acc.compactView ? "Compact card layout enabled" : "Standard card layout restored");
    });
  }

  const deadlineToggle = document.getElementById("settingDeadlineAlerts");
  if (deadlineToggle) {
    deadlineToggle.addEventListener("change", () => {
      const acc = loadAccountSettings();
      acc.deadlineAlerts = deadlineToggle.checked;
      saveAccountSettings(acc);
    });
  }

  const newSchemesToggle = document.getElementById("settingNewSchemesAlert");
  if (newSchemesToggle) {
    newSchemesToggle.addEventListener("change", () => {
      const acc = loadAccountSettings();
      acc.newSchemesAlert = newSchemesToggle.checked;
      saveAccountSettings(acc);
    });
  }

  const autoSaveChecklistToggle = document.getElementById("settingAutoSaveChecklist");
  if (autoSaveChecklistToggle) {
    autoSaveChecklistToggle.addEventListener("change", () => {
      const acc = loadAccountSettings();
      acc.autoSaveChecklist = autoSaveChecklistToggle.checked;
      saveAccountSettings(acc);
    });
  }

  const exportBtn = document.getElementById("exportDataBtn");
  if (exportBtn) exportBtn.addEventListener("click", exportUserData);

  const clearBtn = document.getElementById("clearAllDataBtn");
  if (clearBtn) clearBtn.addEventListener("click", clearAllUserData);
}

document.addEventListener("DOMContentLoaded", () => {
  initTheme();
  initSettingsDialog();
  initFormListeners();
  initPresetChips();
  initChecklistDialog();
  initExploreTab();
  initPortalsDirectory();
  initSidebarSync();
  initResultsFilterChips();
  initClearBtn();

  // Load and apply saved profile and account preferences
  const userProf = loadUserProfile();
  updateAvatarDisplay(userProf);

  const acc = loadAccountSettings();
  applyCompactCards(acc.compactView);

  // Auto-run evaluation with initial profile values
  submitProfile();
  syncSidebar();
});

// -------------------------------------------------------------
// 1. Theme Toggle
// -------------------------------------------------------------
function initTheme() {
  const toggleBtn = document.getElementById("themeToggleBtn");
  const savedTheme = localStorage.getItem("scheme_finder_theme") || "light";
  document.documentElement.setAttribute("data-theme", savedTheme);
  updateThemeIcon(savedTheme);

  const darkToggle = document.getElementById("settingDarkToggle");
  if (darkToggle) darkToggle.checked = (savedTheme === "dark");

  if (toggleBtn) {
    toggleBtn.addEventListener("click", () => {
      const current = document.documentElement.getAttribute("data-theme") || "light";
      const nextTheme = current === "dark" ? "light" : "dark";
      document.documentElement.setAttribute("data-theme", nextTheme);
      localStorage.setItem("scheme_finder_theme", nextTheme);
      updateThemeIcon(nextTheme);

      if (darkToggle) darkToggle.checked = (nextTheme === "dark");
      const acc = loadAccountSettings();
      acc.theme = nextTheme;
      saveAccountSettings(acc);
      showToast(nextTheme === "dark" ? "🌙 Dark mode enabled" : "☀️ Light mode enabled");
    });
  }
}

function updateThemeIcon(theme) {
  const iconSpan = document.getElementById("themeIcon");
  const toggleBtn = document.getElementById("themeToggleBtn");
  if (iconSpan) {
    iconSpan.textContent = theme === "dark" ? "☀️" : "🌙";
  }
  if (toggleBtn) {
    toggleBtn.setAttribute("title", theme === "dark" ? "Switch to Light Theme" : "Switch to Dark Theme");
    toggleBtn.setAttribute("aria-label", theme === "dark" ? "Switch to Light Theme" : "Switch to Dark Theme");
  }
}


// -------------------------------------------------------------
// 1b. Sidebar Sync & Auto-Evaluation
// -------------------------------------------------------------
let _autoEvalTimer = null;
function triggerAutoEvalIfNeeded() {
  const acc = loadAccountSettings();
  if (acc.autoEval) {
    submitProfile();
  }
}
function debounceAutoEval() {
  const acc = loadAccountSettings();
  if (acc.autoEval) {
    clearTimeout(_autoEvalTimer);
    _autoEvalTimer = setTimeout(() => {
      submitProfile();
    }, 500);
  }
}

function initSidebarSync() {
  const watchIds = ["stateSelect", "incomeInput", "categorySelect", "marksInput", "courseSelect",
    "firstGraduateCheck", "govtSchoolCheck", "farmerCheck", "singleGirlCheck", "disabledCheck"];
  watchIds.forEach(id => {
    const el = document.getElementById(id);
    if (el) {
      el.addEventListener("change", () => {
        syncSidebar();
        triggerAutoEvalIfNeeded();
      });
    }
    if (el && (el.type === "number" || el.type === "text")) {
      el.addEventListener("input", () => {
        syncSidebar();
        debounceAutoEval();
      });
    }
  });
  document.querySelectorAll('input[name="gender"]').forEach(r => r.addEventListener("change", () => {
    syncSidebar();
    triggerAutoEvalIfNeeded();
  }));

  const editLink = document.getElementById("sidebarEditLink");
  if (editLink) {
    editLink.addEventListener("click", () => {
      document.getElementById("stateSelect")?.focus();
      document.getElementById("finderSection")?.scrollIntoView({ behavior: "smooth" });
    });
  }
}

function syncSidebar() {
  const stateEl = document.getElementById("stateSelect");
  const incomeEl = document.getElementById("incomeInput");
  const catEl = document.getElementById("categorySelect");
  const courseEl = document.getElementById("courseSelect");

  // State
  if (stateEl) {
    const el = document.getElementById("sidebarState");
    if (el) el.textContent = stateEl.value;
  }

  // Income
  if (incomeEl) {
    const val = parseFloat(incomeEl.value) || 0;
    const el = document.getElementById("sidebarIncome");
    if (el) el.textContent = "\u20B9" + val.toLocaleString("en-IN");
  }

  // Category
  if (catEl) {
    const el = document.getElementById("sidebarCategory");
    const catMap = { General: "General / Open", OBC: "OBC / BC", SC: "SC", ST: "ST", EWS: "EWS" };
    if (el) el.textContent = catMap[catEl.value] || catEl.value;
  }

  // Level
  if (courseEl) {
    const el = document.getElementById("sidebarLevel");
    const levelMap = {
      UG: "Undergraduate", PG: "Postgraduate", Diploma: "Diploma",
      "Class 12": "Class 12", "Class 10": "Class 10", PhD: "Ph.D."
    };
    if (el) el.textContent = levelMap[courseEl.value] || courseEl.value;
  }

  // Circumstances
  const circs = [];
  if (document.getElementById("firstGraduateCheck")?.checked) circs.push("First Graduate");
  if (document.getElementById("govtSchoolCheck")?.checked) circs.push("Govt School");
  if (document.getElementById("farmerCheck")?.checked) circs.push("Farmer");
  if (document.getElementById("singleGirlCheck")?.checked) circs.push("Single Girl Child");
  if (document.getElementById("disabledCheck")?.checked) circs.push("PwD");
  const circEl = document.getElementById("sidebarCircumstances");
  if (circEl) circEl.textContent = circs.length > 0 ? circs.join(", ") : "None selected";
}

// -------------------------------------------------------------
// 1c. Results Filter Chips
// -------------------------------------------------------------
let activeResultCategory = "All";
let allResultSchemes = [];

function initResultsFilterChips() {
  const chips = document.querySelectorAll(".result-filter-chip");
  chips.forEach(chip => {
    chip.addEventListener("click", () => {
      chips.forEach(c => c.classList.remove("active"));
      chip.classList.add("active");
      activeResultCategory = chip.getAttribute("data-cat") || "All";
      renderFilteredResults();
    });
  });

  const sortSel = document.getElementById("resultsSortSelect");
  if (sortSel) sortSel.addEventListener("change", renderFilteredResults);
}

function renderFilteredResults() {
  let filtered = allResultSchemes;
  if (activeResultCategory !== "All") {
    filtered = filtered.filter(s => (s.category_type || "").toLowerCase() === activeResultCategory.toLowerCase());
  }
  const sortSel = document.getElementById("resultsSortSelect");
  if (sortSel && sortSel.value === "name") {
    filtered = [...filtered].sort((a, b) => a.name.localeCompare(b.name));
  }
  renderEligibleSchemesIntoDOM(filtered);
}

// -------------------------------------------------------------
// 1d. Clear Button
// -------------------------------------------------------------
function initClearBtn() {
  const clearBtn = document.getElementById("clearFormBtn");
  if (clearBtn) {
    clearBtn.addEventListener("click", () => {
      document.getElementById("profileForm")?.reset();
      document.getElementById("stateSelect").value = "Andhra Pradesh";
      document.getElementById("incomeInput").value = "200000";
      document.getElementById("categorySelect").value = "OBC";
      document.getElementById("marksInput").value = "85";
      document.getElementById("courseSelect").value = "UG";
      const maleRadio = document.querySelector('input[name="gender"][value="Male"]');
      if (maleRadio) maleRadio.checked = true;
      syncSidebar();
    });
  }
}

// -------------------------------------------------------------
// 2. Preset Quick Fill
// -------------------------------------------------------------
function initPresetChips() {
  const chips = document.querySelectorAll(".preset-chip");
  chips.forEach(chip => {
    chip.addEventListener("click", () => {
      const presetKey = chip.getAttribute("data-preset");
      const data = PRESETS[presetKey];
      if (data) {
        populateForm(data);
        submitProfile();
      }
    });
  });

  // Income quick buttons
  const quickIncomeBtns = document.querySelectorAll(".quick-income-btn");
  quickIncomeBtns.forEach(btn => {
    btn.addEventListener("click", () => {
      const val = btn.getAttribute("data-val");
      document.getElementById("incomeInput").value = val;
    });
  });
}

function populateForm(data) {
  if (data.state) document.getElementById("stateSelect").value = data.state;
  if (data.income !== undefined) document.getElementById("incomeInput").value = data.income;
  if (data.category) document.getElementById("categorySelect").value = data.category;
  if (data.marks !== undefined) document.getElementById("marksInput").value = data.marks;
  if (data.course_level) document.getElementById("courseSelect").value = data.course_level;

  if (data.gender) {
    const radio = document.querySelector(`input[name="gender"][value="${data.gender}"]`);
    if (radio) radio.checked = true;
  }

  document.getElementById("firstGraduateCheck").checked = !!data.is_first_graduate;
  document.getElementById("disabledCheck").checked = !!data.is_disabled;
  document.getElementById("singleGirlCheck").checked = !!data.is_single_girl_child;
  
  const govtSchoolCheck = document.getElementById("govtSchoolCheck");
  if (govtSchoolCheck) govtSchoolCheck.checked = !!data.is_govt_school;

  const farmerCheck = document.getElementById("farmerCheck");
  if (farmerCheck) farmerCheck.checked = !!data.is_farmer;
}

// -------------------------------------------------------------
// 3. Form Handling & Evaluation
// -------------------------------------------------------------
function initFormListeners() {
  const form = document.getElementById("profileForm");
  if (form) {
    form.addEventListener("submit", (e) => {
      e.preventDefault();
      submitProfile();
    });
  }
}

function getFormData() {
  const state = document.getElementById("stateSelect").value;
  const income = parseFloat(document.getElementById("incomeInput").value) || 0;
  const category = document.getElementById("categorySelect").value;
  const marks = parseFloat(document.getElementById("marksInput").value) || 0;
  const course_level = document.getElementById("courseSelect").value;
  
  const genderRadio = document.querySelector('input[name="gender"]:checked');
  const gender = genderRadio ? genderRadio.value : "Any";

  const is_first_graduate = document.getElementById("firstGraduateCheck").checked;
  const is_disabled = document.getElementById("disabledCheck").checked;
  const is_single_girl_child = document.getElementById("singleGirlCheck").checked;
  
  const govtSchoolElem = document.getElementById("govtSchoolCheck");
  const is_govt_school = govtSchoolElem ? govtSchoolElem.checked : false;

  const farmerElem = document.getElementById("farmerCheck");
  const is_farmer = farmerElem ? farmerElem.checked : false;

  return {
    state,
    income,
    category,
    marks,
    gender,
    course_level,
    is_first_graduate,
    is_disabled,
    is_single_girl_child,
    is_govt_school,
    is_farmer
  };
}

async function submitProfile() {
  const profile = getFormData();
  currentProfile = profile;
  syncSidebar();
  const submitBtn = document.getElementById("findSchemesBtn");

  if (submitBtn) {
    submitBtn.textContent = "Evaluating...";
    submitBtn.disabled = true;
  }

  try {
    const response = await fetch("/api/evaluate", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(profile)
    });

    if (response.ok) {
      const data = await response.json();
      renderEligibleSchemes(data.eligible_schemes);
    } else {
      const localMatches = evaluateLocally(profile);
      renderEligibleSchemes(localMatches);
    }
  } catch (err) {
    const localMatches = evaluateLocally(profile);
    renderEligibleSchemes(localMatches);
  } finally {
    if (submitBtn) {
      submitBtn.textContent = "Find eligible schemes";
      submitBtn.disabled = false;
    }
  }
}

// -------------------------------------------------------------
// 4. Local Evaluation Engine Fallback
// -------------------------------------------------------------
function evaluateLocally(profile) {
  const results = [];
  const userState = (profile.state || "").toLowerCase().trim();

  FALLBACK_SCHEMES.forEach(scheme => {
    const schemeState = (scheme.state || "All India").toLowerCase().trim();
    if (schemeState !== "all india" && schemeState !== "pan-india") {
      if (userState !== schemeState) {
        return;
      }
    }

    let eligible = true;
    let matchedExplanations = [];

    if (schemeState in { "andhra pradesh": 1, "telangana": 1, "tamil nadu": 1 }) {
      matchedExplanations.push(`Resident of ${scheme.state} (State Welfare Scheme)`);
    }

    for (let rule of scheme.rules) {
      const val = profile[rule.attr];
      let passed = false;

      if (rule.op === "<=") passed = Number(val) <= Number(rule.target);
      else if (rule.op === ">=") passed = Number(val) >= Number(rule.target);
      else if (rule.op === "==") passed = String(val).toLowerCase() === String(rule.target).toLowerCase();

      if (passed) {
        matchedExplanations.push(rule.text);
      } else {
        eligible = false;
        break;
      }
    }

    if (eligible) {
      results.push({
        eligible: true,
        scheme_id: scheme.id,
        name: scheme.name,
        department: scheme.department,
        category_type: scheme.category_type,
        state: scheme.state,
        description: scheme.description,
        benefit: scheme.benefit,
        official_portal_url: scheme.official_portal_url,
        documents: scheme.documents,
        match_percentage: 95,
        why_you_qualify: matchedExplanations
      });
    }
  });

  return results;
}

// Helper for Extracting Clean Government Portal Domain
function getPortalDomain(url) {
  try {
    const parsed = new URL(url);
    return parsed.hostname.replace(/^www\./, '');
  } catch (e) {
    return "gov.in";
  }
}

// Helper for State Badges
function getStateBadge(state) {
  const norm = (state || "").toLowerCase().trim();
  if (norm === "andhra pradesh") {
    return `<span class="badge badge-ap">🟡 Andhra Pradesh</span>`;
  } else if (norm === "telangana") {
    return `<span class="badge badge-ts">🔵 Telangana</span>`;
  } else if (norm === "tamil nadu") {
    return `<span class="badge badge-tn">🔴 Tamil Nadu</span>`;
  } else {
    return `<span class="badge badge-central">🇮🇳 All-India</span>`;
  }
}

// -------------------------------------------------------------
// 5. Render Eligible Schemes (new card design)
// -------------------------------------------------------------
function renderEligibleSchemes(schemes) {
  allResultSchemes = schemes || [];
  currentSchemesData = schemes || [];

  // Show/hide results section
  const resultsSection = document.getElementById("resultsSection");
  if (resultsSection) resultsSection.style.display = schemes.length > 0 ? "" : "none";

  // Update count
  const countBadge = document.getElementById("eligibleCountBadge");
  const titleEl = document.getElementById("resultsTitle");
  if (countBadge) countBadge.textContent = `${schemes.length} scheme${schemes.length !== 1 ? "s" : ""}`;
  if (titleEl) titleEl.textContent = schemes.length > 0
    ? `${schemes.length} scheme${schemes.length !== 1 ? "s" : ""} match your profile`
    : "No schemes matched";

  // Reset filter to All
  activeResultCategory = "All";
  document.querySelectorAll(".result-filter-chip").forEach(c => {
    c.classList.toggle("active", c.getAttribute("data-cat") === "All");
  });

  renderFilteredResults();

  // Scroll to results
  if (schemes.length > 0) {
    setTimeout(() => {
      document.getElementById("resultsSection")?.scrollIntoView({ behavior: "smooth", block: "start" });
    }, 120);
  }
}

function renderEligibleSchemesIntoDOM(schemes) {
  const container = document.getElementById("schemesResultsContainer");
  const noMatchesNotice = document.getElementById("noMatchesNotice");
  if (!container) return;

  if (!schemes || schemes.length === 0) {
    container.innerHTML = "";
    if (noMatchesNotice) noMatchesNotice.style.display = "block";
    return;
  }
  if (noMatchesNotice) noMatchesNotice.style.display = "none";

  let html = "";
  schemes.forEach((item, index) => {
    const domain = getPortalDomain(item.official_portal_url);
    const whyQualifyHtml = (item.why_you_qualify || [])
      .map(r => `<li class="why-qualify-item"><span class="why-qualify-check">✓</span><span>${r}</span></li>`)
      .join("");

    const docsHtml = (item.documents || []).slice(0, 4)
      .map(doc => `<li class="doc-inline-item">
        <input type="checkbox" aria-label="${doc}" />
        <span class="doc-name">${doc}</span>
      </li>`).join("");
    const extraDocs = (item.documents || []).length > 4 ? `<li class="doc-inline-item" style="color:var(--text-muted);font-size:0.75rem;">+${(item.documents.length - 4)} more document(s)…</li>` : "";

    html += `
      <article class="scheme-card animate-fade-in" style="animation-delay:${index * 0.05}s">
        <div class="scheme-card-inner">
          <div class="scheme-card-top">
            <div class="scheme-tags">
              ${getStateBadge(item.state)}
              <span class="badge badge-info">${item.category_type || "Welfare"}</span>
              <span class="portal-verified-domain" title="Verified official government portal">🏛️ ${domain}</span>
            </div>
            <div class="scheme-match-pill">
              <span class="match-pct">${item.match_percentage || 95}%</span>
              <span class="match-label">Match</span>
            </div>
          </div>

          <h3 class="scheme-name">${item.name}</h3>
          <p class="scheme-dept">${item.department}</p>
          <p class="scheme-desc" style="margin-top:0.55rem;">${item.description}</p>

          <div class="benefit-highlight">
            <strong>Benefit:</strong> ${item.benefit}
          </div>
        </div>

        <div class="scheme-detail-cols">
          <div class="detail-col">
            <div class="detail-col-title">Why you qualify</div>
            <ul class="why-qualify-list">
              ${whyQualifyHtml || "<li class='why-qualify-item'><span class='why-qualify-check'>✓</span><span>All eligibility criteria satisfied</span></li>"}
            </ul>
          </div>
          <div class="detail-col">
            <div class="detail-col-title">Documents to keep ready</div>
            <ul class="doc-inline-list">${docsHtml}${extraDocs}</ul>
          </div>
        </div>

        <div class="scheme-card-actions">
          <a href="${item.official_portal_url}" target="_blank" rel="noopener noreferrer" class="btn btn-primary btn-sm" title="Apply directly on official ${domain} portal in new tab">
            Apply on Official Portal ↗
          </a>
          <button class="btn btn-secondary btn-sm view-checklist-btn" data-id="${item.scheme_id}">
            Save to checklist
          </button>
          <button class="btn btn-outline btn-sm bookmark-scheme-btn ${isSchemeBookmarked(item.scheme_id) ? 'bookmarked' : ''}" data-id="${item.scheme_id}" title="Bookmark this scheme">
            ${isSchemeBookmarked(item.scheme_id) ? '★ Bookmarked' : '☆ Bookmark'}
          </button>
          <button class="save-chip view-checklist-btn" data-id="${item.scheme_id}">📋 Checklist: ${item.documents ? item.documents.length : 0} docs</button>
        </div>
      </article>
    `;
  });

  container.innerHTML = html;

  // Bind checklist buttons
  container.querySelectorAll(".view-checklist-btn").forEach(btn => {
    btn.addEventListener("click", () => openChecklistModal(btn.getAttribute("data-id")));
  });

  // Bind bookmark buttons
  container.querySelectorAll(".bookmark-scheme-btn").forEach(btn => {
    btn.addEventListener("click", () => toggleBookmarkScheme(btn.getAttribute("data-id")));
  });

  // Bind inline doc checkboxes
  container.querySelectorAll(".doc-inline-item input[type=checkbox]").forEach(cb => {
    cb.addEventListener("change", () => {
      cb.closest(".doc-inline-item").classList.toggle("checked", cb.checked);
    });
  });
}

// -------------------------------------------------------------
// 6. Document Checklist Modal Dialog
// -------------------------------------------------------------
function initChecklistDialog() {
  const dialog = document.getElementById("checklistDialog");
  const closeBtn = document.getElementById("closeDialogBtn");
  const printBtn = document.getElementById("printChecklistBtn");

  if (closeBtn && dialog) {
    closeBtn.addEventListener("click", () => dialog.close());
  }

  // Light dismiss on backdrop click
  if (dialog) {
    dialog.addEventListener("click", (e) => {
      const rect = dialog.getBoundingClientRect();
      const isInDialog = (
        rect.top <= e.clientY && e.clientY <= rect.top + rect.height &&
        rect.left <= e.clientX && e.clientX <= rect.left + rect.width
      );
      if (!isInDialog) {
        dialog.close();
      }
    });
  }

  if (printBtn) {
    printBtn.addEventListener("click", () => {
      window.print();
    });
  }
}

function openChecklistModal(schemeId) {
  let scheme = currentSchemesData.find(s => s.scheme_id === schemeId || s.id === schemeId);
  if (!scheme) {
    scheme = FALLBACK_SCHEMES.find(s => s.id === schemeId || s.scheme_id === schemeId);
  }
  if (!scheme) {
    const acc = loadAccountSettings();
    scheme = (acc.savedSchemes || []).find(s => s.id === schemeId || s.scheme_id === schemeId);
  }
  if (!scheme) return;
  activeSchemeForModal = scheme;

  const dialog = document.getElementById("checklistDialog");
  const titleElem = document.getElementById("modalSchemeTitle");
  const listContainer = document.getElementById("documentItemsContainer");
  const officialLink = document.getElementById("modalOfficialLink");

  if (titleElem) titleElem.textContent = scheme.name;
  if (officialLink) officialLink.href = scheme.official_portal_url;

  // Retrieve saved checklist states from localStorage
  const schemeKey = scheme.scheme_id || scheme.id;
  const storageKey = `checklist_state_${schemeKey}`;
  const savedState = JSON.parse(localStorage.getItem(storageKey) || "{}");

  const docs = scheme.documents || [];
  let html = "";
  docs.forEach((doc, idx) => {
    const isChecked = !!savedState[idx];
    html += `
      <label class="doc-check-item ${isChecked ? 'checked' : ''}" data-idx="${idx}">
        <input type="checkbox" ${isChecked ? 'checked' : ''} />
        <span class="doc-name">${doc}</span>
      </label>
    `;
  });

  if (listContainer) {
    listContainer.innerHTML = html;

    // Attach checkbox click listeners
    const checkLabels = listContainer.querySelectorAll(".doc-check-item");
    checkLabels.forEach(label => {
      const checkbox = label.querySelector('input[type="checkbox"]');
      checkbox.addEventListener("change", () => {
        const idx = label.getAttribute("data-idx");
        if (checkbox.checked) {
          label.classList.add("checked");
          savedState[idx] = true;
        } else {
          label.classList.remove("checked");
          delete savedState[idx];
        }
        localStorage.setItem(storageKey, JSON.stringify(savedState));
        updateChecklistProgress(docs.length, Object.keys(savedState).length);
      });
    });
  }

  updateChecklistProgress(docs.length, Object.keys(savedState).length);

  if (dialog && typeof dialog.showModal === "function") {
    dialog.showModal();
  }
}

function updateChecklistProgress(total, checkedCount) {
  const textElem = document.getElementById("progressStatusText");
  const fillElem = document.getElementById("progressBarFill");
  const pct = total > 0 ? Math.round((checkedCount / total) * 100) : 0;

  if (textElem) {
    textElem.textContent = `${checkedCount} of ${total} documents ready (${pct}%)`;
  }
  if (fillElem) {
    fillElem.style.width = `${pct}%`;
  }
}

// -------------------------------------------------------------
// 7. Explore All Schemes Tab, State Tabs & Live Search
// -------------------------------------------------------------
async function initExploreTab() {
  const searchInput = document.getElementById("exploreSearchInput");
  const stateTabs = document.querySelectorAll(".state-tab-btn");
  const filterChips = document.querySelectorAll(".filter-chip");

  let allSchemes = [];
  try {
    const res = await fetch("/api/schemes");
    if (res.ok) {
      const data = await res.json();
      allSchemes = data.schemes;
    } else {
      allSchemes = FALLBACK_SCHEMES;
    }
  } catch (e) {
    allSchemes = FALLBACK_SCHEMES;
  }

  function filterAndDisplay() {
    const query = searchInput ? searchInput.value.toLowerCase().trim() : "";
    const activeStateTab = document.querySelector(".state-tab-btn.active");
    const selectedState = activeStateTab ? activeStateTab.getAttribute("data-state") : "All";

    const activeCatChip = document.querySelector(".filter-chip.active");
    const category = activeCatChip ? activeCatChip.getAttribute("data-cat") : "All";

    const filtered = allSchemes.filter(s => {
      // State match
      let matchesState = true;
      if (selectedState !== "All") {
        const sState = (s.state || "All India").toLowerCase();
        matchesState = (sState === selectedState.toLowerCase() || sState === "all india" || sState === "pan-india");
      }

      // Category match
      let matchesCat = true;
      if (category !== "All") {
        matchesCat = (s.category_type && s.category_type.toLowerCase() === category.toLowerCase());
      }

      // Query match
      let matchesQuery = true;
      if (query) {
        matchesQuery = (
          (s.name && s.name.toLowerCase().includes(query)) ||
          (s.department && s.department.toLowerCase().includes(query)) ||
          (s.description && s.description.toLowerCase().includes(query)) ||
          (s.state && s.state.toLowerCase().includes(query))
        );
      }

      return matchesState && matchesCat && matchesQuery;
    });

    renderExploreGrid(filtered);
  }

  if (searchInput) {
    searchInput.addEventListener("input", filterAndDisplay);
  }

  stateTabs.forEach(tab => {
    tab.addEventListener("click", () => {
      stateTabs.forEach(t => t.classList.remove("active"));
      tab.classList.add("active");
      filterAndDisplay();
    });
  });

  filterChips.forEach(chip => {
    chip.addEventListener("click", () => {
      filterChips.forEach(c => c.classList.remove("active"));
      chip.classList.add("active");
      filterAndDisplay();
    });
  });

  filterAndDisplay();
}

function renderExploreGrid(schemes) {
  const grid = document.getElementById("exploreGrid");
  if (!grid) return;

  if (schemes.length === 0) {
    grid.innerHTML = `<div style="grid-column: 1/-1; text-align: center; padding: 2.5rem; color: var(--text-muted);">No schemes found matching the selected state and category.</div>`;
    return;
  }

  grid.innerHTML = schemes.map(s => {
    const sId = s.id || s.scheme_id;
    const isBookmarked = isSchemeBookmarked(sId);
    const domain = getPortalDomain(s.official_portal_url);
    return `
    <div class="explore-scheme-card">
      <div>
        <div style="display:flex;gap:0.4rem;align-items:center;flex-wrap:wrap;margin-bottom:0.55rem;">
          ${getStateBadge(s.state)}
          <span class="badge badge-info">${s.category_type}</span>
          <span class="portal-verified-domain" title="Verified official government portal">🏛️ ${domain}</span>
        </div>
        <h4 style="font-size:1rem;font-weight:700;margin-bottom:0.25rem;line-height:1.3;">${s.name}</h4>
        <p style="font-size:0.75rem;color:var(--text-muted);margin-bottom:0.55rem;">${s.department}</p>
        <p style="font-size:0.82rem;color:var(--text-secondary);line-height:1.5;">${s.description}</p>
      </div>
      <div>
        <div style="font-size:0.83rem;font-weight:600;color:var(--accent-primary);margin-bottom:0.7rem;line-height:1.35;">${s.benefit}</div>
        <div style="display:flex;gap:0.4rem;align-items:center;">
          <a href="${s.official_portal_url}" target="_blank" rel="noopener noreferrer" class="btn btn-outline btn-sm" style="flex:1;justify-content:center;" title="Apply on official ${domain} portal">
            Apply on Official Portal ↗
          </a>
          <button type="button" class="btn btn-ghost btn-sm bookmark-scheme-btn ${isBookmarked ? 'bookmarked' : ''}" data-id="${sId}" title="Bookmark this scheme">
            ${isBookmarked ? '★' : '☆'}
          </button>
        </div>
      </div>
    </div>
  `;
  }).join("");

  // Bind bookmark buttons in explore grid
  grid.querySelectorAll(".bookmark-scheme-btn").forEach(btn => {
    btn.addEventListener("click", () => toggleBookmarkScheme(btn.getAttribute("data-id")));
  });
}

// =============================================================
// 8. Official Government Portals Directory System
// =============================================================
const FALLBACK_PORTALS = [
  // Central
  {
    id: "central-nsp",
    name: "National Scholarship Portal (NSP)",
    state: "Central",
    category: "Scholarships & Education",
    department: "Ministry of Electronics & IT / Ministry of Education, Govt. of India",
    url: "https://scholarships.gov.in",
    domain: "scholarships.gov.in",
    badge: "Central Govt",
    icon: "🎓",
    description: "Official Government of India single-window platform for application, renewal, and DBT disbursement of 100+ Central, UGC, and AICTE scholarship programs.",
    services: [
      "Central Sector Scheme for College & University Students (CSSS)",
      "Post-Matric Scholarships for SC, ST, OBC and Minorities",
      "AICTE Pragati, Saksham & Swanath Technical Scholarships",
      "Direct Benefit Transfer (DBT) payment tracking"
    ]
  },
  {
    id: "central-myscheme",
    name: "myScheme Portal (National Schemes Gateway)",
    state: "Central",
    category: "National Gateways",
    department: "National e-Governance Division (NeGD) & MeitY, Govt. of India",
    url: "https://www.myscheme.gov.in",
    domain: "myscheme.gov.in",
    badge: "Central Govt",
    icon: "🏛️",
    description: "National e-Governance marketplace helping citizens find eligibility across 1,200+ Central and State welfare schemes based on demographic criteria.",
    services: [
      "Universal Scheme Search across all Ministries",
      "Multi-criteria citizen eligibility evaluation",
      "Direct links to official departmental application forms",
      "Document requirements & guideline checklists"
    ]
  },
  {
    id: "central-digilocker",
    name: "DigiLocker (National Document Wallet)",
    state: "Central",
    category: "Identity & Records",
    department: "Digital India Corporation, Ministry of Electronics & IT",
    url: "https://www.digilocker.gov.in",
    domain: "digilocker.gov.in",
    badge: "Digital India",
    icon: "📁",
    description: "Legally recognized digital wallet under IT Act 2000. Fetch, verify, and store authentic marksheets, Aadhaar, Caste, and Income certificates online.",
    services: [
      "Fetch authentic 10th & 12th Board Marksheets (CBSE & State)",
      "Store Tahsildar Income & Community/Caste certificates",
      "Paperless digital document sharing for admissions",
      "Verify Aadhaar, PAN, and Ration Card digitally"
    ]
  },
  {
    id: "central-pmkisan",
    name: "PM-KISAN Samman Nidhi Portal",
    state: "Central",
    category: "Agriculture",
    department: "Department of Agriculture & Farmers Welfare, Govt. of India",
    url: "https://pmkisan.gov.in",
    domain: "pmkisan.gov.in",
    badge: "Central Govt",
    icon: "🌾",
    description: "Direct financial support portal transferring ₹6,000 annually to landholding farmer families across India in three equal installments.",
    services: [
      "New Farmer Registration",
      "Beneficiary Status & Payment Installment Tracking",
      "Mandatory OTP / Biometric e-KYC Verification",
      "Aadhaar & Bank Account Seeding Verification"
    ]
  },
  {
    id: "central-pmjay",
    name: "Ayushman Bharat - PM-JAY Portal",
    state: "Central",
    category: "Healthcare",
    department: "National Health Authority (NHA), Ministry of Health & Family Welfare",
    url: "https://pmjay.gov.in",
    domain: "pmjay.gov.in",
    badge: "Central Govt",
    icon: "🏥",
    description: "World's largest health assurance scheme providing cashless hospital coverage of ₹5,00,000 per family per year for secondary and tertiary care.",
    services: [
      "Check Household Eligibility (SECC 2011)",
      "Create and download Ayushman / ABHA Cards",
      "Empanelled Public & Private Hospital Search",
      "Cashless Treatment Claim Tracking"
    ]
  },
  {
    id: "central-uidai",
    name: "myAadhaar (UIDAI Official Citizen Portal)",
    state: "Central",
    category: "Identity & Records",
    department: "Unique Identification Authority of India (UIDAI), Govt. of India",
    url: "https://myaadhaar.uidai.gov.in",
    domain: "myaadhaar.uidai.gov.in",
    badge: "UIDAI",
    icon: "🆔",
    description: "Official Aadhaar portal to download e-Aadhaar, update demographic address, and verify NPCI bank account DBT mapping for welfare payments.",
    services: [
      "Download Password-Protected e-Aadhaar PDF",
      "Verify Aadhaar - Bank Account Seeding / NPCI DBT Status",
      "Online Address & Demographic Information Update",
      "Order Secure Aadhaar PVC Card"
    ]
  },
  {
    id: "central-umang",
    name: "UMANG (Unified Citizen Services Gateway)",
    state: "Central",
    category: "National Gateways",
    department: "Ministry of Electronics and Information Technology (MeitY)",
    url: "https://web.umang.gov.in",
    domain: "web.umang.gov.in",
    badge: "Digital India",
    icon: "📱",
    description: "All-in-one web and mobile governance portal integrating 1,200+ Central and State government citizen services, EPFO, pensions, and utility bills.",
    services: [
      "Access Central & State Welfare Programs",
      "EPFO Passbook & UAN claim tracking",
      "National Pension System (NPS) and Atal Pension Yojana",
      "Online certificate applications and fee payments"
    ]
  },
  {
    id: "central-aicte",
    name: "AICTE Student Development Schemes Portal",
    state: "Central",
    category: "Scholarships & Education",
    department: "All India Council for Technical Education, Ministry of Education",
    url: "https://www.aicte-india.org/schemes/students-development-schemes",
    domain: "aicte-india.org",
    badge: "AICTE",
    icon: "🎓",
    description: "Technical education scholarships providing Pragati (girls in engineering/diploma), Saksham (specially-abled), and Swanath scholarships (₹50,000/yr).",
    services: [
      "AICTE Pragati Scholarship for Girls in Degree/Diploma",
      "AICTE Saksham Scholarship for Specially Abled Students",
      "AICTE Swanath Scholarship for Orphans & Wards of Martyrs",
      "PG Scholarship for GATE / GPAT qualified students"
    ]
  },

  // Andhra Pradesh
  {
    id: "ap-jnanabhumi",
    name: "JnanaBhumi AP (Higher Education & Scholarships)",
    state: "Andhra Pradesh",
    category: "Scholarships & Education",
    department: "Higher Education & Social Welfare Department, Govt. of Andhra Pradesh",
    url: "https://jnanabhumi.ap.gov.in",
    domain: "jnanabhumi.ap.gov.in",
    badge: "Govt of AP",
    icon: "🟡",
    description: "Andhra Pradesh's student welfare portal managing 100% Fee Reimbursement (Jagananna Vidya Deevena) and Hostel Allowance (Vasathi Deevena).",
    services: [
      "Jagananna Vidya Deevena (RTF - Full Tuition Fee Reimbursement)",
      "Jagananna Vasathi Deevena (MTF - Boarding & Mess Allowance)",
      "Post-Matric Scholarship Fresh & Renewal Registrations",
      "College Biometric Attendance & Disbursal Status Tracking"
    ]
  },
  {
    id: "ap-navasakam",
    name: "Navasakam AP (Welfare Schemes Delivery Portal)",
    state: "Andhra Pradesh",
    category: "National Gateways",
    department: "Department of Village & Ward Secretariats, Govt. of Andhra Pradesh",
    url: "https://navasakam.ap.gov.in",
    domain: "navasakam.ap.gov.in",
    badge: "Govt of AP",
    icon: "📋",
    description: "Comprehensive beneficiary identification portal coordinating doorstep governance and social audit for all AP welfare schemes.",
    services: [
      "Beneficiary verification for JVD, Cheyutha, Aasara & Amma Vodi",
      "Grama / Ward Sachivalayam Social Audit Lists",
      "Rice Card & Pension Eligibility Status",
      "Spandana Grievance redressal integration"
    ]
  },
  {
    id: "ap-meeseva",
    name: "MeeSeva AP (Online Citizen Service Portal)",
    state: "Andhra Pradesh",
    category: "e-Governance & Certificates",
    department: "ITE&C Department, Government of Andhra Pradesh",
    url: "https://onlineap.meeseva.gov.in",
    domain: "onlineap.meeseva.gov.in",
    badge: "Govt of AP",
    icon: "📜",
    description: "Official AP citizen services portal for applying and downloading digitally signed Tahsildar certificates required for fee reimbursement.",
    services: [
      "Integrated Community, Nativity & Date of Birth (Caste) Certificate",
      "Tahsildar Income Certificate (for fee reimbursement & pensions)",
      "Residence / Domicile Certificate",
      "Family Member & Legal Heir Certificates"
    ]
  },
  {
    id: "ap-aarogyasri",
    name: "Dr. YSR Aarogyasri Health Care Trust",
    state: "Andhra Pradesh",
    category: "Healthcare",
    department: "Dr. YSR Aarogyasri Health Care Trust, Government of Andhra Pradesh",
    url: "https://ysraarogyasri.ap.gov.in",
    domain: "ysraarogyasri.ap.gov.in",
    badge: "Govt of AP",
    icon: "🏥",
    description: "State health insurance offering 100% cashless medical and surgical treatment up to ₹25,00,000 per family per year across 3,257 procedures.",
    services: [
      "Dr. YSR Aarogyasri Health Card download & verification",
      "Network Empanelled Hospital directory (AP, HYD, BLR, CHN)",
      "Pre-authorization & treatment package tariff search",
      "Aarogya Mithra hospital assistance contacts"
    ]
  },
  {
    id: "ap-rythu",
    name: "YSR Rythu Bharosa Portal",
    state: "Andhra Pradesh",
    category: "Agriculture",
    department: "Department of Agriculture & Cooperation, Govt. of Andhra Pradesh",
    url: "https://ysrrythubharosa.ap.gov.in",
    domain: "ysrrythubharosa.ap.gov.in",
    badge: "Govt of AP",
    icon: "🌾",
    description: "Farmer financial support portal transferring ₹13,500/year to landholding and tenant farmers (CCRC holders) in three seasonal installments.",
    services: [
      "Farmer Payment Status by Aadhaar Number",
      "e-Crop Booking & Village Social Audit Display",
      "Tenant Cultivator (CCRC) Registration and Approval",
      "Free Crop Insurance (YSR Uchitha Vyavasaya Bima) status"
    ]
  },
  {
    id: "ap-sachivalayam",
    name: "AP Grama & Ward Sachivalayam Portal",
    state: "Andhra Pradesh",
    category: "e-Governance & Certificates",
    department: "Village & Ward Secretariats Dept., Govt. of Andhra Pradesh",
    url: "https://gramawardsachivalayam.ap.gov.in",
    domain: "gramawardsachivalayam.ap.gov.in",
    badge: "Govt of AP",
    icon: "🏛️",
    description: "Grassroots citizen service delivery portal offering 540+ government services through 15,004 Village and Ward Secretariats.",
    services: [
      "Doorstep delivery of 540+ Government Services",
      "Rice Card, Aarogyasri Card & Pension card application",
      "Volunteer mapping and doorstep biometric verification",
      "Track service application token status online"
    ]
  },

  // Telangana
  {
    id: "ts-epass",
    name: "Telangana ePASS (Scholarships & Welfare Portal)",
    state: "Telangana",
    category: "Scholarships & Education",
    department: "Scheduled Castes, BC, Tribal & Minority Welfare Depts., Govt. of Telangana",
    url: "https://telanganaepass.cgg.gov.in",
    domain: "telanganaepass.cgg.gov.in",
    badge: "Govt of TS",
    icon: "🔵",
    description: "Telangana's welfare gateway managing Post-Matric Fee Reimbursement (RTF/MTF), Overseas Vidya Nidhi, and Kalyana Lakshmi & Shaadi Mubarak.",
    services: [
      "Post-Matric Scholarship & Full Fee Reimbursement (RTF)",
      "Hostel & Mess Maintenance Allowance (MTF)",
      "Telangana Overseas Vidya Nidhi (up to ₹20 Lakhs for foreign MS/MBA)",
      "Kalyana Lakshmi & Shaadi Mubarak (₹1,00,116 bride marriage grant)",
      "Corporate College Admissions & Pre-Matric Scholarships"
    ]
  },
  {
    id: "ts-meeseva",
    name: "MeeSeva Telangana Citizen Portal",
    state: "Telangana",
    category: "e-Governance & Certificates",
    department: "ITE&C Department & MeeSeva Directorate, Govt. of Telangana",
    url: "https://ts.meeseva.telangana.gov.in",
    domain: "ts.meeseva.telangana.gov.in",
    badge: "Govt of TS",
    icon: "📜",
    description: "Unified citizen portal for applying and securing digitally signed revenue and community certificates required for college admissions.",
    services: [
      "MeeSeva Integrated Caste / Community Certificate",
      "Tahsildar Income Certificate (mandatory for TS ePASS)",
      "Residence & Local Candidate Certificate",
      "Encumbrance (EC) and Revenue Extract services"
    ]
  },
  {
    id: "ts-rythubandhu",
    name: "Rythu Bandhu & Rythu Bima Portal",
    state: "Telangana",
    category: "Agriculture",
    department: "Department of Agriculture & Cooperation, Govt. of Telangana",
    url: "https://rythubandhu.telangana.gov.in",
    domain: "rythubandhu.telangana.gov.in",
    badge: "Govt of TS",
    icon: "🌾",
    description: "Agricultural investment support portal providing direct transfers of ₹12,000–₹15,000 per acre per year and ₹5 Lakh farmer group life insurance.",
    services: [
      "Farmer Investment Support disbursement status",
      "Rythu Bima (₹5 Lakh Group Life Insurance) enrollment & claims",
      "Direct Bank Transfer transaction reconciliation",
      "Agricultural Extension Officer (AEO) cluster contacts"
    ]
  },
  {
    id: "ts-dharani",
    name: "Dharani Portal (Telangana Land Records & Passbook)",
    state: "Telangana",
    category: "Identity & Records",
    department: "Registration & Stamps / Revenue Dept., Government of Telangana",
    url: "https://dharani.telangana.gov.in",
    domain: "dharani.telangana.gov.in",
    badge: "Govt of TS",
    icon: "🗺️",
    description: "Integrated land administration portal providing transparent agricultural land registration, instant mutation, and digital Pattadar Passbook extraction.",
    services: [
      "View Land Details by Survey Number / Khata Number",
      "Download Digital Pattadar Passbook (Agriculture)",
      "Cadastral Map & BhuNaksha GIS view",
      "Online slot booking for land transactions"
    ]
  },
  {
    id: "ts-aarogyasri",
    name: "Rajiv Aarogyasri Telangana Health Care Trust",
    state: "Telangana",
    category: "Healthcare",
    department: "Aarogyasri Health Care Trust, Government of Telangana",
    url: "https://aarogyasri.telangana.gov.in",
    domain: "aarogyasri.telangana.gov.in",
    badge: "Govt of TS",
    icon: "🏥",
    description: "State health insurance platform providing cashless medical treatment and surgery up to ₹10,00,000 per family per year across 1,672 procedures.",
    services: [
      "Check Aarogyasri Card status with FSC / Ration Card",
      "Find Network Hospitals & Specialty Doctors in Telangana",
      "Treatment pre-authorization status tracking",
      "Dial 104 / Aarogyasri toll-free helpdesk"
    ]
  },
  {
    id: "ts-govportal",
    name: "Telangana State Official Portal",
    state: "Telangana",
    category: "National Gateways",
    department: "ITE&C Department, Government of Telangana",
    url: "https://telangana.gov.in",
    domain: "telangana.gov.in",
    badge: "Govt of TS",
    icon: "🏛️",
    description: "Apex government portal providing access to all 33 Telangana district administrations, departments, and Mahalakshmi scheme circulars.",
    services: [
      "Mahalakshmi Free Bus Travel & Financial Aid circulars",
      "Government Orders (GOs) and Gazettes repository",
      "Telangana State Public Service Commission (TGPSC) links",
      "District Collectorate contact directory"
    ]
  },

  // Tamil Nadu
  {
    id: "tn-esevai",
    name: "Tamil Nadu e-Sevai (TNeGA Citizen Portal)",
    state: "Tamil Nadu",
    category: "e-Governance & Certificates",
    department: "Tamil Nadu e-Governance Agency (TNeGA), Govt. of Tamil Nadu",
    url: "https://www.tnesevai.tn.gov.in",
    domain: "tnesevai.tn.gov.in",
    badge: "Govt of TN",
    icon: "🔴",
    description: "Unified online service portal for citizens of Tamil Nadu to apply for, track, and download Revenue Department certificates required for college admissions.",
    services: [
      "Community / Caste Certificate (BC, MBC, SC, ST)",
      "Income Certificate (Revenue Authority)",
      "Nativity / Domicile Certificate",
      "First Graduate Certificate (for tuition fee exemption)",
      "No Male Child / Single Girl Child Certificate"
    ]
  },
  {
    id: "tn-pudhumai",
    name: "Pudhumai Penn Scheme Portal",
    state: "Tamil Nadu",
    category: "Scholarships & Education",
    department: "Social Welfare & Women Empowerment Dept., Govt. of Tamil Nadu",
    url: "https://pudhumaipenn.tn.gov.in",
    domain: "pudhumaipenn.tn.gov.in",
    badge: "Govt of TN",
    icon: "👩",
    description: "Official portal for Moovalur Ramamirtham Ammaiyar Higher Education Assurance Scheme providing ₹1,000/month cash assistance to girls from TN government schools.",
    services: [
      "New Student Registration with EMIS School Code",
      "College Verification and Approval workflow",
      "Direct Benefit Transfer (DBT) monthly payment status",
      "Grievance submission for missing payment credits"
    ]
  },
  {
    id: "tn-kmut",
    name: "Kalaignar Magalir Urimai Thittam (KMUT Portal)",
    state: "Tamil Nadu",
    category: "Women & Social Welfare",
    department: "Special Programme Implementation Dept., Govt. of Tamil Nadu",
    url: "https://kmut.tn.gov.in",
    domain: "kmut.tn.gov.in",
    badge: "Govt of TN",
    icon: "🤝",
    description: "Universal basic income rights scheme providing ₹1,000 monthly rights grant directly to eligible women heads of families in Tamil Nadu.",
    services: [
      "Check Beneficiary Eligibility Status with Smart Ration Card",
      "Aadhaar-seeded Bank Account verification",
      "Appeal & re-verification submission for rejected applicants",
      "Helpdesk & Tahsildar camp schedule lookup"
    ]
  },
  {
    id: "tn-tnea",
    name: "TNEA Online (Tamil Nadu Engineering Admissions)",
    state: "Tamil Nadu",
    category: "Scholarships & Education",
    department: "Directorate of Technical Education (DoTE), Govt. of Tamil Nadu",
    url: "https://www.tneaonline.org",
    domain: "tneaonline.org",
    badge: "Govt of TN",
    icon: "🎓",
    description: "Single-window online engineering counseling portal facilitating admissions and implementing the 7.5% Government School 100% Fee Waiver quota.",
    services: [
      "B.E. / B.Tech Single Window Counseling Registration",
      "7.5% Preferential Reservation & 100% Fee Waiver allotment",
      "First Graduate Fee Concession verification",
      "Cut-off marks & College seat vacancy matrix"
    ]
  },
  {
    id: "tn-dote",
    name: "Tamil Nadu Directorate of Technical Education (DoTE)",
    state: "Tamil Nadu",
    category: "Scholarships & Education",
    department: "Higher Education Department, Govt. of Tamil Nadu",
    url: "https://www.tndte.gov.in",
    domain: "tndte.gov.in",
    badge: "Govt of TN",
    icon: "🏛️",
    description: "Apex technical education directorate overseeing engineering and polytechnic colleges, First Graduate fee concessions, and scholarships.",
    services: [
      "First Graduate Tuition Fee Waiver Guidelines & Approvals",
      "Polytechnic / Diploma Centralized Admissions",
      "Government and Government-Aided College Fee structures",
      "Technical Scholarship circulars & notifications"
    ]
  },
  {
    id: "tn-cmchis",
    name: "Chief Minister's Comprehensive Health Insurance (CMCHIS)",
    state: "Tamil Nadu",
    category: "Healthcare",
    department: "Health & Family Welfare Department, Govt. of Tamil Nadu",
    url: "https://www.cmchistn.com",
    domain: "cmchistn.com",
    badge: "Govt of TN",
    icon: "🏥",
    description: "State health insurance scheme providing cashless hospitalization up to ₹5,00,000 per family per year across 1,090 notified therapy procedures.",
    services: [
      "Check Beneficiary Eligibility with Smart Family Card",
      "Search Empanelled Government and Private Hospitals",
      "Coverage Package list & Special Surgeries directory",
      "Download e-Card and 24x7 Emergency Call Center 104"
    ]
  },
  {
    id: "tn-govportal",
    name: "Tamil Nadu Government Official Web Portal",
    state: "Tamil Nadu",
    category: "National Gateways",
    department: "Information & Public Relations / IT Dept, Govt. of Tamil Nadu",
    url: "https://www.tn.gov.in",
    domain: "tn.gov.in",
    badge: "Govt of TN",
    icon: "🏛️",
    description: "Official apex web portal of the Government of Tamil Nadu providing access to all 38 district administrations, gazettes, policies, and welfare programs.",
    services: [
      "Directory of all Tamil Nadu Welfare Departments",
      "Government Orders (GOs) and Policy Notes",
      "District Collectorate contacts across all 38 districts",
      "Public Information and Press Releases"
    ]
  }
];

async function initPortalsDirectory() {
  const searchInput = document.getElementById("portalSearchInput");
  const stateTabs = document.querySelectorAll(".portal-tab-btn");
  const categoryChips = document.querySelectorAll(".portal-filter-chip");
  const heroViewAllBtn = document.getElementById("heroViewAllPortalsBtn");
  const navGovtPortals = document.getElementById("navGovtPortals");

  let allPortals = [];
  try {
    const res = await fetch("/api/portals");
    if (res.ok) {
      const data = await res.json();
      allPortals = data.portals && data.portals.length > 0 ? data.portals : FALLBACK_PORTALS;
    } else {
      allPortals = FALLBACK_PORTALS;
    }
  } catch (e) {
    allPortals = FALLBACK_PORTALS;
  }

  function filterAndRenderPortals() {
    const query = searchInput ? searchInput.value.toLowerCase().trim() : "";
    const activeStateTab = document.querySelector(".portal-tab-btn.active");
    const selectedState = activeStateTab ? activeStateTab.getAttribute("data-portal-state") : "All";

    const activeCatChip = document.querySelector(".portal-filter-chip.active");
    const selectedCat = activeCatChip ? activeCatChip.getAttribute("data-portal-cat") : "All";

    const filtered = allPortals.filter(p => {
      // State matching
      let matchesState = true;
      if (selectedState !== "All") {
        matchesState = (p.state.toLowerCase() === selectedState.toLowerCase());
      }

      // Category matching
      let matchesCat = true;
      if (selectedCat !== "All") {
        matchesCat = (p.category.toLowerCase() === selectedCat.toLowerCase());
      }

      // Query matching
      let matchesQuery = true;
      if (query) {
        const servicesStr = (p.services || []).join(" ").toLowerCase();
        const haystack = `${p.name} ${p.department} ${p.description} ${p.domain} ${p.state} ${servicesStr}`.toLowerCase();
        matchesQuery = haystack.includes(query);
      }

      return matchesState && matchesCat && matchesQuery;
    });

    renderPortalsGrid(filtered);
  }

  if (searchInput) {
    searchInput.addEventListener("input", filterAndRenderPortals);
  }

  stateTabs.forEach(tab => {
    tab.addEventListener("click", () => {
      stateTabs.forEach(t => t.classList.remove("active"));
      tab.classList.add("active");
      filterAndRenderPortals();
    });
  });

  categoryChips.forEach(chip => {
    chip.addEventListener("click", () => {
      categoryChips.forEach(c => c.classList.remove("active"));
      chip.classList.add("active");
      filterAndRenderPortals();
    });
  });

  if (heroViewAllBtn) {
    heroViewAllBtn.addEventListener("click", (e) => {
      e.preventDefault();
      document.getElementById("portalsSection")?.scrollIntoView({ behavior: "smooth" });
    });
  }

  if (navGovtPortals) {
    navGovtPortals.addEventListener("click", (e) => {
      e.preventDefault();
      document.getElementById("portalsSection")?.scrollIntoView({ behavior: "smooth" });
    });
  }

  filterAndRenderPortals();
}

function renderPortalsGrid(portals) {
  const grid = document.getElementById("portalsGrid");
  if (!grid) return;

  if (!portals || portals.length === 0) {
    grid.innerHTML = `<div style="grid-column: 1/-1; text-align: center; padding: 2.5rem; color: var(--text-muted);">No government portals found matching the selected state and category.</div>`;
    return;
  }

  grid.innerHTML = portals.map(p => {
    const servicesHtml = (p.services || []).slice(0, 3)
      .map(s => `<li class="portal-service-item"><span class="portal-service-check">✓</span><span>${s}</span></li>`)
      .join("");
    const extraCount = (p.services || []).length > 3 ? `<li class="portal-service-item" style="color:var(--text-muted);font-size:0.72rem;">+${p.services.length - 3} more citizen services…</li>` : "";

    return `
      <div class="portal-card animate-fade-in">
        <div>
          <div class="portal-card-header">
            <div class="portal-card-badges">
              ${getStateBadge(p.state)}
              <span class="badge badge-info">${p.category}</span>
            </div>
            <span class="portal-verified-domain" title="Verified official government portal">
              <span class="pulse-indicator"></span>
              ${p.domain}
            </span>
          </div>

          <h3 class="portal-card-title">${p.name}</h3>
          <p class="portal-card-dept">${p.department}</p>
          <p class="portal-card-desc">${p.description}</p>

          <div class="portal-services-box">
            <div class="portal-services-title">Key Citizen Services:</div>
            <ul class="portal-services-list">
              ${servicesHtml}
              ${extraCount}
            </ul>
          </div>
        </div>

        <div class="portal-card-actions">
          <a href="${p.url}" target="_blank" rel="noopener noreferrer" class="portal-visit-btn" title="Open ${p.name} in a new tab">
            Visit Official Portal ↗
          </a>
        </div>
      </div>
    `;
  }).join("");
}
