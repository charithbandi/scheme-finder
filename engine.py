"""
Rule-Based Eligibility Engine for Scheme Finder
Implements the Boolean Threshold Satisfaction Model described in Chapter 4.3 of the project report.

Mathematical Formulation:
E(r_i, U) = 1 if attribute a_j satisfies condition of r_i, else 0
Eligibility(S, U) = Product of E(r_i, U) for all mandatory rules.
"""

from typing import Dict, Any, List, Tuple


class Rule:
    def __init__(
        self,
        attribute_name: str,
        operator: str,
        target_value: Any,
        explanation_template: str,
        is_mandatory: bool = True
    ):
        self.attribute_name = attribute_name
        self.operator = operator  # '<=', '>=', '==', 'in', '!=', 'contains'
        self.target_value = target_value
        self.explanation_template = explanation_template
        self.is_mandatory = is_mandatory

    def evaluate(self, profile: Dict[str, Any]) -> Tuple[bool, str]:
        user_val = profile.get(self.attribute_name)
        if user_val is None:
            return False, f"Missing {self.attribute_name} in user profile."

        passed = False
        try:
            if self.operator == '<=':
                passed = float(user_val) <= float(self.target_value)
            elif self.operator == '>=':
                passed = float(user_val) >= float(self.target_value)
            elif self.operator == '==':
                if isinstance(self.target_value, str) and isinstance(user_val, str):
                    passed = user_val.strip().lower() == self.target_value.strip().lower()
                else:
                    passed = user_val == self.target_value
            elif self.operator == '!=':
                passed = user_val != self.target_value
            elif self.operator == 'in':
                if isinstance(self.target_value, (list, tuple, set)):
                    # Case-insensitive string matching if values are strings
                    norm_target = [str(x).strip().lower() for x in self.target_value]
                    passed = str(user_val).strip().lower() in norm_target or 'all' in norm_target or 'any' in norm_target
                else:
                    passed = user_val in self.target_value
            elif self.operator == 'boolean':
                passed = bool(user_val) is bool(self.target_value)
        except (ValueError, TypeError):
            passed = False

        if passed:
            explanation = self.format_explanation(user_val)
            return True, explanation
        else:
            return False, f"Did not satisfy {self.attribute_name} condition"

    def format_explanation(self, user_val: Any) -> str:
        try:
            if self.attribute_name == 'income':
                limit_lakh = float(self.target_value) / 100000
                user_lakh = float(user_val) / 100000
                return f"Annual income ₹{user_lakh:.2f}L is within eligible limit (≤ ₹{limit_lakh:.2f}L)"
            elif self.attribute_name == 'marks':
                return f"Academic score {user_val}% satisfies minimum requirement (≥ {self.target_value}%)"
            elif self.attribute_name == 'gender':
                return f"Gender ({user_val}) matches scheme target demographic"
            elif self.attribute_name == 'category':
                return f"Social category '{user_val}' is eligible"
            elif self.attribute_name == 'state':
                return f"Domicile in '{user_val}' qualifies for this state/national scheme"
            elif self.attribute_name == 'course_level':
                return f"Enrolled education level '{user_val}' meets eligibility"
            elif self.attribute_name == 'is_first_graduate':
                return "First-generation graduate criterion satisfied"
            elif self.attribute_name == 'is_disabled':
                return "Person with Disability (PwD) reservation satisfied"
            elif self.attribute_name == 'is_single_girl_child':
                return "Single Girl Child quota satisfied"
            elif self.attribute_name == 'is_govt_school':
                return "Government School student (Class 6th-12th) criterion satisfied"
            elif self.attribute_name == 'is_farmer':
                return "Agriculture / farming household criterion satisfied"
            else:
                return self.explanation_template.replace("{user_val}", str(user_val)).replace("{target_val}", str(self.target_value))
        except Exception:
            return self.explanation_template


class Scheme:
    def __init__(
        self,
        id: str,
        name: str,
        department: str,
        category_type: str,  # Education, Healthcare, Agriculture, Women Empowerment, Social Welfare
        state: str,          # "Andhra Pradesh", "Telangana", "Tamil Nadu", or "All India"
        description: str,
        benefit: str,
        official_portal_url: str,
        documents: List[str],
        rules: List[Rule],
        priority_weight: int = 100
    ):
        self.id = id
        self.name = name
        self.department = department
        self.category_type = category_type
        self.state = state
        self.description = description
        self.benefit = benefit
        self.official_portal_url = official_portal_url
        self.documents = documents
        self.rules = rules
        self.priority_weight = priority_weight

    def evaluate_profile(self, profile: Dict[str, Any]) -> Dict[str, Any]:
        """
        Evaluates a profile against all rules of this scheme.
        Returns match status, matched explanations, and match percentage.
        """
        user_state = str(profile.get("state", "Pan-India")).strip().lower()
        scheme_state = self.state.strip().lower()

        # State eligibility check: State schemes require exact match; Central/All-India open to all
        if scheme_state not in ["all india", "pan-india", "central"]:
            if user_state != scheme_state:
                return {
                    "eligible": False,
                    "scheme_id": self.id,
                    "name": self.name,
                    "match_percentage": 0,
                    "why_you_qualify": []
                }

        matched_explanations = []
        # If state matches a state scheme, record that as an explanation
        if scheme_state in ["andhra pradesh", "telangana", "tamil nadu"]:
            matched_explanations.append(f"Resident of {self.state} (State Welfare Scheme)")

        mandatory_passed = True
        total_rules = len(self.rules)
        passed_rules_count = 0

        for rule in self.rules:
            satisfied, explanation = rule.evaluate(profile)
            if satisfied:
                matched_explanations.append(explanation)
                passed_rules_count += 1
            else:
                if rule.is_mandatory:
                    mandatory_passed = False
                    break

        if not mandatory_passed:
            return {
                "eligible": False,
                "scheme_id": self.id,
                "name": self.name,
                "match_percentage": 0,
                "why_you_qualify": []
            }

        # Calculate match percentage (base 80% for meeting all mandatory + bonus for extra alignment)
        match_percentage = min(100, int(80 + (passed_rules_count / max(1, total_rules)) * 20))

        return {
            "eligible": True,
            "scheme_id": self.id,
            "name": self.name,
            "department": self.department,
            "category_type": self.category_type,
            "state": self.state,
            "description": self.description,
            "benefit": self.benefit,
            "official_portal_url": self.official_portal_url,
            "documents": self.documents,
            "match_percentage": match_percentage,
            "why_you_qualify": matched_explanations,
            "priority": self.priority_weight
        }

    def to_dict(self) -> Dict[str, Any]:
        """Serializes scheme metadata for catalog browsing."""
        return {
            "id": self.id,
            "name": self.name,
            "department": self.department,
            "category_type": self.category_type,
            "state": self.state,
            "description": self.description,
            "benefit": self.benefit,
            "official_portal_url": self.official_portal_url,
            "documents": self.documents,
            "rules_count": len(self.rules)
        }


class EligibilityEngine:
    def __init__(self, schemes: List[Scheme] = None):
        self.schemes = schemes or []

    def add_scheme(self, scheme: Scheme):
        self.schemes.append(scheme)

    def evaluate_profile(self, profile: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Evaluates profile against all registered schemes and returns ranked matches.
        """
        eligible_schemes = []

        for scheme in self.schemes:
            res = scheme.evaluate_profile(profile)
            if res.get("eligible"):
                eligible_schemes.append(res)

        # Rank schemes by match percentage descending and priority weight descending
        eligible_schemes.sort(
            key=lambda x: (x.get("match_percentage", 0), x.get("priority", 0)),
            reverse=True
        )

        return eligible_schemes
